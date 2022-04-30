# Tic Tac Toe

An AI that plays tic-tac-toe against its opponent (user). [Starter code & problem.](https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/)
<br><br>
# Installation and Execution

First pull down repo with and go into repo with : <br>
```git clone https://github.com/jevon-23/harvard-online-cs50 && cd harvard-online-cs50/tictactoe```

To install the requirements, first execute:<br>
```pip3 install -r requirements.txt```
<br><br>
Then to run the game execute: <br>
```python3 runner.py```
<br> <br>

# Game Details and debugging tips
X goes first, O goes second. At the first prompt, choose X or O, then the game will start immediately
<br>
If anything doesn't work, you can check out the direct source to see how to run in with the link up above.
<br><br>
# Implementation Details:
The start code provided the implementation for the board and actually drawing the X's and O's. The only job that I had was to implement the functionality
for the AI.
<br><br>
Uses Minimax trees with a basic heuristic function to determine what move to make next based on the current state of the board. 
<br>
One change that I would make now would be to add some randomness to the movement, alongside making different difficulties.
