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

    @classmethod
    def create_gallery(cls):
        cls.items = []

        cls.items.append(
            cls(
                "Right here, right now", "images/v1/scene 21a/v1chlcgTPP.webp", "v1s21a"
            )
        )  # 21a, Chloe, v1_chloe
        cls.items.append(
            cls("Fuck while fucked up", "images/v1/scene 25a/v1s25a_17.webp", "v1s25a")
        )  # 25a, Amber, v1_amber
        cls.items.append(
            cls("Lagoon of love", "images/v1/scene 36/v1jenmo2Start.webp", "v1s36_sg")
        )  # 36, Jenny, v1_jenny
        cls.items.append(
            cls("Good Dr. Lauren", "images/v1/scene 46a/v1s46a_12.webp", "v1s46a_sga")
        )  # 46a, Lauren good (scope is Lauren GIRLFRIEND)
        cls.items.append(
            cls("Evil Dr. Lauren", "images/v1/scene 46a/v1s46a_27c.webp", "v1s46a_sgb")
        )  # 46a, Lauren bad
        cls.items.append(
            cls("Messy with Samantha", "images/v1/scene 53a/v1s53a_16.webp", "v1s53_sg")
        )  # 53a, Samantha, v1_samantha

        cls.items.append(
            cls("Angry with Ms. Rose", "images/v2/scene 15/v2s15_7f.webp", "v2s15sg")
        )  # 15, Ms. Rose, v2_rose
        cls.items.append(
            cls(
                "The List (Amber)",
                "images/v2/scene 18a/v2s18aamber_9e.webp",
                "v2s18a_ambersg",
            )
        )  # 18a, Amber, v2_amber
        cls.items.append(
            cls(
                "The List (Aubrey)",
                "images/v2/scene 18c/v2s18c_imau_14.webp",
                "v2s18c_aubreysg",
            )
        )  # 18c, Aubrey, v2_aubrey
        cls.items.append(
            cls(
                "The List (Autumn)",
                "images/v2/scene 18c/v2autkiss.webp",
                "v2s18c_autumnsg",
            )
        )  # 18c, Autumn, v2_autumn
        cls.items.append(
            cls(
                "The List (Penelope)",
                "images/v2/scene 18c/v2s18c_chpe_11.webp",
                "v2s18c_penelopesg",
            )
        )  # 18c, Penelope, v2_penelope
        cls.items.append(
            cls(
                "The List (Riley)",
                "images/v2/scene 18a/v2s18ariley_14.webp",
                "v2s18a_rileysg",
            )
        )  # 18a, Riley, v2_riley
        cls.items.append(
            cls("Birthday treat", "images/v2/scene 18e/v2s18eend_6.webp", "v2s18e_sg")
        )  # 18e, Lauren, v2_lauren
        cls.items.append(
            cls(
                "Late night sexting",
                "images/v2/scene 29/v2s29_emily_lingerie.webp",
                "v2s29_emilysg",
            )
        )  # 29, Emily, v2_emily
        cls.items.append(
            cls(
                "Fun at the wedding",
                "images/v2/scene 33/v2s33_46b.webp",
                "v2s35_naomisg",
            )
        )  # 33, Naomi, v2_naomi
        cls.items.append(
            cls(
                "Choosing Nora",
                "images/v2/scene 48a/v2noror2Start.webp",
                "v2s48a_norasg",
            )
        )  # 48, Nora, v2_nora

        cls.items.append(
            cls(
                "Fighting Tom",
                "images/v3/Scene 1/fight/tom-stances/v3-tom-stance-def.webp",
                "v3s1",
            )
        )  # 1, Tom
        cls.items.append(
            cls("Relaxing with Riley", "images/v3/scene 3a/v3s3a_1a.webp", "v3s3a")
        )  # 3a, Riley, v3_riley
        cls.items.append(
            cls("Classroom distraction", "images/v3/scene 10/v3s10_2g.webp", "v3s10_sg")
        )  # 10, Lauren, v3_lauren
        cls.items.append(
            cls("Emily video call", "images/v3/scene 25/v3s25_11h.webp", "v3s25_sg")
        )  # 25, Emily, v3_emily
        cls.items.append(
            cls("Bad parents", "images/v3/Scene 48a/v3chlfgStart.webp", "v3s48a")
        )  # 48, Chloe, v3_chloe
        cls.items.append(
            cls("Let me show you", "images/v3/Scene 63a/v3norfgStart.webp", "v3s63_sg")
        )  # 63a, Nora, v3_nora
        cls.items.append(
            cls(
                "Lindsey's craving",
                "images/v3/Scene 63c/v3linbjStart.webp",
                "v3s63c_sg",
            )
        )  # 63c, Lindsey, v3_lindsey
        cls.items.append(
            cls(
                "First time with Penelope",
                "images/v3/Scene 71a/v3penst2Start.webp",
                "v3s71_sg",
            )
        )  # 71a, Penelope, v3_penelope

        if store.has_ep2():
            cls.items.append(
                cls("Game jamming", "images/ep2/Scene 7c/ep2s7c_18.webp", "ep2_s7c_sg")
            )  # 7c, Penelope
            cls.items.append(
                cls(
                    "Hardboiled dick",
                    "images/ep2/Scene 11/ep2s11_rose_dryhump2Start.webp",
                    "ep2_s11_sg",
                )
            )  # 11, Rose
            cls.items.append(
                cls(
                    "Blue-sky thinking",
                    "images/ep2/Scene 17f/ep2s17f_9.webp",
                    "ep2_s17f",
                )
            )  # 17f, Lauren
            cls.items.append(
                cls(
                    "Training gone sexual",
                    "images/ep2/Scene 17h/ep2s17h_7.webp",
                    "ep2_s17h",
                )
            )  # 17h, Riley
            cls.items.append(
                cls(
                    "First time for everything",
                    "images/ep2/Scene 20f/ep2s20f_3b.webp",
                    "ep2_s20f",
                )
            )  # 20f, Autumn
            cls.items.append(
                cls(
                    "Nora takes over",
                    "images/ep2/Scene 26b/ep2s26b_17c.webp",
                    "ep2_s26b",
                )
            )  # 26b, Nora
            cls.items.append(
                cls(
                    "Down to business BJ",
                    "images/ep2/Scene 28b/ep2s28b_5.webp",
                    "ep2_s28b",
                )
            )  # 28b, Lauren
            cls.items.append(
                cls(
                    "Bathroom blowjob",
                    "images/ep2/Scene 31a/ep2s31a_32.webp",
                    "ep2_s31a_sg",
                )
            )  # 31a, Naomi
            cls.items.append(
                cls("A quick dip", "images/ep2/Scene 37g/ep2s37g_5.webp", "ep2_s37g")
            )  # 37g, Nora
            cls.items.append(
                cls("Mother may I?", "images/ep2/Scene 39/ep2s39_3.webp", "ep2_s39")
            )  # 39, Daisy
            cls.items.append(
                cls(
                    "Player versus Player",
                    "images/ep2/Scene 42b/ep2s42b_90.webp",
                    "ep2_s42b",
                )
            )  # 42b, Lindsey
            cls.items.append(
                cls(
                    "Under the stars",
                    "images/ep2/Scene 43c/ep2s43c_32.webp",
                    "ep2_s43c_sg",
                )
            )  # 43c, Aubrey
            cls.items.append(
                cls(
                    "Sneaking around",
                    "images/ep2/Scene 43d/ep2s43d_18a.webp",
                    "ep2_s43d_sg",
                )
            )  # 43d, Samantha
            cls.items.append(
                cls(
                    "SVC Hot Rods",
                    "images/ep2/Scene 45b/ep2s45b_30.webp",
                    "ep2_s45b_sg",
                )
            )  # 45b, Chloe
            cls.items.append(
                cls(
                    "No fucks given",
                    "images/ep2/Scene 48e/ep2s48e_14.webp",
                    "ep2_s48e_sg",
                )
            )  # 48e, Lindsey
            cls.items.append(
                cls(
                    "Riley & Lauren threesome",
                    "images/ep2/Scene 51c/ep2s51c_10b.webp",
                    "ep2_s51c",
                )
            )  # 51c, Riley Lauren
            cls.items.append(
                cls(
                    "The Fandango Finisher",
                    "images/ep2/Scene 54/ep2s54_13.webp",
                    "ep2_s54_sg",
                )
            )  # 54, Amber

        if store.has_ep3():
            cls.items.append(
                cls("All tied up", "images/ep3/Scene 5b/ep3s5b_15.webp", "ep3_s5b")
            )
            cls.items.append(
                cls(
                    "Underwater fun",
                    "images/ep3/Scene 9/ep3s9_47.webp",
                    "ep3_s9.amber_gets_you_off",
                )
            )
            cls.items.append(
                cls(
                    "Guided masturbation",
                    "images/ep3/Scene 13b/ep3s13b_20j.webp",
                    "ep3_s13b",
                )
            )
            cls.items.append(
                cls("Free Use", "images/ep3/Scene 17b/ep3s17b_18.webp", "ep3_s17b")
            )
            cls.items.append(
                cls(
                    "Hallway Sparring",
                    "images/ep3/Scene 18/ep3s18_7.webp",
                    "ep3_s18.start_of_fight",
                )
            )
            cls.items.append(
                cls(
                    "Pleasing the perv",
                    "images/ep3/Scene 21c/ep3s21c_5c.webp",
                    "ep3_s21c",
                )
            )
            cls.items.append(
                cls(
                    "Lockerroom Quickie",
                    "images/ep3/Scene 32d/ep3s32d_20.webp",
                    "ep3_s32d",
                )
            )
            cls.items.append(
                cls(
                    "Hot tub make out Session",
                    "images/ep3/Scene 32e/ep3s32e_25.webp",
                    "ep3_s32e.hot_tub_makeout",
                )
            )
            cls.items.append(
                cls("Hot tub sex", "images/ep3/Scene 35b/ep3s35b_13.webp", "ep3_s35b")
            )
            cls.items.append(
                cls("Dirty dice", "images/ep3/Scene 42b/ep3s42b_30b.webp", "ep3_s42b")
            )
            cls.items.append(
                cls(
                    "Student teacher roleplay",
                    "images/ep3/Scene 48/ep3s48_15i.webp",
                    "ep3_s48",
                )
            )
            cls.items.append(
                cls(
                    "Violet's Striptease",
                    "images/ep3/Scene 49/ep3s49_34.webp",
                    "ep3_s49.violet_dance",
                )
            )
            cls.items.append(
                cls(
                    "Amber's Striptease",
                    "images/ep3/Scene 49/ep3s49_48.webp",
                    "ep3_s49.amber_dance",
                )
            )
            cls.items.append(
                cls("Hot hotel sex", "images/ep3/Scene 51b/ep3s51b_14.webp", "ep3_s51b")
            )
            cls.items.append(
                cls(
                    "Blowjob practice",
                    "images/ep3/Scene 57c/ep3s57c_18.webp",
                    "ep3_s57c",
                )
            )
            cls.items.append(
                cls(
                    "Sneaking off with Aubrey",
                    "images/ep3/Scene 57j/ep3s57j_13.webp",
                    "ep3_s57j",
                )
            )
            cls.items.append(
                cls(
                    "Bathroom make out",
                    "images/ep3/Scene 57m/ep3s57m_3.webp",
                    "ep3_s57m",
                )
            )
            cls.items.append(
                cls(
                    "All powdered up", "images/ep3/Scene 57q/ep3s57q_7.webp", "ep3_s57q"
                )
            )
            cls.items.append(
                cls(
                    "Sneaking off with Chloe",
                    "images/ep3/Scene 57u/ep3s57u_5.webp",
                    "ep3_s57u",
                )
            )
            cls.items.append(
                cls(
                    "Calming your nerves",
                    "images/ep3/Scene 60/ep3s60_31.webp",
                    "ep3_s60.emily_handjob",
                )
            )
            cls.items.append(
                cls(
                    "Winter Versus vs. Perry",
                    "images/ep3/Scene 60/ep3s60_61.webp",
                    "ep3_s60.start_of_perry_fight",
                )
            )
            cls.items.append(
                cls(
                    "Winter Versus vs. Caleb",
                    "images/ep3/Scene 60/ep3s60_47.webp",
                    "ep3_s60.start_of_caleb_fight",
                )
            )


def update_scope(new_scope: dict[str, Any]) -> dict[str, Any]:
    rv: dict[str, Any] = store.scopeDict.copy()
    rv.update(new_scope)
    return rv
