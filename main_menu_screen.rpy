## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    tag menu
    style_prefix "main_menu"

    python:
        with renpy.open_file("whats_new/whats-new.txt") as f:
            what_new_content = f.read()

    default image_path = "gui/main_menu/"

    add "main_menu_background"

    if not is_patreon():
        vbox:
            pos (50, 25)
            spacing 25

            # Unscripted
            imagebutton:
                idle image_path + "unscripted_idle.png"
                hover Transform(image_path + "unscripted_idle.png", matrixcolor=BrightnessMatrix(0.2))
                action OpenURL("steam://openurl/https://store.steampowered.com/app/2156300/Unscripted/")

    else:
        imagebutton:
            idle "main_menu_patreon_idle"
            hover "main_menu_patreon_hover"
            action OpenURL("https://www.patreon.com/collegekings")
            pos (35, 35)

    # Discord
    imagebutton:
        idle "main_menu_discord_idle"
        hover "main_menu_discord_hover"
        action OpenURL("https://discord.gg/collegekings")
        xalign 1.0
        xoffset -35
        ypos 35

    # Scene Gallery
    imagebutton:
        pos (141, 811)
        idle image_path + "scene_gallery_idle.webp"
        hover Transform(image_path + "scene_gallery_hover.webp", pos=(-22, -22))
        action Show("confirm",
            message="Warning: The scene gallery contains spoilers for the story of the game. Are you sure you want to continue?",
            yes_action=[Hide("confirm"), ui.callsinnewcontext("scene_gallery_name_change"), ShowMenu("scene_gallery")])

    # Path Builder
    imagebutton:
        idle image_path + "path_builder_idle.webp"
        hover Transform(image_path + "path_builder_hover.webp", pos=(-20, -20))
        action Show("confirm",
            message="Warning: The Path Builder contains spoilers for the story of the game. Are you sure you want to continue?",
            yes_action=[Hide("confirm"), Start("path_builder")])
        pos (1454, 811)

    # Play Now
    imagebutton:
        idle image_path + "play_now_idle.webp"
        hover Transform(image_path + "play_now_hover.webp", pos=(-31, -31))
        action Start()
        pos (564, 880)

    # Load
    imagebutton:
        idle image_path + "load_idle.webp"
        hover Transform(image_path + "load_hover.webp", pos=(-27, -31))
        action ShowMenu("load")
        pos (1096, 880)

    hbox:
        yalign 1.0
        yoffset -20
        spacing -20

        # WHAT'S NEW
        imagebutton:
            idle image_path + "whats-new-idle.webp"
            hover image_path + "whats-new-hover.webp"
            action Show("whats_new")
            yalign 0.5

        # LEARN MORE
        imagebutton:
            idle image_path + "learn_more_idle.webp"
            hover image_path + "learn_more_hover.webp"
            action OpenURL("http://collegekingsgame.com")
            yalign 0.5

    hbox:
        align (1.0, 1.0)
        yoffset -40

        # SETTINGS
        imagebutton:
            idle "gui/common/settings_idle.webp"
            hover "gui/common/settings_hover.webp"
            action ShowMenu("preferences")

        # QUIT
        imagebutton:
            idle "gui/common/quit_idle.webp"
            hover "gui/common/quit_hover.webp"
            action Quit()

    text "v{}".format('.'.join(str(x) for x in config.version)) align (1.0, 1.0) xoffset -20 color "#4e628f" size 30

    on "show" action [Play("music", audio.music.ck2_main_menu_theme_start), Queue("music", audio.music.ck2_main_menu_theme_loop, loop=True)]

    if not config_debug and not what_new_content == persistent.previous_whats_new:
        on "show" action Show("whats_new")

    if config_debug:
        timer 0.1 action Start()
