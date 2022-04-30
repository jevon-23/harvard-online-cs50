# Minesweeper

An AI that plays Minesweeper. [Starter code & problem.](https://cs50.harvard.edu/ai/2020/projects/1/minesweeper/)
<br><br>
# Installation and Execution

First pull down repo with and go into repo with : <br>
```git clone https://github.com/jevon-23/harvard-online-cs50 && cd harvard-online-cs50/minesweeper```

To install the requirements, first execute:<br>
```pip3 install -r requirements.txt```
<br><br>
Then to run the game execute: <br>
```python3 runner.py```
<br> <br>

# Game Details and debugging tips
Press play game, and starts immediately. On fail, hover over restart and it retries.
<br>
If anything doesn't work in installation/ execution, you can check out the direct source to see how to run in with the link up above.
<br><br>
# Implementation Details:
The start code provided the implementation for the board and all graphics. The only job that I had was to implement the functionality
for the AI (It never wins. It has gotten down to 1 block left, but it has never actually got a win).
<br><br>
Begins by choosing a random location on the board. Also maintains a safe list where we know it is safe to choose a position on the board and it not be a
mine. Definitely some logical implementation error, but reading back on that code is pretty bad so I'll let it be.
<br>

