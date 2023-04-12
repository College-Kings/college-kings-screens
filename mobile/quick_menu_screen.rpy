style pref_vbox:
    variant "medium"
    xsize 675


## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize 38
    left_bar Frame("gui/phone/bar/left.png", Borders(6, 6, 6, 6), tile=False)
    right_bar Frame("gui/phone/bar/right.png", Borders(6, 6, 6, 6), tile=False)

style vbar:
    variant "small"
    xsize 38
    top_bar Frame("gui/phone/bar/top.png", Borders(6, 6, 6, 6), tile=False)
    bottom_bar Frame("gui/phone/bar/bottom.png", Borders(6, 6, 6, 6), tile=False)

style scrollbar:
    variant "small"
    ysize 18
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", Borders(6, 6, 6, 6), tile=False)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", Borders(6, 6, 6, 6), tile=False)

style vscrollbar:
    variant "small"
    xsize 18
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", Borders(6, 6, 6, 6), tile=False)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", Borders(6, 6, 6, 6), tile=False)

style slider:
    variant "small"
    ysize 38
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", Borders(6, 6, 6, 6), tile=False)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize 38
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", Borders(6, 6, 6, 6), tile=False)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
