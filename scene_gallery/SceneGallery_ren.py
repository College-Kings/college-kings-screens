from dataclasses import dataclass, field

from renpy.display.transform import Transform

global_replay_scope: dict[str, object]

"""renpy
init python:
"""


@dataclass
class SceneGallery:
    title: str
    image: str
    label: str
    scope: dict[str, object] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.title = self.title.upper()
        self.idle_image = Transform(self.image, size=(362, 230), pos=(6, 16))
        self.locked_image = Transform(self.image, blur=50, size=(362, 230), pos=(6, 16))


def update_scope(new_scope: dict[str, object]) -> dict[str, object]:
    rv: dict[str, object] = global_replay_scope.copy()
    rv.update(new_scope)
    return rv
