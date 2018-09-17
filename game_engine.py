class GameBoard:
    def __init__(self):
        self.board = []

    def get_board(self):
        return self.board

    def advance_player(self):
        pass


class Action:
    def __init__(self, name, range_min, range_max, damage, speed, armor):
        self.name = name
        self.range_min = range_min
        self.range_max = range_max
        self.damage = damage
        self.speed = speed
        self.armor = armor


class AvailableActions:
    def __init__(self):
        self.type_1_actions = [Action('placeholder', 0,0,0,0,0), Action('placeholder', 0,0,0,0,0), Action('placeholder', 0,0,0,0,0)]
        self.type_2_actions = [Action('placeholder', 0,0,0,0,0), Action('placeholder', 0,0,0,0,0), Action('placeholder', 0,0,0,0,0)]

    def get_action_combos(self):
        combos = []
        for type_1 in self.type_1_actions:
            for type_2 in self.type_2_actions:
                combos += [(type_1, type_2)]
        return combos


class Player:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.available_actions = AvailableActions()

    def get_life(self):
        return self.life

    def change_life(self, life):
        self.life += life


class Game:
    def __init__(self):
        self.board = GameBoard()
        self.players = [Player('p1'), Player('p2')]
        self.turn = 0

    def play_turn(self):
        self.turn += 1
        return True

    def print_turn_results(self):
        print self.turn
        for player in self.players:
            print player.name, player.life


def main():
    game = Game()
    while game.play_turn():
        game.print_turn_results()


if __name__ == '__main__':
    main()
