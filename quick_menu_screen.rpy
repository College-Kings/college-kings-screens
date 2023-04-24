## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    zorder 10
    style_prefix "quick_menu"

    default image_path = "gui/quick_menu/"

    if quick_menu:
        hbox:
            align (0.5, 1.0)
            yoffset -5
            spacing 30

            if not real_life_mode:
                imagebutton:
                    idle Transform(image_path + "rollback_idle.webp", zoom=0.35)
                    hover Transform(image_path + "rollback_hover.webp", zoom=0.35)
                    action Rollback()
            
            imagebutton:
                idle Transform(image_path + "history_idle.webp", zoom=0.35)
                hover Transform(image_path + "history_hover.webp", zoom=0.35)
                action ShowMenu("history")

            imagebutton:
                idle Transform(image_path + "skip_idle.webp", zoom=0.35)
                hover Transform(image_path + "skip_hover.webp", zoom=0.35)
                action Skip()
                alternate Skip(fast=True, confirm=True)

            imagebutton:
                idle Transform(image_path + "auto_forward_idle.webp", zoom=0.35)
                hover Transform(image_path + "auto_forward_hover.webp", zoom=0.35)
                action Preference("auto-forward", "toggle")

            imagebutton:
                idle Transform(image_path + "save_idle.webp", zoom=0.35)
                hover Transform(image_path + "save_hover.webp", zoom=0.35)
                action ShowMenu("save")

            imagebutton:
                idle Transform(image_path + "quick_save_idle.webp", zoom=0.35)
                hover Transform(image_path + "quick_save_hover.webp", zoom=0.35)
                action QuickSave()

            imagebutton:
                idle Transform(image_path + "quick_load_idle.webp", zoom=0.35)
                hover Transform(image_path + "quick_load_hover.webp", zoom=0.35)
                action QuickLoad()

            imagebutton:
                idle Transform(image_path + "settings.webp", zoom=0.35)
                hover Transform(image_path + "settings_hover.webp", zoom=0.35)
                action ShowMenu("preferences")


style quick_menu_button:
    align (0.5, 0.5)

style quick_menu_button_text is bebas_neue_30


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True
