import math
from math import sqrt
import statistics
import time
import os
import webbrowser
print("© 2020 - 2021 CalcOS by Jack Warren. All Rights Reserved.")
time.sleep(2)
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
print("Searching for OS")
print("Loading prompts comencing...")
print('Loading "start"')
def startup():
    clearConsole()
    print("CalcOS by Jack Warren")
    print("")
    return
print('Loading "opselect"')
def opselect():
    print("Select operation")
    print("Simple Interest(S), Comp Interest(C), General Maths(GM),")
    print("")
    print("Pythag(PY), Pi(Pi) & Statistics(St)")
    print("")
    print('Encountered a Bug!? Type "req_update" or "9" to see a list of options')
    print('Enter "0" to quit')
    bestchoice = ["s", "c", "gm", "py", "pi", "st", "req_update", "1", "2", "3", "4", "5", "6", "9", "0"]
    mainchoice = str(input("Enter choice: S(1), C(2), GM(3), PY(4), PI(5), ST(6): ")).lower()
    #FAT input test against all choices, sorry Jake you cant break this one lol.
    if mainchoice in bestchoice:
        clearConsole()
        if mainchoice == 's' or mainchoice == '1':
            simpleint()
        elif mainchoice == 'c' or mainchoice == '2':
            compoundint()
        elif mainchoice == 'gm' or mainchoice == '3':
            genmaths()
        elif mainchoice == 'py' or mainchoice == '4':
            pythagoras()
        elif mainchoice == 'pi' or mainchoice == '5':
            delPi()
        elif mainchoice == 'st' or mainchoice == '6':
            #Del the "nuh uh" print once implemented.
            #Delete these comments and uncomment statistics.
            #no_lol = input("Nuh Uh, not just yet...")
            #opselect()
            statistics()
        elif mainchoice == 'req_update' or mainchoice == "9":
            req_update()
        elif mainchoice == '0':
            clearConsole()
            whyQuit = input("Sad to see you leave. Thanks for using CalcOS!")
            exit()
    else:
        contin = input("Invalid input, press enter to continue: ")
        clearConsole()
        opselect()
print('Loading "simpleInt"')
def simpleint():
    #Simple interest starts here
        print("Work for i or 1 (Paid / earned interest)")
        print("Work for p or 2 (Initial amount of money)")
        print("Work for r or 3 (Interest rate)")
        print("Work for t or 4 (Time)")
        print("")
        print('If you want to go back to the main menu, type "0"')
        print("")
        # Take the input from the user
        # Check if choice is one of the four options with some anti letter code that probably breaks it lol
        try:
            betterchoice = ["i", "p", "r", "t", "1", "2", "3", "4", "0", "main menu"]
            megachoice = str(input("Enter choice, keep in mind this is using I=prt | i or 1 | p or 2 | r or 3 | t or 4 |: ")).lower()
            if megachoice in betterchoice:
                
                if megachoice == '0' or choice == 'main menu':
                    clearConsole()
                    opselect()
                    
                elif choice == 'i' or choice == '1':
                    try:
                        num1 = float(input("Enter value of p: "))
                        if type(num1) == int or type(num1) == float:
                            num2 = float(input("Enter value of r: "))
                            if type(num2) == int or type(num2) == float:
                                num3 = float(input("Enter value of t: "))
                                if type(num3) == int or type(num3) == float:
                                    print("$%0.2f"%(round(num1*(num2/100)*num3,2)))
                                    print("")
                                    contin = input("Your welcome, press enter to continue!")
                                    clearConsole()
                                    opselect()
                                else:
                                    CrashStopperSimp()
                            else:
                                CrashStopperSimp()
                        else:
                            CrashStopperSimp()
                    except:
                           CrashHandler()
                           simpleint()
                elif megachoice == 'p' or choice == '2':
                    try:
                        num1 = float(input("Enter value of i: "))
                        if type(num1) == int or type(num1) == float:
                            num2 = float(input("Enter value of r: "))
                            if type(num2) == int or type(num2) == float:
                                num3 = float(input("Enter value of t: "))
                                if type(num3) == int or type(num3) == float:
                                    print("$%0.2f"%(round(num1/(num2*num3),2)))
                                    print("")
                                    contin = input("Your welcome, press enter to continue!")
                                    clearConsole()
                                    opselect()
                                else:
                                    CrashStopperSimp()
                            else:
                                CrashStopperSimp()
                        else:
                            CrashStopperSimp()
                    except:
                           CrashHandler()
                        
                elif megachoice == 'r' or choice == '3':
                    try:
                        num1 = float(input("Enter value of i: "))
                        if type(num1) == int or type(num1) == float:
                            num2 = float(input("Enter value of p: "))
                            if type(num2) == int or type(num2) == float:
                                num3 = float(input("Enter value of t: "))
                                if type(num3) == int or type(num3) == float:
                                    print("%f%%"%(round((num1/(num2*num3))*100,10)))
                                    print("")
                                    contin = input("Your welcome, press enter to continue!")
                                    clearConsole()
                                    opselect()
                                else:
                                    CrashStopperSimp()
                            else:
                                CrashStopperSimp()
                        else:
                            CrashStopperSimp()
                    except:
                           CrashHandler()
                                
                elif megachoice == 't' or choice == '4':
                    try:
                        num1 = float(input("Enter value of i: "))
                        if type(num1) == int or type(num1) == float:
                            num2 = float(input("Enter value of p: "))
                            if type(num2) == int or type(num2) == float:
                                num3 = float(input("Enter value of r: "))
                                if type(num3) == int or type(num3) == float:
                                    print("%0.2f ∴Total time"%(round((num1/(num2*num3))*100,2)))
                                    print("")
                                    contin = input("Your welcome, press enter to continue!")
                                    clearConsole()
                                    opselect()
                                else:
                                    CrashStopperSimp()
                            else:
                                CrashStopperSimp()
                        else:
                            CrashStopperSimp()
                    except:
                           CrashHandler()       
                else:
                    CrashStopperSImp()
                    
            else:
                CrashStopperSimp()
                
        except:
            CrashHandler()
            return

