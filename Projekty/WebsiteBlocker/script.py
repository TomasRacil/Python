# Run this script as root
import os
import module
 
module.get_sites()
"""if __name__== ten kontrektni soubor, pokud je prvni a neni importovany, tak bude mit jmeno main"""
"""změní hosts cestu podle OS"""
if __name__ == '__main__':
    if os.name=='posix':
        hosts_path = r"/etc/hosts"
    elif os.name=='nt':
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    module.blocks_sites(module.get_sites(),hosts_path)