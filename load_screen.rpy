screen load():
    tag menu

    use file_slots(_("Load"))

    text "We do our best to retain save integrity with every update, however due to the dynamic nature of game development some saves might break. If you experience any errors please let us know via the support channel on the College Kings Discord. You can find a link to our Discord in the Main Menu.":
        font "fonts/BebasNeue-Regular.ttf"
        xalign 0.5
        text_align 0.5
        xsize 1450
        ypos 900

    if is_CK2:
        button:
            idle_background "purple_button_idle"
            hover_background "purple_button_hover"
            padding (200, 45)
            xalign 0.5
            yalign 1.0
            action [ShowMenu("ck1_save_load_warning"), Function(change_save_location, "CollegeKings")]

            text "Load CK1 Save" style "bebas_neue_30" align (0.5, 0.5)