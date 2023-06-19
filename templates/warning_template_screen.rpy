screen warning_template(message, style="blue"):
    zorder 200
    modal True
    style_prefix "warning"

    frame:
        align (0.5, 0.5)
        yoffset -42
        minimum (758, 363)
        background "warning_background_{}".format(style)

        vbox:
            align (0.5, 0.5)
            spacing 45

            null height 50

            text "[message!tu]":
                xalign 0.5
                xsize 650

            hbox:
                xalign 0.5
                spacing 20
                
                transclude

            null height 50
            