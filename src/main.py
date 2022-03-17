from domain.board import Board
from domain.settings import Settings
from service.gameservice import GameService
from ui.gameui import GameUI

if __name__ == "__main__":
    settings = Settings("../settings.properties")
    if settings.dimension < 3:
        print("This game is impossible to set up, try a bigger size for the board")
    else:
        board = Board(settings.dimension)
        game_service = GameService(board, settings.apple_count)
        game_ui = GameUI(game_service)
        try:
            game_ui.play_game()
        except ValueError as ve:
            print(ve)

