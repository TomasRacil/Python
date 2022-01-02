# External import
from colorama import Fore, Style
from time import sleep

# Internal import
from Functions import *
from intro import ActCompare


class Croom:
    def __init__(self, name, inv, map, used):
        self.__name = name
        self.inv = inv
        self.map = map
        self.used = used

        self.__position = "MainHallway_11"
        
        self.__globalComDict = {
            "help":         PrintHelp,
            "exit":         self.ExitFct,
            "inventory":    self.PrintInv,
            "map":          self.PrintMap,

            "read invitation letter": Letter_Invitation,
            "read mailbox note":      Note_Mailbox,

            "go to front porch": self.FrontPorch,
            "go to main hallway downstairs": self.MainHallway_11
        }

        self.UpdateGCD_map()
        self.UpdateGCD_inv()


    # System functions
    def ExitFct(self):          # D
        self.__position = "exit"
    
    def PrintInv(cls):
        __invStr = "".join([" " + __thing + "," for __thing in cls.inv])
        __invStr = __invStr.rstrip(",")

        print(Fore.YELLOW+ "------------------------------------------------------------------------\n INVENTORY\n")
        print(Style.RESET_ALL+ f"{__invStr}")
        print(Fore.YELLOW+ "------------------------------------------------------------------------")
        print(Style.RESET_ALL)

    def PrintMap(cls):
        __mapStr = "".join([" " + __place + "," for __place in cls.map])
        __mapStr = __mapStr.rstrip(",")

        print(Fore.YELLOW+ "------------------------------------------------------------------------\n MAP\n")
        print(Style.RESET_ALL+ f"{__mapStr}")
        print(Fore.YELLOW+ "------------------------------------------------------------------------")
        print(Style.RESET_ALL)

    def UpdateGCD_map(self):    # D
        # Underground
        if(("cellar" in self.map) and ("go to cellar" not in self.__globalComDict)):    self.__globalComDict["go to cellar"] = self.Cellar
        
        # First floor
        if(("workroom" in self.map)            and ("go to workroom" not in self.__globalComDict)):            self.__globalComDict["go to workroom"] = self.WorkRoom
        if(("kitchen" in self.map)             and ("go to kitchen" not in self.__globalComDict)):             self.__globalComDict["go to kitchen"] = self.Kitchen
        if(("dining room" in self.map)         and ("go to dining room" not in self.__globalComDict)):         self.__globalComDict["go to dining room "] = self.DiningRoom
        if(("pantry" in self.map               and ("go to pantry" not in self.__globalComDict))):             self.__globalComDict["go to pantry"] = self.Pantry
        if(("bathroom downstairs" in self.map) and ("go to bathroom downstairs" not in self.__globalComDict)): self.__globalComDict["go to bathroom downstairs"] = self.Bathroom_1
        if(("winter garden" in self.map        and ("go to winter garden" not in self.__globalComDict))):      self.__globalComDict["go to winter garden"] = self.WinterGarden
        if(("garden" in self.map)              and ("go to garden" not in self.__globalComDict)):              self.__globalComDict["go to garden"] = self.Garden
        if(("shed" in self.map)                and ("go to shed" not in self.__globalComDict)):                self.__globalComDict["go to shed"] = self.Shed
        if(("playground" in self.map)          and ("go to playground" not in self.__globalComDict)):          self.__globalComDict["go to playground"] = self.Playground
        if(("gazebo" in self.map)              and ("go to gazebo" not in self.__globalComDict)):              self.__globalComDict["go to gazebo"] = self.Gazebo
        
        # Second floor
        if(("main hallway upstairs" in self.map) and ("go to main hallway upstairs" not in self.__globalComDict)): self.__globalComDict["go to main hallway upstairs"] = self.MainHallway_22
        if(("library" in self.map)               and ("go to library" not in self.__globalComDict)):               self.__globalComDict["go to library"] = self.Library
        if(("terrace" in self.map)               and ("go to terrace" not in self.__globalComDict)):               self.__globalComDict["go to terrace"] = self.Terrace
        if(("bathroom upstairs" in self.map)     and ("go to bathroom upstairs" not in self.__globalComDict)):     self.__globalComDict["go to bathroom upstairs"] = self.Bathroom_2
        if(("childrens room" in self.map)        and ("go to childrens room" not in self.__globalComDict)):        self.__globalComDict["go to childrens room"] = self.ChildrensRoom
        if(("bedroom" in self.map)               and ("go to bedroom" not in self.__globalComDict)):               self.__globalComDict["go to bedroom"] = self.Bedroom

        # Roof
        if(("attic" in self.map) and ("go to attic" not in self.__globalComDict)): self.__globalComDict["go to attic"] = self.Attic

    def UpdateGCD_inv(self):
        # Letters
        if(("fridge letter" in self.inv) and ("read fridge letter" not in self.__globalComDict)): self.__globalComDict["read fridge letter"] = Letter_Fridge
        if(("pigeon note" in self.inv)   and ("read pigeon note" not in self.__globalComDict)):   self.__globalComDict["read pigeon note"] = Note_Pigeon
        if(("book letter" in self.inv)   and ("read book letter" not in self.__globalComDict)):   self.__globalComDict["read book letter"] = Letter_Book

        # Keys
        if(("table key" in self.inv) and ("look at table key" not in self.__globalComDict)): self.__globalComDict["look at table key"] = Key_Table
        else: self.__globalComDict.pop("look at table key", None)

        if(("chest key" in self.inv) and ("look at chest key" not in self.__globalComDict)): self.__globalComDict["look at chest key"] = Key_Chest
        else: self.__globalComDict.pop("look at chest key", None)

        if(("soap key" in self.inv) and ("look at soap key" not in self.__globalComDict)): self.__globalComDict["look at soap key"] = Key_Soap
        else: self.__globalComDict.pop("look at soap key", None)

        if(("safe key" in self.inv)  and ("look at safe key" not in self.__globalComDict)):  self.__globalComDict["look at safe key"] = Key_Safe
        else: self.__globalComDict.pop("look at safe key", None)

        if(("swing key" in self.inv) and ("look at swing key" not in self.__globalComDict)): self.__globalComDict["look at swing key"] = Key_Swing
        else: self.__globalComDict.pop("look at swing key", None)

        # Coins
        if(("fridge coin" in self.inv) and ("look at fridge coin" not in self.__globalComDict)): self.__globalComDict["look at fridge coin"] = Coin_Fridge
        else: self.__globalComDict.pop("look at fridge coin", None)
        
        if(("vase coin" in self.inv) and ("look at vase coin" not in self.__globalComDict)): self.__globalComDict["look at vase coin"] = Coin_Vase
        else: self.__globalComDict.pop("look at vase coin", None)
        
        if(("medicine bottle coin" in self.inv) and ("look at medicine bottle coin" not in self.__globalComDict)): self.__globalComDict["look at medicine bottle coin"] = Coin_MedicineBottle
        else: self.__globalComDict.pop("look at medicine bottle coin", None)
        
        if(("safe coin" in self.inv) and ("look at safe coin" not in self.__globalComDict)): self.__globalComDict["look at safe coin"] = Coin_Safe
        else: self.__globalComDict.pop("look atsafe coin ", None)
        
        if(("doll coin" in self.inv) and ("look at doll coin" not in self.__globalComDict)): self.__globalComDict["look at doll coin"] = Coin_Doll
        else: self.__globalComDict.pop("look at doll coin", None)
        
        if(("trophy coin" in self.inv) and ("look at trophy coin" not in self.__globalComDict)): self.__globalComDict["look at trophy coin"] = Coin_Trophy
        else: self.__globalComDict.pop("look at trophy coin", None)
        
        if(("nest coin" in self.inv) and ("look at nest coin" not in self.__globalComDict)): self.__globalComDict["look at nest coin"] = Coin_Nest
        else: self.__globalComDict.pop("look at nest coin", None)
        
        if(("sandbox coin" in self.inv) and ("look at sandbox coin" not in self.__globalComDict)): self.__globalComDict["look at sandbox coin"] = Coin_Sandbox
        else: self.__globalComDict.pop("look at sandbox coin", None)
        
        if(("rag coin" in self.inv) and ("look at rag coin" not in self.__globalComDict)): self.__globalComDict["look at rag coin"] = Coin_Rag 
        else: self.__globalComDict.pop("look at rag coin", None)
        
        if(("book coin" in self.inv) and ("look at book coin" not in self.__globalComDict)): self.__globalComDict["look at book coin"] = Coin_Book
        else: self.__globalComDict.pop("look at book coin", None)

    def GetCommand(cls, localComDict):  # D
        while(True):
            __command = input(Fore.MAGENTA+ "\n I choose action: ")
            print(Style.RESET_ALL)

            # Article control
            if(__command.lower().find(" the ") != (-1)):
                __command = __command.replace("the ", "")
            elif(__command.lower().find(" a ") != (-1)):
                __command = __command.replace("a ", "")
            elif(__command.lower().find(" an ") != (-1)):
                __command = __command.replace("an ", "")

            # Global command dictionary    
            if(__command in cls.__globalComDict):
                return cls.__globalComDict.get(__command)()

            # Local command dictionary
            elif(__command in localComDict):
                if(__command.find("take") != (-1)):
                    cls.InvIn(localComDict.get(__command))
                elif(__command.find("use") != (-1)):
                    if(__command.find("coin") != (-1)):
                        pass
                    else:
                        cls.InvOut(__command)
                    return localComDict.get(__command)()
                else:
                    return localComDict.get(__command)()

            # Command not found error
            else:
                print(Fore.RED+ "\n YOU CAN NOT DO THAT")
                print(Style.RESET_ALL)

    def InvIn(self, item):      # D
        if(item not in self.inv):
            self.inv.append(item)
            self.UpdateGCD_inv()
            print(f"\n You took the {item}.\n")

    def InvOut(self, command):  # D
        command = command.replace("use ", "")
        try:
            self.inv.remove(command)
            self.UpdateGCD_inv()
        except:
            pass

    def MapIn(self):            # D
        if(self.__position not in self.map):
            self.map.append(self.__position)
            self.UpdateGCD_map()

    def LockedDoor(self):       # D
        print("\n You grab the door handle and try to open the door, but you can't. It is probably locekd.\n")

    def UnlockedDoor(self):     # D
        print(" You have unlocked the door.")

    # Underground
    def Cellar(self):           # DC
        self.__position = "cellar"
        self.MapIn()

        def UseFlashlight():
            print(" When you switch on the flashlight, a cone of light illuminates your surroundings. The cellar looks like\n a workshop. There are many various tools, tables and shelves, but only one table has a drawer.")
            print(" There is also a basket in one corner of the cellar.")

            self.InvIn("flashlight")

            __localComDict["look at drawer"] = OpenDrawer_1
            __localComDict["open drawer"] = OpenDrawer_1
            __localComDict["look at basket"] = LookAtBasket_1

        # Drawer
        def OpenDrawer_1():
            print(" You come to the drawer and try to tug on its handle.\n\n Nothing happens. So you pull on it with all your strength and stumble back, when the drawer abruptly\n flies open, uncovering a pair of pliers.")

            __localComDict["take pliers"] = "pliers"

        def OpenDrawer_2():
            print(" The drawer is empty.")

        #Basket
        def LookAtBasket_1():
            print(" You look inside of the basket and spot a COIN resting on a white rag!")

            __localComDict["look at coin"] = Coin_Rag
            __localComDict["take coin"] = "rag coin"

        def LookAtBasket_2():
            print(" There is only the white rag in the basket.")

        # Local dictionary
        __localComDict = {
            "go back":self.Stairs_1
        }

        def UpdateLCD():
            if(("flashlight" in self.inv) and ("open drawer" not in __localComDict)):
                __localComDict["use flashlight"] = UseFlashlight

            if("pliers" in self.inv):
                __localComDict.update({"open drawer":OpenDrawer_2})
                __localComDict.pop("look at drawer", None)
                __localComDict.pop("take pliers", None)

            if("rag coin" in self.inv):
                __localComDict.update({"look at basket":LookAtBasket_2})
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n CELLAR\n")
        print(Style.RESET_ALL+ " As you go down the stairs to the cellar, the light around you is slowly retreating. In the end, the darkness\n consumes you whole. It is strangely quiet in here. It feels as if you have sunk with closed eyes under water.")
        print(" You just stand there for a while doing nothing, but then you snap determined to continue your adventure.\n You are in a great need of light, though.")

        while(self.__position == "cellar"):
            UpdateLCD()
            self.GetCommand(__localComDict)


    # First floor
    def FrontPorch(self):       # DC
        self.__position = "front porch"

        def LookAtMailbox():
            print(" There is no other note in the mailbox.")

        # Local dictionary
        __localComDict = {
            "go straight":self.MainHallway_11,
            "look at mailbox":LookAtMailbox
        }


        # Description
        print(Fore.YELLOW+ "\n---------------------------------------------------------------------------------------------------------------\n FRONT PORCH\n")
        print(Style.RESET_ALL+ " And here you are, standing on the front porch of the old house once again. Its distinct sound never changes.\n Although the creaking of planks under your feet combined with the sounds of the Grey Forest nearby")
        print(" still gives you an unsettling feeling, it doesn't seem so haunting anymore. The mailbox and the doorbell are\n still the same. As you reach out for the doorknob, the massive wooden door open\n for you on its own accord.\n\n The only thing left for you to do, is to step into the warm yellow welcomming light that awaits you.")

        while(self.__position == "front porch"):
            self.GetCommand(__localComDict)

    def MainHallway_11(self):   # DC
        self.__position = "MainHallway_11"

        def UseKey():
            self.UnlockedDoor()
            self.used.append("table key")

        # Local dictionary
        __localComDict = {
            "go back":self.FrontPorch, 
            "go straight":self.MainHallway_12,
            "go left":self.LockedDoor
        }

        def UpdateLCD():
            if("table key" in self.used):
                __localComDict.update({"go left":self.WorkRoom})
            elif("table key" in self.inv):
                __localComDict["use table key"] = UseKey


        # Description
        print(Fore.YELLOW+      "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY\n")
        print(Style.RESET_ALL+  " You can see several doors. One currently on your left and two at the back of the Main hallway. In the middle,\n there is another hallway crossing the main one. You can not see where it leads from your position.")

        while(self.__position == "MainHallway_11"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def WorkRoom(self):         # DC
        self.__position = "workroom"
        self.MapIn()

        # Desk
        def LookAtDesk():
            print(" There are long, deep unusual scratch markes on the desk as well as on the office chair. They seem almost\n unhuman and growing in length and numbers as the time passes. Some of them are even shaped")
            print(" like numbers. Next to them lies practicly intackt statue of what looks like a human.")

            __localComDict["look at statue"] = LookAtStatue

        # Statue
        def LookAtStatue():
            print(" The golden statue looks like a man, an older gentleman, to be precise. His walking stick is pointing toward\n a painting on the wall. You would bet anything, that just a second ago, it was ponting to his feet.\n ...")
            sleep(3)
            print(" Weird.")

            __localComDict["look at painting"] = LookAtPainting

        # Painting
        def LookAtPainting():
            print(" It is a crooked painting of a landscape depicting a meadow connected to the forest in the back. The sun is\n setting behind the trees. It would be a beautiful painting, if it wasn't for the dust")
            print(" and scratches all over it. As you walk closer, you can see there is something beneath it. You move the painting\n to the side and see a safe.")

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
                print(" There is a COIN! And far in the back lies a key.")

                __localComDict["look at coin"] = Coin_Safe
                __localComDict["take coin"] = "safe coin"
                __localComDict["look at key"] = Key_Safe
                __localComDict["take key"] = "safe key"

            else:
                print(" The entered code is wrong.\n Try again or look for more clues.")

        def OpenSafe_2():
            print(" The safe is opend and far in the back lies a key.")

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
            if(("safe key" in self.inv) or ("safe key" in self.used)):
                __localComDict.pop("look at key", None)
                __localComDict.pop("take key", None)

                if("safe coin" in self.inv):
                    __localComDict.update({"open safe":OpenSafe_4})
                    __localComDict.pop("look at coin", None)
                    __localComDict.pop("take coin", None)
                else:
                    __localComDict.update({"open safe":OpenSafe_3})
                    __localComDict["look at coin"] = Coin_Safe
                    __localComDict["take coin"] = "safe coin"
            
            else:
                if("safe coin" in self.inv):
                    __localComDict.update({"open safe":OpenSafe_2})
                    __localComDict.pop("look at coin", None)
                    __localComDict.pop("take coin", None)


        # Description
        print(Fore.YELLOW+      "\n---------------------------------------------------------------------------------------------------------------\n WORKROOM\n")
        print(Style.RESET_ALL+  " The workroom is a serious looking place. There are piles of paper stocked in every corner of the room.\n Buried under them, you can see an armchair and a desk with an office chair.")

        while(self.__position == "workroom"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def MainHallway_12(self):   # DC
        self.__position = "MainHallway_12"

        # Local dictionary
        __localComDict = {
            "go back":      self.MainHallway_11,
            "go straight":  self.MainHallway_13,
            "go left":      self.Stairs_1,
            "go right":     self.Kitchen
        }


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY\n")
        print(Style.RESET_ALL+ " You leave the place that you were standing on behind you as you proceed to the middle of the main hallway.\n There is an old staircase on your left and hallway, that looks like it leads to the kitchen, on your right.")
        
        while(self.__position == "MainHallway_12"):
            self.GetCommand(__localComDict)

    def Stairs_1(self):         # DC
        self.__position = "Stairs_1"

        def UseKey():
            self.UnlockedDoor()
            self.used.append("chest key")

        # Local dictionary
        __localComDict = {
            "go back":  self.MainHallway_12,
            "go up":    self.MainHallway_22,
            "go down":  self.LockedDoor,
            "go straight": self.LockedDoor
        }

        def UpdateLCD():
            if("chest key" in self.inv):
                __localComDict["use chest key"] = UseKey
            elif("chest key" in self.used):
                __localComDict.update({"go down":self.Cellar})
                __localComDict.update({"go straight":self.Cellar})


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n STAIRS\n")
        print(Style.RESET_ALL+ " You stand in front of the stairs that lead to the second floor and next to them is a door.")

        while(self.__position == "Stairs_1"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def Kitchen(self):          # DC
        self.__position = "kitchen"
        self.MapIn()

        # Cupboard
        def OpenCupboard_1():
            print(" You carefuly open the cupboard door. There are two shelves. On the upper one is a small pocket knife,\n on the lower one are just fragmented dishes.")

            __localComDict["take knife"] = "pocket knife"
            __localComDict["take pocket knife"] = "pocket knife"

        def OpenCupboard_2():
            print(" It's all empty, except for the dirty fragmented dishes.")

        # Fridge
        def LookAtFridge_1():
            print(f" There is a letter pinned to the fridge. Its addressee seems to be you since it has \"{self.__name}\"\n written on top of it.")
            
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
            print(" a COIN!!")

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
            if(("pocket knife" in self.inv) or ("pocket knife" in self.used)):
                __localComDict.update({"open cupboard":OpenCupboard_2})
                __localComDict.pop("take knife", None)
                __localComDict.pop("take pocket knife", None)

            if("fridge letter" in self.inv):
                if("fridge coin" in self.inv):
                    __localComDict.update({"open fridge":OpenFridge_1})
                    __localComDict.pop("look at coin", None)
                    __localComDict.pop("take coin", None)
                else:
                    __localComDict.update({"open fridge":OpenFridge_2})


        # Description
        print(Fore.YELLOW+      "\n---------------------------------------------------------------------------------------------------------------\n KITCHEN\n")
        print(Style.RESET_ALL+  " The kitchen is quite large and it freely passes to a dining room on the left. There is a window covered\n by a torn thin curtain. Under the window is a vintage looking, once white, kitchen unit made of various")
        print(" kitchen cupboards. Some are destroyed more, some less, but there is one, that catches your attention,\n because only this one still has a door. The kitchen unit runs along the wall to the right until it touches")
        print(" a stove. In the middle of the unit on the right is a door. Right next to you\n on the left is a spacious fridge.")

        while(self.__position == "kitchen"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def DiningRoom(self):       # DC
        self.__position = "dining room"
        self.MapIn()

        # Table
        def LookAtTable_1():
            print(" There is a dirty glass vase with a bouquet of dead flowers and a key lying peacefully next to it.")

            __localComDict["look at vase"] = LookAtVase
            __localComDict["look at key"] = Key_Table
            __localComDict["take key"] = "table key"

        def LookAtTable_2():
            print(" There is a dirty glass vase with a bouquet of dead flowers.")

            __localComDict["look at vase"] = LookAtVase

        def LookAtTable_3():
            print(" There is a key lying peacefully among the vase shards.")

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
            print(" to your surprise, a COIN! You breathe out relieved, that you did not break the vase for nothing.")

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
            if(("table key" in self.inv) or ("table key" in self.used)):
                __localComDict.pop("look at key", None)
                __localComDict.pop("take key", None)

                if("vase coin" in self.inv):
                    __localComDict.update({"look at table":LookAtTable_4})
                    __localComDict.pop("look at vase", None)
                    __localComDict.pop("break vase", None)
                    __localComDict.pop("take coin", None)
                    __localComDict.pop("look at coin", None)
                else:
                    __localComDict.update({"look at table":LookAtTable_2})
                    __localComDict["look at vase"] = LookAtVase

            else:
                if("vase coin" in self.inv):
                    __localComDict.update({"look at table":LookAtTable_3})
                    __localComDict["look at key"] = Key_Table
                    __localComDict["take key"] = "table key"


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n DINING ROOM\n")
        print(Style.RESET_ALL+ " You walk up to a spacious room with two of its walls made out of French windows and the third covered by\n a tapestry. You move your gaze from the tapestry to the center of the room where a sturdy mahogany table")
        print(" is situated and surrounded by ten chairs.")  

        while(self.__position == "dining room"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def Pantry(self):           # DC
        self.__position = "pantry"
        self.MapIn()

        def LookAtBarrel():
            print(" It's just a normal barrel full of various seeds. They might be of some use.")

        def TakeBarrel():
            print(" The barrel is too heavy and big.")

        def TakeSeeds():
            print(" You do you want to put the seeds in?")

        def UseBox():
            print(" As you move a little closer to the barrel, a tiny mouse runs out towards you, but changes its mind\n halfway. She then makes two circles around the barrel and disppears under one of the shelves.")
            print(" After this, you are finaly allowed to scoop some seeds into the box.")
            
            self.InvIn("box with seeds")

        # Local dictionary
        __localComDict = {
            "go back": self.Kitchen,
            "look at seeds":  LookAtBarrel,
            "look at barrel": LookAtBarrel,
            "take barrel":  TakeBarrel,
            "take seeds":   TakeSeeds
        }

        def UpdateLCD():
            if("box" in self.inv):
                __localComDict["use box"] = UseBox
            
            if(("box with seeds" in self.inv) or ("box with seeds" in self.used)):
                __localComDict.pop("use box", None)


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n PANTRY\n")
        print(Style.RESET_ALL+ " The pantry is so small, that you can barely fit in it. It is dusky inside, but the omnipresent shelves,\n that exceed you by so much, are difficult not to see. This whole place reeks of mold and rot.")
        print(" It makes you want to throw up. You have to act quickly. You look around and see some rotten apples, a few\n glasses filled with who knows what and a barrel full of seeds.")

        while(self.__position == "pantry"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def MainHallway_13(self):   # DC
        self.__position = "MainHallway_13"

        def UseKey():
            self.UnlockedDoor()
            self.used.append("soap key")

        __localComDict = {
            "go back":self.MainHallway_12,
            "go left":self.Bathroom_1,
            "go straight":self.LockedDoor
        }

        def UpdateLCD():
            if("soap key" in self.used):
                __localComDict.update({"go straight":self.WinterGarden})
            elif("soap key" in self.inv):
                __localComDict["use soap key"] = UseKey


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY\n")
        print(Style.RESET_ALL+ " You are at the back of the Main hallway. There are door on on your left and large glass door in front of you.")

        while(self.__position == "MainHallway_13"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def Bathroom_1(self):       # DC
        self.__position = "bathroom downstairs"
        self.MapIn()

        # Bathroom cabinet
        def OpenBathroomCabinet():
            print(" There are some used toothbrushes, toothpaste and a medicine botlle.")

            __localComDict["open medicine bottle"] = OpenMedicineBottle_1
            __localComDict["open bottle"] = OpenMedicineBottle_1

        # Medicine bottle
        def OpenMedicineBottle_1():
            print(" In the midst of the pills rests a COIN!")

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
            "look at note":LookAtNotes,
            "look at wall":LookAtNotes,
            "look at notes":LookAtNotes,
            "look at walls":LookAtNotes
        }

        def UpdateLCD():
            if("medicine bottle coin" in self.inv):
                __localComDict.update({"open medicine bottle":OpenMedicineBottle_2})
                __localComDict.update({"open bottle":OpenMedicineBottle_2})
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n BATHROOM DOWNSTAIRS\n")
        print(Style.RESET_ALL+ " You hear water under your feet as you step in. There is a shower in one corner and a toilet in the other.\n Any of them particulary clean...\n\n Then there is a wash-basin and above it is a bathroom cabinet with a broken mirror.")
        print(" The thing that disturbs you the most is not the fithiness of this place, athough it's disgusting,\n but the proliferating notes on the walls of the entire bathroom. It's like someone\n out of their mind was scribbling them.\n\n Or were they repeating it to themselves?")

        while(self.__position == "bathroom downstairs"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def WinterGarden(self):     # DC
        self.__position = "winter garden"
        self.MapIn()

        # Flowerpot
        def LookAtFlowerpot_1():
            print(" There is an empty closing box in the floerpot.")

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
            if(("box" in self.inv) or ("box with seeds" in self.inv) or ("box with seeds" in self.used)):
                __localComDict.update({"look at flowerpot":LookAtFlowerpot_2})
                __localComDict.pop("take box", None)


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n WINTER GARDEN\n")
        print(Style.RESET_ALL+ " You step into an unkept, otherwise beautiful, winter garden. There is a fireplace, few chairs, a sofa and\n a coffe table on one side and many gorgeous plants and flowers on the other. There is only one")
        print(" empty flowerpot amongst them.")

        while(self.__position == "winter garden"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def Garden(self):           # DC
        self.__position = "garden"
        self.MapIn()

        # Local dictionary
        __localComDict = {
            "go back":self.WinterGarden,
            "go straight":self.Gazebo,
            "go right":self.Playground,
            "go left":self.Shed
        }


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n GARDEN\n")
        print(Style.RESET_ALL+ " You stand at the intersection of four beaten paths, the house rising behind you. One of the paths leads\n right, one left and the last one goes straight to the forest.")

        while(self.__position == "garden"):
            self.GetCommand(__localComDict)

    def Shed(self):             # DC
        self.__position = "shed"
        self.MapIn()

        def UsePliers():
            print(" You gather all your strength and try to cut the chain with the pliers. It takes you a while,\n but in the end, you manage to do it. With relieve, you throw the dull pliers on the ground")
            print(" along with the chain and padlock.")

            self.used.append("pliers")

            __localComDict.update({"go straight":OpenDoor_2})
            __localComDict.update({"open door":OpenDoor_2})
            __localComDict.update({"open shed":OpenDoor_2})

        def OpenDoor_1():
            print(" You try to open the door of the shed, but they're locked with a strong chain and a padlock.")

        def OpenDoor_2():
            print(" The shed full of garden supplies and other craft tools. There is also a wooden ladder.")

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
            if("pliers" in self.inv):
                __localComDict["use pliers"] = UsePliers

            if("pliers" in self.used):
                __localComDict.update({"go straight":OpenDoor_2})
                __localComDict.update({"open door":OpenDoor_2})
                __localComDict.update({"open shed":OpenDoor_2})

            if("ladder" in self.inv):
                __localComDict.update({"go straight":OpenDoor_3})
                __localComDict.update({"open door":OpenDoor_3})
                __localComDict.update({"open shed":OpenDoor_3})
                __localComDict.pop("take ladder", None)

        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n SHED\n")
        print(Style.RESET_ALL+ " You follow the left path and it leads you to a door of a small garden shed situated by the side of the house.\n A beautiful plane tree is growing next to it.")

        while(self.__position == "shed"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def Playground(self):       # DC
        self.__position = "playground"
        self.MapIn()

        def LookAtSlide():
            print(" It's just an ordinary slide for kids.")

        # Sandbox
        def LookAtSandbox_1():
            print(" There is a sieve lying in the middle of the sandbox.")

            __localComDict["use sieve"] = UseSieve_1

        def UseSieve_1():
            print(" You take the sieve and start sieving the sand in the sandbox little by little, until...")
            sleep(3)
            print(" A COIN has stayed in the sieve!")

            __localComDict["look at coin"] = Coin_Sandbox
            __localComDict["take coin"] = "sandbox coin"

        def UseSieve_2():
            print(" You go through the sandbox again, but without a success this time.")
        
        # Swing
        def LookAtSwing_1():
            print(" The swing is moving on its own accord. You would like to think it's because of the wind, but it is not\n strong enough. Then you notice there is a key on the ground under it!")

            __localComDict["look at key"] = Key_Swing
            __localComDict["take key"] = "swing key"

        def LookAtSwing_2():
            print(" The swing is not moving anymore.")

        # Local dictionary
        __localComDict = {
            "go back":self.Garden,
            "look at sandbox":LookAtSandbox_1,
            "look at swing":LookAtSwing_1,
            "look at swing":LookAtSlide
        }

        def UpdateLCD():
            if(("swing key" in self.inv) or ("swing key" in self.used)):
                __localComDict.update({"look at swing":LookAtSwing_2})
                __localComDict.pop("look at key", None)
                __localComDict.pop("take key", None)

            if("sandbox coin" in self.map):
                __localComDict.update({"use sieve":UseSieve_2})
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n PLAYGROUND\n")
        print(Style.RESET_ALL+ " You follow the path and soon come across a playground. There is a swing, a sandbox and a slide.")

        while(self.__position == "playground"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def Gazebo(self):
        self.__position = "gazebo"
        self.MapIn()
        
        def UseKey():
            self.UnlockedDoor()
            self.used.append("safe key")

        def Inside():
            print(" You step into the gazebo and finally see, what's emmitting the star-like light. It is a golden slot machine!\n\n You can't believe your eyes...")

        def FallThrough():
            print(" The coin fell through the slot machine and jumped out right back at you.")

        def UseCoin(coin):
            print(" ")

        # Local dictionary
        __localComDict = {
            "go back":self.Garden,
            "go straight":self.LockedDoor,
            "open door":self.LockedDoor
        }

        def UpdateLCD():
            __number = 0

            for __item in self.inv:
                if(__item.find("coin")):
                    __number += 1
            
            if(__number == 10):
                __localComDict["use fridge coin"] = UseCoin("fridge coin")


            if("safe key" in self.inv):
                __localComDict["use safe key"] = UseKey
            elif("safe key" in self.used):
                __localComDict.update({"go straight":Inside})
                __localComDict.update({"open door":Inside})
                __localComDict.pop("use safe key", None)


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n GAZEBO\n")
        print(Style.RESET_ALL+ " You let the path lead you. As soon as you step into the forest, you start to have a strange feelig in your\n gut. You try to ignore it and continue walking, passing hight trees and dodging branches,")
        print(" that are trying to touch your shouldres and head as they swing in the wind. You come to a stop, when you\n notice a small glass gazebo, whose golden light shines through the forest,")
        print(" making it look like a star. You close the distance rather quickly, wanting to be in the soothing light again.\n\n You halt in front of the glass door. You can not regognize anything inside, since the image is fuzzy.")

        while(self.__position == "gazebo"):
            UpdateLCD()
            self.GetCommand(__localComDict)


    # Second floor
    def MainHallway_21(self):       # DC
        self.__position = "MainHallway_21"

        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_22,
            "go straight":self.Terrace,
            "go left":self.Terrace,
            "go right":self.Library
        }


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY UPSTAIRS\n")
        print(Style.RESET_ALL+ " You stand at the one end of the hallway. You left the stairs behind you and are now lookig through\n a glass doors, that are in front of you and by your left hand. On your right\n is a standart wooden door.")

        while(self.__position == "MainHallway_21"):
            self.GetCommand(__localComDict)

    def Library(self):              # DC
        self.__position = "library"
        self.MapIn()

        # Golden book
        def LookAtGoldenBook():
            print(f" You take the golden book from the shelve, nearby books immidiately filling its place. The book is\n titled \"Truth behind coins\" and is devoted to {self.__name}. Otherwise it's empty.\n You put it back on the shelf.")

        # Emerald book
        def UseLadder():
            print(" You put the ladder carefuly on the ground and lean the other side on the bookcase, where the emerald book is.")

            self.used.append("ladder")

        def LookAtEmeraldBook_1():
            print(" The emerald book is an encyclopedia, but surprisingly light, cosidering its size. So you climb down\n the ladder, open the book and find the center of the book missing.\n There is a COIN in an carved out square instead of the pages.")

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
            if("ladder" in self.inv):
                __localComDict["use ladder"] = UseLadder

            if("ladder" in self.used):
                __localComDict.pop("use ladder", None)
                __localComDict["look at emerald book"] = LookAtEmeraldBook_1

            if("book coin" in self.inv):
                __localComDict.update({"look at emerald book":LookAtEmeraldBook_2})
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)
                


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n LIBRARY\n")
        print(Style.RESET_ALL+ " This is the biggest private library you have ever seen. There are seven frames on the wall. Six are contain\n portraits of men and women, the last one is empty. There are so many books that the bookcases curve under")
        print(" their weight. However, some of them stand out more than others. For example the book exceeding in both size\n and color, is an emerald book at the very top of a bookcase, right under the ceiling. There is no way")
        print(" you can reach it without an aid. Then there is a smaller golden book that is within your reach.")

        while(self.__position == "library"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def Terrace(self):              # DC
        self.__position = "terrace"
        self.MapIn()

        # Pigeon
        def CatchPigeon_1():
            print(" You can't reach the pigeons. They are too high and won't come down.")

        def CatchPigeon_2():
            __attempt = 0

            while(__attempt < 2):
                print(" You slowly approach the pigeons and with one swift movement catch one of them...")
                sleep(2)
                print(" But it is not the right one. Try again.")

                ActCompare("catch pigeon")

                __attempt += 1
                
            print(" You slowly approach the pigeons and with one swift movement catch one of them...")
            sleep(2)
            print(" A note is hanging from his leg! Third one's the charm, right?\n\n You notice, that the box is nearly empty by now, so you take the note, let the pigeon go\n and decide to not bother them again.")

            self.InvIn("pigeon note")

        def UseBoxWithSeeds():
            print(" You put the box with seeds on the ground under the dovecote and step aside...")
            sleep(3)
            print(" It doesn't take long and the pigeons, one by one, fly down and start devouring the seeds.\n You have to act quickly, it won't take long and they will be back in their dovecote\n and out of your reach.")

            self.used.append("box with seeds")

            __localComDict.update({"catch pigeon":CatchPigeon_2})
            __localComDict.update({"look at pigeon":CatchPigeon_2})

        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_21,
            "catch pigeon":CatchPigeon_1,
            "look at pigeon":CatchPigeon_1,
            "use box with seeds":UseBoxWithSeeds
        }

        def UpdateLCD():
            if("box with seeeds" in self.inv):
                __localComDict["use box with seeds"] = UseBoxWithSeeds
            elif(("box with seeds" in self.used) and ("pigeon note" not in self.inv)):
                __localComDict.update({"catch pigeon":CatchPigeon_2})
                __localComDict.update({"look at pigeon":CatchPigeon_2})
            elif("pigeon note" in self.inv):
                __localComDict.pop("use box with seeds", None)
                __localComDict.pop("catch pigeon", None)


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n TERRACE\n")
        print(Style.RESET_ALL+ " You step on the terrace and immediately start to shiver. Cold wind welcomes you outside together with\n the rustling of fourteen bird's wings. You look around the corner to see a dovecote with pigeons.")
        print(" One of them has a rolled up piece of paper attached to his leg.")

        while(self.__position == "terrace"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def MainHallway_22(self):       # DC
        self.__position = "main hallway upstairs"
        self.MapIn()

        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_21,
            "go straight":self.MainHallway_23,
            "go left":self.Stairs_2,
            "go right":self.Bathroom_2
        }


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY UPSTAIRS\n")
        print(Style.RESET_ALL+ " As you went up, it gradually got colder. The stairs that took you upstairs are on your left. Opposite to them\n is a door. There are some doors in the hallway further away from you and even more of them\n down the hallway behind you.")

        while(self.__position == "main hallway upstairs"):
            self.GetCommand(__localComDict)

    def Stairs_2(self):             # DC
        self.__position = "Stairs_2"

        def TakeLadder():
            print(" The ladder is drilled to the place. You can't take it.")

        #Local dictionary
        __localComDict = {
            "go down":self.MainHallway_12,
            "go up":self.Attic,
            "go back":self.MainHallway_22,
            "take ladder":TakeLadder
        }


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n STAIRS\n")
        print(Style.RESET_ALL+ " You stand in front of the stairs to the first floor and next to them is a steel ladder that leads to\n an opening in the ceiling.")

        while(self.__position == "Stairs_2"):
            self.GetCommand(__localComDict)

    def Bathroom_2(self):           # DC
        self.__position = "bathroom upstairs"
        self.MapIn()
        
        # Mirror
        def LookAtMirror():
            print(" You look at the mirror and there seems to be nothing out of ordinary.")

        def OpenMirror():
            print(" You suddenly remebered the crazed sentences appearing in the bathroom downstairs and out of a pure\n curiosity, you try to open the big mirror. You pull it from the side...")
            sleep(2)
            print(" And it doesn't move a bit.\n\n You try the opposite side and to your surprise, there is a small handle,\n so you pull again and the mirror opens revealing it is a door from the other side.")

            __localComDict.pop("open mirror", None)
            __localComDict["go left"] = self.Bedroom

        # Bathtub
        def LookAtBathtub_1():
            print(" There is only a soap in the bathtub and a small puddle of water.\n\n Soap from which is sticking out a key!")

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
            if("bedroom" in self.map):
                __localComDict.pop("open mirror", None)
                __localComDict["go left"] = self.Bedroom

            if(("soap key" in self.inv) or ("soap key" in self.used)):
                __localComDict.update({"look at bathtub":LookAtBathtub_2})
                __localComDict.pop("look at key", None)
                __localComDict.pop("take key", None)


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n BATHROOM UPSTAIRS\n")
        print(Style.RESET_ALL+ " This is the largest bathroom you have ever seen... There is a white-ish victorian bathtub across from you\n situated before a French window with a torn curtain. On your left is a mirror big enough")
        print(" to cover the space between the floor and ceiling missing only a few centimetres. On your right\n is a small room with opened door and a toilet inside. Next to it, in the middle of the wall,")
        print(" is a washstand with another smaller mirror. There are some bathroom cabinets scattered across the floor.")

        while(self.__position == "bathroom upstairs"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def MainHallway_23(self):       # DC
        self.__position = "MainHallway_23"

        # Local dictionary
        __localComDict = {
            "go back":  self.MainHallway_22,
            "go left":  self.ChildrensRoom,
            "go right": self.LockedDoor
        }


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY UPSTAIRS\n")
        print(Style.RESET_ALL+ " There are doors on you left and your right. While the cold night air is making you shiver, you are looking\n through a broken window at the forrest outside. It looks menacing and neverending")
        print(" because of its tall conifers with long arm-like branches.")

        while(self.__position == "MainHallway_23"):
            self.GetCommand(__localComDict)

    def ChildrensRoom(self):        # DC
        self.__position = "childrens room"
        self.MapIn()

        # Doll
        def LookAtDoll_1():
            print(" You take the doll and examine it properly. There is something sparkling in the place, where she\n used to have an eye.")

        def LookAtDoll_2():
            print(" The doll sits on the bed, with its head on the lap.\n She doesn't look pleased...")

        def UsePocketKnife():
            print(" You cut the doll's head off and find a COIN! You destroyed the pocket knife, though.\n It was a hard material.")

            self.used.append("pocket knife")

            __localComDict["look at coin"] = Coin_Doll
            __localComDict["take coin"] = "doll coin"


        # Local dictionary
        __localComDict = {
            "go back":self.MainHallway_23,
            "look at doll":LookAtDoll_1
        }

        def UpdateLCD():
            if("pocket knife" in self.inv):
                __localComDict["use pocket knife"] = UsePocketKnife
            elif("pocket knife" in self.used):
                __localComDict.update({"look at doll":LookAtDoll_2})
                __localComDict.pop("use pocket knife", None)

            if("doll coin" in self.inv):
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n CHILDREN'S ROOM\n")
        print(Style.RESET_ALL+ " In this room is everything twice... Two beds, two desks and chairs and two sets of toys. On the right side are\n mostly cars, on the other side are dolls. Some of then are missing eyes, some limbs")
        print(" and two of them are missing their entire head. However you notice, that one doll, in particular, is watching\n you intently.")

        while(self.__position == "childrens room"):
            UpdateLCD()
            self.GetCommand(__localComDict)

    def Bedroom(self):              # DC
        self.__position = "bedroom"
        self.MapIn()

        def LookAtNest_1():
            print(" You pull down the smaller branch, and to your surprise, there is a COIN!")

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
            if("nest coin" in self.inv):
                __localComDict.update({"look at nest":LookAtNest_2})
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n BEDROOM\n")
        print(Style.RESET_ALL+ " The dominant of the room was a huge branch sticking out of the wall from outside covering a double bed and a nightstand.\n In fact, it was covering most of the room and blocking the bedroom door. While inspecting the branch,")
        print(" you notice an abandoned nest between leaves on a smaller branch growing from the main one.")

        while(self.__position == "bedroom"):
            UpdateLCD()
            self.GetCommand(__localComDict)


    # Roof
    def Attic(self):                # DC
        self.__position = "attic"
        self.MapIn()

        # Trophy
        def LookAtTrophy_1():
            print(" There is a contour of laurel wreath with number one on the brand new looking trophy.\n You look inside and there is a COIN!")

            __localComDict["look at coin"] = Coin_Trophy
            __localComDict["take coin"] = "trophy coin"

        def LookAtTrophy_2():
            print(" You can see your finger prints on the trophy, but otherwise it's as clean as ever.\n There is nothing inside, anymore.")

        # Chest
        def LookAtChest_1():
            print(" When you step closer, suddenly one of the boxes falls down and you see a squirel running away\n from you to the other side of the attic. You must have scared it. The same way it has scared you.")
            print(" You notice a polished trophy shining among the dirt and dust in this place, where the box used to be.\n\n You take the chest and inspect it. In spite of the dusty enviroment, it is surprisingly clean.\n Also, it is not locked, so you are free to open it.")

            __localComDict["open chest"] = OpenChest
            __localComDict["look at trophy"] = LookAtTrophy_1

        def LookAtChest_2():
            print(" The chest is opend and empty.")

        def OpenChest():
            print(" You open the chest and there is a key lying on the soft velvet padding.")

            __localComDict["look at key"] = Key_Chest
            __localComDict["take key"] = "chest key"

        # Local dictionary
        __localComDict = {
            "go back":self.Stairs_2,
            "look at chest":LookAtChest_1
        }

        def UpdateLCD():
            if("trophy coin" in self.inv):
                __localComDict.update({"look at trophy":LookAtTrophy_2})
                __localComDict.pop("look at coin", None)
                __localComDict.pop("take coin", None)

            if("chest key" in self.inv):
                __localComDict.update({"look at chest":LookAtChest_2})
                __localComDict.pop("open chest", None)
                __localComDict.pop("take key", None)
                __localComDict.pop("look at key", None)


        # Description
        print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n ATTIC\n")
        print(Style.RESET_ALL+ " You climb the steel ladder up to the attic. The room is quite long with a ceiling copying the shape\n of the roof. Light comes in only throught the opening in the floor. There is a lot of junk, broken items,")
        print(" piles of boxes... There is one thing that doesn't fit in this place, a small wooden chest.")

        while(self.__position == "attic"):
            UpdateLCD()
            self.GetCommand(__localComDict)