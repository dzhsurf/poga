from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterable, Tuple

if TYPE_CHECKING:
    from .poga_layout import PogaLayout


class PogaView(ABC):
    """PogaView interface"""

    @abstractmethod
    def size_that_fits(self) -> Tuple[float, float]:
        pass

    @abstractmethod
    def frame_origin(self) -> Tuple[float, float]:
        pass

    @abstractmethod
    def set_frame_origin(self, x: float, y: float):
        pass

    @abstractmethod
    def set_frame_size(self, width: float, height: float):
        pass

    @abstractmethod
    def bounds_size(self) -> Tuple[float, float]:
        pass

    @abstractmethod
    def subviews_count(self) -> int:
        pass

    @abstractmethod
    def subviews(self) -> Iterable[PogaView]:
        pass

    @abstractmethod
    def poga_layout(self) -> PogaLayout:
        pass
