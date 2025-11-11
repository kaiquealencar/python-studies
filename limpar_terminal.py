import os
import sys



def clear(limpar):
    if limpar == '1':
        if sys.platform.startswith('win'):
            os.system('cls') 
        else:
            os.system('clear')