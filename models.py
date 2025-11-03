from dataclasses import dataclass, field
from typing import List

@dataclass
class Tablet:
    name: str
    dosage: str

@dataclass
class Notification:
    id: int = None               # для БД, автоинкремент
    time: str = ""
    enabled: bool = True
    tablets: List[Tablet] = field(default_factory=list)
