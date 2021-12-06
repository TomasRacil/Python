def Menu(low, high, plus):
    # Local variables
    choice = 0

    while((choice < low) or (choice > high) and (choice != plus)):
        try:
            choice = int(input("\n  I choose: "))

            # Error when choice is not defined
            if((choice < low) or (choice > high) and (choice != plus)):
                print("\n YOUR CHOICE IS NOT DEFINED\n")
                choice = 0
            # Choice is defined
            else:
             return choice

        except:
            print("\n USE ONLY NUMBERS\n")