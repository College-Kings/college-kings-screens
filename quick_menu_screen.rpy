## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

image rollback_idle = Transform("gui/quick_menu/rollback_idle.webp", zoom=0.35)
image rollback_hover = Transform("gui/quick_menu/rollback_hover.webp", zoom=0.35)

image history_idle = Transform("gui/quick_menu/history_idle.webp", zoom=0.35)
image history_hover = Transform("gui/quick_menu/history_hover.webp", zoom=0.35)

image skip_idle = Transform("gui/quick_menu/skip_idle.webp", zoom=0.35)
image skip_hover = Transform("gui/quick_menu/skip_hover.webp", zoom=0.35)

image auto_forward_idle = Transform("gui/quick_menu/auto_forward_idle.webp", zoom=0.35)
image auto_forward_hover = Transform("gui/quick_menu/auto_forward_hover.webp", zoom=0.35)

image save_idle = Transform("gui/quick_menu/save_idle.webp", zoom=0.35)
image save_hover = Transform("gui/quick_menu/save_hover.webp", zoom=0.35)

image quick_save_idle = Transform("gui/quick_menu/quick_save_idle.webp", zoom=0.35)
image quick_save_hover = Transform("gui/quick_menu/quick_save_hover.webp", zoom=0.35)

image quick_load_idle = Transform("gui/quick_menu/quick_load_idle.webp", zoom=0.35)
image quick_load_hover = Transform("gui/quick_menu/quick_load_hover.webp", zoom=0.35)

image settings_idle = Transform("gui/quick_menu/settings.webp", zoom=0.35)
image settings_hover = Transform("gui/quick_menu/settings_hover.webp", zoom=0.35)



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
                    idle "rollback_idle"
                    hover "rollback_hover"
                    selected_idle "rollback_hover"
                    selected_hover "rollback_idle"
                    action Rollback()

            imagebutton:
                idle "history_idle"
                hover "history_hover"
                selected_idle "history_hover"
                selected_hover "history_idle"
                action ShowMenu("history")

            imagebutton:
                idle "skip_idle"
                hover "skip_hover"
                selected_idle "skip_hover"
                selected_hover "skip_idle"
                action Skip()
                alternate Skip(fast=True, confirm=True)

            imagebutton:
                idle "auto_forward_idle"
                hover "auto_forward_hover"
                selected_idle "auto_forward_hover"
                selected_hover "auto_forward_idle"
                action Preference("auto-forward", "toggle")

            imagebutton:
                idle "save_idle"
                hover "save_hover"
                selected_idle "save_hover"
                selected_hover "save_idle"
                action ShowMenu("save")

            imagebutton:
                idle "quick_save_idle"
                hover "quick_save_hover"
                selected_idle "quick_save_hover"
                selected_hover "quick_save_idle"
                action QuickSave()

            imagebutton:
                idle "quick_load_idle"
                hover "quick_load_hover"
                selected_idle "quick_load_hover"
                selected_hover "quick_load_idle"
                action QuickLoad()

            imagebutton:
                idle "settings_idle"
                hover "settings_hover"
                selected_idle "settings_hover"
                selected_hover "settings_idle"
                action ShowMenu("preferences")


style quick_menu_button:
    align (0.5, 0.5)

style quick_menu_button_text is bebas_neue_30


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True
