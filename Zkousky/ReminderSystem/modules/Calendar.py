from __future__ import annotations

from .Event import Event, Time

class Calendar:
    name: str
    path: str
    events: list[Event]
    
    def __init__(self, name:str, path:str="") -> None:
        self.name = name
        self.path = path
        if self.path!="":
            with open(self.path,"r") as f:
                self.events =  sorted([Event(event) for event in f.read().split("\n\n")])
            
    def addEvent(self, event:Event) -> None:
        if (event not in self.events):
            self.events.append(event)
            self.events.sort()
        else: print("Event already in calendar","\n")
        
    def findEvent(self, name:str)-> Calendar:
        t = Calendar("Events named " + name)
        t.events = sorted([event for event in self.events if event.name == name])
        return t
    
    def findEventsAfter(self, time:Time)->Calendar:
        t = Calendar("Events after " + time.__repr__())
        t.events = sorted([event for event in self.events if not(event.start_time < time)])
        return t
    
    def findEventsBefore(self, time:Time)->Calendar:
        t = Calendar("Events before " + time.__repr__())
        t.events = sorted([event for event in self.events if event.start_time < time])
        return t
    
    def __repr__(self) -> str:
        out:str = self.name+":\n"
        for event in self.events:
            out+=event.__repr__()+"\n\n"
        return out
    
    def __del__(self) ->None:
        with open(self.name+".txt",'w') as f:
            out:str=""
            for event in self.events:
                out+=f"""{event.name}
{event.start_time.year} {event.start_time.month} {event.start_time.day} {event.start_time.hour} {event.start_time.minute}
{event.end_time.year} {event.end_time.month} {event.end_time.day} {event.end_time.hour} {event.end_time.minute}
{event.place}
{event.description}

"""
            f.write(out)