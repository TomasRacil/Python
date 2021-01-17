import argparse
def argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", metavar="level", type=int,
                        help="Vrací hodnotu obtiznosti 1-3")
    args = parser.parse_args()
    answer = int(args.l)
    if(answer<1 or answer>3 ):
        print("Zvolili jste spatnou variantu, byla automaticky zvolena obtiznost 1")
        return 1
    else:
        return answer

