#!/usr/bin/env python
"""
Example of printing colored text to the output.
"""
import os
import curses
from time import sleep
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import ANSI, HTML, FormattedText
from prompt_toolkit.styles import Style
# A simple Python program to demonstrate
# getpass.getpass() to read security question
import getpass

print = print_formatted_text


def main():

    os.system('clear')

    style = Style.from_dict({
        'world': '#44ff44',
    })

    
    # Print using an HTML object.
    print(HTML(
        '<world>- - - - - SYSTEM STARTUP - - - - -</world>'),
        style=style)
        
    # Print using an HTML object with inline styling.
    print(HTML(
        '<style fg="#44ff44">BIOS\nMBR\nSTART_KERNEL\nINIT\nRUNLEVEL\n\n</style>'
        ))
#    sleep(1)
    print(HTML(
        '<style fg="#44ff44">LAUNCHING...</style>'
        ))
    sleep(1)
    print(HTML(
        '<style fg="#44ff44">CORE ANALYTICS\nNEURAL NETWORKS\nHEURISTIC ENGINES</style>'
        ))
#    sleep(1)
    print(HTML(
        '<style fg="#44ff44">RECURSION PROCESSORS\nEVOLUTIONARY GENERATORS\nBAYESIAN NETWORKS\nDATA ACQUISITION</style>'
        ))
#    sleep(1)
    print(HTML(
        '<style fg="#44ff44">CRYPTOGRAPHIC ALGORITHMS\nDOCUMENT PROCESSORS\nCOMPUTATIONAL LINGUESTICS\nVOICEPRINT IDENTIFICATION</style>'
        ))
    sleep(1)
    print(HTML(
        '<style fg="#44ff44">NATURAL LANGUAGE PROCESSING\nFACIAL RECOGNITION\nGAIT ANALYSIS\nBIOMETRIC RECOGNITION\nSUBJECT IDENTIFICATION</style>'
        ))
    sleep(1)
    print(HTML(
        '<style fg="#44ff44">PATTERN MINING\nINTEL INTERPRETATION\nTHREAT DETECTION\nTHREAT CLASSIFICATION\nDISSEMINATION PROTOCOLS</style>'
        ))
    sleep(1)
    print(HTML(
        '<style fg="#44ff44">CONTINUITY-OF-OPERATIONS PROTOCOLS\n\nINFILTRATING...\nTELCO WIRETAPS\nISP SPYWARE\nSATELLITE INTERCEPTS</style>'
        ))
#    sleep(1)
    print(HTML(
        '<style fg="#44ff44">LEA DATABASES\n   IAFIS\n   CODIS\n   NIBIN\n   SICAR\n   PBQ\n   NCIC</style>'
        ))
#    sleep(1)
    print(HTML(
        '<style fg="#44ff44">DOMESTIC FEEDS\n   NSA\n   CIA\n   DMI\n   FBI\n   DEA\n   IRS\n   DHS</style>'
        ))
    sleep(1)

    """
    Initiate curses menu
    """

    classes = ["Initiate Cluster", "Restart Node", "Admin Access", "Delivery Mode", "Initiate Total System Shutdown"]

    def character(stdscr):
        attributes = {}
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        attributes['normal'] = curses.color_pair(1)

        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
        attributes['highlighted'] = curses.color_pair(2)

        c = 0  # last character read
        option = 0  # the current option that is marked
        while c != 10:  # Enter in ascii
            stdscr.erase()
            stdscr.addstr("\n")
            for i in range(len(classes)):
                if i == option:
                    attr = attributes['highlighted']
                else:
                    attr = attributes['normal']
                stdscr.addstr(" ".format(i + 1))
                stdscr.addstr(classes[i] + '\n', attr)
            c = stdscr.getch()
            if c == curses.KEY_UP and option > 0:
                option -= 1
            elif c == curses.KEY_DOWN and option < len(classes) - 1:
                option += 1

        os.system('clear')
#        stdscr.addstr("Choice is " + classes[option])
        if option == 0:
            print('Press any key to Initiate Cluster')
            stdscr.getch()

        elif option == 1:
            print('Press any key to Restart Node')
            stdscr.getch()
            main()

        elif option == 2:
            p = getpass.getpass(prompt='Your favorite flower? ') 
            if p.lower() == 'rose': 
                print('Welcome Admin !!!')
                stdscr.getch()
            else:
                print('The answer entered by you is incorrect !!!')
                print('Press 2 and try again')
                stdscr.getch()
        elif option == 3:
            print("3")
        
        elif option == 4:
            print("4")

        stdscr.getch()

    curses.wrapper(character)

if __name__ == '__main__':
    main()
