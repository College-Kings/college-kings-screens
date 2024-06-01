screen clear_persistent():
    zorder 200
    modal True
    style_prefix "confirm"

    add "darker_80"

    use alert_template("Clearing your progress will reset all related content, including:\n- Gallery Unlock Progress\n- Seen content (skipping)"):

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            action [Hide(), Function(persistent._clear, progress=False)]
            padding (50, 15)
            xmaximum 275

            text "Clear settings" align (0.5, 0.5)

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            action [Hide(), Function(persistent._clear, progress=True)]
            padding (50, 15)
            xmaximum 275

            text "Clear progress" align (0.5, 0.5)

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            action Hide()
            padding (50, 15)
            xmaximum 150

            text "Cancel" align (0.5, 0.5)

    key "game_menu" action Hide()
