screen alert_template(message):
    zorder 200
    modal True
    style_prefix "alert"

    frame:
        align (0.5, 0.5)
        minimum (758, 363)
        background "alert_background"
        padding (50, 25)

        vbox:
            align (0.5, 0.5)
            spacing 45

            text "[message!t]":
                xsize 700
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 20

                transclude

style alert_text is bebas_neue_30:
    text_align 0.5