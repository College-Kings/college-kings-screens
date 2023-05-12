## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action=Hide(), no_action=Hide()):
    zorder 200
    modal True
    style_prefix "confirm"

    python:
        if not isinstance(yes_action, list):
            yes_action = [yes_action]
        if not isinstance(no_action, list):
            no_action = [no_action]

    add "darker_80"

    use alert_template(message.upper()):

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            action [Hide()] + list(yes_action)
            padding (50, 15)
            xsize 150

            text "YES" align (0.5, 0.5)

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            action [Hide()] + list(no_action)
            padding (50, 15)
            xsize 150

            text "NO" align (0.5, 0.5)

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

    if config_debug:
        timer 0.1 action yes_action


style confirm_text is bebas_neue_30
