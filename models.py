from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Reminder:
    medicine: str
    dosage: str
    time_of_day: str  # утро/день/вечер/ночь
    time: str
    comment: Optional[str] = None

@dataclass
class UserSchedule:
    user_id: int
    reminders: List[Reminder]
