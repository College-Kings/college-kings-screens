screen real_life_mode():
    modal True

    add "images/start/real_life_mode_background.webp"

    use warning_template(_("THIS MODE PROHIBITS you from saving during important choices, meaning all choices are final. this can't be disabled without starting a new game.")):

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            action [SetVariable("real_life_mode", True), SetVariable("config.rollback_enabled", False), SetVariable("show_reputation", False), Show("phone_icon"), Jump("v1_start")]
            xysize (215, 55)

            text _("ENABLE") align (0.5, 0.5)

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            action [SetVariable("real_life_mode", False), SetVariable("config.rollback_enabled", True), SetVariable("show_reputation", True), Show("phone_icon"), Jump("v1_start")]
            xysize (215, 55)

            text _("DISABLE") align (0.5, 0.5)

    if config_debug:
        timer 0.1 action [SetVariable("real_life_mode", False), SetVariable("config.rollback_enabled", True), SetVariable("show_reputation", True), Show("phone_icon"), Jump("v1_start")]
