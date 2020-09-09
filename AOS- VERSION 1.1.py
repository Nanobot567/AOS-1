# AOS version 1.1
# Created on Friday, March 27, 2020
# Finished on April 3, 2020

import time

import sys

pword = ""

cmd = ""

directory = ""

ays = ""

print("\033[1;37;40m \n")

def shutdown():
    print("shutting down AOS...")
    time.sleep(2)

def notes():
    print("Welcome to notes! type 'nhelp' for help with notes.")
    cmd = ""
    while cmd != "esc":
        cmd = input("\nAOST/notes: ")
        if cmd == "nhelp":
            print("availible commands:")
            print("new ", "close ", "edit ", "delete \n")
            while cmd != "esc":
                cmd = input("\nAOST/notes/help: ")
                if cmd == "new":
                    print("the new command allows you to create a new text file.")
                if cmd == "close":
                    print("the close command closes the current document.")
                if cmd == "edit":
                    print("the edit command edits a document.")
                if cmd == "delete":
                    print("the delete command deletes a document.")
                if cmd == "new":                        
                    cmd = input("Please type the name of the new file: ")
                    filename = cmd 
                    cmd = input("Please select the filetype: ")
                    filetype = cmd
                    f = open(filename + "." + filetype, "w")
                    cmd = input("Now type what is in the file: ")
                    f.write(repr(cmd))
                    print("done.")
                    f.close



# just the help section. needed to seperate this from everything bc of OrGaNiZaTiOn
def help():
    cmd = "null"
    print("\nshowing all availible commands. ")
    print("help","fl","dir ", "esc ", "quit ", "gamePortal ", "notes ", "clock \n")
    print("showing all availible filetypes. ")
    print("x", " txt ", "rndr ", "ps ", "kbpp ", "arg \n")
    print("type 'help' for the list again.")
    while cmd != "esc":
        cmd = input("\nAOST/help: ")
        if cmd == "dir":
            print("dir is used in fl to show everything in the directory.")
            print("for example: \n \n")
            print("AOST: fl")
            print("AOST/fl: dir")
            print("junk.rndr morejunk.txt main.x")
            print("\n dir can also be used with the extension -h to view hidden files as well as regular files.")
        if cmd == "fl":
            print("fl is the standard file launcher for AOS, and can open any supported filetype.")
            print("for example: \n \n")
            print("AOST/: fl")
            print("AOST/fl: readme.txt")
            print("\n thanks for reading me :D")
        if cmd == "esc":
            print("esc allows you to quit any program that is running. can be used within anything, even this. so, you should probably open help again if you would like to keep searching.")
        if cmd == "shutdown":
            print("can only be used in the directory AOST. quits AOS.")
        if cmd == "help":
            print("\nshowing all availible commands. ")
            print("help","fl","dir ", "esc ", "quit ", "gamePortal ", "notes \n")
            print("showing all availible filetypes. ")
            print("x", " txt ", "rndr ", "ps ", "kbpp ", "arg \n")
        if cmd == "gamePortal":
            print("gamePortal is a built-in game engine that can run any installed game.")
        if cmd == "clock":
            print("clock is a program that lets you see the time and date in your area.")
        if cmd == "x":
            print(".x is a cross-platform filetype that can be read in MacOS as well as in AOS.")
        if cmd == "txt":
            print(".txt is a standard, formatted text filetype.")
        if cmd == "rndr":
            print(".rndr is a renderable file, meaning it can be used to run simple programs in potatoScript, KBall++, and more.")
        if cmd == "ps":
            print(".ps is the potatoScript filetype, and can be read by a potatoScript reader like smilePotato.")
        if cmd == "kbpp":
            print(".kbpp is the Kball++ filetype, and can be read by a KBPP debugger or runner such as SamolCamel Reader.")
        if cmd == "arg":
            print(".arg is the AOS renderable game filetype. it is used in AOS gamePortal as it is made for a game engine.")


