screen censored_popup(continueLabel):
    modal True

    add "censored_background"

    text _("THE NEXT SCENE HAS NSFW CONTENT"):
        size 70
        color "#FFFFFF"
        style "nsfw_text"
        xalign 0.5
        ypos 125

    text _("* CONTENT NOT SUITABLE FOR TWITCH OR YOUTUBE"):
        size 40
        color "#FFFFFF"
        style "nsfw_italic_text"
        xalign 0.5
        ypos 255

    vbox:
        ypos 450
        xalign 0.5
        xsize 1050

        if is_censored:
            text _("TO VIEW THIS SCENE YOU MUST HAVE NSFW ENABLED"):
                size 35
                color "#FFFFFF"
                style "nsfw_text"
                xalign 0.5

            text _("IN THE SETTINGS MENU"):
                size 35
                color "#FFFFFF"
                style "nsfw_text"
                xalign 0.5

        else:
            text _("YOU HAVE NSFW CONTENT ENABLED SO YOU MAY"):
                size 35
                color "#FFFFFF"
                style "nsfw_text"
                xalign 0.5

            text _("CONTINUE TO VIEW THE FOLLOWING SCENE"):
                size 35
                color "#FFFFFF"
                style "nsfw_text"
                xalign 0.5

    text _("OR YOU MAY CHOOSE TO SKIP THIS SCENE"):
        size 35
        color "#FFFFFF"
        style "nsfw_text"
        xalign 0.5
        ypos 730
        xsize 1050    

    imagebutton:
        xalign 0.5
        ypos 555
        if is_censored:
            idle "censored_settings"
            hover "censored_settings_hover"
            action ShowMenu("preferences")
        else:
            idle "censored_continue"
            hover "censored_continue_hover"
            action Return()

    imagebutton:
        idle "censored_skip_scene"
        hover "censored_skip_scene_hover"
        action Jump(continueLabel)
        xalign 0.5
        ypos 790

    on "show" action Hide("phone_icon")
    on "hide" action Show("phone_icon")
    on "replace" action Hide("phone_icon")
    on "replaced" action Show("phone_icon")