print('Loading "compoundInt"')
def compoundint():
    #Here be compund interests!
    try:
        global n
        compoundTime = ["yearly", "1", "daily", "2", "weekly", "3", "bi-weekly", "4", "semi-monthly", "5", "monthly", "6", "bi-monthly", "7", "quarterly", "8", "semi-annually", "9", "daily2", "10", "0", "main menu"]
        print('If you want to go back to the main menu, type "0" or "main menu\n"')
        print("List of supported compound times")
        print("yearly(1)\ndaily(2)\nweekly(3)\nbi-weekly(3)\nsemi-monthly(5)\nmonthly(6)\nbi-monthly(7)\nquarterly(8)\nsemi-annually(9)\ndaily2(10) this one is 360 days.")
        compTimeChoice = input("Enter your choice here: ").lower()
        if compTimeChoice in compoundTime:
            if compTimeChoice == 'main menu' or compTimeChoice =='0':
                clearConsole()
                opselect()
            elif compTimeChoice == 'yearly' or compTimeChoice =='1':
                n = 1
                compoundint2()
            elif compTimeChoice == 'daily' or compTimeChoice =='2':
                n = 365
                compoundint2()
            elif compTimeChoice == 'weekly' or compTimeChoice =='3':
                n = 52
                compoundint2()
            elif compTimeChoice == 'bi-weekly' or compTimeChoice =='4':
                n = 26
                compoundint2()
            elif compTimeChoice == 'semi-monthly' or compTimeChoice =='5':
                n = 24
                compoundint2()
            elif compTimeChoice == 'monthly' or compTimeChoice =='6':
                n = 12
                compoundint2()
            elif compTimeChoice == 'bi-monthly' or compTimeChoice =='7':
                n = 6
                compoundint2()
            elif compTimeChoice == 'quarterly' or compTimeChoice =='8':
                n = 4
                compoundint2()
            elif compTimeChoice == 'daily2' or compTimeChoice =='10':
                n = 360
                compoundint2()
            else:
                print("Something went wrong, check input and try again.")
                compoundint()
        else:
            print("Something went wrong, check input and try again.")
            compoundint()
    except:
        CrashHandler()
    return
print('Loading "compoundint2"')
def compoundint2():
    try:
        awesomeChoice = ("i", "1", "p", "2", "r", "3", "0", "main menu")
        print('If you want to go back to the main menu, type "0" or "main menu"')
        Compchoice = input("What would you like to work for? |a or 1| |p or 2| |r or 3| :").lower() 
        if Compchoice in awesomeChoice:
            if Compchoice == "i" or Compchoice == "1":
                P = float(input("Enter principle amount(p): "))
                r = float(input("Enter interest rate(r): "))
                y = float(input("Enter the time period in years(t): "))
                FV = P * (((1 + ((r/100.0)/1)) ** (n*y)))
                print("")
                print("The final amount after", y, "years is", FV)
                print("")
                contin = input("Your welcome, press enter to continue!")
                clearConsole()
                compoundint()
            elif Compchoice == "p" or Compchoice == "2":
                A = float(input("Enter final amount of money(a): "))
                r = float(input("Enter interest rate(r): "))
                y = float(input("Enter the time period in years(t): "))
                FV = A / (((1 + ((r/100.0)/1)) ** (n*y)))
                print("")
                print("The final amount after", y, "years is", FV)
                print("")
                contin = input("Your welcome, press enter to continue!")
                clearConsole()
                compoundint()
            elif Compchoice == "r" or Compchoice == "3":
                A = float(input("Enter final amount of money(a): "))
                P = float(input("Enter Principle Amount: "))
                y = float(input("Enter the time period in years(t): "))
                FV = n*((A/P)**(1/(n*y))-1)
                FV = FV * 100
                print("")
                print("The interest rate is:", FV,"%")
                print("")
                contin = input("Your welcome, press enter to continue!")
                clearConsole()
                compoundint()
                
            elif Compchoice == "0" or Compchoice == "main menu":
                clearConsole()
                opselect()
                
        else:
            input("Check your input and try again.")
            clearConsole()
            compoundint()                    
    except:
        CrashHandler()
    return

