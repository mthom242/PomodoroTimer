class Timer:

    def __init__(self, studyMin, studySec, breakMin, breakSec, cycles):
        self.studyMin = studyMin
        self.studySec = studySec
        self.breakMin = breakMin
        self.breakSec = breakSec
        self.cycles = cycles
    
    def __str__(self):
        return f"Studying for {self.studyMin}m{self.studySec}s with a break of {self.breakMin}m{self.breakSec}s for {self.cycles} cycles"
    
    def changeStudy(self, newMin, newSec):
        self.studyMin = newMin
        self.studySec = newSec
    
    def changeBreak(self, newMin, newSec):
        self.breakMin = newMin
        self.breakSec = newSec
    
    def changeCycle(self, newCyc):
        self.cycles = newCyc



if __name__ == "__main__":
    print("Creating a timer...")
    timer = Timer(20,00,5,00,5)
    print(timer, end='\n')

    print("Changing the study times...")
    timer.changeStudy(25,30)
    print(timer, end='\n')

    print("Changing the break times...")
    timer.changeBreak(10,00)
    print(timer, end='\n')

    print("Changing the cycle count...")
    timer.changeCycle(8)
    print(timer, end='\n')