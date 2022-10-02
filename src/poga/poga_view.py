from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterable, Tuple

if TYPE_CHECKING:
    from .poga_layout import PogaLayout


class PogaView(ABC):
    """PogaView interface"""

    @abstractmethod
    def size_that_fits(self, width: float, height: float) -> Tuple[float, float]:
        """Calculate the frame size.

        Args:
            width (float): Parent layout width.
            height (float): Parent layout height.

        Returns:
            Tuple[float, float]: Return frame size (width, height).
        """
        pass

    @abstractmethod
    def frame_origin(self) -> Tuple[float, float]:
        """Return frame position.

        Returns:
            Tuple[float, float]: Return frame (x, y) position.
        """
        pass

    @abstractmethod
    def set_frame_origin(self, x: float, y: float):
        """Set the frame position.

        Args:
            x (float): The frame x position
            y (float): The frame y position
        """
        pass

    @abstractmethod
    def set_frame_size(self, width: float, height: float):
        """Set the frame size.

        Args:
            width (float): The frame width
            height (float): The frame height
        """
        pass

    @abstractmethod
    def bounds_size(self) -> Tuple[float, float]:
        """Return the layout bounds size.

        Returns:
            Tuple[float, float]: bounds size, mainly equal the frame size.
        """
        pass

    @abstractmethod
    def subviews_count(self) -> int:
        """Return subviews count.

        Returns:
            int: subviews count
        """
        pass

    @abstractmethod
    def subviews(self) -> Iterable[PogaView]:
        """Return subviews, subview type must be PogaView.

        Returns:
            Iterable[PogaView]: subviews
        """
        pass

    @abstractmethod
    def is_container(self) -> bool:
        """Return current view is container or not.

        Returns:
            bool: Return True is container.
        """
        pass

    @abstractmethod
    def poga_layout(self) -> PogaLayout:
        """Return PogaLayout

        Returns:
            PogaLayout: PogaLayout object
        """
        pass
