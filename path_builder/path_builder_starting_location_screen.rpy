init python:
    pb_start_label = ""

screen path_builder_starting_location():
    tag path_builder
    modal True
    style_prefix "path_builder"

    default image_path = "screens/path_builder/images"

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

    add image_path + "/path_builder_step_1.webp" xalign 0.5 ypos 220

    text "Pick your starting location" xalign 0.5 ypos 325

    grid 4 1:
        xspacing 10
        xalign 0.5
        ypos 450
        allow_underfull True

        for i, l in pb_starting_locations:
            if renpy.has_label(l):
                vbox:
                    imagebutton:
                        idle "path_builder_{}".format(i.replace(' ', '_').lower())
                        action SetVariable("pb_start_label", l)
                        xalign 0.5

                    imagebutton:
                        idle "path_builder_button_idle_dark"
                        hover "path_builder_button_hover"
                        selected_idle "path_builder_button_hover"
                        action SetVariable("pb_start_label", l)
                        xalign 0.5
                        yoffset -35

                    text i:
                        align (0.5, 0.5)
                        yoffset -87
                        size 30
                        color "#FFF"

    if pb_start_label == "v1_start":
        text "ACHIEVEMENTS ARE EARNABLE" xalign 0.5 ypos 750
    else:
        text "ACHIEVEMENTS ARE NOT EARNABLE FROM THIS START" xalign 0.5 ypos 750

    hbox:
        spacing 50
        align (0.5, 1.0)
        yoffset -50

        imagebutton:
            idle image_path + "/back.webp"
            action MainMenu(False, False)

        imagebutton:
            idle image_path + "/continue.webp"
            insensitive Transform(image_path + "/continue.webp", matrixcolor=SaturationMatrix(0))
            sensitive (pb_start_label)
            action Show("path_builder_reputation")

    on "show" action SetVariable("pb_start_label", "")