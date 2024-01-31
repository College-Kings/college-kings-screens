from dataclasses import dataclass, field
from renpy.display.core import Displayable

from renpy.display.transform import Transform

global_replay_scope: dict[str, object] = {}

"""renpy
init python:
"""


@dataclass
class SceneGallery:
    _title: str
    _image: str
    label: str
    scope: dict[str, object] = field(default_factory=dict)

    @property
    def title(self) -> str:
        return self._title.upper()

    @property
    def idle_image(self) -> "Displayable":
        try:
            return self._idle_image
        except AttributeError:
            self.idle_image = Transform(self._image, size=(362, 230), pos=(6, 16))
            return self._idle_image

    @idle_image.setter
    def idle_image(self, value: "Displayable") -> None:
        self._idle_image: Displayable = value

    @property
    def locked_image(self) -> "Displayable":
        try:
            return self._locked_image
        except AttributeError:
            self.locked_image = Transform(
                self._image, blur=50, size=(362, 230), pos=(6, 16)
            )
            return self._locked_image

    @locked_image.setter
    def locked_image(self, value: "Displayable") -> None:
        self._locked_image: Displayable = value


def update_scope(new_scope: dict[str, object]) -> dict[str, object]:
    rv: dict[str, object] = global_replay_scope.copy()
    rv.update(new_scope)
    return rv
