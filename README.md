# gitar-demo-python

A minimal Flask API set up to demo [Gitar.ai](https://gitar.ai) features on stage. `main` is the clean baseline — 6 pytest tests, no obvious smells. Each Gitar feature is staged as a pre-built PR against `main`; a demo operator opens the PR list, picks the one they want, and lets Gitar do the work.

## Quickstart (optional — for local exploration)

```bash
pip install -r requirements.txt
pytest
flask --app app run
```

```bash
curl localhost:5000/items
curl -XPOST -H 'content-type: application/json' -d '{"title":"hello"}' localhost:5000/items
curl 'localhost:5000/search?q=hello'
```

Running the app is **not required for any demo** — every feature is demoed by opening the PR on GitHub and watching Gitar work.

## Demo PRs

All demo PRs target `main` and are intentionally **not merged**. Leave them open; if you want to re-run a demo, close the existing PR (with branch deletion) and re-create it from the same branch.

| # | Feature to demo | What's in the PR | What to show on stage |
|---|---|---|---|
| [#1](https://github.com/Sonar-Gitar-Demos/gitar-demo-python/pull/1) | **Code Review** | Adds bulk-import, remote-import, and admin-clear endpoints. Hidden inside: SSRF, hard-coded secret, off-by-one, missing tests, magic numbers. | Wait for Gitar's dashboard comment. Walk through findings grouped by severity (Critical → Important → Suggestion). Click "Apply" on one fix to demo one-click apply. |
| [#2](https://github.com/Sonar-Gitar-Demos/gitar-demo-python/pull/2) | **Code Review — reference copy** | Identical diff to #1. Kept untouched so you have a clean reference while #1 is being fixed live. | Open side-by-side with #1 during the fix demo if you need to recover the original issue text. |
| [#3](https://github.com/Sonar-Gitar-Demos/gitar-demo-python/pull/3) | **Auto-Approve** | Clean `GET /items/count` endpoint with a single Suggestion-grade nit (`len(store.all())`). All tests pass. | Gitar's review should land on Suggestion-only findings → auto-approve fires. Show the green dashboard verdict. |
| [#4](https://github.com/Sonar-Gitar-Demos/gitar-demo-python/pull/4) | **CI Failure Analysis** | Wraps `POST /items` response in `{"data": item}`. Two tests fail with `KeyError`. | Wait for CI to fail. Gitar reads the log, identifies the response-shape change as the root cause, and offers a fix (revert the envelope or update the two tests). |
| [#8](https://github.com/Sonar-Gitar-Demos/gitar-demo-python/pull/8) | **Repository Rules** | Same PR adds a new rule (`.gitar/rules/no-print-in-production.md`) **and** a `print(...)` call in `app.py`. | Show the new rule file in the diff, then point at Gitar's inline comment on the `print(...)` line — it cites the just-added rule. Cause and effect in one PR. |

## Running a single demo

1. Open the PR from the table above.
2. Wait for the Gitar dashboard comment (usually < 1 min after open / new commit).
3. Drive the demo from that comment — walk the findings, click an Apply / Fix checkbox, or comment `Gitar <instruction>` to give a targeted ask.
4. **Do not merge.** If the PR's branch state drifts (e.g., you applied fixes), close-with-branch-delete and recreate from the original branch.

## Resetting a demo PR

```bash
# Example for #1
gh pr close 1 -d
git checkout demo/bulk-import-and-cleanup
git push -u origin demo/bulk-import-and-cleanup   # if the branch is already deleted, recreate from the commit SHA in this repo's history
gh pr create --title "[Demo: Code Review] Bulk import endpoints — bugs, vulns, quality" --body-file ...
```

In practice, easier to keep the branches around (the original commits are preserved in branch history) and only delete branches you genuinely won't reuse.

## Configuration the demos rely on

- `.gitar/review/instructions.md` — custom code-review guidance Gitar applies on top of its defaults (no `eval`/`os.system`, type hints required, new endpoints need tests, etc.). This shapes what shows up in #1.
- `.gitar/rules/link-jira-tickets.md` — links PRs whose title contains `[ABC-123]` to Jira.
- `.gitar/rules/label-security-touch.md` — labels PRs that modify `app.py`, `storage.py`, or `auth/`.
- `.gitar/rules/no-print-in-production.md` — added inside #8; flags `print()` in production `.py` files.

## Repository layout

- `app.py` — Flask app, 5 endpoints (the baseline; demo PRs modify or extend this)
- `storage.py` — in-memory `Store`, no persistence
- `tests/test_app.py` — pytest + Flask test client (6 tests; demo PRs may add or break tests)
- `.github/workflows/ci.yml` — runs `pytest` on every PR
- `.gitar/` — Gitar config (review instructions + rules)
