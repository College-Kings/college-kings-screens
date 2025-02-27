screen ep6_1_end_screen():
    tag end_screen
    modal True
    style_prefix "end_screen"

    add "end_screen_background"

    text "College Kings 2: Episode 6 Part 2 is currently in development":
        style "montserrat_extra_bold_56"
        textalign 0.5
        align (0.5, 0.5)
        xsize 1220
        
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
            action Show("team_credits")
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
            action OpenURL("https://discord.gg/undergradsteve")

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    on "replace" action SetVariable("quick_menu", False)
    on "replaced" action SetVariable("quick_menu", True)

    if config_debug:
        timer 0.1 action MainMenu(confirm=False)