from __future__ import annotations

from threading import Lock


class Store:
    def __init__(self) -> None:
        self._items: dict[int, dict] = {}
        self._next_id: int = 1
        self._lock = Lock()

    def reset(self) -> None:
        with self._lock:
            self._items.clear()
            self._next_id = 1

    def all(self) -> list[dict]:
        with self._lock:
            return list(self._items.values())

    def get(self, item_id: int) -> dict | None:
        with self._lock:
            return self._items.get(item_id)

    def create(self, title: str, tags: list[str]) -> dict:
        with self._lock:
            item = {"id": self._next_id, "title": title, "tags": list(tags)}
            self._items[self._next_id] = item
            self._next_id += 1
            return item

    def delete(self, item_id: int) -> bool:
        with self._lock:
            return self._items.pop(item_id, None) is not None

    def search(self, query: str) -> list[dict]:
        needle = query.lower()
        with self._lock:
            return [i for i in self._items.values() if needle in i["title"].lower()]
