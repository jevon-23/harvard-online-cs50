from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Implication(And(AKnight, Not(AKnave)), AKnight),
    Implication(Or(
        And(AKnave, Not(AKnight)), Not(And(AKnave, AKnave)), Not(And(AKnight, AKnight))), AKnave),
    Implication(AKnave, BKnight),
    Implication(AKnight, BKnave)

    #Implication(Not(And(BKnight, BKnave)), BKnave),
    #Implication(Not(And(CKnight, CKnave)), CKnave)
    # TODO
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(Biconditional(AKnight, Not(AKnave)), Biconditional(AKnave, Not(AKnight))),
    Or(Biconditional(BKnight, Not(BKnave)), Biconditional(BKnave, Not(BKnight))),
    Implication(And(AKnave, BKnave), AKnight),
    Implication(Or(And(AKnave, Not(BKnave)), Not(AKnave), Not(BKnave)), AKnave),
    Implication(AKnave, BKnight),
    Implication(AKnight, BKnave)
    # TODO
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
''',

    knowledge1,
    Implication(And(AKnight, BKnight), AKnight),
    Implication(Or(And(AKnight, BKnave), And(AKnave, BKnight)),  BKnight),
    Implication(BKnight, AKnave)'''
knowledge2 = And(
    Or(Biconditional(AKnight, Not(AKnave)), Biconditional(AKnave, Not(AKnight))),
    Or(Biconditional(BKnight, Not(BKnave)), Biconditional(BKnave, Not(BKnight))),
    Implication(Or(And(AKnight, BKnight), And(AKnave, BKnave)), AKnight),
    Implication(Or(And(AKnight, BKnave), And(AKnave, BKnight)),  BKnight),
    Biconditional(BKnight, AKnave),
    Biconditional(AKnight, BKnave)


    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    #Rules of the game
    Or(Biconditional(AKnight, Not(AKnave)), Biconditional(AKnave, Not(AKnight))), Not(And(AKnight, AKnave)),
    Or(Biconditional(BKnight, Not(BKnave)), Biconditional(BKnave, Not(BKnight))), Not(And(BKnight, BKnave)),
    Or(Biconditional(CKnight, Not(CKnave)), Biconditional(CKnave, Not(CKnight))), Not(And(CKnight, CKnave)),
    #A says either...
    Implication(AKnight, Or(AKnight, AKnave)), Implication(AKnave, Not(AKnight)),
    Or(AKnight, AKnave),
    #B says 'A said...'
    Implication(Not(AKnave), BKnave), Implication(AKnave, BKnight),
    #B says C is a Knave
    Biconditional(BKnight, CKnave), Biconditional(CKnight, BKnave),
    Implication(Not(CKnave), BKnave), Implication(CKnave, BKnight),
    #C says A is a Knight
    Or(And(CKnight, AKnight), And(CKnave, AKnave)),
    Or(Biconditional(CKnight, AKnight), Biconditional(AKnave, CKnave)),
    # TODO
)
"""#What makes B a knave / Knight
Biconditional(Or(AKnight, CKnight), BKnave), Biconditional(Or(AKnave, CKnave), BKnight),
#What makes C a Knave / Knight
Biconditional(Or(BKnight, AKnave), CKnave), Biconditional(Or(BKnave, AKnight), CKnight),
#What makes A a knave or knight
Biconditional(Or(BKnight, CKnave), AKnave), Biconditional(Or(BKnave, CKnight), AKnight)"""

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")
            print('=========================')


if __name__ == "__main__":
    main()
