screen ep2_restart(is_episode_3=False):
    frame:
        align (0.5, 0.5)
        xysize (758, 363)
        background "alert_background"

        text "Episode 2 has been remade! Unfortunately, this means previous Episode 2 save files won't work with the updated version. By pressing 'OK' below you will begin Episode 2 anew.":
            xsize 500
            align (0.5, 0.5)

        textbutton "OK":
            align (0.5, 1.0)
            yoffset -20
            selected False
            action Jump("ep2s1")