# gitar-demo-python

A minimal Flask API used to demo [Gitar.ai](https://gitar.ai) features on stage. The `main` branch is the clean baseline — tests pass, no obvious smells. Demo PRs are stacked on top to showcase what Gitar catches.

## Quickstart

```bash
pip install -r requirements.txt
pytest
flask --app app run
```

Then in another shell:

```bash
curl localhost:5000/items
curl -XPOST -H 'content-type: application/json' -d '{"title":"hello"}' localhost:5000/items
curl 'localhost:5000/search?q=hello'
```

## Demo flow

| PR branch | Issue introduced | Gitar feature demoed |
|---|---|---|
| `demo/ssrf-in-search` | `/search` fetches `q` as a URL via `urllib` — SSRF | Code review — Security / Critical |
| `demo/quadratic-dedupe` | O(n²) duplicate check on `POST /items` | Code review — Performance |
| `demo/off-by-one-delete` | `DELETE /items/<id>` deletes `id-1` instead of `id` | Code review — Bug |
| `demo/no-type-hints` | Strips type hints, adds magic numbers, renames vars to `x`/`y` | Code review — Code Quality |
| `demo/break-response-shape` | `POST /items` returns `{data: item}` — breaks `test_create_and_get` | CI failure analysis |
| `demo/[DEMO-42]-rename` | PR title `[DEMO-42] Rename item to task` | Repository rules — Jira link |

## Layout

- `app.py` — Flask app, 5 endpoints
- `storage.py` — in-memory `Store`, no persistence
- `tests/test_app.py` — pytest + Flask test client
- `.github/workflows/ci.yml` — runs `pytest` on every PR
- `.gitar/review/instructions.md` — custom code-review guidance for Gitar
- `.gitar/rules/*.md` — natural-language repository rules
