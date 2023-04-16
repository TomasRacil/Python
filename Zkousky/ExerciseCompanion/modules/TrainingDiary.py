from .Training import Training

class TrainingDiary:
    path:str
    owner:str
    trainings:list[Training]

    def __init__(self, path:str) -> None:
        self.path = path
        with open(path, 'r') as f:
            temp = f.read().split("#")
            self.owner = temp[0]
            self.trainings = [Training(training)for training in temp[1:]]
        self.trainings.sort()
    
    def addTraining(self, training: Training)->None:
        self.trainings.append(training)
        self.trainings.sort()

    def printPersonalBest(self)->None:
        out={}
        for training in self.trainings:
            bests = training.getBests()
            for ex in bests:
                if out.get(ex[0])==None:
                    out[ex[0]]=ex[1]
                else:
                    if out[ex[0]]<ex[1]:
                        out[ex[0]]=ex[1]
        print("Personal best:")
        for key, value in out.items():
            print(f"{key}:{value}")

    def __repr__(self) -> str:
        out=f"{self.owner}"
        for training in self.trainings:
            out+=f"#\n{training.__repr__()}"
        return out

    def __del__(self) ->None:
        with open(self.path,'w') as f:
            out:str=self.__repr__()
            f.write(out)