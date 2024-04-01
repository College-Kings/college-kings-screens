## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen file_slots(title):
    style_prefix "file_slots"

    default page_name_value = FilePageNameInputValue(pattern=_("PAGE {}"), auto=_("AUTOMATIC SAVES"), quick=_("QUICK SAVES"))
    default image_path = "gui/file_slots/"

    add image_path + "background.webp"

    text "{} Game".format(title):
        xalign 0.5
        ypos 56
        style "file_slots_title"

    imagebutton:
        idle "return_button_idle"
        hover "return_button_hover"
        action Return()

    fixed:
        pos (243, 206)
        xysize (1430, 588)

        if not renpy.get_screen("enter_save_name"):
            button:
                xalign 0.5
                ypos 35
                action page_name_value.Toggle()
                key_events True

                input:
                    style "file_slots_page_name"
                    value page_name_value

        ## The grid of file slots.
        default grid_cols = 3
        default grid_rows = 2

        grid grid_cols grid_rows:
            xalign 0.5
            ypos 110
            spacing 35

            for slot in range(1, grid_cols * grid_rows + 1):
                button:
                    background Transform(FileScreenshot(slot), size=(config.thumbnail_width, config.thumbnail_height))
                    if title == _("Save"):
                        action Show("enter_save_name", slot=slot)
                    else:
                        action FileAction(slot)
                    xysize (config.thumbnail_width, config.thumbnail_height)

                    if config.developer:
                        text FileJson(slot, key="_version") or ""

                    vbox:
                        align (0.5, 1.0)

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")).upper() xalign 0.5
                        text FileSaveName(slot).upper() xalign 0.5

                    key "save_delete" action FileDelete(slot)

    # Buttons to access other pages.
    hbox:
        xalign 0.5
        ypos 803
        xysize (1100, 48)
        spacing 35
        xoffset 20

        imagebutton:
            idle image_path + "left_arrow.webp"
            action FilePagePrevious()
            yalign 0.5

        if config.has_autosave:
            textbutton _("{#auto_page}A") action FilePage("auto") yalign 0.5

        if config.has_quicksave:
            textbutton _("{#quick_page}Q") action FilePage("quick") yalign 0.5

        for page in range(1, 10):
            textbutton str(page) action FilePage(page) yalign 0.5

        textbutton "99" action FilePage(99) yalign 0.5

        imagebutton:
            idle image_path + "right_arrow.webp"
            action FilePageNext()
            yalign 0.5

    # Menu buttons
    hbox:
        yalign 1.0

        if title == _("Save"):
            imagebutton:
                idle image_path + "load_idle.webp"
                hover image_path + "load_hover.webp"
                action ShowMenu("load")
        else:
            imagebutton:
                idle image_path + "save_idle.webp"
                hover image_path + "save_hover.webp"
                action ShowMenu("save")

        imagebutton:
            idle image_path + "menu_idle.webp"
            hover image_path + "menu_hover.webp"
            action MainMenu(confirm=not main_menu)

    hbox:
        align (1.0, 1.0)

        imagebutton:
            idle "gui/common/settings_idle.webp"
            hover "gui/common/settings_hover.webp"
            action ShowMenu("preferences")

        imagebutton:
            idle "gui/common/quit_idle.webp"
            hover "gui/common/quit_hover.webp"
            action Quit(confirm=not main_menu)


style file_slots_title is montserrat_extra_bold_64

style file_slots_page_name is bebas_neue_30

style file_slots_text is bebas_neue_30:
    size 22
    yoffset 2

style file_slots_button_text is syne_extra_bold_22
