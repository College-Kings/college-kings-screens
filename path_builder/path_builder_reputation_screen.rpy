screen path_builder_reputation():
    tag path_builder
    modal True
    style_prefix "path_builder"

    default image_path = "screens/path_builder/images"
    default selected_rep = None

    add "path_builder_background"
    add image_path + "/path_builder_box_background.webp" align (0.5, 0.5)

    button:
        idle_background "path_builder_button_idle"
        hover_background "path_builder_button_hover"
        selected_background "path_builder_button_hover"
        action Show("path_builder_advanced_settings")
        xysize (270, 61)
        xalign 1.0
        ypos 20
        xoffset -20

        text "Advanced":
            align (0.5, 0.5)
            color "#FFF"

    imagebutton:
        idle "return_button_idle"
        hover "return_button_hover"
        action MainMenu(False, False)
        pos (50, 20)
         
    add image_path + "/path_builder_step_2.webp" xalign 0.5 ypos 220

    text "Pick your starting reputation" xalign 0.5 ypos 325

    grid 3 1:
        xspacing 10
        align (0.5, 0.5)

        for rep in (Reputations.LOYAL, Reputations.POPULAR, Reputations.CONFIDENT):
            button:
                background "path_builder_button_idle"
                hover_background "path_builder_button_hover"
                selected_background "path_builder_button_hover"
                selected (selected_rep == rep)
                action [SetScreenVariable("selected_rep", rep), Function(reputation.change_reputation, rep)]
                xysize (270, 61)

                text rep.name:
                    align (0.5, 0.5)
                    color "#FFF"

    hbox:
        xalign 0.5
        ypos 750
        spacing 20
        
        imagebutton:
            idle image_path + "/pb_tick.webp"
            hover image_path + "/pb_ticked.webp"
            selected_idle image_path + "/pb_ticked.webp"
            action ToggleVariable("locked_reputation")

        text "Lock Reputation (Prevent it from changing)":
            yoffset -7

    hbox:
        spacing 50
        align (0.5, 1.0)
        yoffset -50

        imagebutton:
            idle image_path + "/back.webp"
            action Show("path_builder_starting_location")

        imagebutton:
            idle image_path + "/continue.webp"
            insensitive Transform(image_path + "/continue.webp", matrixcolor=SaturationMatrix(0))
            sensitive (selected_rep is not None)
            action [Hide(), Show("path_builder_fraternity")]
