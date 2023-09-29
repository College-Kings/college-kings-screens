screen ep2_restart(is_episode_3=False):
    frame:
        align (0.5, 0.5)
        xysize (758, 363)
        background "alert_background"

        if is_episode_3:
            text "We've completely reworked Episode 2 with the help of our community! Unfortunately, this means previous Episode 2 save files will no longer work.  Whilst you can continue your previous Episode 3 save with defaulted Episode 2 decisions, we strongly recommend replaying both Episode 2 and 3 so you can experience all the new content!":
                xsize 500
                xalign 0.5
                ypos 50
                text_align 0.5

        else:
            text "We've completely reworked Episode 2 with the help of our community! Unfortunately, this means previous Episode 2 save files will no longer work. Please click 'Restart' below to play the reworked Episode 2 from the beginning and experience all the new content!":
                xsize 500
                xalign 0.5
                ypos 50
                text_align 0.5

        if is_episode_3:
            hbox:
                spacing 100
                align (0.5, 1.0)
                yoffset -20

                textbutton "Continue":
                    action Return()

                textbutton "Restart":
                    action Jump("ep2s1")

        else:
            textbutton "Restart":
                align (0.5, 1.0)
                yoffset -20
                selected False
                action Jump("ep2s1")

