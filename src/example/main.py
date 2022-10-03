from typing import Iterable, Tuple

from poga import *
from poga import libpoga_capi


class MyView(PogaView):
    def size_that_fits(self) -> Tuple[float, float]:
        return (0.0, 0.0)

    def frame_origin(self) -> Tuple[float, float]:
        pass

    def set_frame_position_and_size(self, x: float, y: float, width: float, height: float):
        pass

    def bounds_size(self) -> Tuple[float, float]:
        return (0.0, 0.0)

    def subviews_count(self) -> int:
        return 0

    def subviews(self) -> Iterable[PogaView]:
        return list[PogaView]()

    def is_container(self) -> bool:
        return False

    def poga_layout(self) -> PogaLayout:
        return None


def main():
    print(libpoga_capi.poga_version())
    print(dir(libpoga_capi))
    view = MyView()
    layout = PogaLayout(view)
    print(layout)


if __name__ == "__main__":
    main()
