# Tic-Tac-Toe trainer

Algorithm that can be trained to play Tic-Tac-Toe (or naughts & crosses) in a few minutes.

# How to use

You can either train the engine by letting it play itself, or you can play against it. When playing it will learn from the wins and losses that happens.

## Play the engine

To play against it, run:

    play.py

The engine will make the first turn and play _X_ by default. The output will be something like this:

    Round 1, ID: 111111111 ([908, 423, 1005, 447, 755, 389, 1300, 700, 1244])
    [' ', ' ', ' ']
    [' ', ' ', ' ']
    [' ', 'x', ' ']
    Round 2, ID: 111111121 ([0, 0, 0, 0, 2, 0, 0, 0, 0])
    Choose position:

The 9-digit number is the code for a particular board configuration and the list of numbers are the weights the engine uses to make the next move.

When it is your turn, the weights for the board is printed for your information - which you can obviously just ignore.

You enter the number of the square (0-8) where you want to place your piece.

The game continues until a side has won or it s a draw.

## Training the engine

The engine can be trained by letting it play itself. To play a game, run:

    play.py -t

The engine will play both sides. The output will be something like this:

    Iteration 0, New Round, x to start
    Iteration 0, Round 1, x to play, ID: 111111111 ([908, 423, 1005, 447, 755, 389, 1300, 700, 1244])
    [' ', ' ', ' ']
    [' ', ' ', 'x']
    [' ', ' ', ' ']
    Iteration 0, Round 2, o to play, ID: 111112111 ([16, 2, 42, 4, 70, 0, 0, 0, 92])
    [' ', ' ', ' ']
    [' ', ' ', 'x']
    [' ', ' ', 'o']
    Iteration 0, Round 3, x to play, ID: 111112113 ([187, 52, 16, 7, 97, 0, 271, 82, 0])
    [' ', 'x', ' ']
    [' ', ' ', 'x']
    [' ', ' ', 'o']
    Iteration 0, Round 4, o to play, ID: 121112113 ([36, 0, 96, 100, 104, 0, 292, 84, 0])
    [' ', 'x', 'o']
    [' ', ' ', 'x']
    [' ', ' ', 'o']
    Iteration 0, Round 5, x to play, ID: 123112113 ([70, 0, 0, 55, 165, 0, 125, 65, 0])
    [' ', 'x', 'o']
    ['x', ' ', 'x']
    [' ', ' ', 'o']
    Iteration 0, Round 6, o to play, ID: 123212113 ([0, 0, 0, 0, 298, 0, 0, 0, 0])
    [' ', 'x', 'o']
    ['x', 'o', 'x']
    [' ', ' ', 'o']
    Iteration 0, Round 7, x to play, ID: 123232113 ([0, 0, 0, 0, 0, 0, 0, 0, 0])
    [' ', 'x', 'o']
    ['x', 'o', 'x']
    [' ', 'x', 'o']
    Iteration 0, Round 8, o to play, ID: 123232123 ([348, 0, 0, 0, 0, 0, 0, 0, 0])
    ['o', 'x', 'o']
    ['x', 'o', 'x']
    [' ', 'x', 'o']
    o won

You can also make the engine play multiple games by using the `-i` option:

    play.py -t -i 100

In this case it will play 100 games against itself. At the end of a training session, the stats are printed:

    {'x': 4, '-': 92, 'o': 4}

In this session _X_ won 4 times, _O_ won 4 times and there were 92 draws.

# Comments about training

Tic-Tac-Toe can be played in a way were a draw is always the outcome. It's really not hard to learn, and when you have mastered it, it becomes quite boring, quite quickly.

The engine will also get to this point, where all games end in a draw and the only way it will win is if it plays against you and you make a mistake. At this point, you will never be able to beat it.

I haven't measured it precisely, but it takes about 2-300000 games for it to reach this level. On my Macbook Pro that is about 2-3 minutes of training!
