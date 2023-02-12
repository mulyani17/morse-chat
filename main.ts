radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    if (receivedNumber == 0) {
        basic.showLeds(`
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        `)
        music.playTone(262, music.beat(BeatFraction.Quarter))
    } else if (receivedNumber == 1) {
        basic.showLeds(`
            . . . . .
                        . . . . .
                        . # # # .
                        . . . . .
                        . . . . .
        `)
        music.playTone(262, music.beat(BeatFraction.Whole))
    } else {
        basic.showLeds(`
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        `)
        basic.pause(500)
    }
    
    basic.clearScreen()
})
input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_long_pressed() {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendNumber(0)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    `)
    music.playTone(262, music.beat(BeatFraction.Quarter))
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    radio.sendNumber(2)
    basic.showLeds(`
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendNumber(1)
    basic.showLeds(`
        . . . . .
                . . . . .
                . # # # .
                . . . . .
                . . . . .
    `)
    music.playTone(262, music.beat(BeatFraction.Whole))
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    radio.sendNumber(0)
})
