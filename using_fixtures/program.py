def hex_to_ascii(hex_string):
    ascii_char = bytes.fromhex(hex_string).decode('ASCII')
    print(ascii_char)
    return ascii_char


class Certification():
    def __init__(self, title, awarding_body, level, completed):
        self.title = title
        self.awarding_body = awarding_body
        self.level = level
        self.completed = completed

    def score(self):
        if self.level == 'Entry':
            score = 1
        elif self.level == 'Intermediate':
            score = 2
        elif self.level == 'Advanced':
            score = 3
        else:
            score = 0
        return score

    def to_dict(self):
        return self.__dict__

    def write_to_db(self):
        with open(f'{self.title}.txt', 'a+') as file:
            file.write(f'{self.to_dict()}')


hex_to_ascii('68656c6c6f')
