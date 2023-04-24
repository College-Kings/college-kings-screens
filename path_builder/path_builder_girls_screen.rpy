
screen path_builder_girls():
    tag path_builder
    modal True
    style_prefix "path_builder"

    default image_path = "screens/path_builder/images"
    default girls = (
        (amber, None, Reputations.POPULAR, (Relationship.FRIEND, Relationship.FWB)),
        (aubrey, None, Reputations.POPULAR, (Relationship.FRIEND, Relationship.FWB, Relationship.GIRLFRIEND)),
        (autumn, None, Reputations.LOYAL, (Relationship.FRIEND, Relationship.FWB)),
        (chloe, None, Reputations.POPULAR, (Relationship.EX, Relationship.FRIEND, Relationship.FWB, Relationship.GIRLFRIEND)),
        (emily, None, Reputations.LOYAL, (Relationship.FRIEND, Relationship.FWB)),
        (jenny, None, Reputations.POPULAR, (Relationship.FRIEND, Relationship.FWB)),
        (lauren, None, Reputations.LOYAL, (Relationship.EX, Relationship.FRIEND, Relationship.FWB, Relationship.GIRLFRIEND)),
        (lindsey, None, Reputations.POPULAR, (Relationship.FRIEND, Relationship.FWB)),
        (ms_rose, Frat.WOLVES, Reputations.CONFIDENT, (Relationship.FRIEND, Relationship.FWB)),
        (naomi, None, Reputations.POPULAR, (Relationship.FRIEND, Relationship.FWB)),
        (nora, None, Reputations.CONFIDENT, (Relationship.EX, Relationship.FRIEND, Relationship.FWB, Relationship.GIRLFRIEND)),
        (penelope, None, Reputations.CONFIDENT, (Relationship.EX, Relationship.FRIEND, Relationship.DATING, Relationship.GIRLFRIEND)),
        (riley, None, Reputations.CONFIDENT, (Relationship.FRIEND, Relationship.FWB)),
        (samantha, Frat.APES, Reputations.LOYAL, (Relationship.FRIEND, Relationship.FWB)),
    )

    default selected_rep = None

    add "path_builder_background"
    add image_path + "/path_builder_box_background.webp" align (0.5, 0.5)

    button:
        idle_background "path_builder_button_idle"
        hover_background "path_builder_button_hover"
        selected_background "path_builder_button_hover"
        action Show("path_builder_advanced_settings")
        xysize (270, 61)
        xalign 1.0
        ypos 20
        xoffset -20

        text "Advanced":
            align (0.5, 0.5)
            color "#FFF"

    imagebutton:
        idle "return_button_idle"
        hover "return_button_hover"
        action MainMenu(False, False)
        pos (50, 20)
         
    add image_path + "/path_builder_step_4.webp" xalign 0.5 ypos 220

    text "Pick which girls you want to be romantically involved with" xalign 0.5 ypos 325

    grid 4 4:
        allow_underfull True
        xspacing 10
        align (0.5, 0.5)
        yoffset 75

        for girl_info in girls:
            python:
                girl = girl_info[0]
                required_frat = girl_info[1]
                preferred_reputation = girl_info[2]
                possible_relationships = girl_info[3]
                relationship = CharacterService.get_relationship(girl, mc)

            button:
                idle_background "images/common/girl_button/idle.webp"
                hover_background "images/common/girl_button/hover.webp"
                insensitive_background Transform("images/common/girl_button/idle.webp", matrixcolor=SaturationMatrix(0))
                sensitive (required_frat is None or required_frat == mc.frat)
                xysize (307, 112)
                action Function(CharacterService.set_relationship, girl, possible_relationships[(possible_relationships.index(relationship) + 1) % len(possible_relationships)], mc)

                if (required_frat is None or required_frat == mc.frat):
                    add Transform(girl.profile_picture, xysize=(100, 100)) xpos 6 yalign 0.5
                else:
                    add Transform(girl.profile_picture, xysize=(100, 100), matrixcolor=SaturationMatrix(0)) xpos 6 yalign 0.5

                vbox:
                    xpos 120
                    yalign 0.5
                    spacing -2

                    text girl.name:
                        size 30
                        color "#FFF"

                    text relationship.name:
                        size 24
                        color "#FFD166"

                    if pb_reputation_shown:
                        text preferred_reputation.name: # This could show the reputation for each girl
                            size 15
                            color "#FFD166"

    hbox:
        spacing 50
        align (0.5, 1.0)
        yoffset -50

        imagebutton:
            idle image_path + "/back.webp"
            action Show("path_builder_reputation")

        imagebutton:
            idle image_path + "/continue.webp"
            insensitive Transform(image_path + "/continue.webp", matrixcolor=SaturationMatrix(0))
            action Show("path_builder_extra_settings")
