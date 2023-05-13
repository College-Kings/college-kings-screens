screen censored_popup(continueLabel):
    modal True

    add "gui/censoredPopup/censored_background.webp"

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
            idle Transform("gui/censoredPopup/censoredSettings.webp", zoom=0.65)
            hover Transform("gui/censoredPopup/censoredSettingsHover.webp", zoom=0.65)
            action ShowMenu("preferences")
        else:
            idle Transform("gui/censoredPopup/censoredContinue.webp", zoom=0.65)
            hover Transform("gui/censoredPopup/censoredContinueHover.webp", zoom=0.65)
            action Return()

    imagebutton:
        idle Transform("gui/censoredPopup/censoredSkipScene.webp", zoom=0.65)
        hover Transform("gui/censoredPopup/censoredSkipSceneHover.webp", zoom=0.65)
        action Jump(continueLabel)
        xalign 0.5
        ypos 790

    on "show" action Hide("phone_icon")
    on "hide" action Show("phone_icon")
    on "replace" action Hide("phone_icon")
    on "replaced" action Show("phone_icon")
