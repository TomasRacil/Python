#Pohyb servo motoru
from time import sleep

def otoc_do_prava(uhel:int):
    """Otoci servo motorkem do prava o zadany pocet stupnu

    Args:
        uhel (int): pocet stupnu
    """
    
    print(f"Otaceni do prava o {uhel}°")
    sleep(1)
    print("Otoceno")

def otoc_do_leva(uhel:int):
    """Otoci servo motorkem do leva o zadany pocet stupnu

    Args:
        uhel (int): pocet stupnu
    """
    
    print(f"Otaceni do leva o {uhel}°")
    sleep(1)
    print("Otoceno")