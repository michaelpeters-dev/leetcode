// GleetCode Content Script
// Runs on LeetCode problem pages to detect submissions

(function() {
  'use strict';

  let isProcessing = false;
  let lastSubmissionTime = 0;
  const DEBOUNCE_MS = 3000;

  // Extract problem info from URL and page
  function getProblemInfo() {
    const url = window.location.href;
    const pathMatch = url.match(/\/problems\/([^\/]+)/);
    const problemSlug = pathMatch ? pathMatch[1] : null;

    let problemNumber = null;
    let problemTitle = null;
    let difficulty = null;

    // Method 1: Try the problem title element (new UI)
    const titleElement = document.querySelector('[data-cy="question-title"]') ||
                         document.querySelector('.text-title-large') ||
                         document.querySelector('div[class*="text-title-large"]') ||
                         document.querySelector('a[href*="/problems/"] span.text-lg');

    if (titleElement) {
      const titleText = titleElement.textContent.trim();
      const match = titleText.match(/^(\d+)\.\s*(.+)$/);
      if (match) {
        problemNumber = match[1];
        problemTitle = match[2].trim();
      }
    }

    // Method 2: Try document title
    if (!problemNumber) {
      const docTitle = document.title;
      const match = docTitle.match(/^(\d+)\.\s*([^-]+)/);
      if (match) {
        problemNumber = match[1];
        problemTitle = match[2].trim();
      }
    }

    // Method 3: Check meta tags
    if (!problemNumber) {
      const metaTitle = document.querySelector('meta[property="og:title"]');
      if (metaTitle) {
        const content = metaTitle.getAttribute('content');
        const match = content.match(/^(\d+)\.\s*(.+?)(?:\s*-\s*LeetCode)?$/);
        if (match) {
          problemNumber = match[1];
          problemTitle = match[2].trim();
        }
      }
    }

    // Get difficulty
    const difficultyElement = document.querySelector('[class*="text-difficulty-easy"]') ||
                              document.querySelector('[class*="text-difficulty-medium"]') ||
                              document.querySelector('[class*="text-difficulty-hard"]') ||
                              document.querySelector('[diff]') ||
                              document.querySelector('.text-olive') ||
                              document.querySelector('.text-yellow') ||
                              document.querySelector('.text-pink');

    if (difficultyElement) {
      const text = difficultyElement.textContent.toLowerCase();
      const className = difficultyElement.className.toLowerCase();

      if (text.includes('easy') || className.includes('easy') || className.includes('olive')) {
        difficulty = 'Easy';
      } else if (text.includes('medium') || className.includes('medium') || className.includes('yellow')) {
        difficulty = 'Medium';
      } else if (text.includes('hard') || className.includes('hard') || className.includes('pink')) {
        difficulty = 'Hard';
      }
    }

    // Fallback: search for difficulty text in common locations
    if (!difficulty) {
      const possibleDiffElements = document.querySelectorAll('div[class*="text-"], span[class*="text-"]');
      for (const el of possibleDiffElements) {
        const text = el.textContent.trim().toLowerCase();
        if (text === 'easy') { difficulty = 'Easy'; break; }
        if (text === 'medium') { difficulty = 'Medium'; break; }
        if (text === 'hard') { difficulty = 'Hard'; break; }
      }
    }

    return {
      slug: problemSlug,
      number: problemNumber,
      title: problemTitle,
      difficulty: difficulty || 'Unknown',
      url: `https://leetcode.com/problems/${problemSlug}/`
    };
  }

  // Get the current code from Monaco editor via DOM
  function getCodeFromEditor() {
    // Method 1: Get from Monaco view-lines (most reliable for visible code)
    const monacoEditor = document.querySelector('.monaco-editor');
    if (monacoEditor) {
      const viewLines = monacoEditor.querySelector('.view-lines');
      if (viewLines) {
        const lines = viewLines.querySelectorAll('.view-line');
        if (lines.length > 0) {
          const codeLines = [];
          lines.forEach((line, index) => {
            // Get the raw text content, preserving structure
            let lineText = '';
            const spans = line.querySelectorAll('span');
            if (spans.length > 0) {
              spans.forEach(span => {
                lineText += span.textContent;
              });
            } else {
              lineText = line.textContent;
            }
            codeLines.push(lineText);
          });

          const code = codeLines.join('\n');
          if (code.trim()) return code;
        }
      }
    }

    // Method 2: Try to get from the editor's textarea (Monaco's hidden input)
    const inputArea = document.querySelector('.monaco-editor textarea.inputarea');
    if (inputArea && inputArea.value) {
      return inputArea.value;
    }

    // Method 3: Try CodeMirror (older LeetCode UI)
    const codeMirror = document.querySelector('.CodeMirror');
    if (codeMirror && codeMirror.CodeMirror) {
      return codeMirror.CodeMirror.getValue();
    }

    // Method 4: Get from any visible code element
    const codeElements = document.querySelectorAll('[class*="editor"] .view-line, .code-area .view-line');
    if (codeElements.length > 0) {
      return Array.from(codeElements).map(el => el.textContent).join('\n');
    }

    return null;
  }

  // Get the selected language
  function getSelectedLanguage() {
    const langButton = document.querySelector('[data-cy="lang-select"]') ||
                       document.querySelector('button[id*="headlessui-listbox-button"]') ||
                       document.querySelector('div[class*="rounded"][class*="flex"] button');

    if (langButton) {
      const text = langButton.textContent.trim().toLowerCase();
      if (text.includes('python')) return 'python';
      if (text.includes('java')) return 'java';
      if (text.includes('javascript')) return 'javascript';
      if (text.includes('c++')) return 'cpp';
      return text;
    }

    const langIndicator = document.querySelector('[class*="language"]') ||
                          document.querySelector('[data-mode-id]');
    if (langIndicator) {
      const mode = langIndicator.getAttribute('data-mode-id') || langIndicator.textContent;
      return mode.toLowerCase();
    }

    return 'python';
  }

  // Wait for submission result
  function waitForResult(timeout = 30000) {
    return new Promise((resolve, reject) => {
      const startTime = Date.now();

      const checkResult = () => {
        if (Date.now() - startTime > timeout) {
          reject(new Error('Timeout waiting for result'));
          return;
        }

        let status = null;
        let runtime = null;
        let memory = null;

        const statusSelectors = [
          '[data-e2e-locator="submission-result"]',
          '[class*="result"] [class*="text-"]',
          '.submission-result',
          '[class*="status"]'
        ];

        for (const selector of statusSelectors) {
          const el = document.querySelector(selector);
          if (el) {
            const text = el.textContent.toLowerCase();
            if (text.includes('accepted')) {
              status = 'Accepted';
              break;
            } else if (text.includes('wrong answer')) {
              status = 'Wrong Answer';
              break;
            } else if (text.includes('time limit')) {
              status = 'Time Limit Exceeded';
              break;
            } else if (text.includes('memory limit')) {
              status = 'Memory Limit Exceeded';
              break;
            } else if (text.includes('runtime error')) {
              status = 'Runtime Error';
              break;
            } else if (text.includes('compile error')) {
              status = 'Compile Error';
              break;
            }
          }
        }

        if (status) {
          const statsElements = document.querySelectorAll('[class*="flex"][class*="items-center"]');
          statsElements.forEach(el => {
            const text = el.textContent;
            const runtimeMatch = text.match(/(\d+)\s*ms/);
            const memoryMatch = text.match(/([\d.]+)\s*MB/);
            if (runtimeMatch) runtime = runtimeMatch[1] + ' ms';
            if (memoryMatch) memory = memoryMatch[1] + ' MB';
          });

          if (!runtime) {
            const runtimeEl = document.querySelector('[class*="runtime"]') ||
                             document.querySelector('[data-e2e-locator="runtime"]');
            if (runtimeEl) {
              const match = runtimeEl.textContent.match(/(\d+)\s*ms/);
              if (match) runtime = match[1] + ' ms';
            }
          }

          if (!memory) {
            const memoryEl = document.querySelector('[class*="memory"]') ||
                            document.querySelector('[data-e2e-locator="memory"]');
            if (memoryEl) {
              const match = memoryEl.textContent.match(/([\d.]+)\s*MB/);
              if (match) memory = match[1] + ' MB';
            }
          }

          resolve({
            status: status,
            runtime: runtime || 'N/A',
            memory: memory || 'N/A'
          });
          return;
        }

        setTimeout(checkResult, 500);
      };

      setTimeout(checkResult, 1000);
    });
  }

  // Get difficulty class
  function getDifficultyClass(difficulty) {
    switch (difficulty.toLowerCase()) {
      case 'easy': return 'gleetcode-easy';
      case 'medium': return 'gleetcode-medium';
      case 'hard': return 'gleetcode-hard';
      default: return '';
    }
  }

  // Show confirmation modal - LeetCode Style
  function showConfirmationModal(problemInfo, result) {
    return new Promise((resolve) => {
      const existingModal = document.getElementById('gleetcode-modal');
      if (existingModal) existingModal.remove();

      const modal = document.createElement('div');
      modal.id = 'gleetcode-modal';
      modal.className = 'gleetcode-modal-overlay';

      const statusClass = result.status === 'Accepted' ? 'gleetcode-accepted' : 'gleetcode-failed';
      const difficultyClass = getDifficultyClass(problemInfo.difficulty);

      modal.innerHTML = `
        <div class="gleetcode-modal">
          <div class="gleetcode-modal-header">
            <h2>Push to GitHub?</h2>
          </div>
          <div class="gleetcode-modal-body">
            <div class="gleetcode-problem-card">
              <div class="gleetcode-problem-title">${problemInfo.number}. ${problemInfo.title}</div>
              <div class="gleetcode-problem-meta">
                <span class="${difficultyClass}">${problemInfo.difficulty}</span>
                <span>Python</span>
              </div>
            </div>
            <div class="gleetcode-stats">
              <div class="gleetcode-stat">
                <div class="gleetcode-stat-label">Status</div>
                <div class="gleetcode-stat-value ${statusClass}">${result.status}</div>
              </div>
              <div class="gleetcode-stat">
                <div class="gleetcode-stat-label">Runtime</div>
                <div class="gleetcode-stat-value">${result.runtime}</div>
              </div>
              <div class="gleetcode-stat">
                <div class="gleetcode-stat-label">Memory</div>
                <div class="gleetcode-stat-value">${result.memory}</div>
              </div>
              <div class="gleetcode-stat">
                <div class="gleetcode-stat-label">Repository</div>
                <div class="gleetcode-stat-value">leetcode</div>
              </div>
            </div>
          </div>
          <div class="gleetcode-modal-footer">
            <button id="gleetcode-no" class="gleetcode-btn gleetcode-btn-secondary">Cancel</button>
            <button id="gleetcode-yes" class="gleetcode-btn gleetcode-btn-primary">Push to GitHub</button>
          </div>
        </div>
      `;

      document.body.appendChild(modal);

      document.getElementById('gleetcode-yes').addEventListener('click', () => {
        modal.remove();
        resolve(true);
      });

      document.getElementById('gleetcode-no').addEventListener('click', () => {
        modal.remove();
        resolve(false);
      });

      modal.addEventListener('click', (e) => {
        if (e.target === modal) {
          modal.remove();
          resolve(false);
        }
      });

      // ESC key to close
      const escHandler = (e) => {
        if (e.key === 'Escape') {
          modal.remove();
          document.removeEventListener('keydown', escHandler);
          resolve(false);
        }
      };
      document.addEventListener('keydown', escHandler);
    });
  }

  // Show notification
  function showNotification(message, isError = false) {
    const notification = document.createElement('div');
    notification.className = `gleetcode-notification ${isError ? 'gleetcode-error' : 'gleetcode-success'}`;
    notification.textContent = message;
    document.body.appendChild(notification);

    setTimeout(() => {
      notification.classList.add('gleetcode-fade-out');
      setTimeout(() => notification.remove(), 300);
    }, 3000);
  }

  // Main submission handler
  async function handleSubmission() {
    if (isProcessing) return;

    const now = Date.now();
    if (now - lastSubmissionTime < DEBOUNCE_MS) return;
    lastSubmissionTime = now;
    isProcessing = true;

    try {
      const problemInfo = getProblemInfo();
      if (!problemInfo.number || !problemInfo.title) {
        console.log('GleetCode: Could not extract problem info');
        isProcessing = false;
        return;
      }

      const code = getCodeFromEditor();
      if (!code) {
        console.log('GleetCode: Could not extract code');
        showNotification('Could not extract code from editor', true);
        isProcessing = false;
        return;
      }

      const language = getSelectedLanguage();
      const result = await waitForResult();
      const confirmed = await showConfirmationModal(problemInfo, result);

      if (confirmed) {
        const response = await chrome.runtime.sendMessage({
          type: 'PUSH_SOLUTION',
          data: {
            problemNumber: problemInfo.number,
            problemTitle: problemInfo.title,
            problemSlug: problemInfo.slug,
            problemUrl: problemInfo.url,
            difficulty: problemInfo.difficulty,
            code: code,
            language: language,
            status: result.status,
            runtime: result.runtime,
            memory: result.memory,
            timestamp: new Date().toISOString()
          }
        });

        if (response && response.success) {
          showNotification('Pushed to GitHub successfully!');
        } else {
          showNotification(response?.error || 'Failed to push', true);
        }
      }
    } catch (error) {
      console.error('GleetCode error:', error);
      if (error.message.includes('Extension context invalidated')) {
        showNotification('Please refresh the page', true);
      } else {
        showNotification('Error: ' + error.message, true);
      }
    } finally {
      isProcessing = false;
    }
  }

  // Set up submit button listener
  function setupSubmitListener() {
    document.addEventListener('click', (event) => {
      const target = event.target;
      const submitButton = target.closest('[data-e2e-locator="console-submit-button"]') ||
                          target.closest('button[data-cy="submit-code-btn"]') ||
                          target.closest('button:not([disabled])');

      if (submitButton) {
        const buttonText = submitButton.textContent.toLowerCase();
        if (buttonText.includes('submit')) {
          setTimeout(handleSubmission, 500);
        }
      }
    }, true);

    document.addEventListener('keydown', (event) => {
      if ((event.ctrlKey || event.metaKey) && event.key === 'Enter') {
        const activeElement = document.activeElement;
        if (activeElement && (
            activeElement.classList.contains('inputarea') ||
            activeElement.closest('.monaco-editor')
        )) {
          setTimeout(handleSubmission, 500);
        }
      }
    }, true);
  }

  // Initialize
  function init() {
    setupSubmitListener();
    console.log('GleetCode: Content script loaded');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
