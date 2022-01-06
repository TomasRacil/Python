# External import
from colorama import Fore, Style
from time import sleep

# Internal import
from Functions.main_fct import *
from Functions.versatile_fct import *
from Functions.letters_fct import *
from Functions.keys_fct import *
from Functions.coins_fct import *
from Functions.outcomes_fct import *
from Functions.intro_fct import *
from Functions.outro_fct import *


class Croom:
    def __init__(self, name, inv, map, used, filePath):
        self.__name = name
        self.__inv = inv
        self.__map = map
        self.__used = used
        self.__filePath = filePath

        self.__position = "start"
        self.__orderOfCoins = []

        # Commands that can be called any time
        self.__globalComDict = {
            "help":PrintHelp,
            "exit":self.ExitFct,
            "inventory":self.PrintInv,
            "map":self.PrintMap,
            "save":self.SaveFct,

            "read invitation letter":Letter_Invitation,
            "read mailbox note":Note_Mailbox,

            "go to front porch":self.FrontPorch,
            "go to main hallway downstairs":self.MainHallway_11
        }

        self.UpdateGCD_map()
        self.UpdateGCD_inv()


    # System functions
    def ExitFct(self):
        # Exits the game

        self.SaveFct()
        self.__position = "exit"
    
    def SaveFct(self):
        # Saves player's progress.

        print(Fore.RED+ " Game saved", Style.RESET_ALL)

        self.__file = open(self.__filePath, "w")
        
        self.__invStr = "".join([self.__thing + ";" for self.__thing in self.__inv])
        self.__mapStr = "".join([self.__place + ";" for self.__place in self.__map])
        self.__usedStr = "".join([self.__thing + ";" for self.__thing in self.__used])
        self.__orderOfCoinsStr = "".join([self.__coin + ";" for self.__coin in self.__orderOfCoins])

        self.__file.write(f"{self.__name}\n{self.__position}\n{self.__invStr}\n{self.__mapStr}\n{self.__usedStr}\n{self.__orderOfCoinsStr}\n")
        self.__file.close()

    def PrintInv(cls):
        # Prints inventory
        # Prints 4 items in row, if not less remaining, then less

        __number = len(cls.__inv)
        __i = 0

        print(Fore.YELLOW+ "------------------------------------------------------------------------\n INVENTORY\n", Style.RESET_ALL)
                
        while(__number != 0):
            if(__number > 4 or __number == 4):
                if(__number > 4):
                    print(f" {cls.__inv[__i + 0]}, {cls.__inv[__i + 1]}, {cls.__inv[__i + 2]}, {cls.__inv[__i + 3]},")
                else:
                    print(f" {cls.__inv[__i + 0]}, {cls.__inv[__i + 1]}, {cls.__inv[__i + 2]}, {cls.__inv[__i + 3]}")
                __number -= 4
                __i += 4
            elif(__number == 3):
                print(f" {cls.__inv[__i + 0]}, {cls.__inv[__i + 1]}, {cls.__inv[__i + 2]}")
                __number -= 3
            elif(__number == 2):
                print(f" {cls.__inv[__i + 0]}, {cls.__inv[__i + 1]}")
                __number -= 2
            elif(__number == 1):
                print(f" {cls.__inv[__i + 0]}")
                __number -= 1

        print(Fore.YELLOW+ "------------------------------------------------------------------------")
        print(Style.RESET_ALL)

    def PrintMap(cls):
        # Prints map
        # Prints 4 items in row, if not less remaining, then less

        __number = len(cls.__map)
        __i = 0

        print(Fore.YELLOW+ "------------------------------------------------------------------------\n MAP\n", Style.RESET_ALL)
                
        while(__number != 0):
            if(__number > 4 or __number == 4):
                if(__number > 4):
                    print(f" {cls.__map[__i + 0]}, {cls.__map[__i + 1]}, {cls.__map[__i + 2]}, {cls.__map[__i + 3]},")
                else:
                    print(f" {cls.__map[__i + 0]}, {cls.__map[__i + 1]}, {cls.__map[__i + 2]}, {cls.__map[__i + 3]}")
                __number -= 4
                __i += 4
            elif(__number == 3):
                print(f" {cls.__map[__i + 0]}, {cls.__map[__i + 1]}, {cls.__map[__i + 2]}")
                __number -= 3
            elif(__number == 2):
                print(f" {cls.__map[__i + 0]}, {cls.__map[__i + 1]}")
                __number -= 2
            elif(__number == 1):
                print(f" {cls.__map[__i + 0]}")
                __number -= 1

        print(Fore.YELLOW+ "------------------------------------------------------------------------")
        print(Style.RESET_ALL)

    def UpdateGCD_map(self):
        # Updates map commands in __globalComDict according to the __map list

        # Underground
        if(("cellar" in self.__map) and ("go to cellar" not in self.__globalComDict)):    self.__globalComDict["go to cellar"] = self.Cellar
        
        # First floor
        if(("workroom" in self.__map)            and ("go to workroom" not in self.__globalComDict)):            self.__globalComDict["go to workroom"] = self.WorkRoom
        if(("kitchen" in self.__map)             and ("go to kitchen" not in self.__globalComDict)):             self.__globalComDict["go to kitchen"] = self.Kitchen
        if(("dining room" in self.__map)         and ("go to dining room" not in self.__globalComDict)):         self.__globalComDict["go to dining room"] = self.DiningRoom
        if(("pantry" in self.__map               and ("go to pantry" not in self.__globalComDict))):             self.__globalComDict["go to pantry"] = self.Pantry
        if(("bathroom downstairs" in self.__map) and ("go to bathroom downstairs" not in self.__globalComDict)): self.__globalComDict["go to bathroom downstairs"] = self.Bathroom_1
        if(("winter garden" in self.__map        and ("go to winter garden" not in self.__globalComDict))):      self.__globalComDict["go to winter garden"] = self.WinterGarden
        if(("garden" in self.__map)              and ("go to garden" not in self.__globalComDict)):              self.__globalComDict["go to garden"] = self.Garden
        if(("shed" in self.__map)                and ("go to shed" not in self.__globalComDict)):                self.__globalComDict["go to shed"] = self.Shed
        if(("playground" in self.__map)          and ("go to playground" not in self.__globalComDict)):          self.__globalComDict["go to playground"] = self.Playground
        if(("gazebo" in self.__map)              and ("go to gazebo" not in self.__globalComDict)):              self.__globalComDict["go to gazebo"] = self.Gazebo
        
        # Second floor
        if(("main hallway upstairs" in self.__map) and ("go to main hallway upstairs" not in self.__globalComDict)): self.__globalComDict["go to main hallway upstairs"] = self.MainHallway_22
        if(("library" in self.__map)               and ("go to library" not in self.__globalComDict)):               self.__globalComDict["go to library"] = self.Library
        if(("terrace" in self.__map)               and ("go to terrace" not in self.__globalComDict)):               self.__globalComDict["go to terrace"] = self.Terrace
        if(("bathroom upstairs" in self.__map)     and ("go to bathroom upstairs" not in self.__globalComDict)):     self.__globalComDict["go to bathroom upstairs"] = self.Bathroom_2
        if(("childrens room" in self.__map)        and ("go to childrens room" not in self.__globalComDict)):        self.__globalComDict["go to childrens room"] = self.ChildrensRoom
        if(("bedroom" in self.__map)               and ("go to bedroom" not in self.__globalComDict)):               self.__globalComDict["go to bedroom"] = self.Bedroom

        # Roof
        if(("attic" in self.__map) and ("go to attic" not in self.__globalComDict)): self.__globalComDict["go to attic"] = self.Attic

    def UpdateGCD_inv(self):
        # Updates inventory commands in __globalComDict according to the __inv list

        # Letters
        if(("fridge letter" in self.__inv) and ("read fridge letter" not in self.__globalComDict)): self.__globalComDict["read fridge letter"] = Letter_Fridge
        if(("pigeon note" in self.__inv)   and ("read pigeon note" not in self.__globalComDict)):   self.__globalComDict["read pigeon note"] = Note_Pigeon

        # Keys
        if(("table key" in self.__inv) and ("look at table key" not in self.__globalComDict)): self.__globalComDict["look at table key"] = Key_Table
        else: self.__globalComDict.pop("look at table key", None)

        if(("chest key" in self.__inv) and ("look at chest key" not in self.__globalComDict)): self.__globalComDict["look at chest key"] = Key_Chest
        else: self.__globalComDict.pop("look at chest key", None)

        if(("soap key" in self.__inv) and ("look at soap key" not in self.__globalComDict)): self.__globalComDict["look at soap key"] = Key_Soap
        else: self.__globalComDict.pop("look at soap key", None)

        if(("safe key" in self.__inv)  and ("look at safe key" not in self.__globalComDict)):  self.__globalComDict["look at safe key"] = Key_Safe
        else: self.__globalComDict.pop("look at safe key", None)

        if(("swing key" in self.__inv) and ("look at swing key" not in self.__globalComDict)): self.__globalComDict["look at swing key"] = Key_Swing
        else: self.__globalComDict.pop("look at swing key", None)

        # Coins
        if(("fridge coin" in self.__inv) and ("look at fridge coin" not in self.__globalComDict)): self.__globalComDict["look at fridge coin"] = Coin_Fridge
        else: self.__globalComDict.pop("look at fridge coin", None)
        
        if(("vase coin" in self.__inv) and ("look at vase coin" not in self.__globalComDict)): self.__globalComDict["look at vase coin"] = Coin_Vase
        else: self.__globalComDict.pop("look at vase coin", None)
        
        if(("medicine bottle coin" in self.__inv) and ("look at medicine bottle coin" not in self.__globalComDict)): self.__globalComDict["look at medicine bottle coin"] = Coin_MedicineBottle
        else: self.__globalComDict.pop("look at medicine bottle coin", None)
        
        if(("safe coin" in self.__inv) and ("look at safe coin" not in self.__globalComDict)): self.__globalComDict["look at safe coin"] = Coin_Safe
        else: self.__globalComDict.pop("look atsafe coin ", None)
        
        if(("doll coin" in self.__inv) and ("look at doll coin" not in self.__globalComDict)): self.__globalComDict["look at doll coin"] = Coin_Doll
        else: self.__globalComDict.pop("look at doll coin", None)
        
        if(("costume coin" in self.__inv) and ("look at costume coin" not in self.__globalComDict)): self.__globalComDict["look at costume coin"] = Coin_Costume
        else: self.__globalComDict.pop("look at costume coin", None)
        
        if(("nest coin" in self.__inv) and ("look at nest coin" not in self.__globalComDict)): self.__globalComDict["look at nest coin"] = Coin_Nest
        else: self.__globalComDict.pop("look at nest coin", None)
        
        if(("sandbox coin" in self.__inv) and ("look at sandbox coin" not in self.__globalComDict)): self.__globalComDict["look at sandbox coin"] = Coin_Sandbox
        else: self.__globalComDict.pop("look at sandbox coin", None)
        
        if(("rag coin" in self.__inv) and ("look at rag coin" not in self.__globalComDict)): self.__globalComDict["look at rag coin"] = Coin_Rag 
        else: self.__globalComDict.pop("look at rag coin", None)
        
        if(("book coin" in self.__inv) and ("look at book coin" not in self.__globalComDict)): self.__globalComDict["look at book coin"] = Coin_Book
        else: self.__globalComDict.pop("look at book coin", None)

    def GetCommand(cls, localComDict):
        '''
        Lets user enter his choice of action. Controls thatit is a defined
        option, corrects it to lower case and gets rid of articles.

        Args:
            localComDict(dict): Local dictionary passed from a room.

        Returns:
            A value corresponding to the command in either of dictionaries.
        '''

        while(True):
            __command = input(Fore.MAGENTA+ "\n I choose action: ")
            print(Style.RESET_ALL)

            __command = __command.lower()
            __command = ArticleCheck(__command)

            # Global command dictionary    
            if(__command in cls.__globalComDict):
                if("read" in __command):
                    return cls.__globalComDict.get(__command)(cls.__name)
                else:
                    return cls.__globalComDict.get(__command)()

            # Local command dictionary
            elif(__command in localComDict):
                if(("take" in __command) and ("seeds" not in __command) and ("barrel" not in __command)):
                    cls.__invIn(localComDict.get(__command))
                elif("use" in __command):
                    cls.__invOut(__command)
                    return localComDict.get(__command)()
                elif(("coin" in __command) and ("look at" not in __command)):
                    cls.__invOut(__command)
                elif("read" in __command):
                    return localComDict.get(__command)(cls.__name)
                else:
                    return localComDict.get(__command)()

            # Command not found error
            else:
                CantDoThat()

    def InvIn(self, item):
        # Stores item in __inv list

        if(item not in self.__inv):
            self.__inv.append(item)
            self.UpdateGCD_inv()
            print(f"\n You took the {item}.\n")

    def InvOut(self, command):
        # Deletes an item from __inv after using it

        command = command.replace("use ", "")
        try:
            self.__inv.remove(command)
            self.UpdateGCD_inv()
        except:
            pass

    def MapIn(self):
        # Stores place in __map list

        if(self.__position not in self.__map):
            self.__map.append(self.__position)
            self.UpdateGCD_map()

    def UnlockedDoor(self):
        # Prints that you have unlocked the door

        print(" You have unlocked the door.")

    # Underground
    def Cellar(self):
        self.__position = "cellar"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n CELLAR\n")
        print(Style.RESET_ALL+ " As you go down the stairs to the cellar, the light around you is slowly retreating. In the end, the darkness\n consumes you whole. It is strangely quiet in here. It feels as if you have sunk with closed eyes under water.")
        print(" You just stand there for a while doing nothing, but then you snap determined to continue your adventure.\n You are in a great need of light, though.")

        def UseFlashlight():
            print(" When you switch on the flashlight, a cone of light illuminates your surroundings. The cellar looks like\n a workshop. There are many various tools, tables and shelves, but only one table has", Fore.MAGENTA+ "a drawer.", Style.RESET_ALL)
            print(" There is also", Fore.MAGENTA+ "a basket", Style.RESET_ALL+ "in one corner of the cellar.")

            self.InvIn("flashlight")

            __localComDict["look at drawer"] = OpenDrawer_1
            __localComDict["open drawer"] = OpenDrawer_1
            __localComDict["look at basket"] = LookAtBasket_1

        # Drawer
        def OpenDrawer_1():
            print(" You come to the drawer and try to tug on its handle.\n\n Nothing happens. So you pull on it with all your strength and stumble back, when the drawer abruptly\n flies open, uncovering a pair of", Fore.MAGENTA+ "pliers.", Style.RESET_ALL)

            __localComDict["take pliers"] = "pliers"

        def OpenDrawer_2():
            print(" The drawer is empty.")

        #Basket
        def LookAtBasket_1():
            print(" You look inside of the basket and spot", Fore.YELLOW+ "a COIN", Style.RESET_ALL+ "resting on a white rag!")

            __localComDict["look at coin"] = Coin_Rag
            __localComDict["take coin"] = "rag coin"

        def LookAtBasket_2():
            print(" There is only the white rag in the basket.")

        # Local dictionary
        __localComDict = {
            "go back":self.Stairs_1
        }

        def UpdateLCD():
            if(("flashlight" in self.__inv) and ("open drawer" not in __localComDict)):
                __localComDict["use flashlight"] = UseFlashlight

            if("pliers" in self.__inv):
                __localComDict.update({"open drawer":OpenDrawer_2})
                __localComDict.pop("look at drawer", None)
                __localComDict.pop("take pliers", None)

            if("rag coin" in self.__inv):
                __localComDict.update({"look at basket":LookAtBasket_2})
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)

        while(self.__position == "cellar"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()


    # First floor
    def FrontPorch(self):       
        self.__position = "front porch"

        # Description
        print(Fore.YELLOW+ "\n---------------------------------------------------------------------------------------------------------------\n FRONT PORCH\n")
        print(Style.RESET_ALL+ " And here you are, standing on the front porch of the old house once again. Its distinct sound never changes.\n Although the creaking of planks under your feet combined with the sounds of the Grey Forest nearby")
        print(" still gives you an unsettling feeling, it doesn't seem so haunting anymore. The mailbox and the doorbell are\n still the same. As you reach out for the doorknob, the massive wooden door open\n for you on its own accord.\n\n The only thing left for you to do, is to step into the warm yellow welcoming light that awaits you.")

        def LookAtMailbox():
            print(" There is no other note in the mailbox.")

        # Local dictionary
        __localComDict = {
            "go straight":self.MainHallway_11,
            "look at mailbox":LookAtMailbox
        }

        while(self.__position == "front porch"):
            self.GetCommand(__localComDict)

            self.UpdateGCD_inv()

    def MainHallway_11(self):   
        self.__position = "MainHallway_11"

        # Description
        print(Fore.YELLOW+      "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY\n")
        print(Style.RESET_ALL+  " You can see several doors. One currently on your left and two at the back of the Main hallway. In the middle,\n there is another hallway crossing the main one. You can not see where it leads from your position.")

        def LockedDoor():
            print(" You grab the door handle and try to open the door, but you can't. It is probably locked.\n There is something that looks like an old school pen carved in the door.")
        
        def UseKey():
            self.UnlockedDoor()
            self.__used.append("table key")

        # Local dictionary
        __localComDict = {
            "go back":self.FrontPorch, 
            "go straight":self.MainHallway_12,
            "go left":LockedDoor
        }

        def UpdateLCD():
            if("table key" in self.__used):
                __localComDict.update({"go left":self.WorkRoom})
            elif("table key" in self.__inv):
                __localComDict["use table key"] = UseKey

        while(self.__position == "MainHallway_11"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def WorkRoom(self):         
        self.__position = "workroom"
        self.MapIn()

        # Description
        print(Fore.YELLOW+      "\n---------------------------------------------------------------------------------------------------------------\n WORKROOM\n")
        print(Style.RESET_ALL+  " The workroom is a serious looking place. There are piles of paper stocked in every corner of the room.\n Buried under them, you can see an armchair and", Fore.MAGENTA+ "a desk", Style.RESET_ALL+ "with an office chair.")

        # Desk
        def LookAtDesk():
            print(" There are long, deep unusual scratch markes on the desk as well as on the office chair. They seem almost\n unhuman and growing in length and numbers as the time passes. Some of them are even shaped")
            print(" like numbers. Next to them lies practicly intackt", Fore.MAGENTA+ "statue", Style.RESET_ALL+ "of what looks like a human.")

            __localComDict["look at statue"] = LookAtStatue

        # Statue
        def LookAtStatue():
            print(" The golden statue looks like a man, an older gentleman, to be precise. His walking stick is pointing toward\n", Fore.MAGENTA+ "a painting", Style.RESET_ALL+ "on the wall. You would bet anything, that just a second ago, it was ponting to his feet.")
            PressEnter()
            print("\n ...")
            sleep(3)
            print("\n Weird.")

            __localComDict["look at painting"] = LookAtPainting

        # Painting
        def LookAtPainting():
            print(" It is a crooked painting of a landscape depicting a meadow connected to the forest in the back. The sun is\n setting behind the trees. It would be a beautiful painting, if it wasn't for the dust")
            print(" and scratches all over it. As you walk closer, you can see there is something beneath it. You move the painting\n to the side and see", Fore.MAGENTA+ "a safe.", Style.RESET_ALL)

            __localComDict["look at safe"] = LookAtSafe
            __localComDict["open safe"] = OpenSafe_1

        # Safe
        def LookAtSafe():
            print(" The safe is of a greyish colour and medium size, meaning a LOT of money and jewelry could fit in there, but\n nothing particulary large. You will need a six digit code to open it.")

        def OpenSafe_1():
            codeDef = "659286"
            codePl = input(Fore.MAGENTA+ "\n Enter the code: ")
            print(Style.RESET_ALL)

            if(codeDef == codePl):
                print(" You entered the right code!\n\n You hear the ratchets unlock and then...")
                sleep(3)
                print(" There is", Fore.YELLOW+ "a COIN!", Style.RESET_ALL+ "And far in the back lies", Fore.MAGENTA+ " a key.", Style.RESET_ALL)

                __localComDict["look at coin"] = Coin_Safe
                __localComDict["take coin"] = "safe coin"
                __localComDict["look at key"] = Key_Safe
                __localComDict["take key"] = "safe key"

            else:
                print(" The entered code is wrong.\n Try again or look for more clues.")

        def OpenSafe_2():
            print(" The safe is opend and far in the back lies", Fore.MAGENTA+ "a key.", Style.RESET_ALL)

        def OpenSafe_3():
            print(" The safe is opend and the coin lies there.")

        def OpenSafe_4():
            print(" The safe is opend and empty.")

        # Local dictionary
        __localComDict = {
            "go back": self.MainHallway_11,
            "look at desk": LookAtDesk
        }

        def UpdateLCD():
            if(("safe key" in self.__inv) or ("safe key" in self.__used)):
                __localComDict.pop("look at key", None)
                __localComDict.pop("take key", None)

                if("safe coin" in self.__inv):
                    __localComDict.update({"open safe":OpenSafe_4})
                    __localComDict.pop("look at coin", None)
                    __localComDict.pop("take coin", None)
                else:
                    __localComDict.update({"open safe":OpenSafe_3})
                    __localComDict["look at coin"] = Coin_Safe
                    __localComDict["take coin"] = "safe coin"
            
            else:
                if("safe coin" in self.__inv):
                    __localComDict.update({"open safe":OpenSafe_2})
                    __localComDict.pop("look at coin", None)
                    __localComDict.pop("take coin", None)

        while(self.__position == "workroom"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def MainHallway_12(self):   
        self.__position = "MainHallway_12"

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY\n")
        print(Style.RESET_ALL+ " You leave the place that you were standing on behind you as you proceed to the middle of the main hallway.\n There is an old staircase on your left and hallway, that looks like it leads to the kitchen, on your right.")

        # Local dictionary
        __localComDict = {
            "go back":      self.MainHallway_11,
            "go straight":  self.MainHallway_13,
            "go left":      self.Stairs_1,
            "go right":     self.Kitchen
        }
        
        while(self.__position == "MainHallway_12"):
            self.GetCommand(__localComDict)

            self.UpdateGCD_inv()

    def Stairs_1(self):         
        self.__position = "Stairs_1"

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n STAIRS\n")
        print(Style.RESET_ALL+ " There is a staircase that leads upstairs and a door in front of you.")

        def LockedDoor():
            print(" You grab the door handle and try to open the door, but you can't. It is probably locked.\n The door is completely black. So black that you almost can't see it in the dim light.")
        
        def UseKey():
            self.UnlockedDoor()
            self.__used.append("chest key")

        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_12,
            "go up":self.MainHallway_22,
            "go down":LockedDoor,
            "go straight":LockedDoor
        }

        def UpdateLCD():
            if("chest key" in self.__inv):
                __localComDict["use chest key"] = UseKey
            elif("chest key" in self.__used):
                __localComDict.update({"go down":self.Cellar})
                __localComDict.update({"go straight":self.Cellar})

        while(self.__position == "Stairs_1"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def Kitchen(self):          
        self.__position = "kitchen"
        self.MapIn()

        # Description
        print(Fore.YELLOW+      "\n---------------------------------------------------------------------------------------------------------------\n KITCHEN\n")
        print(Style.RESET_ALL+  " The kitchen is quite large and it freely passes to a dining room on the left. There is a window covered\n by a torn thin curtain. Under the window is a vintage looking, once white, kitchen unit made of various")
        print(" kitchen cupboards. Some are damaged more, some less, but there is one", Fore.MAGENTA+ "cupboard,", Style.RESET_ALL+ "that catches\n your attention, because only this one still has a door. The kitchen unit runs along the wall")
        print(" to the right until it touches a stove. In the middle of the unit on the right is a door. Right next to you\n on the left is a spacious", Fore.MAGENTA+ "fridge.", Style.RESET_ALL)

        # Cupboard
        def OpenCupboard_1():
            print(" You carefuly open the cupboard door. There are two shelves. On the upper one is a small", Fore.MAGENTA+ "pocket knife,", Style.RESET_ALL+ "\n on the lower one are just fragmented dishes.")

            __localComDict["take knife"] = "pocket knife"
            __localComDict["take pocket knife"] = "pocket knife"

        def OpenCupboard_2():
            print(" It's all empty, except for the dirty fragmented dishes.")

        # Fridge
        def LookAtFridge_1():
            print(" There is", Fore.MAGENTA+ "a letter", Style.RESET_ALL+ f" pinned to the fridge. Its addressee seems to be you since it has \"{self.__name}\"\n written on top of it.")
            
            __localComDict["read letter"] = Letter_Fridge
            __localComDict["take letter"] = "fridge letter"

        def LookAtFridge_2():
            print(" There is only a silhouette of the letter burned by the sun meaning it had to hang there for quite some time.")

        def OpenFridge_1():
            print(" When you open the fridge, you can't believe your eyes! There is...")
            sleep(3)
            print(" absolutely nothing...\n\n You are closing the fridge feeling disappointed.")

        def OpenFridge_2():
            print(" When you open the fridge, you can't believe your eyes! There is...")
            sleep(3)
            print("", Fore.YELLOW+ "a COIN!!", Style.RESET_ALL)

            __localComDict["look at coin"] = Coin_Fridge
            __localComDict["take coin"] = "fridge coin"


        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_12,
            "go left":self.DiningRoom,
            "go right":self.Pantry,
            "open cupboard":OpenCupboard_1,
            "look at fridge":LookAtFridge_1,
            "open fridge":OpenFridge_1,
        }

        def UpdateLCD():
            if(("pocket knife" in self.__inv) or ("pocket knife" in self.__used)):
                __localComDict.update({"open cupboard":OpenCupboard_2})
                __localComDict.pop("take knife", None)
                __localComDict.pop("take pocket knife", None)

            if("fridge letter" in self.__inv):
                if("fridge coin" in self.__inv):
                    __localComDict.update({"look at fridge":LookAtFridge_2})
                    __localComDict.update({"open fridge":OpenFridge_1})
                    __localComDict.pop("look at coin", None)
                    __localComDict.pop("take coin", None)
                else:
                    __localComDict.update({"open fridge":OpenFridge_2})

        while(self.__position == "kitchen"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def DiningRoom(self):       
        self.__position = "dining room"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n DINING ROOM\n")
        print(Style.RESET_ALL+ " You walk up to a spacious room with two of its walls made out of French windows and the third covered by\n", Fore.MAGENTA+ "a tapestry.", Style.RESET_ALL+ "You move your gaze from the tapestry to the center of the room where a sturdy mahogany", Fore.MAGENTA+ "table", Style.RESET_ALL+ "")
        print(" is situated and surrounded by ten chairs.")

        # Table
        def LookAtTable_1():
            print(" There is a dirty glass", Fore.MAGENTA+ "vase", Style.RESET_ALL+ "with a bouquet of dead flowers and", Fore.MAGENTA+ "a key", Style.RESET_ALL+ "lying peacefully next to it.")

            __localComDict["look at vase"] = LookAtVase
            __localComDict["look at key"] = Key_Table
            __localComDict["take key"] = "table key"

        def LookAtTable_2():
            print(" There is a dirty glass", Fore.MAGENTA+ "vase", Style.RESET_ALL+ "with a bouquet of dead flowers.")

            __localComDict["look at vase"] = LookAtVase

        def LookAtTable_3():
            print(" There is", Fore.MAGENTA+ "a key", Style.RESET_ALL+ "lying peacefully among the vase shards.")

            __localComDict["look at key"] = Key_Table
            __localComDict["take key"] = "table key"

        def LookAtTable_4():
            print(" There are dead flowers on the table lying among the shards of their vase. They look even more sad and abandoned now.")

        # Vase
        def LookAtVase():
            print(" As you look at the vase closer, you notice there is something inside. You can not see what,\n because of the dirt, though. You take out the flowers and flip the vase upside down, but nothing comes out.")

            __localComDict["break vase"] = BreakVase

        def BreakVase():
            print(" You smash the vase with your full strength against the table. The glass shards spread across the table\n and even hit the flowers that they protected just a minute ago. Among the shards lies,")
            print(" to your surprise,", Fore.YELLOW+ "a COIN!", Style.RESET_ALL+ "You breathe out relieved, that you did not break the vase for nothing.")

            __localComDict.pop("look at vase", None)
            __localComDict["take coin"] = "vase coin"
            __localComDict["look at coin"] = Coin_Vase

        # Tapestry
        def LookAtTapestry():
            print(" It depicts the old house, but in his long lost glory. It used to be a beige house with dark brown\n wooden beams. The ivy and briar were growing only on some parts, opposite to nowadays, when almost")
            print(" the whole house is swallowed by them. Thanks to that you can even see the house number, which is 659.\n It truly used to look magnificent.")

        # Local dictionary
        __localComDict = {
            "go back":self.Kitchen,
            "look at table":LookAtTable_1,
            "look at tapestry":LookAtTapestry
        }

        def UpdateLCD():
            if(("table key" in self.__inv) or ("table key" in self.__used)):
                __localComDict.pop("look at key", None)
                __localComDict.pop("take key", None)

                if("vase coin" in self.__inv):
                    __localComDict.update({"look at table":LookAtTable_4})
                    __localComDict.pop("look at vase", None)
                    __localComDict.pop("break vase", None)
                    __localComDict.pop("take coin", None)
                    __localComDict.pop("look at coin", None)
                else:
                    __localComDict.update({"look at table":LookAtTable_2})
                    __localComDict["look at vase"] = LookAtVase

            else:
                if("vase coin" in self.__inv):
                    __localComDict.update({"look at table":LookAtTable_3})
                    __localComDict["look at key"] = Key_Table
                    __localComDict["take key"] = "table key"

        while(self.__position == "dining room"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def Pantry(self):           
        self.__position = "pantry"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n PANTRY\n")
        print(Style.RESET_ALL+ " The pantry is so small, that you can barely fit in it. It is dusky inside, but the omnipresent shelves,\n that exceed you by so much, are difficult not to see. This whole place reeks of mold and rot.")
        print(" It makes you want to throw up. You have to act quickly. You look around and see some rotten apples, a few\n glasses filled with who knows what, mouse traps and", Fore.MAGENTA+ "a barrel full of seeds.", Style.RESET_ALL)

        def LookAtBarrel():
            print(" It's just a normal barrel full of various seeds. They might be of some use.")

        def TakeBarrel():
            print(" The barrel is too heavy and big.")

        def TakeSeeds():
            print(" What do you want to put the seeds in?")

        def UseBox():
            print(" As you move a little closer to the barrel, a tiny mouse runs out towards you, but changes its mind\n halfway. She then makes two circles around the barrel and disppears under one of the shelves.")
            print(" After this, you are finaly allowed to scoop some seeds into the box.")
            
            self.InvvIn("box with seeds")

        # Local dictionary
        __localComDict = {
            "go back":self.Kitchen,
            "look at seeds":LookAtBarrel,
            "look at barrel":LookAtBarrel,
            "take barrel":TakeBarrel,
            "take seeds":TakeSeeds
        }

        def UpdateLCD():
            if("box" in self.__inv):
                __localComDict["use box"] = UseBox
            
            if(("box with seeds" in self.__inv) or ("box with seeds" in self.__used)):
                __localComDict.pop("use box", None)

        while(self.__position == "pantry"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def MainHallway_13(self):   
        self.__position = "MainHallway_13"

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY\n")
        print(Style.RESET_ALL+ " You are at the back of the Main hallway. There are door on on your left and large glass door in front of you.")

        def LockedDoor():
            print(" You grab the door handle and try to open the door, but you can't. It is probably locked.\n In the door is a small window, throug which you can see plants.")

        def UseKey():
            self.UnlockedDoor()
            self.__used.append("soap key")

        __localComDict = {
            "go back":self.MainHallway_12,
            "go left":self.Bathroom_1,
            "go straight":LockedDoor
        }

        def UpdateLCD():
            if("soap key" in self.__used):
                __localComDict.update({"go straight":self.WinterGarden})
            elif("soap key" in self.__inv):
                __localComDict["use soap key"] = UseKey

        while(self.__position == "MainHallway_13"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def Bathroom_1(self):       
        self.__position = "bathroom downstairs"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n BATHROOM DOWNSTAIRS\n")
        print(Style.RESET_ALL+ " You hear water under your feet as you step in. There is a shower in one corner and a toilet in the other.\n None of them particulary clean...\n\n Then there is a wash-basin and above it is", Fore.MAGENTA+ "a bathroom cabinet", Style.RESET_ALL+ "with a broken mirror.")
        print(" The thing that disturbs you the most is not the filthiness of this place, athough it's disgusting,\n but the proliferating", Fore.MAGENTA+ "notes", Style.RESET_ALL+ "on the walls of the entire bathroom. It's like someone\n out of their mind was scribbling them.\n\n Or were they repeating it to themselves?")

        # Bathroom cabinet
        def OpenBathroomCabinet():
            print(" There are some used toothbrushes, toothpaste and", Fore.MAGENTA+ "a medicine bottle.", Style.RESET_ALL)

            __localComDict["open medicine bottle"] = OpenMedicineBottle_1
            __localComDict["open bottle"] = OpenMedicineBottle_1

        # Medicine bottle
        def OpenMedicineBottle_1():
            print(" In the midst of the pills rests", Fore.YELLOW+ "a COIN!", Style.RESET_ALL)

            __localComDict["look at coin"] = Coin_MedicineBottle
            __localComDict["take coin"] = "medicine bottle coin"

        def OpenMedicineBottle_2():
            print(" The bottle is half filled with piils.")

        # Notes
        def LookAtNotes():
            print(" N O T   A L L   M I R R O R S   A R E   W H A T   T H E Y   S E E M")

        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_13,
            "open bathroom cabinet":OpenBathroomCabinet,
            "read note":LookAtNotes,
            "read notes":LookAtNotes,
            "look at note":LookAtNotes,
            "look at wall":LookAtNotes,
            "look at notes":LookAtNotes,
            "look at walls":LookAtNotes
        }

        def UpdateLCD():
            if("medicine bottle coin" in self.__inv):
                __localComDict.update({"open medicine bottle":OpenMedicineBottle_2})
                __localComDict.update({"open bottle":OpenMedicineBottle_2})
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)

        while(self.__position == "bathroom downstairs"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def WinterGarden(self):     
        self.__position = "winter garden"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n WINTER GARDEN\n")
        print(Style.RESET_ALL+ " You step into an unkept, otherwise beautiful, winter garden. There is a fireplace, few chairs, a sofa and\n a coffe table on one side and many gorgeous plants and flowers on the other. There is only one")
        print(" empty", Fore.MAGENTA+ "flowerpot", Style.RESET_ALL+ "amongst them. Another glass door is in front of you.")

        # Flowerpot
        def LookAtFlowerpot_1():
            print(" There is an empty closing", Fore.MAGENTA+ "box", Style.RESET_ALL+ "in the flowerpot.")

            __localComDict["take box"] = "box"

        def LookAtFlowerpot_2():
            print(" It is empty.")

        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_13,
            "go straight":self.Garden,
            "look at flowerpot":LookAtFlowerpot_1
        }

        def UpdateLCD():
            if(("box" in self.__inv) or ("box with seeds" in self.__inv) or ("box with seeds" in self.__used)):
                __localComDict.update({"look at flowerpot":LookAtFlowerpot_2})
                __localComDict.pop("take box", None)

        while(self.__position == "winter garden"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def Garden(self):           
        self.__position = "garden"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n GARDEN\n")
        print(Style.RESET_ALL+ " You stand at the intersection of four beaten paths, the house rising behind you. One of the paths leads\n right, one left and the last one goes straight to the forest.")

        # Local dictionary
        __localComDict = {
            "go back":self.WinterGarden,
            "go straight":self.Gazebo,
            "go right":self.Playground,
            "go left":self.Shed
        }

        while(self.__position == "garden"):
            self.GetCommand(__localComDict)

            self.UpdateGCD_inv()

    def Shed(self):             
        self.__position = "shed"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n SHED\n")
        print(Style.RESET_ALL+ " You follow the left path and it leads you to a door of a small garden shed situated by the side of the house.\n A beautiful plane tree is growing next to it.")

        def UsePliers():
            print(" You gather all your strength and try to cut the chain with the pliers. It takes you a while,\n but in the end, you manage to do it. With relieve, you throw the dull pliers on the ground")
            print(" along with the chain and padlock.")

            self.__used.append("pliers")

            __localComDict.update({"go straight":OpenDoor_2})
            __localComDict.update({"open door":OpenDoor_2})
            __localComDict.update({"open shed":OpenDoor_2})

        def OpenDoor_1():
            print(" You try to open the door of the shed, but they're locked with a strong chain and a padlock.")

        def OpenDoor_2():
            print(" The shed full of garden supplies and other craft tools. There is also a wooden", Fore.MAGENTA+ " ladder.", Style.RESET_ALL)

            __localComDict["take ladder"] = "ladder"

        def OpenDoor_3():
            print(" The shed full of garden supplies and other craft tools.")

        # Local dictionary
        __localComDict = {
            "go back":self.Garden,
            "go straight":OpenDoor_1,
            "open door":OpenDoor_1,
            "open shed":OpenDoor_1
        }

        def UpdateLCD():
            if("pliers" in self.__inv):
                __localComDict["use pliers"] = UsePliers

            if("pliers" in self.__used):
                __localComDict.update({"go straight":OpenDoor_2})
                __localComDict.update({"open door":OpenDoor_2})
                __localComDict.update({"open shed":OpenDoor_2})

            if("ladder" in self.__inv):
                __localComDict.update({"go straight":OpenDoor_3})
                __localComDict.update({"open door":OpenDoor_3})
                __localComDict.update({"open shed":OpenDoor_3})
                __localComDict.pop("take ladder", None)

        while(self.__position == "shed"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def Playground(self):       
        self.__position = "playground"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n PLAYGROUND\n")
        print(Style.RESET_ALL+ " You follow the path and soon come across a playground. There is", Fore.MAGENTA+ "a swing, a sandbox", Style.RESET_ALL+ "and", Fore.MAGENTA+ "a slide.", Style.RESET_ALL)

        def LookAtSlide():
            print(" It's just an ordinary slide for kids.")

        # Sandbox
        def LookAtSandbox_1():
            print(" There is", Fore.MAGENTA+ "a sieve", Style.RESET_ALL+ "lying in the middle of the sandbox.")

            __localComDict["use sieve"] = UseSieve_1

        def UseSieve_1():
            print(" You take the sieve and start sieving the sand in the sandbox little by little, until...")
            sleep(3)
            print("", Fore.YELLOW+ "A COIN", Style.RESET_ALL+ "has stayed in the sieve!")

            __localComDict["look at coin"] = Coin_Sandbox
            __localComDict["take coin"] = "sandbox coin"

        def UseSieve_2():
            print(" You go through the sandbox again, but without a success this time.")
        
        # Swing
        def LookAtSwing_1():
            print(" The swing is moving on its own accord. You would like to think it's because of the wind, but it is not\n strong enough. Then you notice there is", Fore.MAGENTA+ "a key", Style.RESET_ALL+ "on the ground under it!")

            __localComDict["look at key"] = Key_Swing
            __localComDict["take key"] = "swing key"

        def LookAtSwing_2():
            print(" The swing is not moving anymore.")

        # Local dictionary
        __localComDict = {
            "go back":self.Garden,
            "look at sandbox":LookAtSandbox_1,
            "look at swing":LookAtSwing_1,
            "look at slide":LookAtSlide
        }

        def UpdateLCD():
            if(("swing key" in self.__inv) or ("swing key" in self.__used)):
                __localComDict.update({"look at swing":LookAtSwing_2})
                __localComDict.pop("look at key", None)
                __localComDict.pop("take key", None)

            if("sandbox coin" in self.__inv):
                __localComDict.update({"use sieve":UseSieve_2})
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)

        while(self.__position == "playground"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def Gazebo(self):
        self.__position = "gazebo"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n GAZEBO\n")
        print(Style.RESET_ALL+ " You let the path lead you. As soon as you step into the forest, you start to have a strange feelig in your\n gut. You try to ignore it and continue walking, passing hight trees and dodging branches,")
        print(" that are trying to touch your shouldres and head as they swing in the wind. You come to a stop, when you\n notice a small glass gazebo, whose golden light shines through the forest,")
        print(" making it look like a star. You close the distance rather quickly, wanting to be in the soothing light again.\n\n You halt in front of the glass door. You can not regognize anything inside, since the image is fuzzy.")
        
        def LockedDoor():
            print(" You grab the door handle and try to open the door, but you can't. It is probably locked.")

        def UseKey():
            self.UnlockedDoor()
            self.__used.append("safe key")

        def Inside():
            print(" You step into the gazebo and a star-like light embraces you, a golden slot machine standing in the center.\n You blink a few to times in order to get used to the strong glow...")
            sleep(3)
            print(" Then you take two steps toward the slot machine and expect it. There is a coin hole and a long handle\n with a sphere at the of it. The display is empty.")
            print(" There is a riddle at the top of the slot machine saying:\n\n  With hands full of gold, pull on the globe.\n  Wishing for your gain, I must obtain.\n  Align your needs, wait for my deeds.\n  Cast findings away, let me travail.\n  With one last blink, pull the handgrip.")

        def PullHandle_1():
            self.__position = "slot machine"
            __numOfInsert = 0

            print(" You pull on the handle and colorful lights start to flicker, the display suddenly showing \"0\".")

            self.__orderOfCoins.clear()

            __useCoinsDict = {
                "pull handle":PullHandle_2,
                "use handle":PullHandle_2
            }

            if(("fridge coin" in self.__inv) and ("fridge coin" not in __useCoinsDict)): __useCoinsDict["fridge coin"] = self.InvOut
            else: __useCoinsDict.pop("fridge coin", None)
            
            if(("vase coin" in self.__inv) and ("vase coin" not in __useCoinsDict)): __useCoinsDict["vase coin"] = self.InvOut
            else: __useCoinsDict.pop("vase coin", None)
            
            if(("medicine bottle coin" in self.__inv) and ("medicine bottle coin" not in __useCoinsDict)): __useCoinsDict["medicine bottle coin"] = self.InvOut
            else: __useCoinsDict.pop("medicine bottle coin", None)
            
            if(("safe coin" in self.__inv) and ("safe coin" not in __useCoinsDict)): __useCoinsDict["safe coin"] = self.InvOut
            else: __useCoinsDict.pop("safe coin ", None)
            
            if(("doll coin" in self.__inv) and ("doll coin" not in __useCoinsDict)): __useCoinsDict["doll coin"] = self.InvOut
            else: __useCoinsDict.pop("doll coin", None)
            
            if(("costume coin" in self.__inv) and ("costume coin" not in __useCoinsDict)): __useCoinsDict["costume coin"] = self.InvOut
            else: __useCoinsDict.pop("costume coin", None)
            
            if(("nest coin" in self.__inv) and ("nest coin" not in __useCoinsDict)): __useCoinsDict["nest coin"] = self.InvOut
            else: __useCoinsDict.pop("nest coin", None)
            
            if(("sandbox coin" in self.__inv) and ("sandbox coin" not in __useCoinsDict)): __useCoinsDict["sandbox coin"] = self.InvOut
            else: __useCoinsDict.pop("sandbox coin", None)
            
            if(("rag coin" in self.__inv) and ("rag coin" not in __useCoinsDict)): __useCoinsDict["rag coin"] = self.InvOut
            else: __useCoinsDict.pop("rag coin", None)
            
            if(("book coin" in self.__inv) and ("book coin" not in __useCoinsDict)): __useCoinsDict["book coin"] = self.InvOut
            else: __useCoinsDict.pop("book coin", None)
            
            # Insert coins into slot machine
            while(self.__position == "slot machine"):
                __actPl = input(Fore.MAGENTA+ "\n Insert coin: ")
                print(Style.RESET_ALL)

                # Case control
                __actPl = __actPl.lower()

                # Article control
                __actPl = ArticleCheck(__actPl)

                # "use" control
                if(("use" in __actPl) and ("coin" in __actPl)):
                    __actPl = __actPl.replace("use ", "")

                if(__actPl in __useCoinsDict):
                    if("coin" in __actPl):
                        __numOfInsert += 1

                        print(f" The coin rattles inside the slot machine and you wait until the silence settles.\n Your coin is gone and the display now shows \"{__numOfInsert}\".")

                        __useCoinsDict.get(__actPl)(__actPl)
                        __useCoinsDict.pop(__actPl, None)

                        self.__orderOfCoins.append(__actPl)
                    else:
                        return __useCoinsDict.get(__actPl)(__numOfInsert)
                else:
                    CantDoThat()

        def PullHandle_2(numOfInsert):
            self.__position = "gazebo"

            if(numOfInsert != 10):
                print(" All the coins, that you have just inserted into the slot machine, fall out and its display goes blank again.\n You take the coins back thinking about your next step.")

                for item in self.__orderOfCoins:
                    self.__inv.append(item)
                    #self.__used.remove(item)
            else:
                print(" The slot machine starts to play a victorious, but crazy hotchpotch and gradually shines more and more\n until you are completely blinded by it...\n\n")
                print(Fore.YELLOW+ "\n---------------------------------------------------------------------------------------------------------------\n", Style.RESET_ALL)

                self.__position = "outro"
                self.SaveFct()
                Outro(self.__name, self.__orderOfCoins)

        # Local dictionary
        __localComDict = {
            "go back":self.Garden,
            "go straight":LockedDoor,
            "open door":LockedDoor
        }

        def UpdateLCD():
            if("safe key" in self.__inv):
                __localComDict["use safe key"] = UseKey
            elif("safe key" in self.__used):
                __localComDict["pull handle"] = PullHandle_1
                __localComDict["use handle"] = PullHandle_1
                __localComDict.update({"go straight":Inside})
                __localComDict.update({"open door":Inside})
                __localComDict.pop("use safe key", None)

        while(self.__position == "gazebo"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()


    # Second floor
    def MainHallway_21(self):       
        self.__position = "MainHallway_21"

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY UPSTAIRS\n")
        print(Style.RESET_ALL+ " You stand at the one end of the hallway. You left the stairs behind you and are now looking through\n a glass doors, that are in front of you and by your left hand. On your right\n is a standart wooden door.")

        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_22,
            "go straight":self.Terrace,
            "go left":self.Terrace,
            "go right":self.Library
        }

        while(self.__position == "MainHallway_21"):
            self.GetCommand(__localComDict)

            self.UpdateGCD_inv()

    def Library(self):              
        self.__position = "library"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n LIBRARY\n")
        print(Style.RESET_ALL+ " This is the biggest private library you have ever seen. There are seven frames on the wall. Six are containing\n portraits of men and women, the last one is empty. There are so many books that the bookcases curve under")
        print(" their weight. However, some of them stand out more than others. For example the book exceeding in both size\n and color, is", Fore.MAGENTA+ "an emerald book", Style.RESET_ALL+ "at the very top of a bookcase, right under the ceiling. There is no way")
        print(" you can reach it without an aid. Then there is a smaller", Fore.MAGENTA+ "golden book", Style.RESET_ALL+ "that is within your reach.")

        # Golden book
        def LookAtGoldenBook():
            print(" You take the golden book from the shelve, nearby books immidiately filling its place. The book sure looked\n interesting, but is't empty. You put it back on the shelf.")

        # Emerald book
        def UseLadder():
            print(" You put the ladder carefuly on the ground and lean the other side on the bookcase, where the emerald book is.")

            self.__used.append("ladder")

        def LookAtEmeraldBook_1():
            print(" The emerald book is an encyclopedia, but surprisingly light, cosidering its size. So you climb down\n the ladder, open the book and find the center of the book missing.\n There is", Fore.YELLOW+ "a COIN", Style.RESET_ALL+ "in an carved out square instead of the pages.")

            __localComDict["look at coin"] = Coin_Book
            __localComDict["take coin"] = "book coin"

        def LookAtEmeraldBook_2():
            print(" The book is empty.")

        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_21,
            "look at golden book":LookAtGoldenBook
        }

        def UpdateLCD():
            if("ladder" in self.__inv):
                __localComDict["use ladder"] = UseLadder

            if("ladder" in self.__used):
                __localComDict.pop("use ladder", None)
                __localComDict["look at emerald book"] = LookAtEmeraldBook_1

            if("book coin" in self.__inv):
                __localComDict.update({"look at emerald book":LookAtEmeraldBook_2})
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)

        while(self.__position == "library"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def Terrace(self):              
        self.__position = "terrace"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n TERRACE\n")
        print(Style.RESET_ALL+ " You step on the terrace and immediately start to shiver. Cold wind welcomes you outside together with\n the rustling of fourteen bird's wings. You look around the corner to see a dovecote with", Fore.MAGENTA+ "pigeons.", Style.RESET_ALL)
        print(" One of them has a rolled up piece of paper attached to his leg.")

        # Pigeon
        def CatchPigeon_1():
            print(" You can't reach the pigeons. They are too high and won't come down.")

        def CatchPigeon_2():
            __attempt = 0

            while(__attempt < 2):
                print(" You slowly approach the pigeons and with one swift movement catch one of them...")
                sleep(2)
                print(" But it is not the right one. Try again.")

                acts = ["catch pigeon", "take pigeon"]
                ActCompare(acts)

                __attempt += 1
                
            print(" You slowly approach the pigeons and with one swift movement catch one of them...")
            sleep(2)
            print(" A note is hanging from his leg! Third one's the charm, right?\n\n You notice, that the box is nearly empty by now, so you take the note, let the pigeon go\n and decide to not bother them again.")

            self.__invIn("pigeon note")

        def UseBoxWithSeeds():
            print(" You put the box with seeds on the ground under the dovecote and step aside...")
            sleep(3)
            print(" It doesn't take long and the pigeons, one by one, fly down and start devouring the seeds.\n You have to act quickly, it won't take long and they will be back in their dovecote\n and out of your reach.")

            self.__used.append("box with seeds")

            __localComDict.update({"catch pigeon":CatchPigeon_2})
            __localComDict.update({"look at pigeon":CatchPigeon_2})

        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_21,
            "catch pigeon":CatchPigeon_1,
            "take pigeon":CatchPigeon_1,
            "look at pigeon":CatchPigeon_1,
            "use box with seeds":UseBoxWithSeeds
        }

        def UpdateLCD():
            if("box with seeeds" in self.__inv):
                __localComDict["use box with seeds"] = UseBoxWithSeeds
            elif(("box with seeds" in self.__used) and ("pigeon note" not in self.__inv)):
                __localComDict.update({"catch pigeon":CatchPigeon_2})
                __localComDict.update({"look at pigeon":CatchPigeon_2})
            elif("pigeon note" in self.__inv):
                __localComDict.pop("use box with seeds", None)
                __localComDict.pop("catch pigeon", None)
                __localComDict.pop("take pigeon", None)

        while(self.__position == "terrace"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def MainHallway_22(self):       
        self.__position = "main hallway upstairs"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY UPSTAIRS\n")
        print(Style.RESET_ALL+ " It is colder here, than it was downstairs. The stairs that took you upstairs are on your left. Opposite to them\n is a door. There are some doors in the hallway further away from you and glass doors down\n the hallway behind you.")

        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_21,
            "go straight":self.MainHallway_23,
            "go left":self.Stairs_2,
            "go right":self.Bathroom_2
        }

        while(self.__position == "main hallway upstairs"):
            self.GetCommand(__localComDict)

            self.UpdateGCD_inv()

    def Stairs_2(self):             
        self.__position = "Stairs_2"

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n STAIRS\n")
        print(Style.RESET_ALL+ " You stand in front of the stairs to the first floor and next to them is a steel ladder that leads to\n an opening in the ceiling.")

        def TakeLadder():
            print(" The ladder is drilled to the place. You can't take it.")

        #Local dictionary
        __localComDict = {
            "go down":self.MainHallway_12,
            "go up":self.Attic,
            "go back":self.MainHallway_22,
            "take ladder":TakeLadder
        }

        while(self.__position == "Stairs_2"):
            self.GetCommand(__localComDict)

            self.UpdateGCD_inv()

    def Bathroom_2(self):           
        self.__position = "bathroom upstairs"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n BATHROOM UPSTAIRS\n")
        print(Style.RESET_ALL+ " This is the largest bathroom you have ever seen... There is a white-ish victorian", Fore.MAGENTA+ "bathtub", Style.RESET_ALL+ "across from you\n situated before a French window with a torn curtain. On your left is", Fore.MAGENTA+ "a mirror", Style.RESET_ALL+ "big enough")
        print(" to cover the space between the floor and ceiling missing only a few centimetres. On your right\n is a small room with opened door and a toilet inside. Next to it, in the middle of the wall,")
        print(" is a washstand with another smaller mirror. There are some bathroom cabinets scattered across the floor.")
        
        # Mirror
        def LookAtMirror():
            print(" You look at the mirror and there seems to be nothing out of ordinary.")

        def OpenMirror():
            print(" You suddenly remebered the crazed sentences appearing in the bathroom downstairs and out of a pure\n curiosity, you try to open the big mirror. You pull it from the side.")
            PressEnter()
            print("\n ...")
            sleep(2)
            print("\n And it doesn't move a bit.\n\n You try the opposite side and to your surprise, there is a small handle,\n so you pull again and the mirror opens revealing it is a door from the other side.")

            __localComDict.pop("open mirror", None)
            __localComDict["go left"] = self.Bedroom

        # Bathtub
        def LookAtBathtub_1():
            print(" There is only a soap in the bathtub and", Fore.MAGENTA+ "a small puddle of water.", Style.RESET_ALL+"\n\n Soap from which is sticking out", Fore.MAGENTA+ "a key!", Style.RESET_ALL)

            __localComDict["look at key"] = LookAtKey

        def LookAtBathtub_2():
            print(" There is only the small puddle of water in the bathtub.")

        # Key
        def LookAtKey():
            print(" The key is stuck inside of the soap. You won't be able to use it this way.")

            __localComDict["use water"] = UseWater
            __localComDict["use puddle"] = UseWater
            __localComDict["use puddle of water"] = UseWater

        def UseWater():
            print(" You begin to rub the soap in the water and after what feels like a century, you manage\n to get rid of most of the soap that has been covering the key.")

            __localComDict.pop("use water", None)
            __localComDict.pop("use puddle", None)
            __localComDict.pop("use puddle of water", None)
            
            __localComDict.update({"look at key":Key_Soap})
            __localComDict["take key"] = "soap key"


        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_22,
            "look at mirror":LookAtMirror,
            "look at bathtub":LookAtBathtub_1,
            "open mirror":OpenMirror
        }

        def UpdateLCD():
            if("bedroom" in self.__map):
                __localComDict.pop("open mirror", None)
                __localComDict["go left"] = self.Bedroom

            if(("soap key" in self.__inv) or ("soap key" in self.__used)):
                __localComDict.update({"look at bathtub":LookAtBathtub_2})
                __localComDict.pop("look at key", None)
                __localComDict.pop("take key", None)

        while(self.__position == "bathroom upstairs"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def MainHallway_23(self):       
        self.__position = "MainHallway_23"

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY UPSTAIRS\n")
        print(Style.RESET_ALL+ " There are doors on you left and your right. While the cold night air is making you shiver, you are looking\n through a broken window at the forrest outside. It looks menacing and neverending")
        print(" because of its tall conifers with long arm-like branches.")

        def LockedDoorBedroom():
            print(" You grab the door handle and try to open the door, but you can't. It is probably locked.")

        def LockedDoorChildren():
            print(" You grab the door handle and try to open the door, but you can't. It is probably locked.\n There is a toy carved in to the wooden door.")

        def UseKey():
            self.UnlockedDoor()
            self.__used.append("swing key")

        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_22,
            "go left":LockedDoorChildren,
            "go right":LockedDoorBedroom
        }

        def UpdateLCD():
            if("swing key" in self.__inv):
                __localComDict["use swing key"] = UseKey

            elif("swing key" in self.__used):
                __localComDict.pop("use swing key", None)
                __localComDict.update({"go left":self.ChildrensRoom})

        while(self.__position == "MainHallway_23"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def ChildrensRoom(self):        
        self.__position = "childrens room"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n CHILDREN'S ROOM\n")
        print(Style.RESET_ALL+ " In this room is everything twice... Two beds, two desks and chairs and two sets of toys. On the right side are\n mostly cars, on the other side are dolls. Some of them are missing eyes, some limbs")
        print(" and two of them are missing their entire head. However you notice, that one", Fore.MAGENTA+ "doll,", Style.RESET_ALL+ "in particular, is watching\n you intently.")

        # Doll
        def LookAtDoll_1():
            print(" You take the doll and examine it properly. There is something sparkling in the place, where she\n used to have an eye.")

        def LookAtDoll_2():
            print(" The doll sits on the bed, with its head on the lap.\n She doesn't look pleased...")

        def UsePocketKnife():
            print(" You cut the doll's head off and find", Fore.YELLOW+ "a COIN!", Style.RESET_ALL+ "You destroyed the pocket knife, though.\n It was a hard material.")

            self.__used.append("pocket knife")

            __localComDict["look at coin"] = Coin_Doll
            __localComDict["take coin"] = "doll coin"


        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_23,
            "look at doll":LookAtDoll_1
        }

        def UpdateLCD():
            if("pocket knife" in self.__inv):
                __localComDict["use pocket knife"] = UsePocketKnife
            elif("pocket knife" in self.__used):
                __localComDict.update({"look at doll":LookAtDoll_2})
                __localComDict.pop("use pocket knife", None)

            if("doll coin" in self.__inv):
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)

        while(self.__position == "childrens room"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()

    def Bedroom(self):              
        self.__position = "bedroom"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n BEDROOM\n")
        print(Style.RESET_ALL+ " The dominant of the room was a huge branch sticking out of the wall from outside covering a double bed and\n a nightstand. In fact, it was covering most of the room and blocking the bedroom door. While inspecting")
        print(" the branch, you notice an abandoned", Fore.MAGENTA+ "nest", Style.RESET_ALL+ "between leaves on a smaller branch growing from the main one.")

        def LookAtNest_1():
            print(" You pull down the smaller branch, and to your surprise, there is", Fore.YELLOW+ "a COIN!", Style.RESET_ALL)

            __localComDict["look at coin"] = Coin_Nest
            __localComDict["take coin"] = "nest coin"

        def LookAtNest_2():
            print(" The nest is empty.")

        # Local dictionary
        __localComDict = {
            "go back":self.Bathroom_2,
            "look at nest":LookAtNest_1
        }

        def UpdateLCD():
            if("nest coin" in self.__inv):
                __localComDict.update({"look at nest":LookAtNest_2})
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)

        while(self.__position == "bedroom"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()


    # Roof
    def Attic(self):                
        self.__position = "attic"
        self.MapIn()

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n ATTIC\n")
        print(Style.RESET_ALL+ " You climb the steel ladder up to the attic. The room is quite long with a ceiling copying the shape\n of the roof. Light comes in only throught the opening in the floor. There is a lot of junk, broken items,")
        print(" piles of boxes and cracked nuts and cones... There is one thing that doesn't fit in this place,\n a small wooden", Fore.MAGENTA+ "chest.", Style.RESET_ALL)

        # Costume
        def LookAtCostume_1():
            print(" There is one golden feather.\n You look under it and you find", Fore.YELLOW+ "a COIN!", Style.RESET_ALL)

            __localComDict["look at coin"] = Coin_Costume
            __localComDict["take coin"] = "costume coin"

        def LookAtCostume_2():
            print(" You can see your hand prints on the costume, but otherwise it's as clean as ever.")

        # Chest
        def LookAtChest_1():
            print(" When you step closer, suddenly one of the boxes falls down and you see a squirel running away\n from you to the other side of the attic. You must have scared it. The same way it has scared you.")
            print(" You notice clean white", Fore.MAGENTA+ "costume wings", Style.RESET_ALL+ "shining among the dirt and dust in this place, where the box used to be.\n\n You take", Fore.MAGENTA+ "the chest", Style.RESET_ALL+ "and inspect it. In spite of the dusty enviroment, it is surprisingly clean.\n Also, it is not locked, so you are free to open it.")

            __localComDict["open chest"] = OpenChest
            __localComDict["look at wings"] = LookAtCostume_1
            __localComDict["look at costume wings"] = LookAtCostume_1

        def LookAtChest_2():
            print(" The chest is opend and empty.", Fore.MAGENTA+ "The costume wings", Style.RESET_ALL+ "are few boxes away.")

        def OpenChest():
            print(" You open the chest and there is", Fore.MAGENTA+ "a key", Style.RESET_ALL+ "lying on the soft velvet padding.")

            __localComDict["look at key"] = Key_Chest
            __localComDict["take key"] = "chest key"

        # Local dictionary
        __localComDict = {
            "go back":self.Stairs_2,
            "look at chest":LookAtChest_1
        }

        def UpdateLCD():
            if("costume coin" in self.__inv):
                __localComDict.update({"look at wings":LookAtCostume_2})
                __localComDict.update({"look at costume wings":LookAtCostume_2})
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)

            if(("chest key" in self.__inv) or ("chest key" in self.__used)):
                __localComDict.update({"look at chest":LookAtChest_2})
                __localComDict.pop("open chest", None)
                __localComDict.pop("take key", None)
                __localComDict.pop("look at key", None)

                if("costume coin" not in self.__inv):
                    __localComDict["look at wings"] = LookAtCostume_1
                    __localComDict["look at costume wings"] = LookAtCostume_1
                else:
                    __localComDict.update({"look at wings":LookAtCostume_2})
                    __localComDict.update({"look at costume wings":LookAtCostume_2})
                    __localComDict.pop("look at coin", None)
                    __localComDict.pop("take coin", None)

        while(self.__position == "attic"):
            UpdateLCD()
            self.GetCommand(__localComDict)
            UpdateLCD()

            self.UpdateGCD_inv()