from typing import Counter, Protocol

from models import Database, EventRealization


class BaseCounter(Protocol):
    def __call__(
        self,
        data: Database,
        event_realizations: list[EventRealization],
    ) -> Counter[str, int]:
        pass
