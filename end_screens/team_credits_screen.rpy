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
        "{b}Mozzart{/b} - Lead Artist & Coordinator"
    )

    default art_team = (
        "{b}Mugi{/b} - Animator",
        "{b}TheFatLebowski{/b} - Animator",
        "{b}day1patch{/b} - Renderer",
        "{b}Fooxied{/b} - Renderer",
        "{b}Francois{/b} - Renderer",
        "{b}RogueRoach{/b} - Renderer",
        "{b}SexFM{/b} - Renderer",
        "{b}zoneh69{/b} - Renderer",
        "{b}Filip Jankovic{/b} - Photoshopper & UI/UX Designer",
        "{b}stefan33{/b} - Photoshopper",
    )

    default audio_team = ()

    default engineering_team = ("{b}Irish{/b} - Transcriber & Gameplay Engineer",)

    default game_design_team = ()
    
    default narrative_team = (
        "{b}Peter{/b} - Lead Writer",
        "{b}Ozzy{/b} - Writer",
        "{b}Nicki5617{/b} - Editor",
    )

    default qa_team = (
        "{b}Rev{/b} - Quality Assurance Specialist",
        "{b}Skepticalz{/b} - Quality Assurance Specialist",
        "{b}Stefan{/b} - Quality Assurance Specialist",
    )

    default ui_ux_team = ()

    default business_team = ()

    default consumer_products_team = ()

    default information_technology_team = ("{b}Jack Tomalin{/b} - Render Server Administrator",)

    default marketing_team = (
        "{b}Adrian{/b} - Marketing Manager",
        "{b}NicoMS{/b} - Marketing",
    )

    default live_operations_team = (
        "{b}Chaser{/b} - Community Administrator & Lead Support Team",
        "{b}Oskin{/b} - Community Moderator & Support Team",
        "{b}Asp{/b} - Community Moderator",
        "{b}Lucass{/b} - Community Moderator",
        "{b}Omni{/b} - Community Moderator",
    )

    default internship_team = ()

    default localization_team = ()

    default additional = (
        "{b}Chinay{/b} - For volunteer testing and contributing to the project",
    )

    default teams = (management, team_leads, art_team, audio_team, engineering_team, game_design_team, narrative_team, qa_team, ui_ux_team, business_team, consumer_products_team, information_technology_team, marketing_team, live_operations_team, internship_team, localization_team, additional)

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
