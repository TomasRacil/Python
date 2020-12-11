import argparse
parser = argparse.ArgumentParser(description="Tohle je napoveda, hm...")
parser.add_argument("-m", metavar="morse", type=str, default="", help="Zde zadate zprávu, která má být převedena do morseovy abecedy")

letters = [ ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]
morseLett = ["  ", ". _", "_ . . .", "_ . _ .", "_ . .", ".", ". . _ .", "_ _ .", ". . . .", ". .", ". _ _ _", "_ . _", ". _ . .",  "_ _", "_ .", "_ _ _", ". _ _ .", "_ _ . _", ". _ .", ". . .", "_", ". . _", ". . . _", ". _ _", "_ . . _", "_ . _ _", "_ _ . .", ". _ _ _ _", ". . _ _ _", ". . . _ _", ". . . . _", ". . . . .", "_ . . . .", "_ _ . . .", "_ _ _ . .", "_ _ _ _ .", "_ _ _ _ _"]
mText = ""

text = parser.parse_args()
text = str(text.m)

if len(text) > 0:
    for letterInput in text:
        for i in range(len(letters)):
            if letterInput.lower() == letters[i]:
                mText += morseLett[i] + " | "
                break
    print(f"Text v Morseove abecede\n  {mText}")

else: print("Nic nebylo zadano.")