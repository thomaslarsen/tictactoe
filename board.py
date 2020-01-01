def checkEqualIvo(lst):
    return lst[0] != ' ' and lst.count(lst[0]) == len(lst)

class Board():
    def __init__(self):
        self.board = [' '] * 9
        self.done = False

    def __str__(self):
        return str(self.board[0:3]) + '\n' + str(self.board[3:6]) + '\n' + str(self.board[6:9])

    def code(self, side):
        code = ''

        for state in self.board:
            if state == ' ':
                code += '1'
            elif state == side:
                code += '2'
            elif state != side:
                code += '3'
            else:
                raise Exception('Unknown state ({state}) of position'.format(state=state))

        return code

    def set(self, position, side):
        if self.done:
            raise Exception("Game already finished")

        if position not in range(0, 9):
            raise Exception("Position {position} is off board".format(position=position))

        if self.taken(position):
            raise Exception("Position {position} already placed".format(position=position))

        self.board[position] = side

        # Check the status of the game
        self.done, self.winner = self.__check()

        return self.done, self.winner

    def taken(self, position):
        return self.board[position] != ' '

    def free(self, position):
        return self.board[position] == ' '

    def __check(self):
        if checkEqualIvo(self.board[0:3]):
            return True, self.board[0]
        if checkEqualIvo(self.board[3:6]):
            return True, self.board[3]
        if checkEqualIvo(self.board[6:9]):
            return True, self.board[6]
        if checkEqualIvo(self.board[0::3]):
            return True, self.board[0]
        if checkEqualIvo(self.board[1::3]):
            return True, self.board[1]
        if checkEqualIvo(self.board[2::3]):
            return True, self.board[2]
        if checkEqualIvo([self.board[0], self.board[4], self.board[8]]):
            return True, self.board[0]
        if checkEqualIvo([self.board[2], self.board[4], self.board[6]]):
            return True, self.board[2]

        return self.board.count(' ') == 0, None

    def status(self):
        return self.done, self.winner
