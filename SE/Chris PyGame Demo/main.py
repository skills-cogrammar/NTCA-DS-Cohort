from objects.GameObject import GameObject
from GameView import GameView


def main():
    game_view = GameView("HyperionDev Test Game", (800, 600))
    player = GameObject("sprites/ship.png", 400, 300, 5, True, (50, 50))
    game_view.add_game_object(player)
    game_view.run()

if __name__ == "__main__":
    main()
