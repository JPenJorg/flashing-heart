def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_leds("""
    # # . # .
        # # # # #
        # # # # #
        . # . . .
        . . # . #
""")
music.play_melody("F F - E D - - - ", 120)

def on_forever():
    basic.show_leds("""
        # # . # #
                # # . . .
                # # # . #
                . # . # #
                . . # . .
    """)
basic.forever(on_forever)
