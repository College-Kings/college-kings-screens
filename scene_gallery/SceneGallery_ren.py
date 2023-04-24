"""renpy
init python:
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any

if TYPE_CHECKING:
    from renpy.exports import store


class SceneGallery:
    items: list[SceneGallery] = []

    def __init__(
        self, title: str, image: str, label: str, scope: Optional[dict[str, Any]] = None
    ) -> None:
        self.title: str = title.upper()
        self.idle_image = Transform(image, size=(362, 230), pos=(6, 16))  # type: ignore
        self.locked_image = Transform(image, blur=50, size=(362, 230), pos=(6, 16))  # type: ignore
        self.label: str = label

        if scope is None:
            self.scope: dict[str, Any] = {}
        else:
            self.scope: dict[str, Any] = scope


def update_scope(new_scope: dict[str, Any]) -> dict[str, Any]:
    rv: dict[str, Any] = store.scopeDict.copy()
    rv.update(new_scope)
    return rv
