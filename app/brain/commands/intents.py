from enum import Enum


class Intent(Enum):

    OPEN_APP = "OPEN_APP"

    OPEN_WEBSITE = "OPEN_WEBSITE"

    GET_TIME = "GET_TIME"

    GET_DATE = "GET_DATE"

    UNKNOWN = "UNKNOWN"