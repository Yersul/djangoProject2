from enum import Enum


class Choice(Enum):
    @classmethod
    def choice(cls):
        return [(c.value, c.name) for c in cls]

    @classmethod
    def repr(cls):
        return {c.name: {'id': c.value, 'name': c.name} for c in cls}

    @classmethod
    def list(cls):
        return [c.value for c in cls]

    def __str__(self):
        return self.value


class GenderChoice(str, Choice):
    MALE = "MALE"
    FEMALE = "FEMALE"


class PostKindChoice(str, Choice):
    BLOG = 'BLOG'
    ADVERTISING = 'ADVERTISING'
    NEWS = 'NEWS'


class LikeKindChoice(str, Choice):
    LIKE = 'LIKE'
    DISLIKE = 'DISLIKE'
