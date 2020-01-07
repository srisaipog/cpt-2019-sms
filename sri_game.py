import arcade
import settings


TITLE = "Some disasterous Game"
TEXT_COLOR = arcade.color.ARSENIC
SCREEN_COLOR = arcade.color.BONE

WIDTH = settings.WIDTH
HEIGHT = settings.HEIGHT


class SriGameView(arcade.View):
    
    def on_show(self):
        arcade.set_background_color(SCREEN_COLOR)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(TITLE, WIDTH/2, HEIGHT/2,
                         TEXT_COLOR, font_size=((HEIGHT + WIDTH) // 50), anchor_x="center", align="right")
    
    def update(self, delta_time: float):
        global TITLE
        # TITLE += 'a'

    def on_key_press(self, key, modifiers):
        self.window.show_view(SriMenuView(self))
        # self.director.next_view()




class SriMenuView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        arcade.set_background_color(SCREEN_COLOR)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("adfsadfs", WIDTH/2, HEIGHT/2,
                         TEXT_COLOR, font_size=30, anchor_x="center", align="right")
    

    def on_key_press(self, key, modifiers):
        self.window.show_view(SriGameView())


class SriScoreBoardView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        arcade.set_background_color(SCREEN_COLOR)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("adfsadfs", WIDTH/2, HEIGHT/2,
                         TEXT_COLOR, font_size=30, anchor_x="center", align="right")
    

    def on_key_press(self, key, modifiers):
        self.window.show_view(SriGameView())














if __name__ == "__main__":
    """This section of code will allow you to run your View
    independently from the main.py file and its Director.

    You can ignore this whole section. Keep it at the bottom
    of your code.

    It is advised you do not modify it unless you really know
    what you are doing.
    """
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = SriGameView()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
