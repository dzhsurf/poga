from typing import List, Tuple

from poga import PogaView, PogaLayout, libpoga_capi


class MyView(PogaView):
    def size_that_fits(self, width: float, height: float) -> Tuple[float, float]:
        return (0.0, 0.0)

    def frame_origin(self) -> Tuple[float, float]:
        return (0, 0)

    def set_frame_position_and_size(
        self, x: float, y: float, width: float, height: float
    ):
        pass

    def bounds_size(self) -> Tuple[float, float]:
        return (0.0, 0.0)

    def subviews_count(self) -> int:
        return 0

    def subviews(self) -> List[PogaView]:
        return list[PogaView]()

    def is_container(self) -> bool:
        return False

    def poga_layout(self) -> PogaLayout:
        return PogaLayout(self)


def main():
    print(libpoga_capi.poga_version())
    print(dir(libpoga_capi))
    view = MyView()
    layout = PogaLayout(view)
    print(layout)


if __name__ == "__main__":
    main()
