screen animated_value_bar(old_value, new_value, max_value, left_frame=None, right_frame=None, offset=(0, 0), size=(0, 0), delay=2):
    tag animated_value_bar

    bar:
        value AnimatedValue(new_value, max_value, delay, old_value)
        left_bar left_frame
        right_bar right_frame
        offset offset
        xysize size