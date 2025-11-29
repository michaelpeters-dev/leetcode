// GleetCode Background Service Worker
// Handles GitHub API interactions

const REPO_NAME = 'leetcode';
const GITHUB_API = 'https://api.github.com';

// Difficulty colors (LeetCode style)
const DIFFICULTY_COLORS = {
  Easy: '#00b8a3',
  Medium: '#ffc01e',
  Hard: '#ff375f',
  Unknown: '#808080'
};

// Get stored GitHub token
async function getToken() {
  const result = await chrome.storage.local.get('github_token');
  return result.github_token;
}

// Get stored GitHub username
async function getUsername() {
  const result = await chrome.storage.local.get('github_username');
  return result.github_username;
}

// Make GitHub API request
async function githubRequest(endpoint, options = {}) {
  const token = await getToken();
  if (!token) {
    throw new Error('GitHub token not configured. Click the extension icon to set it up.');
  }

  const response = await fetch(`${GITHUB_API}${endpoint}`, {
    ...options,
    headers: {
      'Authorization': `token ${token}`,
      'Accept': 'application/vnd.github.v3+json',
      'Content-Type': 'application/json',
      ...options.headers
    }
  });

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    if (response.status === 401) {
      throw new Error('Invalid GitHub token. Please update it in extension settings.');
    }
    return { ok: false, status: response.status, data };
  }

  return { ok: true, status: response.status, data };
}

// Get file content from repo
async function getFileContent(username, path) {
  const result = await githubRequest(`/repos/${username}/${REPO_NAME}/contents/${path}`);

  if (!result.ok) {
    if (result.status === 404) {
      return null;
    }
    throw new Error(result.data.message || `GitHub API error: ${result.status}`);
  }

  return {
    content: atob(result.data.content.replace(/\n/g, '')),
    sha: result.data.sha
  };
}

// Create or update file in repo
async function createOrUpdateFile(username, path, content, message, sha = null) {
  const body = {
    message: message,
    content: btoa(unescape(encodeURIComponent(content)))
  };

  if (sha) {
    body.sha = sha;
  }

  const result = await githubRequest(`/repos/${username}/${REPO_NAME}/contents/${path}`, {
    method: 'PUT',
    body: JSON.stringify(body)
  });

  if (!result.ok) {
    if (result.status === 404) {
      throw new Error(`Repository '${REPO_NAME}' not found. Make sure it exists in your GitHub account.`);
    }
    if (result.status === 409) {
      throw new Error('Conflict: File was modified. Please try again.');
    }
    if (result.status === 422) {
      throw new Error(result.data.message || 'Invalid request. Check file path and content.');
    }
    throw new Error(result.data.message || `GitHub API error: ${result.status}`);
  }

  return result.data;
}

// Format problem slug to filename
function formatFilename(problemNumber, problemSlug) {
  const formattedSlug = problemSlug.replace(/-/g, '_');
  return `${problemNumber}_${formattedSlug}.py`;
}

// Format file content
function formatFileContent(data) {
  return `# Problem: ${data.problemTitle}
# Number: ${data.problemNumber}
# Difficulty: ${data.difficulty}
# URL: ${data.problemUrl}
# Submission Status: ${data.status}
# Runtime: ${data.runtime}
# Memory: ${data.memory}

${data.code}
`;
}

