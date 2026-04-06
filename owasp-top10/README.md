# OWASP Top 10:2025

Reference: https://owasp.org/Top10/2025/

| # | Category | Severity |
|---|---|---|
| A01 | Broken Access Control | 🔴 Critical |
| A02 | Security Misconfiguration | 🔴 Critical |
| A03 | Software Supply Chain Failures | 🟠 High |
| A04 | Cryptographic Failures | 🔴 Critical |
| A05 | Injection | 🔴 Critical |
| A06 | Insecure Design | 🟠 High |
| A07 | Authentication Failures | 🔴 Critical |
| A08 | Software or Data Integrity Failures | 🟠 High |
| A09 | Security Logging & Alerting Failures | 🟡 Medium |
| A10 | Mishandling of Exceptional Conditions | 🟡 Medium |

## A01 — Broken Access Control
**Description:** User can act outside intended permissions (IDOR, path traversal, privilege escalation).
**Test:** Access `/admin`, `/api/users/1` while authenticated as user ID 2.
**Mitigation:** Deny by default; enforce server-side access control on every request.

## A05 — Injection
**Description:** Untrusted data sent to interpreter as command (SQL, NoSQL, OS, LDAP).
**Test:** `' OR '1'='1` in login fields; `; ls -la` in input fields.
**Mitigation:** Use parameterized queries; never concatenate user input into queries.

## A07 — Authentication Failures
**Description:** Weak passwords, credential stuffing, broken session management.
**Test:** Test rate limiting on `/login`; check if session tokens are invalidated on logout.
**Mitigation:** MFA, rate limiting, secure session management, strong password policy.
