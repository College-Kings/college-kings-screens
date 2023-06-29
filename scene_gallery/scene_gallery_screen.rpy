default persistent.name = ""
default persistent.gallery_lock = None
default global_replay_scope = {}

screen scene_gallery():
    tag menu
    modal True
    style_prefix "scene_gallery"

    add "scene_gallery_background"

    imagebutton:
        idle "scene_gallery_return_idle"
        hover "scene_gallery_return_hover"
        action ShowMenu("main_menu")
        pos (120, 80)

    # Gallery unlock
    if is_deluxe():
        frame:
            xalign 1.0
            xoffset -50
            ypos 50

            if persistent.gallery_lock is None:
                textbutton "Unlock Scene Gallery":
                    action SetField(persistent, "gallery_lock", False)
                    text_size 36
            else:
                textbutton "Lock Scene Gallery":
                    action SetField(persistent, "gallery_lock", None)
                    text_size 36

    fixed:
        pos (114, 178)
        ypos 178
        xysize (1688, 830)

        vpgrid id "vpg":
            cols 4
            spacing 20
            xalign 0.5
            top_margin 50
            bottom_margin 80
            mousewheel True
            allow_underfull True
            
            for gallery_item in scene_gallery_items:
                frame:
                    xysize (374, 300)

                    button:
                        background gallery_item.idle_image
                        insensitive_background gallery_item.locked_image
                        idle_foreground "scene_gallery_button_idle"
                        hover_foreground "scene_gallery_button_hover"
                        insensitive_foreground "scene_gallery_button_idle"
                        action Replay(gallery_item.label, scope=update_scope(gallery_item.scope), locked=persistent.gallery_lock)
                    frame:
                        xysize (250, 49)
                        xalign 0.5
                        ypos 224

                        text gallery_item.title align (0.5, 0.5)

            null

    add "scene_gallery_shadow" xalign 0.5 ypos 893

    add Transform("scene_gallery_bar_base", size=(27, 734)) pos (1743, 226)
    vbar:
        pos (1748, 231)
        xysize (17, 724)
        base_bar "#0000"
        thumb "gui/bar/bar_thumb.webp"
        value YScrollValue("vpg")


style scene_gallery_text is bebas_neue_30:
    size 22


label scene_gallery_name_change:
    scene black

    if not persistent.name.strip():
        $ persistent.name = renpy.input(_("What's your name?"), default=_("Alex")).strip() or _("Alex")

    $ global_replay_scope = {"name": persistent.name}

    return
