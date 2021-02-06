from script import blocker
from souborSFunkciCteniSouboru import readfile

def main():
	blocked_websites=readfile()
	blocker(blocked_websites)

if __name__=="__main__":
	main()