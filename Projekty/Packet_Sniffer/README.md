## Packet sniffer 

Program na odchytávání nezašifrované síťové komunikace na protokolech (HTTP,FTP,DNS). 
Po spuštění odposlouchávání se data zapisují na obazovku a zároveň se ukládájí do lokálního souboru ve formátu CSV.

Před spuštěním:
1. Stáhnout knihovnu scapy pomocí balíčkovacího manageru pip - "pip install scapy"
2. V případě spuštění na Linuxové distrubuci musí být program spuštěň s emulovat práva administrátora(sudo) - "sudo python3 main.py"


## Návrhy na vylepšení
- Přidat barvy k jednotlivým paketům(rozlišení protokolů)
- Přidaní podopory dalších protokolů(TELNET..)
