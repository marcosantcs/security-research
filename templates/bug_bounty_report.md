# Bug Bounty Report — [Vulnerability Title]

**Program:** [HackerOne / Bugcrowd / Intigriti]
**Target:** [target.com]
**Date:** [YYYY-MM-DD]
**Severity:** [Critical / High / Medium / Low / Informational]
**CVSS Score:** [0.0 - 10.0]

---

## Summary
Brief description of the vulnerability in 2-3 sentences.

## Vulnerability Details

- **Type:** [e.g. IDOR, SQL Injection, XSS, SSRF]
- **OWASP Category:** [e.g. A01:2025 - Broken Access Control]
- **Endpoint:** `POST /api/v1/users/{id}/profile`
- **Parameter:** `user_id`

## Steps to Reproduce

1. Authenticate as User A (`user_a@email.com`)
2. Send the following request:

```http
GET /api/v1/users/1337/profile HTTP/1.1
Host: target.com
Authorization: Bearer <token_of_user_A>
```

3. Observe that profile data of User B (ID 1337) is returned.

## Impact
Attacker can access/modify data of any user without authorization.
Potential for full account takeover or PII exfiltration.

## Proof of Concept
[Screenshot or response body showing unauthorized data]

## Recommended Fix
Validate that the authenticated user's ID matches the requested resource ID server-side.

## References
- https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/
