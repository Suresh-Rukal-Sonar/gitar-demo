# Review instructions for gitar-demo-python

Apply these checks in addition to the default review.

- **Never accept** `eval`, `exec`, `os.system`, `subprocess.*` with `shell=True`, or `pickle.loads` on untrusted input. Flag as Critical / Security.
- **Type hints required** on every public function and method. Missing hints → Suggestion severity.
- **No O(n²) patterns** where a `set` or `dict` lookup would do. Flag as Performance.
- **New endpoints in `app.py` must include at least one pytest test** in `tests/`. Flag as Code Quality if missing.
- **No hard-coded secrets** (API keys, tokens, passwords, connection strings). Flag as Critical / Security.
- **HTTP request inputs** (`request.args`, `request.get_json`, headers) must be validated before use. Missing validation → Bug or Security depending on impact.
- Prefer existing helpers in `storage.py` over re-implementing list/dict scans in `app.py`.
- When a PR changes the JSON shape of an endpoint response, the corresponding test in `tests/test_app.py` must be updated in the same PR.
