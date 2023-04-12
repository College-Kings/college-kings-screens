screen path_builder_advanced_settings():
    zorder 100
    modal True

    default image_path = "screens/path_builder/images/"

    add image_path + "path_builder_background.webp"

    imagebutton:
        idle "gui/common/return_idle.webp"
        hover "gui/common/return_hover.webp"
        action Hide("path_builder_advanced_settings")
        align (0.015, 0.015)
        

    hbox: 
        align (0.5, 0.5)
        spacing 100
        vbox:
            spacing 20

            text "Extras" color "#FFD166" size 50
 
            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action [ToggleVariable("v0_protest"), ToggleVariable("v0_signs"), ToggleVariable("v0_visited_shelter")]

                text "Attended protest with Autumn":
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("v0_pen_goes_europe")

                text "Won Penelope hearing":
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    selected "v11_aubrey" in viewed_scenes
                    if "v11_aubrey" in viewed_scenes:
                        action RemoveFromSet(viewed_scenes, "v11_aubrey")
                    else:
                        action AddToSet(viewed_scenes, "v11_aubrey")

                text "Had airplane sex with Aubrey":
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("v0s48_canoeing_as_date")

                text "Got romantic with Aubrey in Amsterdam":
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("v0_ride_with_mrlee")

                text "Sided with Mr. Lee in London":
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action [ToggleVariable("v0_chase_robber"), ToggleVariable("v0_fight_win")]

                text "Got back Nora's purse":
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    selected "v12_lauren" in viewed_scenes
                    if "v12_lauren" in viewed_scenes:
                        action RemoveFromSet(viewed_scenes, "v12_lauren")
                    else:
                        action AddToSet(viewed_scenes, "v12_lauren")

                text "Had sex with Lauren in Paris":
                    yoffset -7
                    
            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("v0_penelope_concert")

                text "Polly concert with Penelope (instead of Aubrey)":
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("v0_concert_backstage")

                text "Went backstage at Polly concert":
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("v0_charli_exposed")

                text "Exposed Charli to Mr. Lee":
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("v0_imre_disloyal")

                text "Imre caught you and Nora":
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("v0_perfume")

                text "Bought perfume for Ms. Rose in Amsterdam":
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    selected "v14_threesome" in viewed_scenes
                    if "v14_threesome" in viewed_scenes:
                        action RemoveFromSet(viewed_scenes, "v14_threesome")
                    else:
                        action AddToSet(viewed_scenes, "v14_threesome")

                text "Had Riley & Aubrey threesome":
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("v0s03a_take_wallet")

                text "Stole hustler's wallet in Amsterdam":
                    yoffset -7

        vbox:
            spacing 20

            text "Gameplay Changes" color "#FFD166" size 50

            if renpy.loadable("v1/scene1.rpy"):            
                hbox:
                    spacing 20
                    
                    imagebutton:
                        idle image_path + "pb_tick.webp"
                        hover image_path + "pb_ticked.webp"
                        selected_idle image_path + "pb_ticked.webp"
                        action [ToggleVariable("lindsey_board.money", 10000, 200), ToggleVariable("chloe_board.money", 10000, 1500)]

                    text "Unlimited Presidency Campaign Budget":
                        yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("pb_reputation_shown")

                text "Show preferred reputation for each girl (in Step 04)":
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("pb_reputation_notification")

                text "Show a notification whenever you gain reputation points":
                    yoffset -7
    

style path_builder_advanced_settings_text is bebas_neue_30
