První spuštění git 
- zadejte následující příkazy do příkazového řádku  
- zadejte vlastní uživatelské jméno a email použitý při registraci na github 

git config --global user.name "Uživatelské jméno" \
git config --global user.email email@domena.cz 


Pro naklonování repozitáře 
- zadejte následující příkaz do příkazového řádku  

 git clone https://github.com/TomasRacil/Python.git 


Pokud nastane chyba Fatal: repository not found 
- zkuste zadat následující příkaz s administrátorskými právy  

git credential-manager remove -force 


Pro nahrání změn do sdíleného repozitáře 
- zadejte následující příkazy do příkazového řádku otevřeného ve vašem lokálním repozitáři 
- pro přidání nově vytvořených souborů 

git add .  
- pro zavedení změn do lokálního repozitáře  
- do zprávy uveďte jakou změnu jste provedli 

git commit -m "Zpráva" 
- pro zavedení změn do společného repozitáře 

git push
- poslání dat na mateřský odresář z mého lokálního úložiště

git pull
- aktualizace (stažení nových souborů z mateřského adresáře)