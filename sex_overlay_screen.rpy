screen sex_overlay(continue_label):
    default show_sex_overlay = False

    vbox:
        pos (100, 100)
        spacing -100

        imagebutton:
            idle "sex_overlay_sex_positions_idle"
            hover "sex_overlay_sex_positions_hover"
            selected_idle "sex_overlay_sex_positions_selected"
            action ToggleScreenVariable("show_sex_overlay")

        null height 150

        if show_sex_overlay:
            for sex_move, l in sex_overlay_options:
                button:
                    idle_background "sex_overlay_sex_button_idle"
                    hover_background "sex_overlay_sex_button_hover"
                    focus_mask True
                    action Jump(l)
                    xysize (366, 191)
                    xpos -25

                    text "[sex_move!t]" align (0.5, 0.5)

    imagebutton:
        idle "sex_overlay_continue_idle"
        hover "sex_overlay_continue_hover"
        action Show("confirm", message=_("Are you sure you want to end the scene?"), yes_action=Jump(continue_label))
        xalign 1.0
        xoffset -100
        ypos 100

    on "show" action Hide("phone_icon")
    on "hide" action Show("phone_icon")
    on "replace" action Hide("phone_icon")
    on "replaced" action Show("phone_icon")

    if config_debug:
        timer 0.1 repeat True action SetField(config, "skipping", "slow")
