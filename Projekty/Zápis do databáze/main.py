from Moduly import Uloz,jsonGetInfo

def main(): 
    data = jsonGetInfo()
    Uloz(data)
    print("Data saved")

if __name__ == '__main__':
	main()
