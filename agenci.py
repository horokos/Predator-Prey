# To jest taki zarys mniej wiecej jak to powinno wygladac
# Genrelanie nie ma powiedziane jak to musi wygladac bo mozna do teg ododawac ile sie chce parametrow
# Np jakis bread_rate czyli jakie sa szanse na rozmnozenie
# Move moze byc poprostu wybieramy jedna z pozycji obok czyli jedna z 8 wokol losowo


class Agent:
    def __init__(self, pos):
        # pozycja agenta
        self.pos = pos
        # energia od ktorej bedzie zalezec czy moze cos zrobic i czy umiera
        self.energy = 10

    # przemieszczenie sie agenta
    def move(self):
        pass


class Predator(Agent):
    def __init__(self, pos):
        super().__init__(pos)

    # ta metoda odpowiada za to co agent bedzie robil
    # bo potem w modelu bedzie ona wywolywana dla kazdego agenta
    def step(self):
        self.energy -= 1
        super().move()
        # dalej trzeba sprawdzic czy na tym polu znajduje sie prey (i czy chcemy go zjesc)
        # (bo moze jestesmy najedzeni)
        if self.energy == 0:
            # zabij
            pass
        # jeszcze trzeba sprawdzic czy np znajduje sie na polu z jakims innym osobnikiem swojego gatunku
        # jesli tak no to czy sie rozmnaza. np czy sa wystarczjaca najedzenie zeby sie rozmanzac
        # albo mozna pominac to czy tam jest ktos inny i samemu (przez podzielenie xd)


class Prey(Agent):
    def __init__(self, pos):
        super().__init__(pos)

    def step(self):
        self.energy -= 1
        super().move()
        # dalej trzeba sprawdzic czy na tym polu znajduje sie grass (i czy chcemy ja zjesc)
        # (bo moze jestesmy najedzeni)
        if self.energy == 0:
            # zabij
            pass
        # jeszcze trzeba sprawdzic czy np znajduje sie na polu z jakims innym osobnikiem swojego gatunku
        # jesli tak no to czy sie rozmnaza. np czy sa wystarczjaca najedzenie zeby sie rozmanzac
        # albo mozna pominac to czy tam jest ktos inny i samemu (przez podzielenie xd)


class Grass:
    def __init__(self, pos):
        self.pos = pos
        # grown - czy urosnieta jesli tak to bedzie ja mozna zjesc jesli nie to nie
        self.grown = True
        # licznik za ile stepów bedzie urosnieta
        self.count = 0

    def step(self):
        # jesli nie jest urosnieta to rosnie jak jest to nic nie robi
        if not self.grown:
            self.count -= 1
            if self.count == 0:
                self.grown = True
