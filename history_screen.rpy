## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    frame:
        xysize (1000, 975)
        xalign 0.5
        ypos 20
        background "#00000080"
        padding (20, 20)

        viewport:
            mousewheel True
            draggable True
            pagekeys True

            vbox:
                spacing 20

                for h in _history_list:
                    hbox:
                        spacing 10

                        if h.who:
                            text h.who:
                                substitute False
                                color h.who_args.get("color", "#fff")
                                yalign 0.5

                        text renpy.filter_text_tags(h.what, allow=gui.history_allow_tags):
                            substitute False

                if not _history_list:
                    text _("The dialogue history is empty.")
    
    textbutton _("Return"):
        action Return()
        xalign 0.5
        yalign 1.0
        yoffset -20
        text_size 36
        text_bold True


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }
