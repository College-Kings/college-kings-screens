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


style navigation_hint is button:
    xalign 1.0

style navigation_hint_text is button_text:
    size 20
    outlines [(1, "#000")]