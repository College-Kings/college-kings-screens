## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    tag menu
    style_prefix "main_menu"

    python:
        with open(os.path.join(config.gamedir, "whats_new", "whats-new.txt"), "r") as f:
            what_new_content = f.read()

    default image_path = "gui/main_menu/"


    add image_path + "background.webp"

    if not is_patreon():
        vbox:
            pos (50, 25)
            spacing 25

            # College Kings Next Episodes
            if not has_ep2():
                imagebutton:
                    idle image_path + "ck_episode_2.png"
                    hover Transform(image_path + "ck_episode_2.png", matrixcolor=BrightnessMatrix(0.2))
                    action OpenURL("steam://openurl/https://store.steampowered.com/app/2100540/College_Kings_2__Episode_2_The_Pool_Party/")

            elif not has_ep3():
                imagebutton:
                    idle image_path + "ck_episode_3.png"
                    hover Transform(image_path + "ck_episode_3.png", matrixcolor=BrightnessMatrix(0.2))
                    action OpenURL("steam://openurl/https://store.steampowered.com/app/2267960/College_Kings_2__Episode_3_Back_To_Basics/")

            # Unscripted
            imagebutton:
                idle image_path + "unscripted_idle.png"
                hover Transform(image_path + "unscripted_idle.png", matrixcolor=BrightnessMatrix(0.2))
                action OpenURL("steam://openurl/https://store.steampowered.com/app/2156300/Unscripted/")

    else:
        imagebutton:
            idle image_path + "patreon_idle.webp"
            hover Transform(image_path + "patreon_hover.webp", xpos=-28)
            action OpenURL("https://www.patreon.com/collegekings")
            pos (118, 36)

    # Discord
    imagebutton:
        idle image_path + "discord_idle.png"
        hover image_path + "discord_hover.png"
        action OpenURL("https://discord.gg/collegekings")
        xalign 1.0
        xoffset -25
        ypos 25

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
        action [ShowMenu("load"), Function(change_save_location, "CollegeKings2")]
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

    if has_ep3() and not has_ep2():
        on "show" action Show("ep3_warning")

    if not config_debug and not what_new_content == persistent.previous_whats_new:
        on "show" action Show("whats_new")

    if config_debug:
        timer 0.1 action Start()

screen ep3_warning():
    zorder 200
    modal True
    style_prefix "warning"

    add "darker_80"

    frame:
        align (0.5, 0.5)
        yoffset -42
        minimum (758, 363)
        background "warning_background_blue"

        vbox:
            align (0.5, 0.5)
            spacing 45

            null height 50

            vbox:
                xalign 0.5
                xsize 650
                spacing 15

                text _("Warning: You're missing essential content.") size 64 xalign 0.5 text_align 0.5
                text _("It seems that you have installed \"College Kings 2: Episode 3 - Back To Basics\" without owning \"College Kings 2: Episode 2 - The Pool Party\".")
                text _("College Kings 2 is an episodic game, where each episode builds on the previous one. Whilst you are able to play Episode 3 via the path builder, you may experience bugs, glitches and other issues and saves are unlikely to work at all. To get the most out of Episode 3 and experience the story in full, we therefore highly recommend you install and play Episode 2 before jumping into Episode 3.")

            hbox:
                xalign 0.5
                spacing 35

                button:
                    idle_background "blue_button_idle"
                    hover_background "blue_button_hover"
                    action Hide("ep3_warning")
                    padding (30, 20)

                    text _("Continue at my own risk") size 32

                button:
                    idle_background "blue_button_idle"
                    hover_background "blue_button_hover"
                    action OpenURL("steam://openurl/https://store.steampowered.com/app/2100540/College_Kings_2__Episode_2_The_Pool_Party/")
                    padding (30, 20)

                    text _("Buy Episode 2 Now") size 32

            null height 50
