screen alert_template(message):
    zorder 200
    modal True
    style_prefix "alert"

    python:
        message = message.upper()
        message = message.replace("{B}", "{b}").replace("{/B}", "{/b}")

    frame:
        align (0.5, 0.5)
        minimum (758, 363)
        background "alert_background"

        vbox:
            align (0.5, 0.5)
            spacing 45

            text _(message) xalign 0.5 xsize 650

            hbox:
                xalign 0.5
                spacing 20

                transclude