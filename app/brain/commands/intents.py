from enum import Enum


class Intent(Enum):

    UNKNOWN = 0

    OPEN_APP = 1

    OPEN_WEBSITE = 2

    GET_TIME = 3

    GET_DATE = 4

    REMEMBER = 5

    RECALL = 6

    FORGET = 7