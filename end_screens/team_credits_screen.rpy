screen team_credits():
    tag end_screen
    modal True
    style_prefix "team_credits"

    default image_path = "screens/end_screens/images/"

    default management = (
        "{b}UndergradSteve{/b} - Game Creator",
        "{b}KingLui{/b} - Operations Manager",
        "{b}OscarSix{/b} - Chief Technology Officer"
    )

    default team_leads = (
        "{b}Messy17{/b} - Lead Transcriber & Renderer & Gameplay Engineer",
        "{b}Mozzart{/b} - Art Director",
        "{b}Spacestorm{/b} - QA Manager",
    )

    default art_team = (
        "{b}Mugi{/b} - Animator",
        "{b}TheFatLebowski{/b} - Animator",
        "{b}Francois{/b} - Renderer",
        "{b}Freja{/b} - Renderer",
        "{b}RogueRoach{/b} - Renderer",
        "{b}SexFM{/b} - Renderer",
        "{b}Stefan{/b} - Renderer & Photoshopper",
        "{b}Zoneh69{/b} - Renderer",
        "{b}Filip Jankovic{/b} - Photoshopper & UI/UX Designer",
    )

    default audio_team = ()

    default business_team = ()

    default consumer_products_team = ()

    default engineering_team = (
        "{b}Irish{/b} - Transcriber & Gameplay Engineer",
        "{b}Smudger{/b} - Transcriber",
        "{b}StefanGaming{/b} - Gameplay Engineer",
    )

    default game_design_team = ()
    
    default information_technology_team = ("{b}Jack Tomalin{/b} - Render Server Administrator",)

    default internship_team = ()

    default leadership = ()

    default localization_team = ()

    default narrative_team = (
        "{b}Pete{/b} - Lead Writer",
        "{b}Ozzy{/b} - Writer",
        "{b}Nicki5617{/b} - Editor",
    )

    default production_team = ()

    default marketing_team = (
        "{b}Adam{/b} - Marketing Manager",
        "{b}Adrien{/b} - Marketing",
        "{b}NicoMS{/b} - Marketing",
    )

    default qa_team = (
        "{b}Dux90{/b} - Quality Assurance",
        "{b}EilDownTown{/b} - Quality Assurance",
        "{b}Rev{/b} - Quality Assurance",
        "{b}Sanjinn{/b} - Quality Assurance",
        "{b}Skepticalz{/b} - Quality Assurance",
        "{b}Zack{/b} - Quality Assurance",
    )

    default ui_ux_team = ()

    default live_operations_team = (
        "{b}Chaser{/b} - Community Administrator & Lead Support Team",
        "{b}Asp{/b} - Community Moderator",
        "{b}Lucass{/b} - Community Moderator",
        "{b}Omni{/b} - Community Moderator",
        "{b}Oskin{/b} - Community Moderator",
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
            action Show("patreon_credits")
            yalign 0.5

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    on "replace" action SetVariable("quick_menu", False)
    on "replaced" action SetVariable("quick_menu", True)
