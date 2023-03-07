from os.path import realpath, join, dirname

from modules import *

if __name__=="__main__":
    t = Time("2023 1 10 20 53");
    print(t,"\n")

    e = Event("Presentation\n2023 3 2 14 00\n2023 3 2 16 15\nS9A/67\nInformation technology presentation.Complete projects and tasks");
    print(e,"\n")

    c = Calendar("TEST", join(dirname(realpath(__file__)),"events.txt"));
    print(c,"\n")

    c.addEvent(e);

    e1 = Event("Launch\n2023 3 2 12 00\n2023 3 2 13 00\nCanteen\nEnjoy your meal.");
    c.addEvent(e1);
    print(c,"\n")

    print(c.findEvent("Exam"),"\n")

    print(c.findEventsAfter(Time("2023 3 2 15 40")),"\n")
    print(c.findEventsBefore(Time("2023 3 2 8 00")),"\n")
