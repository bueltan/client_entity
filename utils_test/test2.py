class abc:
    a = 1
    b = 2
    c = 3


class xyz:
    x = 4
    y = 5
    z = 6

    def sumAll(self, other):
        print(self.x + self.y + self.z + other.a + other.b + other.c)


xyz.sumAll(xyz, abc)
