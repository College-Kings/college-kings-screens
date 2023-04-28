screen ck1_end_screen():
    tag end_screen
    modal True
    style_prefix "end_screen"

    add "ck1_end_screen_background{}".format("_steam" if config.enable_steam else "")

    imagebutton:
        idle "menu_idle"
        hover "menu_hover"
        action MainMenu()
        xalign 0.15
        ypos 805

    imagebutton:
        idle "get_access_idle"
        hover "get_access_hover"
        if config.enable_steam:
            action OpenURL("https://store.steampowered.com/app/1924480/College_Kings_2__Episode_1/")
        else:
            action OpenURL("https://www.patreon.com/collegekings")
        xalign 0.5
        ypos 800

    imagebutton:
        idle "gui/common/credits_idle.webp"
        hover "gui/common/credits_hover.webp"
        action Show("patreon_credits", None, "")
        xalign 0.8
        ypos 847

    on "show" action Hide("phone_icon")
    on "hide" action Show("phone_icon")
    on "replace" action Hide("phone_icon")
    on "replaced" action Show("phone_icon")