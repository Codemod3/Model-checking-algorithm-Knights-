from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

KnowledgeBase = And(
    Or(AKnave,AKnight),
    Or(BKnave,BKnight),
    Or(CKnave,CKnight),
    Not(And(AKnave,AKnight)),
    Not(And(BKnave,BKnight)),
    Not(And(CKnave,CKnight))
)
# Puzzle 0s
# A says "I am both a knight and a knave."
knowledge0 = And(
    KnowledgeBase,
    Implication(AKnight,And(AKnight,AKnave)),
    Implication(AKnave, Not(And(AKnave,AKnight)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    KnowledgeBase,
    Implication(AKnight,And(AKnave,BKnave)),
    Implication(AKnave,Not(And(AKnave,BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    KnowledgeBase,
    Implication(AKnight,(Or(And(AKnave,BKnave),And(AKnight,BKnight)))),
    Implication(BKnight,(Or(And(AKnave,BKnight),And(AKnight,BKnave)))),
    
    Implication(AKnave,Not((Or(And(AKnave,BKnave),And(AKnight,BKnight))))),
    Implication(BKnave,Not((Or(Not(And(AKnave,BKnight)),Not(And(AKnave,BKnight)))))),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    KnowledgeBase,
    Implication(AKnight,Or(AKnave,AKnight)),
    Implication(AKnave,Not(Or(AKnave,AKnight))),

    Or(Implication(BKnight,Or(Implication(AKnave,Not(AKnave)),Implication(AKnight,AKnave))),Implication(BKnave,Not(Or(Implication(AKnave,Not(AKnave)),Implication(AKnight,AKnave))))),

    Implication(BKnave,Not(CKnave)),
    Implication(BKnight,CKnave),
    
    Implication(CKnave,Not(AKnight)),
    Implication(CKnight,AKnight),
)


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


if __name__ == "__main__":
    main()
