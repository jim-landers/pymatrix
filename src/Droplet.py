import string, random






# Acts as the "head" of a falling droplet. For storing positions.
class Droplet:
    CHARS = "!#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    bordersYX = ''

    def __init__(self, borders):
        # self.posyx = pos
        self.maxY  = borders[0]
        self.maxX  = borders[1]
        self.y     = 0
        self.x     = 0
        self.ChooseRandPos()
        self.token = self.GenRandChar()



    def GetPos(self) -> list:
        return (self.y, self.x)

    def GetY(self) -> int:
        return self.y

    def GetX(self) -> int:
        return self.x

    def GetToken(self) -> str:
        return self.token


    def ChooseRandPos(self) -> list:
        self.y = random.randrange(0, self.maxY)
        self.x = random.randrange(0, self.maxX)




    def GenRandChar(self) -> str:
        return (random.choice(self.CHARS))


    def Tick(self):
        self.token = self.GenRandChar()
        self.y += 1

        if (self.y > self.maxY):
            self.ChooseRandPos()
