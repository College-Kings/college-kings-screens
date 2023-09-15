screen ep2_restart(is_episode_3=False):
    frame:
        align (0.5, 0.5)
        xysize (758, 363)
        background "alert_background"

        if is_episode_3:
            text "We've reworked Episode 2 with the help of the community, previous Episode 2 save files will no longer work. While we strongly recommend replaying episode 2 and then episode 3, you can continue Episode 3 using default decisions in the Episode 2 rework.":
                xsize 500
                xalign 0.5
                ypos 50
                text_align 0.5

        else:
            text "We've reworked Episode 2 with the help of the community! Unfortunately, this means previous Episode 2 save files will no longer work. Please click 'Restart' below to restart the reworked Episode 2.":
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

