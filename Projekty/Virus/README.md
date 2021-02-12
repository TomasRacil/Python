virus2.py
- Program, který vytvoři virus, který sám sebe replikuje do všech python souborů PC oběti
- Jeho škodlivost spočívá v zašifrování souborů pomocí symetrického šifrování Fernet
- První část se týká replikace samotného viru
- V druhé části následuje škodlivá část - funkce, jež zajistí generaci symetrického klíče, jeho uložení do souboru a opětovné načtení a použití klíče na zašifrování dat
- Soubor encrypting.py obsahuje metodu šifrování
- Soubor virus2.exe zajistí spuštění na počítačích, kde není python nainstalovaný

Možné vylepšení a další postupy k úpravě kódu:
- Uspůsobit program tak, aby infikoval i soubory jiného typu
- Zkusit obsah programu zašifrovat tak, aby si ho každý nemohl přečíst
- Exe soubor je již známý pro antiviry, takže by to chtělo např. změnit koncovku, popř.něco jiného??
