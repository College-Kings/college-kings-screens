screen save():
    tag menu

    use file_slots(_("Save"))


screen enter_save_name(slot):
    tag menu
    style_prefix "save"

    use save

    text "SAVE NAME:" pos (270, 240)
    
    frame:
        xysize (1083, 99)
        pos (477, 210)
        background "gui/file_slots/save_name.webp"

        input:
            align (0.5, 0.5)
            default save_name
            copypaste True
            value VariableInputValue("save_name")
            allow " .,_-0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

        imagebutton:
            idle "gui/file_slots/save_game_idle.webp"
            hover "gui/file_slots/save_game_hover.webp"
            action [Show("save"), FileAction(slot)]
            align (1.0, 0.5)
            xoffset 13


style save_text is file_slot_text
style save_input is text:
    font "fonts/Montserrat-Bold.ttf"
    size 36
