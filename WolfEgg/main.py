from window import Window

window_object = Window()

while window_object.running:
    window_object.curr_menu.display_menu()
    window_object.game_loop()
