## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items, seconds=3, fail_label=None):
    style_prefix "choice"

    default number_of_rows = math.ceil(len(items) / 3)

    # Show reputation
    if show_reputation and len(items) > 1:
        use reputation_choice_hint

    vbox:
        xfill True
        yalign 1.0
        yoffset -50

        for i in range(number_of_rows):
            hbox:
                xalign 0.5
                spacing 25

                for j in range(min(3, len(items) - i * 3)):
                    $ item = items[i*3 + j]
                    
                    button:
                        idle_background "choice_button_idle"
                        hover_background "choice_button_hover"
                        action item.action
                        padding (25, 35)
                        minimum (550, 131)

                        text "[item.caption!uit]" align (0.5, 0.5)

    if fail_label is not None:
        timer seconds:
            action Jump(fail_label)

        use timer_bar(seconds)

    if config_debug:
        $ item = renpy.random.choice(items)
        timer 0.1 action item.action

    on "show" action [Hide("phone_icon"), If(persistent.enabled_tutorials["reputation_tutorial"], Show("reputation_tutorial"))]
    on "hide" action Show("phone_icon")
    on "replace" action Hide("phone_icon")
    on "replaced" action Show("phone_icon")

style choice_text is bebas_neue_30

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text
