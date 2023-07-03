screen alert_template(message):
    zorder 200
    modal True
    style_prefix "alert"
    
    frame:
        align (0.5, 0.5)
        minimum (758, 363)
        background "alert_background"

        vbox:
            align (0.5, 0.5)
            spacing 45

            text "[message!t]":
                xalign 0.5
                xsize 650

            hbox:
                xalign 0.5
                spacing 20

                transclude
