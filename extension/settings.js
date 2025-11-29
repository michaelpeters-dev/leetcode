// GleetCode Settings Page Script

document.addEventListener('DOMContentLoaded', async () => {
  // Settings elements
  const form = document.getElementById('settings-form');
  const usernameInput = document.getElementById('username');
  const tokenInput = document.getElementById('token');
  const saveBtn = document.getElementById('save-btn');
  const statusDiv = document.getElementById('status');
  const currentUsername = document.getElementById('current-username');
  const currentToken = document.getElementById('current-token');

  // Load current configuration
  async function loadConfig() {
    try {
      const result = await chrome.storage.local.get(['github_username', 'github_token']);

      if (result.github_username) {
        currentUsername.textContent = result.github_username;
        currentUsername.classList.remove('not-set');
        currentUsername.classList.add('success');
        usernameInput.value = result.github_username;
      } else {
        currentUsername.textContent = 'Not configured';
        currentUsername.classList.add('not-set');
        currentUsername.classList.remove('success');
      }

      if (result.github_token) {
        currentToken.textContent = '••••••••' + result.github_token.slice(-4);
        currentToken.classList.remove('not-set');
        currentToken.classList.add('success');
      } else {
        currentToken.textContent = 'Not configured';
        currentToken.classList.add('not-set');
        currentToken.classList.remove('success');
      }
    } catch (error) {
      console.error('Error loading config:', error);
    }
  }

  // Show status message
  function showStatus(element, message, type) {
    const icon = element.querySelector('.status-icon') || element;
    const text = element.querySelector('.status-text');

    if (text) {
      text.textContent = message;
    } else {
      element.innerHTML = `<span class="status-icon"></span><span class="status-text">${message}</span>`;
    }

    element.className = `status ${type}`;

    const iconEl = element.querySelector('.status-icon');
    if (iconEl) {
      if (type === 'success') iconEl.textContent = '✓';
      else if (type === 'error') iconEl.textContent = '✕';
      else iconEl.textContent = 'i';
    }
  }

  // Hide status message
  function hideStatus(element) {
    element.className = 'status';
  }

  // Set loading state
  function setLoading(loading) {
    if (loading) {
      saveBtn.disabled = true;
      saveBtn.innerHTML = '<span class="loading"></span> Validating...';
    } else {
      saveBtn.disabled = false;
      saveBtn.textContent = 'Save & Validate';
    }
  }

  // Form submission handler
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    hideStatus(statusDiv);

    const username = usernameInput.value.trim();
    const token = tokenInput.value.trim();

    if (!username) {
      showStatus(statusDiv, 'Please enter your GitHub username', 'error');
      return;
    }

    if (!token) {
      showStatus(statusDiv, 'Please enter your GitHub token', 'error');
      return;
    }

    if (!token.startsWith('ghp_') && !token.startsWith('github_pat_')) {
      showStatus(statusDiv, 'Token should start with "ghp_" or "github_pat_"', 'error');
      return;
    }

    setLoading(true);

    try {
      const response = await chrome.runtime.sendMessage({
        type: 'VALIDATE_TOKEN',
        token: token,
        username: username
      });

      if (response.valid) {
        await chrome.storage.local.set({
          github_username: username,
          github_token: token
        });

        showStatus(statusDiv, `Connected to ${response.repoName}`, 'success');
        loadConfig();
        tokenInput.value = '';
      } else {
        showStatus(statusDiv, response.error || 'Validation failed', 'error');
      }
    } catch (error) {
      showStatus(statusDiv, 'Error: ' + error.message, 'error');
    } finally {
      setLoading(false);
    }
  });

  // Initial load
  loadConfig();
});
