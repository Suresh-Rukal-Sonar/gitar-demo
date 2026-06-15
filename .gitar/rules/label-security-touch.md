---
title: "Label PRs touching security-sensitive files"
description: "Auto-label PRs that modify storage, request-handling, or auth code so security reviewers see them."
when: "A pull request adds, modifies, or deletes any file matching app.py, storage.py, or anything under auth/."
actions: "Add the 'security-review' label to the PR. Request review from @security-owners. Post a comment listing the touched files and reminding the author to include a threat-model note in the PR description."
---

# Details

The label `security-review` must exist on the repo. If missing, create it with color `#d73a4a` and description "Touches auth, storage, or HTTP request handling — needs a security pass."

Do not duplicate the comment or re-request review if the label is already present (the rule has already run on a prior revision).
