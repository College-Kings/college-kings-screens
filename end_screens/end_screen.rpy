screen end_screen(support_link):
    tag end_screen
    modal True
    style_prefix "end_screen"

    add "end_screen_background"

    text "College Kings 2: Episode 4 \"Moving Out\" is currently in development":
        style "montserrat_extra_bold_56"
        textalign 0.5
        xalign 0.5
        xsize 1220
        ypos 75
        # action OpenURL("steam://openurl/https://store.steampowered.com/app/2267960/College_Kings_2__Episode_3_Back_To_Basics/")

    frame:
        background "end_screen_frame_background"
        xysize (1090, 656)
        align (0.5, 0.5)
        padding (54, 54)

        add "steam_logo":
            yalign 1.0
            offset (10, -10)

        imagebutton:
            idle "end_screen_wishlist_now"
            action OpenURL("steam://openurl/https://store.steampowered.com/app/2267960/College_Kings_2__Episode_3_Back_To_Basics/")
            align (0.5, 1.0)
            yoffset 46

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
            action Show("team_credits", None, support_link)
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
