class GameBoard:
    def __init__(self, player_1, player_2):
        # board array for arbitrary stuff
        self.board = []
        # easy player lookup
        self.player_location = {}
        self.player_location[player_1] = 3
        self.player_location[player_2] = 5

    def get_board(self):
        return self.board

    def advance_player(self, player, opp, distance):
        direction = 1
        if self.player_location[player] > self.player_location[opp]:
            direction = -1
        for _ in range(distance):
            new_location = self.player_location[player] + direction
            # hop opponent
            if new_location == self.player_location[opp]:
                new_location += direction
            # move if in bounds
            if new_location > 0 and new_location < 8:
                self.player_location[player] = new_location


class Action:
    def __init__(self, name, range_min, range_max, damage, speed, armor, before=None, start=None, hit=None, after=None):
        self.name = name
        self.range_min = range_min
        self.range_max = range_max
        self.damage = damage
        self.speed = speed
        self.armor = armor


class AvailableActions:
    def __init__(self):
        self.type_1_actions = [Action('placeholder', 0,0,0,0,0), Action('placeholder', 0,0,0,0,0), Action('placeholder', 0,0,0,0,0)]
        self.type_2_actions = [
            Action('Grasp', range_min=1,range_max=1,damage=2,speed=5,armor=0),
            Action('Drive', range_min=1,range_max=1,damage=3,speed=4, armor=0),
            Action('Burst', range_min=2,range_max=3,damage=3,speed=1,armor=0),
            Action('Shot',  range_min=1,range_max=4,damage=3,speed=2,armor=2),
            Action('Strike',range_min=1,range_max=1,damage=4,speed=3,armor=5),
            Action('Dodge', range_min=None,range_max=None,damage=4,speed=3,armor=0),
        ]
        self.discard_1 = None
        self.discard_2 = None

    def get_action_combos(self):
        combos = []
        for type_1 in self.type_1_actions:
            for type_2 in self.type_2_actions:
                combos += [(type_1, type_2)]
        return combos

    def discard_actions(self, action_pair):
        type_1, type_2 = self.discard_1
        self.type_1_actions += [type_1]
        self.type_2_actions += [type_2]
        self.discard_1 = self.discard_2
        self.discard_2 = action_pair


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
        self.players = [Player('p1'), Player('p2')]
        self.board = GameBoard(self.players[0], self.players[1])
        self.turn = 0

    def play_turn(self):
        self.turn += 1
        # game turn resolve logic

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
