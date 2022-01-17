import queue
import time
from threading import Thread


exitFlag = False


class Sniffer(Thread):

    def __init__(self, id, q):
        super().__init__()
        self.id = id
        self.q = q
        print(f"{id}: Sniffer vytvoren")

    def run(self):
        print(f"{self.id} spousteni ... ")
        self.snif()
        print(f"{self.id}: ukoncuji se...")

    def snif(self):
        i = 0
        while True:
            self.q.put(i)
            i += 1
            time.sleep(1)
            if exitFlag:
                break


class GUI(Thread):
    def __init__(self, id, q):
        super().__init__()
        self.id = id
        self.q = q
        print(f"{id}: Sniffer vytvoren")

    def run(self):
        print(f"{self.id} spousteni ... ")
        self.launchGUI()
        print(f"{self.id}: ukoncuji se...")

    def launchGUI(self):
        while True:
            try:
                item = self.q.get(timeout=0.1)
                print(f"Item {item}")
            except queue.Empty:
                print(f"No item in que")
                pass
            if exitFlag:
                break


if __name__ == "__main__":

    workQueue = queue.Queue()
    gui = GUI(1, workQueue)
    gui.start()
    ids = [1]
    sniffers = []

    for id in ids:
        sniffer = Sniffer(id, workQueue)
        sniffer.start()
        sniffers.append(sniffer)

    time.sleep(5)

    exitFlag = True

    for sniffer in sniffers:
        sniffer.join()

    gui.join()
    print("Exiting Main Thread")