def gamePortal():
    cmd = ""
    print("GAMEPORTAL \n \n")
    time.sleep(1)
    print("the game engine of the future(TM) \n \n")
    time.sleep(1)
    print("Welcome to gamePortal! This is a pre-installed game engine that can play any installed game. To install a game, type install and the game you want to install. Please note that to cons- \n")
    print("erve space on your AOS system, the games will uninstall after they have been used. (type gpHelp for help and games that you can install.)")
    while cmd != "esc":
        cmd = input("AOST/gp: ")
        if cmd == "gpHelp ":
            print("list of commands in gp:")
            print("install", " esc", "\n")
            print("list of games you can download:")
            print("sample.arg \n")
            while cmd != "esc":
                cmd = input("AOST/gp/help: ")
                if cmd == "install":
                    print("the install command is used for installing a game. syntax: install sample.arg")
                    if cmd == "esc":
                        print("esc is used for quitting either gamePortal or help, which you just did for help.")
        if cmd == "install sample":
            print("installing game 'sample'")
            time.sleep(1)             
            print("done! running 'sample.arg'...")
            time.sleep(0.8)
            cmd = input("great job, you ran me! type 'esc' to exit... ")
            while cmd != "esc":
                cmd = input("great job, you ran me! type 'esc' to exit... ")


# startup is kind of the full engine for AOS. 
def startup():
    cmd = "null"
    print("starting up AOS  \n")
    time.sleep(0.6)
    print("if you need help with AOS, please type help into the command prompt. \n")
    time.sleep(1)
    while cmd != "shutdown":
        cmd = input("\nAOST/: ")
        directory = "main"
        if cmd == "help":
            help()
        if cmd == "fl":
            while cmd != "esc":
                cmd = input("AOST/fl: ")
                if cmd == "dir":
                    if directory == "main":
                        print("pypoem.txt", " fl.rndr", "virus.rndr")
                if cmd == "dir -h":
                    if directory == "main":
                        print("pypoem.txt", " fl.rndr", " virus.rndr", " .superhot")
                if cmd == "pypoem.txt":
                    import this
                    print("\n" *3)
                if cmd == "virus.rndr":
                    print("Ha! You just activated a virus! Have fun restarting!")
                    time.sleep(1)
                    print("LOL" *1000)
                    print("\n" *50)
                    print("AOS has sent the following message: \n")
                    print("Your computer has been shut down because of the program [VIRUS.RNDR]. \n Please restart your computer, and enter recovery mode by pressing [R] on startup to retrieve your files. \n")
                    print("If this keeps happening, contact your PC provider.")
                    time.sleep(8)
                    print("\n"*3)
                    shutdown()
                if cmd == ".superhot":
                    print("\033[1;31;40m\n")
                    print("GO INTO FULLSCREEN.")
                    time.sleep(1)
                    while "1" == "1":
                        print("""    
                                                             _____ _____ _____ _____ _____   
                                                            |   __|  |  |  _  |   __| __  |  
                                                            |__   |  |  |   __|   __|    -|  
                                                            |_____|_____|__|  |_____|__|__|  

                                 """)
                        time.sleep(1)
                        print("""
                                                                   _____ _____ _____ 
                                                                  |  |  |     |_   _|
                                                                  |     |  |  | | |  
                                                                  |__|__|_____| |_|
                    
                        """)
                        time.sleep(1)

            
        if cmd == "gamePortal":
            print("opening gameportal... \n \n")
            gamePortal()
        if cmd == "notes":
            print("Notes is soon to be implemented into AOS 1.2. We're sorry for the inconvienience this could have caused.")
        if cmd == "clock":
            print("Welcome to clock, the best way to view time(TM).")
            time.sleep(1)
            print("If you need help with clock, please type chelp.")
            while cmd != "esc":
                cmd = input("AOST/clock: ")
                if cmd == "chelp":
                    print("showing all commands...")
                    print("\n time ", "date ", "\n")
                    while cmd != "esc":
                        cmd = input("AOST/clock/help: ")
                        if cmd == "time":
                            print("the 'time' command lets you view the current time in your area. \n")
                        if cmd == "date":
                            print("the 'date' command lets you see the current month, day, and year, in that order.")
                if cmd == "time":
                    print(time.strftime('\n%X %Z\n'))
                if cmd == "date":
                    print(time.strftime('\n%x %Z \n'))






    ays = input("are you sure you want to shut down AOS? (all unsaved documents will be lost) [Y/N]")    
    if ays == "N":
        print("\n"*4)
        startup()
    elif ays == "Y":
        shutdown()
    else:
        print("wat. plz rsrt ur AOs nouw")
                

print("Starting up... \n")
time.sleep(1)
print("Checking for AOSchip...  \n")
time.sleep(0.2)
print("AOS Chip detected  \n")
time.sleep(0.2)
print("filecmnder.rndr presence check... \n")
# rndr is short for render. i wanted to make something else other than .exe or .app, so i did that.
time.sleep(1.2)
print("ready for startup. \n")
if pword == "":
    startup()

# adding this fnction later.

else:
    print("please enter pword on newline:")
    inputpw = input(">>> ")