print('Loading "genMaths"')
def genmaths():
    #General Mathmatics starts here
    try:
        print('Type "m" to return to the main menu')
        print("(Multiply = *   Divide = /   Subtract = -   Add = +   Power of = **")
        print("")
        calc = input("Type calculation:\n").lower()
        if calc != 'm':
            print("Thinking...")
            print("")
            print("Answer: " + str(eval(calc)))
            print("")
            contin = input("Your welcome, press enter to continue!")
            clearConsole()
            genmaths()
        else:
            clearConsole()
            opselect()
    except:
        CrashHandler()
        genmaths()
        return

print('Loading "pythagoras"')
def pythagoras():
    #Pythagoras starts here
    print("Pythagorean theorem calculator! Calculate your right angled triangles sides!")
    print("Assume the sides are a, b, c and c is the hypotenuse")
    betterchoice = ["a", "b", "c"]
    choice = input("Which side do you wish to calculate? Enter choice(A/B/C): ").lower()
    try:
        if choice in betterchoice:
            if choice == 'c':
                try:
                    side_a = float(input("Input the length of side a: "))
                    if type(side_a) == int or type(side_a) == float:
                        side_b = float(input("Input the length of side b: "))
                        if type(side_b) == int or type(side_b) == float:
                            if side_b <= 0 or side_a <= 0:
                                print("Cant be 0 or less")
                                CrashStopperPy()
                            else:
                                try:
                                    side_c = float(sqrt((side_a * side_a) + (side_b * side_b)))
                                    print("∴The length of side c is:", side_c)
                                    print("")
                                    contin = input("Your welcome, press enter to continue!")
                                    clearConsole()
                                    opselect()
                                except:
                                    CrashHandler()
                        else:
                            CrashStopperPy()
                    else:
                        CrashStopperPy()
                except:
                    CrashHandler()
                
            elif choice == 'a':
                try:
                    side_b = float(input("Input the length of side b: "))
                    if type(side_b) == int or type(side_b) == float:
                        side_c = float(input("Input the length of side c: "))
                        if type(side_c) == int or type(side_c) == float:
                            if side_b <= 0 or side_c <= 0:
                                print("Cant be 0 or less")
                                CrashStopperPy()
                            elif side_b >= side_c:
                                print("Side C has to be the longest")
                                CrashStopperPy()
                            else:
                                try:
                                    side_a = float(sqrt((side_c * side_c) - (side_b * side_b)))
                                    print("∴The length of side a is:", side_a)
                                    print("")
                                    contin = input("Your welcome, press enter to continue!")
                                    clearConsole()
                                    opselect()
                                except:
                                    CrashHandler()
                        else:
                            CrashStopperPy()
                    else:
                        CrashStopperPy()
                except:
                    CrashHandler()

            elif choice == 'b':
                try:
                    side_a = float(input("Input the length of side a: "))
                    if type(side_a) == int or type(side_a) == float:
                        side_c = float(input("Input the length of side c: "))
                        if type(side_c) == int or type(side_c) == float:
                            if side_a <=0 or side_c <= 0:
                                print("Cant be 0 or less")
                                CrashStopperPy()
                            elif side_a >= side_c:
                                print("Side C has to be the longest")
                                CrashStopperPy()
                            else:
                                try:
                                    side_b = float(sqrt((side_c * side_c) - (side_a * side_a)))
                                    print("∴The length of side b is:", side_b)
                                    print("")
                                    contin = input("Your welcome, press enter to continue!")
                                    clearConsole()
                                    opselect()
                                except:
                                    CrashHandler()
                        else:
                            CrashStopperPy()
                    else:
                        CrashStopperPy()
                except:
                    CrashHandler()
            elif choice == '0':
                clearConsole()
                opselect()
        else:
            CrashStopperPy()
    except:
        CrashHandler()
        return

