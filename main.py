def on_received_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
    elif receivedNumber == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . # # # .
                        . . . . .
                        . . . . .
        """)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
    else:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
        basic.pause(500)
    basic.clear_screen()
radio.on_received_number(on_received_number)

def on_logo_long_pressed():
    radio.send_number(1)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    radio.send_number(0)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_number(2)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_number(1)
    basic.show_leds("""
        . . . . .
                . . . . .
                . # # # .
                . . . . .
                . . . . .
    """)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    radio.send_number(0)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
