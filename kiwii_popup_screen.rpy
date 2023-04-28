screen kiwiiPopup():
    modal True
    zorder 200

    use alert_template(_("You've just unlocked the social media app Kiwii! Open it now from the homescreen.")):

        textbutton _("OK"):
            xalign 0.5
            action [Function(kiwii_firstTimeMessages), SetVariable("kiwii_first_time", False), Hide("kiwiiPopup")]

    if config_debug:
        timer 0.1 action [Function(kiwii_firstTimeMessages), SetVariable("kiwii_first_time", False), Hide("kiwiiPopup")]