## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xsize 1116
            pos (402, 75)

            text prompt:
                font "fonts/OpenSans-Bold.ttf"
                size 30

            hbox:
                spacing 5
                
                text ">"
                input id "input"


style input:
    color "#ffffff"
    outlines [ (2, "#000000") ]
    size 30
    font "fonts/OpenSans-Bold.ttf"

style input_window is say_window