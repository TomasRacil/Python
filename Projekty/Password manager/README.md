# Password manager

Program na uchování a přihlašovacích údaju pro ůčty uživatele.
  
- Program vytvoří databázi (.db) pomoci knihovny sqlite3, která obsahuje database engine a je schopny samostatně a rychle zpracovávat data
- Po prvni spuštění programu se objeví okno na zadaní "Master hesla" a v databázi se přepíše kolonka (hesh)
- Heshovaní hesel pomocí knihovny hashlib a comandu .hexdigest zašivruje heslo na dvojnásobnou délku s obsahem tvořeným z hexadecimální řady
- Hlavní okno programu obsahuje příslušné kolonky, které jsou hashovany do databaze s možností kopírování obsahu do schránky (ctrl+c,ctrl+v)

Obsažený jednoduchý podpogram na vytvoření hesla ze písmen, čísel a speciálních znaků

- počet znaků zadá uživatel

Guide na vytvoření generátoru hesel: <https://tkinter.com/build-a-strong-password-generator-app-python-tkinter-gui-tutorial-170/>
Implementace databáze a hashování hesel: <https://www.youtube.com/watch?v=UrH2WCoYEVo>

TODO:
  
- Práce přímo se stránkami na automatické vkládání hesel
- Vylepšení generátoru hesel pomocí bezpečnostních otázek a přidáním podmínek na hesla
- Vyřešit nefunkčnost generátoru hesel na Linuxu
