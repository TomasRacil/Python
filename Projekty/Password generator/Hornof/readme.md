Program, který vytvoří heslo na základě požadavků uživatele.

1) Počet znaků hesla (defaultní hodnota je 8 znaků)
2) Obsah písmen v hesle (Uživatel volí: True - False)
3) Obsah čísle v hesle (Pokud uživatel volí: True - False)
4) Obsah interpunkce (Pokud uživatel volí: True - False)

Popis

V projektu jsou 4 funkce co upravují heslo.
get_password_length()
password_generator(cbl, length=8)
password_combination_choice()
fetch_string_constant(choice_list)

Výsledek
Program vygeneruje silné heslo na základě požadavků uživatele. Heslo není zapamatovatelné, tento problém lze vyřešit přidáním otázek.
Samozřejmě heslo by nemělo být generované z údajů, které jsou veřejně dostupné, jako například jméno uživatele.

Příklad otázek:
Jaký je váš oblíbený sportovní tým?
Jaké bylo vaše první auto?

Budoucí možné rozšíření: vytvořit heslo na základě odpovědí uživatele, kontrolní otázky
                         dále přidat podmínku, která by upravovala heslo, například ,že každé heslo musí obsahovat alespoň jedno číslo
                         a jedno velké písmeno
 