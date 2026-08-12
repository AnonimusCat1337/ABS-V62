import json
import random
import string


class Player:
    ClientVersion = "0.0.0"

    ID = [0, 1]
    Token = ""
    Name = "Brawler"
    Registered = False
    Thumbnail = 0
    Namecolor = 0
    Region = "RU"
    ContentCreator = "Project ABS V62.250.1"

    Coins = 0
    Gems = 0
    Blings = 0
    Trophies = 100000
    HighestTrophies = 100000
    TrophyRoadTier = 1337
    Experience = 99999
    Level = 500
    Tokens = 200
    TokensDoubler = 1000

    SelectedSkins = {}
    SelectedBrawlers = [0, 1, 2]
    RandomizerSelectedSkins = []
    OwnedPins = []
    OwnedThumbnails = []
    OwnedSkins = []
    OwnedBrawlers = {
        0: {'CardID': 0, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        1: {'CardID': 4, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        2: {'CardID': 8, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        3: {'CardID': 12, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        4: {'CardID': 16, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        5: {'CardID': 20, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        6: {'CardID': 24, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        7: {'CardID': 28, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        8: {'CardID': 32, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        9: {'CardID': 36, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        10: {'CardID': 40, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        11: {'CardID': 44, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        12: {'CardID': 48, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        13: {'CardID': 52, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        14: {'CardID': 56, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        15: {'CardID': 60, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        16: {'CardID': 64, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        17: {'CardID': 68, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        18: {'CardID': 72, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        19: {'CardID': 95, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        20: {'CardID': 100, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        21: {'CardID': 105, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        22: {'CardID': 110, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        23: {'CardID': 115, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        24: {'CardID': 120, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        25: {'CardID': 125, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        26: {'CardID': 130, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        27: {'CardID': 177, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        28: {'CardID': 182, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        29: {'CardID': 188, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        30: {'CardID': 194, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        31: {'CardID': 200, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        32: {'CardID': 206, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        34: {'CardID': 218, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        35: {'CardID': 224, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        36: {'CardID': 230, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        37: {'CardID': 236, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        38: {'CardID': 279, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        39: {'CardID': 296, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        40: {'CardID': 303, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        41: {'CardID': 320, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        42: {'CardID': 327, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        43: {'CardID': 334, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        44: {'CardID': 341, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        45: {'CardID': 358, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        46: {'CardID': 365, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        47: {'CardID': 372, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        48: {'CardID': 379, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        49: {'CardID': 386, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        50: {'CardID': 393, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        51: {'CardID': 410, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        52: {'CardID': 417, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        53: {'CardID': 427, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        54: {'CardID': 434, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        56: {'CardID': 448, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        57: {'CardID': 466, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        58: {'CardID': 474, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        59: {'CardID': 491, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        60: {'CardID': 499, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        61: {'CardID': 507, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        62: {'CardID': 515, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        63: {'CardID': 523, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        64: {'CardID': 531, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        65: {'CardID': 539, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        66: {'CardID': 547, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        67: {'CardID': 557, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        68: {'CardID': 565, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        69: {'CardID': 573, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        70: {'CardID': 581, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        71: {'CardID': 589, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        72: {'CardID': 597, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        73: {'CardID': 605, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        74: {'CardID': 619, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        75: {'CardID': 633, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        76: {'CardID': 642, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        77: {'CardID': 655, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        78: {'CardID': 663, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        79: {'CardID': 669, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        80: {'CardID': 675, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        81: {'CardID': 681, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        82: {'CardID': 687, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        83: {'CardID': 693, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        84: {'CardID': 699, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        85: {'CardID': 705, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        86: {'CardID': 711, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        87: {'CardID': 717, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        88: {'CardID': 723, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        89: {'CardID': 729, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        90: {'CardID': 735, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        91: {'CardID': 741, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        92: {'CardID': 747, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        93: {'CardID': 774, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        94: {'CardID': 756, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
        95: {'CardID': 762, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11},
    }

    def __init__(self):
        pass

    def getDataTemplate(self, highid, lowid, token):
        if highid == 0 or lowid == 0:
            self.ID[0] = int(''.join([str(random.randint(0, 9)) for _ in range(1)]))
            self.ID[1] = int(''.join([str(random.randint(0, 9)) for _ in range(8)]))
            self.Token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40))
        else:
            self.ID[0] = highid
            self.ID[1] = lowid
            self.Token = token

        DBData = {
            'ID': self.ID,
            'Token': self.Token,
            'Name': self.Name,
            'Registered': self.Registered,
            'Thumbnail': self.Thumbnail,
            'Namecolor': self.Namecolor,
            'Region': self.Region,
            'ContentCreator': self.ContentCreator,
            'Coins': self.Coins,
            'Gems': self.Gems,
            'Blings': self.Blings,
            'Trophies': self.Trophies,
            'HighestTrophies': self.HighestTrophies,
            'TrophyRoadTier': self.TrophyRoadTier,
            'Experience': self.Experience,
            'Level': self.Level,
            'Tokens': self.Tokens,
            'TokensDoubler': self.TokensDoubler,
            'SelectedBrawlers': self.SelectedBrawlers,
            'OwnedPins': self.OwnedPins,
            'OwnedThumbnails': self.OwnedThumbnails,
            'OwnedBrawlers': self.OwnedBrawlers,
            'OwnedSkins': self.OwnedSkins,
        }
        return DBData

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4))