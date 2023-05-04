style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.webp"

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style nsfw_text is text:
    font "fonts/Montserrat-Bold.ttf"

style nsfw_italic_text is text:
    font "fonts/Montserrat-MediumItalic.ttf"