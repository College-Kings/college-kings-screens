screen path_builder_extra_settings():
    tag path_builder
    modal True
    style_prefix "path_builder"


    add "path_builder_background"
    add "path_builder_box_background" align (0.5, 0.5)

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

    add "path_builder_step_5" xalign 0.5 ypos 220

    text "Select extra settings to customize your playthrough." xalign 0.5 ypos 325

    grid 3 3:
        xspacing 10
        allow_underfull True
        align (0.5, 0.5)

        for name, actions in pb_extra_options:
            hbox:
                ysize 80
                spacing 10

                imagebutton:
                    idle "path_builder_tick"
                    hover "path_builder_ticked"
                    selected_idle "path_builder_ticked"
                    action actions

                text name ypos -5

    hbox:
        spacing 50
        align (0.5, 1.0)
        yoffset -50

        imagebutton:
            idle "path_builder_back_idle"
            action Show("path_builder_girls")

        imagebutton:
            idle "path_builder_continue_idle"
            insensitive "path_builder_continue_insensitive"
            action [SetVariable("path_builder", True), SetVariable("quick_menu", True), Jump(pb_start_label)]
