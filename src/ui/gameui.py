class GameUI:
    def __init__(self, game_service):
        self.__game_service = game_service

    def __print_board(self):
        print(self.__game_service.get_board_for_printing())

    def __move_snake(self, command):
        if len(command) == 2:
            try:
                command_count = int(command[1])
            except ValueError:
                raise ValueError("Invalid number of steps! It is not an integer!")
            if command_count < 1:
                raise ValueError("Invalid number of steps! It is not a strictly positive integer!")
            for i in range(command_count):
                game_over = self.__game_service.move_snake()
                if game_over:
                    return True
            return False
        elif len(command) == 1:
            return self.__game_service.move_snake()
        else:
            raise ValueError("Invalid number of parameters for the move command!")

    def __turn(self, command_word):
        return self.__game_service.turn(command_word)

    def play_game(self):
        self.__game_service.set_up()
        game_done = False
        while not game_done:
            try:
                self.__print_board()
                command = input("Give a command: ")
                command = command.split()
                if len(command) > 0:
                    command_word = command[0]
                    if command_word == "move":
                        game_done = self.__move_snake(command)
                    elif len(command) == 1 and command_word in ["up", "down", "left", "right"]:
                        game_done = self.__turn(command_word)
                    else:
                        raise ValueError("Invalid command!")
                else:
                    raise ValueError("Invalid command!")
            except ValueError as ve:
                print(ve)
        print("Game over! The snake is no more!")