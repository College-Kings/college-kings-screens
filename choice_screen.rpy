## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items, seconds=3, fail_label=None):
    style_prefix "choice"

    # Show reputation
    if show_reputation and len(items) > 1:
        use reputation_choice_hint

    vbox:
        xalign 0.5
        yalign 1.0
        yoffset -50
        spacing 25

        for i in range(0, len(items), 3):
            hbox:
                xalign 0.5
                spacing 25

                for item in items[i:min(i+3, len(items))]:
                    button:
                        idle_background "choice_button_idle"
                        hover_background "choice_button_hover"
                        action item.action
                        padding (30, 35)
                        minimum (550, 131)
                        
                        hbox:
                            align (0.5, 0.5)
                            spacing 10
                            
                            text "[item.caption!uit]" yalign 0.5
                            
                            if walkthrough:
                                for character in item.args:
                                    text "{color=#00FF00}[[[character.name]]" yalign 0.5

    if fail_label is not None:
        bar value AnimatedValue(0, seconds, seconds, seconds) at alpha_dissolve

        timer seconds:
            action Jump(fail_label)

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
