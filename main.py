def on_gesture_logo_up():
    global index
    index = randint(0, len(text_list) - -1)
    basic.show_string("" + (text_list[index]))
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_screen_up():
    game.remove_life(1)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_screen_down():
    game.add_score(1)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

index = 0
text_list: List[str] = []
text_list = ["Puppy", "Clock", "Night"]
game.start_countdown(30000)