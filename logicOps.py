# This is a complex logic statement

C = 6
D = 2

if (C > 5 and D > 5) or (C > 1 and D > 1):
    print("It worked!")

if (not (C > 5 and D > 5)) or (C > 1 and D > 1):
    print("It still worked!")

if not (C > 1 and D > 1) or (C > 5 and D > 5):
    print("WTF?!")
else: print("I got nuthin'")

if not ((C > 1 and D > 1) or (C > 5 and D > 5)):
    print("WTF?!")