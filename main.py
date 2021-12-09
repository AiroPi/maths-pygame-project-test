import os

from game import Game

os.chdir(os.path.abspath((os.path.dirname(__file__))))


if __name__ == "__main__":
    app = Game()

    try:
        app.loop()
    except KeyboardInterrupt:
        app.quit()
