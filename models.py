from dataclasses import dataclass, field
from typing import List

@dataclass
class Tablet:
    name: str
    dosage: str

@dataclass
class Notification:
    time: str           # HH:MM формат
    tablets: List[Tablet] = field(default_factory=list)
    enabled: bool = True
