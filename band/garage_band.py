from abc import ABC, abstractmethod

class Musician(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass

class Guitarist(Musician):
    def __init__(self, name):
        Musician.__init__(self, name)

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    def __init__(self, name):
        Musician.__init__(self,name)

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self, name):
        Musician.__init__(self,name)

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"

class Band():
    instances = []
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.instances.append(self.name)

    def play_solos(self):
        rythem = []
        for member in self.members:
            rythem.append(member.play_solo())
        return (rythem)

    @classmethod
    def to_list(cls):
        return Band.instances

if __name__ == "__main__":
    pass
    # the_nobodies = Band("The Nobodies", [])
    # print(len(Band.instances))
    # print(Band.instances[0])