print('Loading "deliciousPi"')


def delPi():
    #Delicious Pie starts here
    try:
        print("Pie is 3.14159265358979323846264338327950288419716939937510582097494459230781640")
        print("             (            ")
        print("              )           ")
        print("         __..---..__      ")
        print("     ,-='  /  |  \  `=-.  ")
        print("    :--..___________..--; ")
        print("     \.,_____________,./  ")
        print("")
        contin = input("MM, MMMMM, Delicious! Press enter to continue!")
        clearConsole()
        opselect()
    except:
        CrashHandler()
        return

print('Loading "Statistics"')


def statistics():
    #Statistics starts here
    #try:
    BetterChoice = ["mean", "median", "1", "2", "0", "main menu"]
    StatChoice = input("Enter choice: Mean(1), Median(2), Main menu(0): ").lower()
    if StatChoice in BetterChoice:
        clearConsole()
        if StatChoice == 'mean' or StatChoice == '1':
            clearConsole()
            mean()
            
        elif StatChoice == 'median' or StatChoice == '2':
            clearConsole()
            compoundint()
            
        elif StatChoice == 'else' or StatChoice == '3':
            clearConsole()
            genmaths()
            
        elif StatChoice == 'nelse' or StatChoice == '4':
            clearConsole()
            pythagoras()
            
        elif StatChoice == 'yelse' or StatChoice == '5':
            clearConsole()
            delPi()
            
        elif StatChoice == '0' or StatChoice == 'main menu':
            clearConsole()
            opselect()
        else:
            CrashHandler()
    else:
        contin = input("Invalid input, press enter to continue: ")
        clearConsole()
        statistics()
    #except:
        #CrashHandler()
        return

print('Loading "mean"')
def mean():
    #Mean starts here
    #try:
    YeahNah = ["y", "n", "1", "0", "9", "main menu"]
    print('Want to go to the main menu? type "9" instead')
    YesOrNo = str(input("Would you like to add the numbers here? y(1) or n(0) or Main menu(9): ")).lower()
    if YesOrNo in YeahNah:
        if YesOrNo == 'y' or YesOrNo == '1': 
            total = 0
            print("Enter the number with a space inbetween each one. (supports negatives)")
            n = input("Enter here: ").split()
            for x in n:
                    total = total + float(x)
            print("The Mean is: ", total / len(n))
            print("")
            contin = input("Your welcome, press enter to continue!")
            statistics()

        elif YesOrNo == 'n' or YesOrNo == '0':     
            total = float(input("Input the Total of the numbers: "))
            numberOfValues = float(input("input how many numbers there are: "))
            print("The mean is: %0.5f" % (round(total/numberOfValues, 5)))
            print("")
            contin = input("Your welcome, press enter to continue!")
            statistics()
            
        elif YesOrNo == 'main menu' or YesOrNo == '9':
            clearConsole()
            opselect()
            
        else:
            CrashStopperStat()
    else:
        CrashStopperStat()
    #except:
        #CrashHandler()
        return

print('Loading "median"')


def median():
    try:
        if choice == 'median':
            medical = float(input("Input your numbers with a comma and space after." +
            "For example, 1, 2, 3, 4, 5: "))
            print("The median is: %0.2f" % (round(statistics.median([medical], 2))))
    except:
        CrashHandler()
        return
print('Loading "CrashStopperPy"')


def CrashStopperPy():
    contin = input("Invalid input, press enter to continue: ")
    clearConsole()
    pythagoras()
    return
print('Loading "CrashStopperSimp"')


def CrashStopperSimp():
    contin = input("Invalid input, press enter to continue: ")
    clearConsole()
    simpleint()
    return
print('Loading "CrashStopperStat"')


def CrashStopperStat():
    contin = input("Invalid input, press enter to continue: ")
    clearConsole()
    statistics()
    return
print('Loading "CrashHandler"')


def CrashHandler():
    contin = input("That didn't quite work, check input and try again. " +
                   "If you believe it is a bug, please report it, it only takes a minute!")
    clearConsole()
    opselect()
    return

print('Loading "req_update')
def req_update():
    print("You can:")
    print("1. Download the latest version")
    print("2. Use the chat on the bottom right of the webpage to address the issue")
    print("Remember to tell me how you got there so I can replicate it. Ty :D")
    print("3. You didn't mean to get here. Enter "'"0"'" to go back.")
    contin = input("Press enter to Continue to webpage: ")
    if contin == '0':
        clearConsole()
        opselect()    
    else:
        webbrowser.open('https://2001429.wixsite.com/website/shop')
        clearConsole()
        opselect() 
    return
print("Finished!")
print("Booting...")
startup()
opselect()
