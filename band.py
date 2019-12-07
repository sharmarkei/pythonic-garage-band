class Band():
    members = []

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    @classmethod
    def play_solos(cls):
        for member in cls.members:
            print(f'{member} has an amazing {member.instrument} solo')

    @classmethod
    def create_from_data(cls, data):
        for musician in data:
            if musician['instrument'] == 'Guitar':
                cls.members.append(
                    Guitarist(musician['name'], musician['instrument']))

            elif musician['instrument'] == 'Bass':
                cls.members.append(
                    Bassist(musician['name'], musician['instrument']))

            elif musician['instrument'] == 'Drums':
                cls.members.append(
                    Drummer(musician['name'], musician['instrument']))

    @classmethod
    def to_list(cls):
        return cls.members


class Musician(Band):
    musician_list = []

    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.__class__.musician_list.append(self)

    @classmethod
    def get_members(cls):
        return cls.musician_list


class Guitarist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'Guitar Solo'

    def get_instrument(self):
        return 'guitar'


class Bassist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'Bass Solo'

    def get_instrument(self):
        return 'Bass'


class Drummer(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'Drum Solo'

    def get_instrument(self):
        return 'Drums'




data = [
    {'name': 'James',
        'instrument': 'Bass'
     },
    {'name': 'Sam',
        'instrument': 'Drums'
     },
    {'name': 'Rick',
     'instrument': 'Guitar'
     }
]


Band.moment_of_fame()
Band.create_from_data(data)
Band.to_list()
Musician.play_solos()