# Security Policy

PiCoding is early-stage and does not yet have a formal security response team. Security reports are still welcome and should be handled responsibly.

## Reporting a Security Issue

Please do not open a public GitHub issue for a suspected vulnerability.

Instead, report security concerns through GitHub's private vulnerability reporting feature if it is enabled for this repository. If private reporting is not available, contact the maintainers through the repository owner's preferred GitHub contact path and include only the minimum detail needed to establish a secure reporting channel.

## In Scope

Security issues may include:

- Code execution vulnerabilities in PiCoding tools or examples.
- Unsafe handling of untrusted model inputs, generated code, or files.
- Dependency vulnerabilities that affect project users.
- Prompt or agent workflows that could cause unsafe repository actions.
- Leakage of secrets, credentials, private data, or environment details.
- Supply-chain risks in project automation or release workflows.
- Examples and automation workflows that allow unsafe code execution, exposed secrets, insecure dependencies, or weak input validation.

## Out of Scope

The following are generally out of scope unless they create a concrete vulnerability in this repository:

- General requests for security hardening without a specific issue.
- Vulnerabilities in third-party services not controlled by PiCoding.
- Physical-system safety claims about examples that are clearly marked as educational or illustrative.
- Social engineering reports without a technical repository impact.

## Responsible Disclosure

Please give maintainers a reasonable opportunity to investigate and address security issues before public disclosure. A helpful report includes:

- A concise description of the issue.
- Steps to reproduce, if safe to share.
- Affected files, examples, or workflows.
- Potential impact.
- Suggested mitigation, if known.

Maintainers will aim to acknowledge reports promptly, but response times may vary while the project is small.
