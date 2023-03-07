from os.path import realpath, join, dirname
from modules import Item, ShoppingList


if __name__=="__main__":
    sl = ShoppingList(join(dirname(realpath(__file__)),"list.txt"))
    sl.getItem("rohliky").changeCurency();
    print(sl)
    pl = sl.getItemsByCategory("potraviny")
    print(pl)
    print(pl.calculateTotalPrice("CZK"))
    sl.changeDiscount(10)
    print(sl)
    print(sl.calculateTotalPrice("EUR"))