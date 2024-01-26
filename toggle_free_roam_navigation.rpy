screen toggle_free_roam_navigation():
    if free_roam_navigation:
        textbutton "Disable Navigation Hints":
            action SetVariable("free_roam_navigation", False)
            style "navigation_hint"
            text_style "navigation_hint_text"
    else:
        textbutton "Enable Navigation Hints":
            action SetVariable("free_roam_navigation", True)
            style "navigation_hint"
            text_style "navigation_hint_text"

    on "show" action Hide("phone_icon")
    on "replace" action Hide("phone_icon")
    on "hide" action Show("phone_icon")
    on "replaced" action Show("phone_icon")

style navigation_hint is button:
    xalign 1.0

style navigation_hint_text is button_text:
    size 20
    outlines [(1, "#000")]