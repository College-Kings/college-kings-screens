screen path_builder_fraternity():
    tag path_builder
    modal True
    style_prefix "path_builder"

    default image_path = "screens/path_builder/images"
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

    add image_path + "/path_builder_step_3.webp" xalign 0.5 ypos 220

    text "Pick a fraternity" xalign 0.5 ypos 325

    grid 2 1:
        xspacing 10
        align (0.5, 0.5)

        for frat in Frat:
            button:
                background "path_builder_button_idle"
                hover_background "path_builder_button_hover"
                selected_background "path_builder_button_hover"
                selected (mc.frat == frat)
                action SetField(mc, "frat", frat)
                xysize (270, 61)

                text frat.name:
                    align (0.5, 0.5)
                    color "#FFF"

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
            action [Hide(), Show("path_builder_girls")]
