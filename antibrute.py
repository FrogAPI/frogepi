# fonctions pour protéger contre le brute force (utilisé par le controller et reset appelé par app.py)

import os , signal

class BruteForceProtection(Exception):

    def __init__(self, message = "Brute Force Attack detected check records.log for more information") -> None:
        super().__init__(message)
        print(message)
        os.kill(os.getpid(), signal.SIGINT)


MAX_NBR = 250
nbr = 0


def reset_nad():
    global nbr
    nbr = 0


def addf_verifBrute():
    global nbr 
    nbr += 1
    #print(nbr)
    if nbr >= MAX_NBR:
        raise BruteForceProtection()
