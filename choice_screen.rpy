## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items, seconds=3, fail_label=None):
    style_prefix "choice"
    
    default timer = 0.0
    default fail_action = False

    # Show reputation
    if show_reputation and len(items) > 1:
        use reputation_choice_hint

    vbox:
        align (0.5, 1.0)
        yoffset -50
        spacing 25

        for i in range(0, len(items), 3):
            hbox:
                xalign 0.5
                spacing 25

                for item in items[i:min(i+3, len(items))]:
                    python:
                        show_after = item.kwargs.pop("show_after", 0)
                        hide_after = item.kwargs.pop("hide_after", -1)
                        if item.kwargs.pop("fail", False):
                            fail_action = item.action

                    if show_after <= timer and (hide_after > timer or hide_after == -1):
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
                                    for arg, is_positive in item.kwargs.items():
                                        if is_positive:
                                            text "{color=#00FF00}[[[arg]]" yalign 0.5
                                        else:
                                            text "{color=#FF0000}[[[arg]]" yalign 0.5

    if fail_label is not None or fail_action:
        bar value AnimatedValue(0, seconds, seconds, seconds) at alpha_dissolve

    if fail_action:
        timer seconds action fail_action
    elif fail_label is not None:
        timer seconds action Jump(fail_label)

    timer 0.25 repeat True action IncrementScreenVariable("timer", 0.25)

    if config_debug:
        $ item = renpy.random.choice(items)
        timer 0.1 action item.action

    on "show" action [Hide("phone_icon"), If(persistent.enabled_tutorials["reputation_tutorial"], Show("reputation_tutorial"))]
    on "hide" action Show("phone_icon")
    on "replace" action Hide("phone_icon")
    on "replaced" action Show("phone_icon")

style choice_text is bebas_neue_30