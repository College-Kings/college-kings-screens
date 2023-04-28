screen sex_overlay(continue_label):
    default image_path = "images/custom-screens/sex-overlay/"
    default show_sex_overlay = False

    vbox:
        pos (100, 100)
        spacing -100

        imagebutton:
            idle image_path + "sex-positions-idle.webp"
            hover image_path + "sex-positions-hover.webp"
            selected_idle image_path + "sex-positions-selected.webp"
            action ToggleScreenVariable("show_sex_overlay")

        null height 150

        if show_sex_overlay:
            for option in sex_overlay_options:
                button:
                    idle_background image_path + "sex-button-idle.webp"
                    hover_background image_path + "sex-button-hover.webp"
                    focus_mask True
                    action Jump(option[1])
                    xysize (366, 191)
                    xpos -25

                    text option[0] align (0.5, 0.5)

    imagebutton:
        idle image_path + "continue-idle.webp"
        hover image_path + "continue-hover.webp"
        action Show("confirm", message=_("Are you sure you want to end the free roam?"), yes_action=[Hide("confirm"), Jump(continue_label)])
        xalign 1.0
        xoffset -100
        ypos 100

    on "show" action Hide("phone_icon")
    on "hide" action Show("phone_icon")
    on "replace" action Hide("phone_icon")
    on "replaced" action Show("phone_icon")

    if config_debug:
        timer 0.1 repeat True action SetField(config, "skipping", "slow")