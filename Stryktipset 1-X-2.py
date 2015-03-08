__author__ = 'AntonF'
import random
runTime = 0
print("Answer every row with 1, x or 2.")
print("Example: 1 if you think that the first team will win.")
print("Example: 2 if you think that the second team will win.\nExample: x if you think that it will be a draw.")


def runnow():
    print("")
    rstring = ""
    list1 = ["", "", "", "", ""]
    i = 0
    while i < 5:
        i += 1

        if i == 1:
            rstring = "Halmstad - Örebro-------"
        elif i == 2:
            rstring = "Gefle - Elfsborg--------"
        elif i == 3:
            rstring = "Hammarby - Värnamo------"
        elif i == 4:
            rstring = "Valberg - Kristianstad--"
        elif i == 5:
            rstring = "Kalmar FF - Elfsborg----"
        cinput = input("* {0} [1/X/2]: ".format(rstring))

        rannumb = random.randrange(1, 4, 1)
        if rannumb == 1:
            option1 = "1"
            if i == 1:
                if option1 == cinput:
                    list1[0] = "-------------\n|•1•| x | 2 | (1)\n-------------"
                else:
                    list1[0] = "-------------\n|-1-| x | 2 | (1)\n-------------"
            elif i == 2:
                if option1 == cinput:
                    list1[1] = "|•1•| x | 2 | (1)\n-------------"
                else:
                    list1[1] = "|-1-| x | 2 | (1)\n-------------"
            elif i == 3:
                if option1 == cinput:
                    list1[2] = "|•1•| x | 2 | (1)\n-------------"
                else:
                    list1[2] = "|-1-| x | 2 | (1)\n-------------"
            elif i == 4:
                if option1 == cinput:
                    list1[3] = "|•1•| x | 2 | (1)\n-------------"
                else:
                    list1[3] = "|-1-| x | 2 | (1)\n-------------"
            elif i == 5:
                if option1 == cinput:
                    list1[4] = "|•1•| x | 2 | (1)\n-------------"
                else:
                    list1[4] = "|-1-| x | 2 | (1)\n-------------"

        elif rannumb == 2:
            optionx = "x"
            if i == 1:
                if optionx == cinput or "X" == cinput:
                    list1[0] = "-------------\n| 1 |•x•| 2 | (x)\n-------------"
                else:
                    list1[0] = "-------------\n| 1 |-x-| 2 | (x)\n-------------"
            elif i == 2:
                if optionx == cinput or "X" == cinput:
                    list1[1] = "| 1 |•x•| 2 | (x)\n-------------"
                else:
                    list1[1] = "| 1 |-x-| 2 | (x)\n-------------"
            elif i == 3:
                if optionx == cinput or "X" == cinput:
                    list1[2] = "| 1 |•x•| 2 | (x)\n-------------"
                else:
                    list1[2] = "| 1 |-x-| 2 | (x)\n-------------"
            elif i == 4:
                if optionx == cinput or "X" == cinput:
                    list1[3] = "| 1 |•x•| 2 | (x)\n-------------"
                else:
                    list1[3] = "| 1 |-x-| 2 | (x)\n-------------"
            elif i == 5:
                if optionx == cinput or "X" == cinput:
                    list1[4] = "| 1 |•x•| 2 | (x)\n-------------"
                else:
                    list1[4] = "| 1 |-x-| 2 | (x)\n-------------"

        elif rannumb == 3:
            option2 = "2"
            if i == 1:
                if option2 == cinput:
                    list1[0] = "-------------\n| 1 | x |•2•| (2)\n-------------"
                else:
                    list1[0] = "-------------\n| 1 | x |-2-| (2)\n-------------"
            elif i == 2:
                if option2 == cinput:
                    list1[1] = "| 1 | x |•2•| (2)\n-------------"
                else:
                    list1[1] = "| 1 | x |-2-| (2)\n-------------"
            elif i == 3:
                if option2 == cinput:
                    list1[2] = "| 1 | x |•2•| (2)\n-------------"
                else:
                    list1[2] = "| 1 | x |-2-| (2)\n-------------"
            elif i == 4:
                if option2 == cinput:
                    list1[3] = "| 1 | x |•2•| (2)\n-------------"
                else:
                    list1[3] = "| 1 | x |-2-| (2)\n-------------"
            elif i == 5:
                if option2 == cinput:
                    list1[4] = "| 1 | x |•2•| (2)\n-------------"
                else:
                    list1[4] = "| 1 | x |-2-| (2)\n-------------"

    print("\nMatcherna spelas...")
    print("{0}\n{1}\n{2}\n{3}\n{4}".format(list1[0], list1[1], list1[2], list1[3], list1[4]))
    print("\"-\" för fel.\n\"•\" för rätt.")
    global runTime
    runTime = 1
    start()


def start():
    if runTime == 0:
        runnow()
    elif runTime != 0:
        runner = input("\nVill du fylla i stryktipset igen? [Y/N]: ")
        if runner == "y" or runner == "Y":
            runnow()
        else:
            exit()
start()