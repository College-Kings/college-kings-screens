screen path_builder_advanced_settings():
    zorder 100
    modal True

    if is_CK2:
        default gameplay_options = (
            ("Show preferred reputation for each girl (in Step 04)", ToggleVariable("pb_reputation_shown")),
            ("Show a notification whenever you gain reputation points", ToggleVariable("pb_reputation_notification")),
            ("Unlimited Presidency Campaign Budget", [ToggleVariable("lindsey_board.money", 10000, 200), ToggleVariable("chloe_board.money", 10000, 1500)])
        )
    else:
        default gameplay_options = (
            ("Show preferred reputation for each girl (in Step 04)", ToggleVariable("pb_reputation_shown")),
            ("Show a notification whenever you gain reputation points", ToggleVariable("pb_reputation_notification"))
        )

    add "path_builder_background"

    imagebutton:
        idle "return_button_idle"
        hover "return_button_hover"
        action Hide("path_builder_advanced_settings")
        align (0.015, 0.015)

    hbox: 
        align (0.5, 0.5)
        spacing 100
        vbox:
            spacing 20

            text "Extras" color "#FFD166" size 50

            for name, actions in pb_advanced_options:

                hbox:
                    spacing 20

                    imagebutton:
                        idle "path_bulder_tick"
                        hover "path_bulder_ticked"
                        selected_idle "path_bulder_ticked"
                        action actions

                    text name


        vbox:
            spacing 20

            text "Gameplay Changes" color "#FFD166" size 50

            for name, actions in gameplay_options:
                hbox:
                    spacing 20

                    imagebutton:
                        idle "path_bulder_tick"
                        hover "path_bulder_ticked"
                        selected_idle "path_bulder_ticked"
                        action actions

                    text name:
                        yoffset -7
