Informace ke hře Kámen,Nůžky,Papír,Tapír, Spock.
Celá hra se spouští soubourem Klient.
Nejdříve před spuštěním je nutno změnit nastavení IP adresy(server) 
počítače který poskytuje server pro tuhle hru v souboru server a síť 
(je možné že na vašem počítači bude obsazen také port 5555 tudíž je nutno změnit port určený k této hře za jiný libovolný volný port)

Soubor Síť:
soubor síť slouží k nastavení připojení k síti kde pomocí connect se připojíme k adrese(serveru a portu) a obdržíme číslo hráče(0-hráč 1, 1- hráč2)

Server:
V souboru server přiřazujeme k serveru port, vytváříme slovník s hrami a ke každé hře přiřadíme unikátní ID(kterou můžeme i mzat v případě že ji hráč opustí)
a vytváříme novou hru pokud není vytvořena.

Hra:
v tomto souboru řešíme hru jako obecnou podmínky vítězství tah hráče(jako tah hráče bereme pouze první písmeno z textu tlačítka)

Klient:
Zde řešíme formu(vzhled,velikost,text,barvu,umistění) tlačítek ve hře a definujeme kliknutí na ně
potom definujeme uspořádání okna hry(vizualizaci- rozdělení na tah muj a protihráče)
upgradujeme info o tahu mém a protihráče a upravujeme okno podle toho jestli jsme hráč 1 nebo 2
posíláme data na server, vykreslujeme text jestli jsme vyhráli nebo prohráli, ošetříme ukončení hry křížkem

