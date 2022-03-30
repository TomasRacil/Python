## REDDIT BOT

Tento program slouží ke stahhování, komentování a zobrazení obrázku z webové stránky reddit.

## JAK FUNGUJE

  - Po spuštění programu se otevře okno se třemi tlačítky : Cute, Meme a Exit
    - Tlačítka cute a meme pracují na stejném principu
      - Otevře se nové okno s tlačítky : komentovat, stáhnout a zavřít okno
        - Tlačítko koment - okomentuje nejnovější obrázek z vybraného subredditu
        - Tlačítko stáhnout - stáhne obrázek do složky
        - Tlačítko zavřít okno - zavře okno
    - Tlačítko exit vypne program

## POPIS SOUBORŮ
  - Třída bEnd.py slouží jako tzv. backend programu, kde je veškěrá logika bota
    jako je stáhování obrázkua komentování

  - Třída bot.py slouží jako main třída
    - Obsahuje GUI a zprovozňuje funkce z bEnd.py 
  
  - CuteObrazky je složka, do které se stahují obrázky ze subredditu r/awww
  - MemeObrazky je složka, do které se stahují obrázky ze subredditu r/memes

## JAK VYLEPŠIT PROGRAM
  - Na internetu najdete různé boty pro reddit, které by se mohli přidat do programu
    - např. Upvote bot
  - Vyskakovací okna by byla nahrazena tlačítky na liště
  - Obrázky, které chceme ukázat by se objevili přímo v okně programu a neotevírali by se
  - Možnost pro výběr subredditu
    - vytvořit konfigurační soubor, kde by uživatel přepsal jméno subredditu na který se mu zachce
  - Zbavit se globálních proměnných (pokud je to možné)


