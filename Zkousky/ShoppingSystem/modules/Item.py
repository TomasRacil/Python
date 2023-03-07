from __future__ import annotations

class Item:
    def __init__(self, name:str, category:str, price:float, curency:str, eur_to_czk:float = 25.5) -> None:
        """Initialize instance of Item class

        Args:
            name (str): item name
            category (str): item category
            price (float): item price
            curency (str): price curency
            eur_to_czk (float, optional): Exchange rate eur to czk. Defaults to 25.5.
        """
        self.name= name
        self.category = category
        self.price = price
        self.curency = curency
        self.eur_to_czk = eur_to_czk
    
    def changeCurency(self)->None:
        """Switch between curencies EUR and CZK
        """
        if self.curency == "EUR":
            self.price = self.price*self.eur_to_czk
            self.curency = "CZK"
        else:
            self.price = self.price/self.eur_to_czk
            self.curency = "EUR"
    def discountedItem(self, discount:float)->Item:
        """Return discounte version of item

        Args:
            discount (float): size of discount

        Returns:
            Item: discounte item
        """
        return Item(self.name, self.category, self.price*((100-discount)/100), self.curency)
    
    def __repr__(self) -> str:
        """One line item representation

        Returns:
            str: %name; %category; %price; %curency
        """
        return f"{self.name}; {self.category}; {self.price} {self.curency}\n"