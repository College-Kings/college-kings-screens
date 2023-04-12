## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        if who is not None:

            window:
                xpos 360
                xanchor 0.0
                padding (5, 5, 5, 5)

                text who id "who":
                    size 45
                    font "fonts/OpenSans-Bold.ttf"

        text what id "what":
            pos (402, 75)
            xsize 1116
            size 30
            font "fonts/OpenSans-Bold.ttf"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() yalign 1.0


style say_window is window:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 278