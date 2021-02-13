from Exit import run_Exit


def run_Restart():
    
    check = input('If you want to repeat your last action type anything if you want to go back to the main menue type x: ')
    
    exitbool = False
    if check == 'x':
        exitbool = True
    return exitbool