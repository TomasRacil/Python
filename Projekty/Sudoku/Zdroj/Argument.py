import argparse
def argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display the square of a given number")
    args = parser.parse_args()
    answer = int(args.square)
    if(answer<1 or answer>3 ):
        print("Zvolili jste spatnou variantu, byla automaticky zvolena obtiznost 1")
        return 1
    else:
        return answer

