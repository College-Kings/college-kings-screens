screen team_credits(support_link=None):
    tag end_screen
    modal True
    style_prefix "team_credits"
    default image_path = "screens/end_screens/images/"

    if support_link is None:
        $ support_link = "https://store.steampowered.com/app/1924480/"

    default management = (
        "{b}UndergradSteve{/b} - Game Creator",
        "{b}Irish{/b} - Operations Officer"
    )

    default team_leads = ()

    default art_team = (
        "{b}Stefan{/b} - Lead Artist, Game Renderer, Photoshopper",
        "{b}SexFM{/b} - Animator, Gamer Renderer",
        "{b}Messy{/b} - Game Renderer, Marketing & Patreon Renderer",
        "{b}Takeover Rug{/b} - Game Renderer, Marketing & Patreon Renderer"        
    )

    default audio_team = ()

    default business_team = ()

    default consumer_products_team = ()

    default engineering_team = (
        "{b}Irish{/b} - Transcriber & Gameplay Engineer",
        "{b}Messy{/b} - Transcriber, Tools Developer, Gameplay Engineer"
    )

    default game_design_team = ()

    default information_technology_team = ("{b}Jack Tomalin{/b} - Render Server Administrator",)

    default internship_team = ()

    default leadership = ()

    default localization_team = ()

    default narrative_team = (
        "{b}Ozzy{/b} - Writer",
    )

    default production_team = ()

    default marketing_team = (
        "{b}Adam{/b} - Marketing Manager",
        "{b}Adrien{/b} - Marketing",
    )

    default qa_team = (
        "{b}Dux90{/b} - Quality Assurance",
        "{b}Ozzy{/b} - Quality Assurance",
        "{b}Irish{/b} - Quality Assurance",
        "{b}Messy{/b} - Quality Assurance",
        "{b}Rev{/b} - Quality Assurance",
        "{b}Sanjinn{/b} - Quality Assurance",
        "{b}Skepticalz{/b} - Quality Assurance",
        "{b}Zack{/b} - Quality Assurance",
    )

    default ui_ux_team = ()

    default live_operations_team = (
        "{b}Irish{/b} - Community Administrator & Lead Support Team",        
        "{b}Asp{/b} - Community Moderator",
        "{b}Lucass{/b} - Community Moderator",
        "{b}Onni{/b} - Community Moderator",
        "{b}Oskin{/b} - Community Moderator",
        "{b}Messy{/b} - Game Support"
    )

    default teams = (
        management,
        team_leads,
        art_team,
        audio_team,
        business_team,
        consumer_products_team,
        engineering_team,
        game_design_team,
        information_technology_team,
        internship_team,
        leadership,
        live_operations_team,
        localization_team,
        narrative_team,
        production_team,
        marketing_team,
        qa_team,
        ui_ux_team
    )

    add image_path + "team_credits_background.webp"

    fixed:
        ysize 890
        ypos 125

        viewport:
            mousewheel True
            ysize 850
            yalign 0.5

            vbox:
                xfill True

                for team in (team for team in teams if team):
                    for i in team:
                        text i

                    null height 25

                null height 100

                text _("Special thanks to all the community members and players who have made this possible")

    hbox:
        align (0.5, 1.0)

        imagebutton:
            idle image_path + "main_menu_idle.webp"
            hover image_path + "main_menu_hover.webp"
            action MainMenu()
            yalign 0.5

        imagebutton:
            idle Transform("gui/common/credits_idle.webp", zoom=0.72)
            hover Transform("gui/common/credits_hover.webp", zoom=0.72)
            action Show("patreon_credits", None, support_link)
            yalign 0.5

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    on "replace" action SetVariable("quick_menu", False)
    on "replaced" action SetVariable("quick_menu", True)
