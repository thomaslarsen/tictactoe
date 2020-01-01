from board import Board
import random
import json
import os.path

weight_file_path = './weights.json'

class Game():
    def __init__(self, weights=None):
        if weights:
            self.w = dict(weights)
        else:
            if os.path.isfile(weight_file_path):
                with open(weight_file_path, 'r') as w_file:
                    self.w = json.load(w_file)
            else:
                self.w = {}

    def __get_cue(self, b):
        if b.code() in self.w:
            return self.w[b.code()]
        else:
            return [100 if state == '1' else 0 for state in b.code()]

    def __take_turn(self, b, turn, cue):
        if sum(cue) == 0:
            position = int(random.random() * 9)
            while b.taken(position):
                position = int(random.random() * 9)
        else:
            choice = int(random.random() * sum(cue))

            for i, p in enumerate(cue):
                if choice < p:
                    position = i
                    break
                else:
                    choice -= p

        if b.taken(position):
            raise Exception('Chosen position ({position}) taken'.format(position=position))

        done, winner = b.set(position, turn)

        return done, winner, position

    def __learn(self, winner, steps):
        if winner:
            for i, s in enumerate(steps):
                cue = s['cue']

                if s['side'] == winner:
                    if i == len(steps) - 1: # The winning move
                        cue = [cue[p] if p == s['position'] else 0 for p in range(0,9)]
                    cue[s['position']] += 1 + i
                else:
                    if i == len(steps) - 2: # The loosing move
                        cue[s['position']] = 0   # Never make this move again
                    else:
                        cue[s['position']] -= 1 + i

                # Normalise the cue
                if min(cue) < 0:
                    cue_adjust = -(min(cue))
                    norm_cue = [c + (cue_adjust if s['code'][i] == '1' else 0) for i, c in enumerate(cue)]
                else:
                    norm_cue = cue

                self.w[s['code']] = norm_cue

    def train(self, iterations=1, break_at_win=False, start_with='x', take_turns_to_start=False):
        stats = {
            'x': 0,
            'o': 0,
            '-': 0
        }

        for iteration in range(0, iterations):
            b = Board()

            print('Iteration {iteration}, New Round, {turn} to start'.format(iteration=iteration, turn=start_with))

            turn = start_with
            done = False
            steps = []
            winner = None

            while not done:
                cue = self.__get_cue(b)
                pre_move_code = b.code()

                print('Iteration {iteration}, Round {round}, {turn} to play, ID: {code} ({cue})'.format(iteration=iteration, round=len(steps) + 1, turn=turn, code=pre_move_code, cue=cue))

                done, winner, position = self.__take_turn(b, turn, cue)

                print(b)

                steps.append({
                    'code': pre_move_code,
                    'side': turn,
                    'position': position,
                    'cue': cue
                })

                turn = 'x' if turn == 'o' else 'o'

            print('{winner} won'.format(winner=winner))

            self.__learn(winner, steps)

            stats[winner if winner else '-'] += 1

            if winner and break_at_win:
                return

            if take_turns_to_start:
                start_with = 'x' if start_with == 'o' else 'o'

        print(stats)

        # save weights
        with open(weight_file_path, 'w') as w_file:
            json.dump(self.w, w_file)

    def play(self, i_start=False, start_with='x'):
        b = Board()

        player_side = start_with if i_start else ('o' if start_with == 'x' else 'x')

        turn = start_with
        done = False
        winner = None
        steps = []

        while not done:
            cue = self.__get_cue(b)

            print('Round {round}, ID: {code} ({cue})'.format(round=len(steps) + 1, code=b.code(), cue=cue))

            if (turn == player_side):
                ok = False
                while not ok:
                    position = int(input("Choose position: "))
                    if position in range(0, 9) and b.free(position):
                        ok = True
                done, winner = b.set(position, turn)
            else:
                done, winner, position = self.__take_turn(b, turn, cue)

            steps.append({
                'code': b.code(),
                'side': turn,
                'position': position,
                'cue': cue
            })

            print(b)

            turn = 'x' if turn == 'o' else 'o'

        self.__learn(winner, steps)

        if winner:
            print('You {result}'.format(result='WIN' if winner==player_side else 'LOOSE'))
        else:
            print('DRAW')