// Generate SVG progress chart
function generateProgressChart(problems) {
  // Sort problems by timestamp
  const sortedProblems = [...problems].filter(p => p.timestamp).sort((a, b) =>
    new Date(a.timestamp) - new Date(b.timestamp)
  );

  if (sortedProblems.length === 0) {
    return '';
  }

  // Group by date and calculate cumulative count
  const dateMap = new Map();
  let cumulative = 0;

  sortedProblems.forEach(p => {
    const date = p.timestamp.split('T')[0];
    cumulative++;
    dateMap.set(date, cumulative);
  });

  const dates = Array.from(dateMap.keys());
  const values = Array.from(dateMap.values());
  const maxValue = Math.max(...values);

  // Chart dimensions
  const width = 800;
  const height = 300;
  const padding = { top: 30, right: 30, bottom: 50, left: 50 };
  const chartWidth = width - padding.left - padding.right;
  const chartHeight = height - padding.top - padding.bottom;

  // Scale functions
  const xScale = (i) => padding.left + (i / (dates.length - 1 || 1)) * chartWidth;
  const yScale = (v) => padding.top + chartHeight - (v / maxValue) * chartHeight;

  // Generate path
  let pathD = `M ${xScale(0)} ${yScale(values[0])}`;
  for (let i = 1; i < values.length; i++) {
    pathD += ` L ${xScale(i)} ${yScale(values[i])}`;
  }

  // Generate area fill path
  let areaD = pathD + ` L ${xScale(values.length - 1)} ${padding.top + chartHeight} L ${xScale(0)} ${padding.top + chartHeight} Z`;

  // Generate grid lines
  const gridLines = [];
  const yTicks = 5;
  for (let i = 0; i <= yTicks; i++) {
    const y = padding.top + (i / yTicks) * chartHeight;
    const value = Math.round(maxValue * (1 - i / yTicks));
    gridLines.push(`<line x1="${padding.left}" y1="${y}" x2="${width - padding.right}" y2="${y}" stroke="#3e3e3e" stroke-dasharray="4"/>`);
    gridLines.push(`<text x="${padding.left - 10}" y="${y + 4}" fill="#888" font-size="12" text-anchor="end">${value}</text>`);
  }

  // Generate x-axis labels (show first, middle, last)
  const xLabels = [];
  if (dates.length > 0) {
    const formatDate = (d) => {
      const date = new Date(d);
      return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
    };

    xLabels.push(`<text x="${xScale(0)}" y="${height - 15}" fill="#888" font-size="11" text-anchor="start">${formatDate(dates[0])}</text>`);
    if (dates.length > 2) {
      const midIdx = Math.floor(dates.length / 2);
      xLabels.push(`<text x="${xScale(midIdx)}" y="${height - 15}" fill="#888" font-size="11" text-anchor="middle">${formatDate(dates[midIdx])}</text>`);
    }
    if (dates.length > 1) {
      xLabels.push(`<text x="${xScale(dates.length - 1)}" y="${height - 15}" fill="#888" font-size="11" text-anchor="end">${formatDate(dates[dates.length - 1])}</text>`);
    }
  }

  // Generate data points
  const points = values.map((v, i) =>
    `<circle cx="${xScale(i)}" cy="${yScale(v)}" r="4" fill="#ffa116"/>`
  ).join('\n    ');

  return `
<svg viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="areaGradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#ffa116;stop-opacity:0.3"/>
      <stop offset="100%" style="stop-color:#ffa116;stop-opacity:0.05"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="${width}" height="${height}" fill="#1a1a1a" rx="8"/>

  <!-- Title -->
  <text x="${width/2}" y="22" fill="#eff1f6" font-size="14" font-weight="600" text-anchor="middle">Cumulative Problems Solved</text>

  <!-- Grid lines -->
  ${gridLines.join('\n  ')}

  <!-- Area fill -->
  <path d="${areaD}" fill="url(#areaGradient)"/>

  <!-- Line -->
  <path d="${pathD}" fill="none" stroke="#ffa116" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Data points -->
  ${points}

  <!-- X-axis labels -->
  ${xLabels.join('\n  ')}

  <!-- Y-axis label -->
  <text x="15" y="${height/2}" fill="#888" font-size="12" text-anchor="middle" transform="rotate(-90, 15, ${height/2})">Problems Solved</text>
</svg>`;
}

// Generate difficulty badge SVG
function getDifficultyBadge(difficulty) {
  const color = DIFFICULTY_COLORS[difficulty] || DIFFICULTY_COLORS.Unknown;
  return `![${difficulty}](https://img.shields.io/badge/${difficulty}-${color.replace('#', '')}?style=flat-square)`;
}

// Parse existing README to get problems list
function parseReadme(content) {
  const lines = content.split('\n');
  const problems = [];
  let inTable = false;
  let headerPassed = false;

  for (const line of lines) {
    if (line.includes('| # |') || line.includes('|#|')) {
      inTable = true;
      continue;
    }
    if (inTable && line.match(/^\|[-:\s|]+\|$/)) {
      headerPassed = true;
      continue;
    }
    if (inTable && headerPassed && line.startsWith('|')) {
      const parts = line.split('|').map(p => p.trim()).filter(p => p);
      if (parts.length >= 5) {
        const num = parseInt(parts[0]);
        if (!isNaN(num)) {
          // Extract difficulty from badge or text
          let difficulty = 'Unknown';
          const diffMatch = parts[2].match(/badge\/(Easy|Medium|Hard)/i) ||
                           parts[2].match(/(Easy|Medium|Hard)/i);
          if (diffMatch) {
            difficulty = diffMatch[1].charAt(0).toUpperCase() + diffMatch[1].slice(1).toLowerCase();
          }

          // Extract timestamp if present
          let timestamp = null;
          if (parts.length >= 6) {
            timestamp = parts[5];
          }

          problems.push({
            number: num,
            title: parts[1],
            difficulty: difficulty,
            file: parts[3],
            status: parts[4],
            timestamp: timestamp
          });
        }
      }
    }
    if (inTable && !line.startsWith('|') && line.trim() !== '') {
      inTable = false;
    }
  }

  return problems;
}

