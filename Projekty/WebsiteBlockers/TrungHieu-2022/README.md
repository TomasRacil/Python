# Website blocker
Cíl:
  -Vytvořím aplikaci na blokování webových stránek.
  -Aplikace bude mít možnost Blokovat a Odblokovat.
  -Aplikace je kompatibilní s operačními systémy Windows i Linux.
Popis:
  - Nejprve používám knihovnu sys k testování operačního systému.Odtud definuji vstup do file hosts.
  - pokud OS je Windows,povolím oprávnění upravovat soubor hosts v Properties/Security. Pokud OS je Linux,Uděluji oprávnění k úpravě file hosts pomocí příkazu na Terminálu: sudo chmod 777 /etc/hosts.
  - Použivám rozhraní Tkinter
  - Pomocí rozhraní Tkinter vám umožním zadat jakoukoli webovou stránku, kterou chcete zablokovat.
  - Když zadáte názvy webových stránek, které chcete blokovat, program přiřadí IP adresu počítače (127.0.0.1) před název webové stránky a poté ji zapíše do file Hosts. Když vstoupíme na webovou stránku, počítač se připojí sám k sobě, takže na webovou stránku nebudete mít přístup.
  - Když zadáte názvu webu, který chcete odblokovat, program najde název v file Hosts a smaže jej.


## TODO
- kód není okomentován
- kód není rozdělen do modulů
- třeba dodělat kompatibilitu s os linux
- chybí popis programu a možnosti rozšíření v readme.md
