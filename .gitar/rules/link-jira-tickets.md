---
title: "Link PRs to Jira tickets"
description: "When a PR title contains a Jira-style ticket key, link to the ticket and post a summary comment."
when: "A pull request is opened or its title is edited, and the title matches the pattern [ABC-123] (uppercase letters, hyphen, digits)."
actions: "Fetch the referenced Jira ticket. Add a comment on the PR containing the ticket summary, status, and assignee. Edit the PR description to include a 'Jira: <ticket-url>' line at the top if not already present."
integrations: ["jira"]
---

# Details

Expected Jira project keys for this repo: `DEMO`, `GTR`, `OPS`. If a PR title contains a key from a different project, still post the comment but note that the project key is unfamiliar.

Skip this rule for draft PRs. If the rule has already added a comment on a previous revision, do not post a duplicate — update the existing comment in place.
