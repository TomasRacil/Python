from os.path import dirname, realpath, join, isfile

folder = dirname(dirname(realpath(__file__)))
file = join(folder, 'data.csv')


def csvRead():
    packets = []
    with open(file, 'r') as f:
        for line in f:
            packets.append(line.strip())
    return packets


def csvWrite(packets: list):
    mode = 'a' if isfile(file) else 'w'
    with open(file, mode) as f:
        for packet in packets:
            f.write(str(packet)+'\n')


if __name__ == "__main__":
    csvWrite(['1', '2', '3', '4', '5'])
    print(csvRead())