// Generate README content
function generateReadme(problems, username) {
  problems.sort((a, b) => a.number - b.number);

  // Count by difficulty
  const counts = { Easy: 0, Medium: 0, Hard: 0, total: problems.length };
  problems.forEach(p => {
    if (counts.hasOwnProperty(p.difficulty)) {
      counts[p.difficulty]++;
    }
  });

  // Generate progress chart
  const chart = generateProgressChart(problems);

  let content = `# LeetCode Solutions

<div align="center">

![Total](https://img.shields.io/badge/Total-${counts.total}-ffa116?style=for-the-badge)
![Easy](https://img.shields.io/badge/Easy-${counts.Easy}-00b8a3?style=for-the-badge)
![Medium](https://img.shields.io/badge/Medium-${counts.Medium}-ffc01e?style=for-the-badge)
![Hard](https://img.shields.io/badge/Hard-${counts.Hard}-ff375f?style=for-the-badge)

</div>

My LeetCode solutions, automatically pushed by **GleetCode** Chrome Extension.

## Progress

${chart ? `<div align="center">\n\n${chart}\n\n</div>` : '_No progress data yet. Solve more problems!_'}

## Solutions

| # | Title | Difficulty | Solution | Status | Date |
|:---:|:------|:----------:|:--------:|:------:|:----:|
`;

  for (const problem of problems) {
    const diffBadge = getDifficultyBadge(problem.difficulty);
    const statusEmoji = problem.status === 'Accepted' ? '✅' : '❌';
    const dateStr = problem.timestamp ? new Date(problem.timestamp).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) : '-';

    content += `| ${problem.number} | ${problem.title} | ${diffBadge} | ${problem.file} | ${statusEmoji} ${problem.status} | ${dateStr} |\n`;
  }

  content += `

---

<div align="center">
<sub>Auto-generated by <a href="https://github.com">GleetCode</a> Chrome Extension</sub>
</div>
`;

  return content;
}

// Update README with new problem
async function updateReadme(username, problemNumber, problemTitle, filename, status, difficulty, timestamp) {
  let problems = [];
  let existingSha = null;

  const existingReadme = await getFileContent(username, 'README.md');
  if (existingReadme) {
    problems = parseReadme(existingReadme.content);
    existingSha = existingReadme.sha;
  }

  const existingIndex = problems.findIndex(p => p.number === parseInt(problemNumber));

  const newProblem = {
    number: parseInt(problemNumber),
    title: problemTitle,
    difficulty: difficulty,
    file: `[${filename}](${filename})`,
    status: status,
    timestamp: timestamp
  };

  if (existingIndex >= 0) {
    // Preserve original timestamp if updating
    if (!newProblem.timestamp && problems[existingIndex].timestamp) {
      newProblem.timestamp = problems[existingIndex].timestamp;
    }
    problems[existingIndex] = newProblem;
  } else {
    problems.push(newProblem);
  }

  const newReadmeContent = generateReadme(problems, username);

  await createOrUpdateFile(
    username,
    'README.md',
    newReadmeContent,
    `Update README with ${problemNumber}. ${problemTitle}`,
    existingSha
  );
}

// Main push function
async function pushSolution(data) {
  const username = await getUsername();
  if (!username) {
    throw new Error('GitHub username not configured. Click the extension icon to set it up.');
  }

  const repoCheck = await githubRequest(`/repos/${username}/${REPO_NAME}`);
  if (!repoCheck.ok) {
    if (repoCheck.status === 404) {
      throw new Error(`Repository '${username}/${REPO_NAME}' not found. Please create it on GitHub first.`);
    }
    throw new Error(repoCheck.data.message || `Cannot access repository: ${repoCheck.status}`);
  }

  const filename = formatFilename(data.problemNumber, data.problemSlug);
  const fileContent = formatFileContent(data);
  const commitMessage = `${data.problemNumber}. ${data.problemTitle} (Python)`;

  const existingFile = await getFileContent(username, filename);
  const sha = existingFile ? existingFile.sha : null;

  await createOrUpdateFile(username, filename, fileContent, commitMessage, sha);
  await updateReadme(username, data.problemNumber, data.problemTitle, filename, data.status, data.difficulty, data.timestamp);

  return { success: true };
}

// Validate GitHub token
async function validateToken(token, username) {
  try {
    const response = await fetch(`${GITHUB_API}/repos/${username}/${REPO_NAME}`, {
      headers: {
        'Authorization': `token ${token}`,
        'Accept': 'application/vnd.github.v3+json'
      }
    });

    if (response.status === 401) {
      return { valid: false, error: 'Invalid token' };
    }

    if (response.status === 404) {
      return { valid: false, error: `Repository '${REPO_NAME}' not found for user '${username}'` };
    }

    if (!response.ok) {
      return { valid: false, error: `GitHub API error: ${response.status}` };
    }

    const data = await response.json();

    if (!data.permissions || !data.permissions.push) {
      return { valid: false, error: 'Token does not have write access to this repository' };
    }

    return { valid: true, repoName: data.full_name };
  } catch (error) {
    return { valid: false, error: error.message };
  }
}

// Message handler
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'PUSH_SOLUTION') {
    pushSolution(message.data)
      .then(result => sendResponse(result))
      .catch(error => sendResponse({ success: false, error: error.message }));
    return true;
  }

  if (message.type === 'VALIDATE_TOKEN') {
    validateToken(message.token, message.username)
      .then(result => sendResponse(result))
      .catch(error => sendResponse({ valid: false, error: error.message }));
    return true;
  }

  if (message.type === 'GET_CONFIG') {
    Promise.all([getToken(), getUsername()])
      .then(([token, username]) => {
        sendResponse({ hasToken: !!token, hasUsername: !!username, username });
      });
    return true;
  }
});

// Extension install/update handler
chrome.runtime.onInstalled.addListener((details) => {
  if (details.reason === 'install') {
    chrome.tabs.create({ url: 'settings.html' });
  }
});
