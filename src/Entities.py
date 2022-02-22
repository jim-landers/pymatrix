import random



# Acts as the "head" of a falling string. For storing positions and such.
class Droplet:
    # CHARS = "!#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    CHARS = "#$%&()+/0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]abcdefghijklmnopqrstuvwxyz{|}"

    maxY = None
    maxX = None

    def __init__(self, borders):
        if (self.maxY or self.maxX) is None:
            self.maxY    = borders[0] - 1
            self.maxX    = borders[1] - 1

        self.y       = 0
        self.x       = 0
        self.prevpos = None
        self.token = self.GenRandChar()
        self.ChooseRandPos()



    def GetPos(self) -> list:
        return (self.y, self.x)

    def GetY(self) -> int:
        return self.y

    def GetX(self) -> int:
        return self.x

    def GetToken(self) -> str:
        return self.token

    def GetPrevPos(self) -> list:
        return self.prevpos

    def HasPrevPos(self) -> bool:
        if self.prevpos is None:
            return False
        return True


    def ChooseRandPos(self) -> list:
        # Dividing to make droplets start in top area of screen.
        self.y = random.randrange(0, self.maxY // 8)
        self.x = random.randrange(0, self.maxX)


    # Used to give a droplet varying lengths where some reset before the bottom.
    def EndEarly(self) -> bool:
        # Bounds the chance to reset with terminal length. The calculation is arbitrary, it just
        # looked good from my tests.
        # longer terminal = lower chance, and vice versa
        x = random.randrange(0, self.maxY // 2.5)

        if x == 0:
            return True

        return False


    def GenRandChar(self) -> str:
        return (random.choice(self.CHARS))


    def Tick(self):
        self.token = self.GenRandChar()
        self.prevpos = (self.y, self.x)
        self.y += 1

        if (self.y >= self.maxY) or self.EndEarly():
            self.ChooseRandPos()










# This should have been done through the inheritence of an Entity base class, but I would have to rewrite a bunch
# to get that working now for the Droplet. This works good enough for now.
class Wiper:
    maxY = None
    maxX = None

    def __init__(self, borders):
        if (self.maxY or self.maxX) is None:
            self.maxY    = borders[0] - 1
            self.maxX    = borders[1] - 1

        self.ChooseRandPos()



    def GetPos(self) -> list:
        return [self.y, self.x]

    def GetY(self) -> int:
        return self.y

    def GetX(self) -> int:
        return self.x


    def ChooseRandPos(self) -> list:
        # Wipers always start in top row.
        self.y = 0
        self.x = random.randrange(0, self.maxX)


    def Tick(self):
        self.y += 1

        if (self.y >= self.maxY):
            self.ChooseRandPos()
