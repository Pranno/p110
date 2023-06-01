import random

ans = input("Do you wnat to Rool a Dice?")

def count(ans):
    while ans == "yes":
        no = random.randint(1,6)

        if no == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")

        elif no == 2:
            print("[-----]")
            print("[     ]")
            print("[  00  ]")
            print("[     ]")
            print("[-----]")

        elif no == 3:
            print("[-----]")
            print("[     ]")
            print("[ 000  ]")
            print("[     ]")
            print("[-----]")

        elif no == 4:
            print("[-----]")
            print("[     ]")
            print("[  0000  ]")
            print("[     ]")
            print("[-----]")

        elif no == 5:
            print("[-----]")
            print("[     ]")
            print("[  00000  ]")
            print("[     ]")
            print("[-----]")

        elif no == 6:
            print("[-----]")
            print("[     ]")
            print("[  000000  ]")
            print("[     ]")
            print("[-----]")




        



                   