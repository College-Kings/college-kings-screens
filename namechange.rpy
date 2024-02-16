label change_name:
    scene black 

    $ name = renpy.input(_("What's your name?"), default=_("Alex")).strip() or _("Alex")
    $ pb_name_set = True
