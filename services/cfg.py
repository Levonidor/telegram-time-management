from enum import StrEnum,IntEnum

USERDATA_COLUMNS = [
    "ACTIVITY_TYPE",
    "ACTIVITY_NAME",
    "TIMESTAMP",
    "DURATION"
]

class USERDATA(StrEnum):
    TYPE = "ACTIVITY_TYPE",
    NAME = "ACTIVITY_NAME",
    TIMESTAMP = 'TIMESTAMP',
    DURATION = "DURATION"
