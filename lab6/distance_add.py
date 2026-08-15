class distance:
    def __init__(self, cm, m, km):
        self.cm = cm
        self.m = m
        self.km = km
    def add(self, d):
        s = distance(self.cm + d.cm, self.m + d.m, self.km + d.km)
        return f"{self.cm}cm + {self.m}m + {self.km}km) + ({d.cm}cm + {d.m}m + {d.km}km) = ({s.cm}cm + {s.m}m + {s.km}km"
    def input(self):
        self.cm = float(input("Enter cm: "))
        self.m = float(input("Enter m: "))
        self.km = float(input("Enter km: "))
d1 = distance(0, 0, 0)
d2 = distance(0, 0, 0)
d1.input()
d2.input()
print(d1.add(d2))