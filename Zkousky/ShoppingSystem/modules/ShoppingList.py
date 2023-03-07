from __future__ import annotations
from .Item import Item

class ShoppingList:
    
    items:list
    discount:float
    
    def __init__(self, file:str="") -> None:
        """Initialize intance of shopping list. 
        
        Set discount to 0. If file is empty string create empty shoping list.

        Args:
            file (str, optional): file to load shopping list from. Defaults to "".
        """
        self.items = []
        if file!="":
            with open(file, "r", encoding="utf_8") as f:
                self.items = [
                    Item(
                        line.split(';')[0],
                        line.split(';')[1],
                        float(line.split(';')[2]),
                        line.split(';')[3]
                        ) for line in f.read().split("\n")]
                self.sort()
        self.discount = 0
    
    
    def sort(self)->None:
        """Sort list by converted price
        """
        self.items.sort(key=lambda x: x.price if x.curency == "CZK" else x.price*x.eur_to_czk)
    
    def addItem(self, item:Item)->None:
        """Add item into shoppig list

        Args:
            item (Item): item to be added into shopping list
        """
        self.items.append(item)
        self.sort()
    
    def getItem(self, name:str)->Item:
        """Return item from shopping lit by its name

        Args:
            name (str): name of searched item

        Raises:
            Exception: if no item with this name found throw Exception

        Returns:
            Item: found item
        """
        for i in self.items: 
            if i.name == name: return i
        else: raise Exception();
    
    def changeDiscount(self, discount:float)->None:
        """Set discount for shopping list

        Args:
            discount (float): size of discount
        """
        self.discount = discount
        
    def getItemsByCategory(self, category:str)->ShoppingList:
        """Return new shoping list of items in selected category

        Args:
            category (str): chosen category

        Returns:
            ShoppingList: Shoping list of items in selected category
        """
        cl = ShoppingList()
        cl.items = list(filter(lambda x: x.category==category, self.items))
        return cl
    
    def calculateTotalPrice(self, curency: str)->str:
        """Total price of all items in selected curency. 
        
        If discount is applied print also discounted price

        Args:
            curency (str): selected curency

        Returns:
            str: formated text informing about total and optionaly about discounted price
        """
        sum = 0
        for i in self.items:
            if i.curency != curency:
                i.changeCurency()
                sum+= i.price
                i.changeCurency()
            else:
                sum+= i.price
        out = f"Total price is {sum} {curency}\n"
        if self.discount!=0:
            out+=f"Price after discount {sum*((100-self.discount)/100)} {curency}\n"
        
        return out
    
    def __repr__(self) -> str:
        """String representation of shopping list. 
        Each item on new line. If item is discounted, show it twice, without and with discount aplied.

        Returns:
            str: shopping list string representation
        """
        out: str = ""
        for i in self.items:
            out+=i.__repr__()
            if self.discount > 0:
                out+=i.discountedItem(self.discount).__repr__()
        return out