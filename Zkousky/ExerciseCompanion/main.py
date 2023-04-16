from os.path import join, dirname, realpath

from modules import Rep, Exercise,Training, TrainingDiary

if __name__ == "__main__":
    r1 = Rep("12 x 100 kg")
    print(r1)
    e1 = Exercise("Benchpress")
    e1.addRep(r1)
    print(e1)
    t1 = Training("3.1.2023\nBench press(3)\n12 x 60 kg\n10 x 70 kg\n6 x 85 kg\nCable crossover(2)\n12 x 40 kg\n12 x 35 kg")
    print(t1)
    d = TrainingDiary(join(dirname(realpath(__file__)), "diary.txt"))
    d.addTraining(t1)
    print(d)
    d.printPersonalBest()
