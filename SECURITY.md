# Security Vulnerability Report

## Vulnerability: Hardcoded Secret Key

### Where
`app.py`, line 8

### What I did
I hardcoded a secret key directly in the source code:

SECRET_KEY = "supersecret123"

### Why this is a problem
Once code goes into a Git repository, that value is basically public — especially if the repo is public on GitHub. Even if you delete the line later, it stays in the commit history. Anyone who finds it can use it to forge session tokens or impersonate users, because the key is what the app uses to sign and verify those tokens.

In short: hardcoded secrets in source code are one of the most common real-world vulnerabilities, and one of the easiest to avoid.

### Severity
High — this falls under CWE-798 (Use of Hard-coded Credentials)

### The fix
Load the secret from an environment variable instead:

SECRET_KEY = os.environ.get("SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is not set")

The actual value then lives outside the codebase:
- Locally — in a .env file that never gets committed
- Render.com — set it under Environment Variables in the dashboard
- GitHub Actions — add it under Settings -> Secrets and Variables -> Actions

This is exactly how RENDER_DEPLOY_HOOK_URL is handled in the pipeline — stored as a GitHub Secret, never written in the code.

### One more thing
Make sure .env is in your .gitignore. It already is in this project, but it is worth stating explicitly — a .env file with real secrets that accidentally gets pushed is just as bad as hardcoding them.
