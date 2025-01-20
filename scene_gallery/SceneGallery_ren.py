from typing import Optional
from renpy.display.displayable import Displayable

from renpy.display.transform import Transform

global_replay_scope: dict[str, object] = {}

"""renpy
init python:
"""


class SceneGallery:
    def __init__(
        self,
        title: str,
        image: str,
        label: str,
        scope: Optional[dict[str, object]] = None,
    ) -> None:
        self._title: str = title
        self.idle_image: "Displayable" = Transform(image, size=(362, 230), pos=(6, 16))
        self.locked_image: "Displayable" = Transform(self.idle_image, blur=50)
        self.label: str = label
        self.scope: dict[str, object] = scope or {}

    @property
    def title(self) -> str:
        return self._title.upper()


def update_scope(new_scope: dict[str, object]) -> dict[str, object]:
    rv: dict[str, object] = global_replay_scope.copy()
    rv.update(new_scope)
    return rv
