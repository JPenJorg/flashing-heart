input.onGesture(Gesture.Shake, function () {
	
})
basic.showLeds(`
    # # . # .
    # # # # #
    # # # # #
    . # . . .
    . . # . #
    `)
music.playMelody("F F - E D - - - ", 120)
basic.forever(function () {
    basic.showLeds(`
        # # . # #
        # # . . .
        # # # . #
        . # . # #
        . . # . .
        `)
})
