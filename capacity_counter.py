from collections import Counter


# noinspection PyUnusedLocal
from models import Database, EventRealization


def counter(data: Database, event_realizations: list[EventRealization]) -> Counter[str, int]:
    capacity_exceeded: Counter[str, int] = Counter()
    for ev, r in event_realizations.items():
        if r.event.capacity_required > r.room.total_capacity:
            capacity_exceeded[ev] += 1
    return capacity_exceeded
