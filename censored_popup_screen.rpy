screen censored_popup(continue_label):
    modal True

    add "censored_background"

    text _("THE NEXT SCENE HAS NSFW CONTENT"):
        style "nsfw_text"
        xalign 0.5
        ypos 125
        size 70
        color "#FFFFFF"

    text _("* CONTENT NOT SUITABLE FOR TWITCH OR YOUTUBE"):
        style "nsfw_italic_text"
        xalign 0.5
        ypos 255
        size 40
        color "#FFFFFF"

    vbox:
        xalign 0.5
        ypos 450
        xsize 1050

        if is_censored:
            text _("TO VIEW THIS SCENE YOU MUST HAVE NSFW ENABLED"):
                style "nsfw_text"
                xalign 0.5
                size 35
                color "#FFFFFF"

            text _("IN THE SETTINGS MENU"):
                style "nsfw_text"
                xalign 0.5
                size 35
                color "#FFFFFF"

        else:
            text _("YOU HAVE NSFW CONTENT ENABLED SO YOU MAY"):
                style "nsfw_text"
                xalign 0.5
                size 35
                color "#FFFFFF"

            text _("CONTINUE TO VIEW THE FOLLOWING SCENE"):
                style "nsfw_text"
                xalign 0.5
                size 35
                color "#FFFFFF"

    text _("OR YOU MAY CHOOSE TO SKIP THIS SCENE"):
        style "nsfw_text"
        xalign 0.5
        ypos 730
        xsize 1050    
        size 35
        color "#FFFFFF"

    if is_censored:
        imagebutton:
            idle "censored_settings"
            hover "censored_settings_hover"
            action ShowMenu("preferences")
            xalign 0.5
            ypos 555
            
    else:
        imagebutton:
            idle "censored_continue"
            hover "censored_continue_hover"
            action Return()
            xalign 0.5
            ypos 555

    imagebutton:
        idle "censored_skip_scene"
        hover "censored_skip_scene_hover"
        action Jump(continue_label)
        xalign 0.5
        ypos 790

    on "show" action Hide("phone_icon")
    on "hide" action Show("phone_icon")
    on "replace" action Hide("phone_icon")
    on "replaced" action Show("phone_icon")
