screen ep3_end_screen():
    tag end_screen
    modal True
    style_prefix "end_screen"

    add "end_screen_background"

    text "College Kings 2: Episodes 4 & 5 \"Moving Out\" is now available on Steam!":
        style "montserrat_extra_bold_56"
        textalign 0.5
        xalign 0.5
        xsize 1220
        ypos 75

    frame:
        background "end_screen_frame_background"
        xysize (1090, 656)
        align (0.5, 0.5)
        padding (54, 54)

        add "steam_logo":
            yalign 1.0
            offset (10, -10)

        button:
            background "end_screen_action_button"
            action OpenURL("steam://openurl/https://store.steampowered.com/app/2725540/College_Kings_2__Episodes_4__5_Moving_Out/")
            xysize (311, 91)
            align (0.5, 1.0)
            yoffset 46

            text "BUY NOW":
                style "bebas_neue_33"
                align (0.5, 0.5)

    hbox:
        xpos 50
        yalign 1.0
        yoffset -25
        spacing 25

        imagebutton:
            idle "main_menu_idle"
            hover "main_menu_hover"
            action MainMenu()

        imagebutton:
            idle "team_idle"
            hover "team_hover"
            action Show("team_credits", None, "https://store.steampowered.com/app/2725540/College_Kings_2__Episodes_4__5_Moving_Out/")
            yalign 0.5

    hbox:
        align (1.0, 1.0)
        offset (-50, -50)
        spacing 25

        text "JOIN OUR COMMUNITY":
            style "bebas_neue_33"
            yalign 0.5

        imagebutton:
            idle "discord_idle"
            action OpenURL("https://discord.gg/collegekings")

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    on "replace" action SetVariable("quick_menu", False)
    on "replaced" action SetVariable("quick_menu", True)

    if config_debug:
        timer 0.1 action MainMenu(confirm=False)