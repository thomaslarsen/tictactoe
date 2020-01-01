#!/usr/bin/env python

from game import Game
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-i", "--iterations", dest="iterations",
                    default=1, type=int, metavar='NUM',
                    help="number of training iterations")
parser.add_argument("-t", "--train",
                    action="store_true", dest="train", default=False,
                    help="train the engine")
parser.add_argument("-f", "--first",
                    action="store_true", dest="player_go_first", default=False,
                    help="player go first")
parser.add_argument("-b", "--break",
                    action="store_true", dest="break_at_win", default=False,
                    help="break at win")
parser.add_argument("-s", "--swap",
                    action="store_true", dest="take_turns_to_start", default=False,
                    help="swap sides when training")
parser.add_argument("-w", "--weight", dest="weight",
                    default=None, type=str, metavar='CODE',
                    help="return the value of a weight")

def main(args):
    g = Game()

    if args.weight:
        print(g.w[args.weight])
        return

    if args.train:
        g.train(
            iterations=args.iterations,
            break_at_win=args.break_at_win,
            take_turns_to_start=args.take_turns_to_start
        )
    else:
        g.play(
            i_start=args.player_go_first
        )

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
