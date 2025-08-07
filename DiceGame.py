import random
class Die:
    def __init__(self, value=None):
        self._value =value

    @property
    def value(self):
        return self._value

    def roll(self):
        new_val= random.randint(1,6)
        self._value=new_val
        return new_val

#my_die =Die()

class Player:


    def __init__(self, die, is_computer=False):
        self._die=die
        self._is_computer = is_computer
        self._counter=5

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter


    def increment_value(self):
        self._counter+=1

    def decrement_value(self):
        self._counter-=1

    def roll_die(self):
        return self._die.roll()

#my_die =Die()

#player= Player(my_die, True)

class DieGame:


    def __init__(self, player,computer):

        self._player=player
        self._computer=computer
    @property
    def player(self):
        return self._player
    @property
    def computer(self):
        return self._computer

    def start_play(self):
        print("Welcome to game!")

        while True:
            self.play_round()
            game_over=self.check_game_over()
            if game_over:
                break
    def check_game_over(self):
        if self._player.counter ==0:
            self.show_game_over(winner=self._player)
            return True
        elif self._computer.counter==0:
            self.show_game_over(winner=self._computer)
            return True
        else:
            return False
    def show_game_over(self,winner):
        if winner.is_computer:
            print("Game over!")
            print("computer wins!")
        else:
            print("Game over!")
            print("You won the match!")




    def play_round(self):

        print("--------enter a new round:-----------")

        input("please press a key to roll dice:")

        player_value = self._player.roll_die()
        computer_value =self._computer.roll_die()

        if computer_value > player_value:
            print(f"player value:{player_value}")
            print(f"computer value:{computer_value}")
            print("computer wins round!")

            self._computer.decrement_value()
            self._player.increment_value()
        elif computer_value< player_value:
            print(f"player value:{player_value}")
            print(f"computer value:{computer_value}")
            self._player.decrement_value()
            self._computer.increment_value()
            print("You win round!")
        else:
            print("Match tie!")

        print(f"computer score: {self._computer.counter}")
        print(f"Your score: {self._player.counter}")



my_die=Die()
comp_die=Die()
player= Player(my_die,False)

computer=Player(comp_die,True)
game=DieGame(player,computer)

game.start_play()


