from flask import Flask, Response, abort, jsonify, request

from storage import Store

app = Flask(__name__)
store = Store()


@app.get("/items")
def list_items():
    return jsonify(store.all())


@app.post("/items")
def create_item() -> tuple[Response, int]:
    body = request.get_json(silent=True) or {}
    title = body.get("title")
    if not isinstance(title, str) or not title.strip():
        abort(400, description="title is required")
    tags = body.get("tags", [])
    if not isinstance(tags, list):
        abort(400, description="tags must be a list of strings")
    unique_tags = list(set(str(t) for t in tags))
    item = store.create(title=title.strip(), tags=unique_tags)
    return jsonify({"data": item}), 201


@app.get("/items/<int:item_id>")
def get_item(item_id: int):
    item = store.get(item_id)
    if item is None:
        abort(404)
    return jsonify(item)


@app.delete("/items/<int:item_id>")
def delete_item(item_id: int):
    if not store.delete(item_id):
        abort(404)
    return "", 204

#This is simple commit
@app.get("/search")
def search():
    query = request.args.get("q", "").strip()
    if not query:
        return jsonify([])
    return jsonify(store.search(query))


if __name__ == "__main__":
    app.run(debug=False)
