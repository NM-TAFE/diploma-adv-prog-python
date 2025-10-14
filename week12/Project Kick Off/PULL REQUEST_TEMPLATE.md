# Pull Request Title

_Provide a concise, descriptive title (e.g., “Add Observer Pattern for Prediction Logging”)._

---

## 1. Summary of Changes

Describe what was added, updated, or fixed in this pull request.

-   Which module(s) were affected (`ml/`, `api/`, `classifier/`, etc.)
-   What problem or requirement does this PR address?
-   Briefly summarise any design decisions or trade-offs.

---

## 2. Related Issues

Link to one or more existing issues:

-   Resolves #
-   Addresses #
-   Related to #

Each PR should close or reference at least one tracked issue.

---

## 3. Implementation Details

Explain technical highlights of this PR.

-   [ ] Uses separation of concerns correctly (views, serializers, ML logic, templates separated)
-   [ ] Includes authentication or permissions checks if applicable
-   [ ] Integrates the logging decorator or observer pattern where needed
-   [ ] Adds or modifies database models or migrations
-   [ ] Updates UI templates for responsiveness or improved UX
-   [ ] Adds or updates documentation / comments

---

## 4. Testing Summary

Summarise the tests you ran to verify your changes.

-   [ ] Unit tests created and passing
-   [ ] Integration or API endpoint tests passing
-   [ ] Manual verification via browser or Postman
-   [ ] Logging output checked in `logs/app.log`
-   [ ] Error handling tested with invalid inputs
-   [ ] Code coverage confirmed ≥ 80%

Provide a short log or output snippet if useful.

---

## 5. Deployment Notes

Confirm your deployment or environment checks.

-   [ ] Application successfully runs on local dev environment
-   [ ] Static files collected (`collectstatic` run)
-   [ ] `.env` or settings updated (no secrets in code)
-   [ ] Deployed to Proxmox VM and verified via URL or IP
-   [ ] Systemd service is active (`systemctl status`)

If deployment not yet complete, describe what remains.

---

## 6. Journal Update

Each student must update their project journal in `docs/journal.md`.

-   [ ] Journal entry added for this feature
-   [ ] Describes key learning, decisions, or debugging steps

---

## 7. Review Checklist

Before requesting merge, confirm all the following:

-   [ ] PR description is complete and accurate
-   [ ] Code follows PEP8 / Django conventions
-   [ ] No console errors or linter warnings
-   [ ] No secrets or credentials committed
-   [ ] Peer review requested from at least one classmate or lecturer

---

### Reviewer Notes (Lecturer / Peer)

_This section is for reviewers to record feedback before merging._

**Feedback Summary:**  
...

**Merge Decision:**

-   [ ] Approved
-   [ ] Changes Requested
-   [ ] Closed without merge
