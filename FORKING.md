# 🍴 Forking Open Grouch

This guide documents everything needed to properly fork Open Grouch and set it up as an independent project for demos, development, or customization.

## Overview

Open Grouch is a personality fork of OpenHands-CLI. When you fork it, you'll want to:
1. Update package identity (name, repository URLs)
2. Configure GitHub Actions secrets
3. Set up automated PR reviews
4. Configure release automation
5. Update installation instructions

---

## Step 1: Fork the Repository

1. Go to [github.com/jpshackelford/open-grouch](https://github.com/jpshackelford/open-grouch)
2. Click **Fork** (top-right)
3. Choose your account/organization
4. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-FORK-NAME.git
   cd YOUR-FORK-NAME
   ```

---

## Step 2: Update Package Identity

### 2.1 Update `pyproject.toml`

Change the following fields to match your fork:

```toml
[project]
name = "your-package-name"  # e.g., "my-grouch-fork"
description = "Your description here"
authors = [
  { name = "Your Name" },
]

# Entry points - update command name if desired
scripts = { your-command = "grouch.entrypoint:main", "your-command-acp" = "openhands_cli.acp_cli:main" }
```

### 2.2 Update `release-please-config.json`

Update the package name:

```json
{
  "packages": {
    ".": {
      "package-name": "your-package-name"
    }
  }
}
```

### 2.3 Update `.release-please-manifest.json`

Reset version if starting fresh:

```json
{
  ".": "0.1.0"
}
```

### 2.4 Update `README.md`

Replace all references to the original repository:

- `github.com/jpshackelford/open-grouch` → `github.com/YOUR-USERNAME/YOUR-FORK-NAME`
- Installation commands
- Badge URLs (if any)
- Clone URLs

---

## Step 3: Configure GitHub Actions

### Required: No Secrets Needed for Basic CI

These workflows work immediately without configuration:
- **`tests.yml`** - Unit and snapshot tests
- **`lint.yml`** - Pre-commit linting
- **`commit-lint.yml`** - Conventional commit validation
- **`check-package-versions.yml`** - Dependency version checks

### Optional: PR Review by OpenHands

The `pr-review-by-openhands.yml` workflow provides automated AI code reviews.

**To enable:**

1. **Create repository secret `LLM_API_KEY`**:
   - Go to your fork → Settings → Secrets and variables → Actions
   - Click **New repository secret**
   - Name: `LLM_API_KEY`
   - Value: Your LiteLLM proxy key or OpenAI API key

2. **Update the workflow** (if using a different LLM endpoint):
   ```yaml
   # In .github/workflows/pr-review-by-openhands.yml
   with:
       llm-model: litellm_proxy/claude-sonnet-4-5-20250929  # Your model
       llm-base-url: https://your-llm-endpoint.com          # Your endpoint
       llm-api-key: ${{ secrets.LLM_API_KEY }}
   ```

3. **Alternative: Disable the workflow**:
   - Delete `.github/workflows/pr-review-by-openhands.yml`, or
   - Rename it to `.github/workflows/pr-review-by-openhands.yml.disabled`

### Upstream Sync

The `upstream-sync.yml` workflow automatically syncs with the original Open Grouch repository.

**Recommended: Disable upstream sync**

Unless you want to track new changes from jpshackelford/open-grouch or want to handle complex merges directly from OpenHands-CLI, disable upstream sync:
```bash
rm .github/workflows/upstream-sync.yml
```

**Advanced: If you want to maintain sync**

*Option A: Keep syncing with jpshackelford/open-grouch*
- No changes needed

*Option B: Sync with upstream OpenHands-CLI instead*
- Modify the upstream URL in the workflow:
  ```yaml
  git remote add upstream https://github.com/OpenHands/OpenHands-CLI.git
  ```

### Optional: Automatic Releases

The `release.yml` workflow uses release-please for automatic versioning and GitHub Releases.

**This works automatically** using `GITHUB_TOKEN` (no additional secrets needed).

If you don't want automatic releases:
- Delete `.github/workflows/release.yml`
- Delete `release-please-config.json`
- Delete `.release-please-manifest.json`

---

## Step 4: Verify Your Fork Works Locally

Before pushing to GitHub, verify your fork works locally.

### Run the test suite:

```bash
make install-dev
make lint
make test
make test-snapshots
```

### Test local development:

```bash
uv sync
uv run your-command --help  # or whatever you named your entrypoint
```

---

## Step 5: Push and Test Remote Installation

After verifying locally, push your changes and test installation from GitHub:

### Push your changes:

```bash
git add .
git commit -m "chore: update package identity for fork"
git push origin main
```

### Test installation from GitHub:

#### Using uv (Recommended)

```bash
# Install latest
uv tool install git+https://github.com/YOUR-USERNAME/YOUR-FORK-NAME.git

# Install specific version/tag
uv tool install git+https://github.com/YOUR-USERNAME/YOUR-FORK-NAME.git@v0.1.0

# Install from a specific branch
uv tool install git+https://github.com/YOUR-USERNAME/YOUR-FORK-NAME.git@main
```

#### Using pip

```bash
pip install git+https://github.com/YOUR-USERNAME/YOUR-FORK-NAME.git
```

### Test PR review workflow:

1. Create a test branch
2. Make a small change
3. Open a PR
4. Verify the PR review triggers (if configured)

---

## Complete Checklist

Use this checklist when setting up your fork:

### Package Identity
- [ ] Updated `name` in `pyproject.toml`
- [ ] Updated `description` in `pyproject.toml`
- [ ] Updated `authors` in `pyproject.toml`
- [ ] Updated entry point commands in `pyproject.toml` (if desired)
- [ ] Updated `package-name` in `release-please-config.json`
- [ ] Reset version in `.release-please-manifest.json` (optional)
- [ ] Updated all URLs in `README.md`
- [ ] Updated installation commands in `README.md`

### GitHub Configuration
- [ ] Forked repository created
- [ ] Repository cloned locally
- [ ] Changes pushed to your fork

### GitHub Actions (Optional)
- [ ] `LLM_API_KEY` secret configured (for PR reviews)
- [ ] Upstream sync workflow configured/disabled as needed
- [ ] Release workflow tested or disabled as needed

### Verification
- [ ] `make lint` passes
- [ ] `make test` passes
- [ ] Installation from fork works
- [ ] CLI command runs correctly

---

## Troubleshooting

### "Package not found" when installing

Ensure you've pushed your `pyproject.toml` changes:
```bash
git add pyproject.toml release-please-config.json
git commit -m "chore: update package identity for fork"
git push origin main
```

### PR review workflow doesn't run on external contributor PRs

**Expected behavior**: PRs from external contributors (forks of your fork) won't trigger the PR review workflow. This is a security feature - GitHub doesn't expose secrets to workflows triggered by external PRs to prevent malicious code from accessing your API keys. The workflow is configured to only run for PRs from the same repository.

### Tests fail after forking

1. Check if you've updated any hardcoded repository URLs in tests
2. Ensure all dependencies are properly synced: `uv sync --group dev`
3. Run `make lint` to ensure code formatting is correct

### Release workflow doesn't trigger

Release-please only triggers on pushes to `main` branch. Ensure:
1. You're pushing to `main` (not a feature branch)
2. Your commit messages follow conventional commit format
3. The workflow file exists and is not disabled

---

## Files Reference

| File | Purpose | Needs Update? |
|------|---------|---------------|
| `pyproject.toml` | Package metadata | **Yes** |
| `README.md` | Documentation | **Yes** |
| `release-please-config.json` | Release automation | **Yes** |
| `.release-please-manifest.json` | Version tracking | Optional |
| `.github/workflows/pr-review-by-openhands.yml` | AI code reviews | Configure or disable |
| `.github/workflows/upstream-sync.yml` | Sync with upstream | Configure or disable |
| `.github/workflows/release.yml` | Automatic releases | Works automatically |
| `.github/workflows/tests.yml` | CI tests | Works automatically |
| `.github/workflows/lint.yml` | Linting | Works automatically |
| `CONTRIBUTING.md` | Contribution guide | Update repo URLs |
| `AGENTS.md` | Development guide | Update repo URLs |

---

## Security Notes

- **Never commit API keys** to your repository
- Use GitHub Secrets for all sensitive values
- The `LLM_API_KEY` secret is only needed for the PR review feature
- All other workflows use the built-in `GITHUB_TOKEN`

---

*Questions? Open an issue on the original repo or your fork.*
