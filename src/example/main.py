import poga


class TestContext:
    def __del__(self):
        print("context destroy")


def set_context(node: poga.libpoga_capi.YGNodeRef):
    a = [1, 2, 3]
    poga.libpoga_capi.YGNodeSetContext(node, a)


def get_context(node: poga.libpoga_capi.YGNodeRef):
    a = poga.libpoga_capi.YGNodeGetContext(node)
    print(a)


def fn(a: int, b: int) -> poga.libpoga_capi.YGSize:
    return (a + b, 0)


def main():
    print(dir(poga.libpoga_capi))
    print(poga.PogaLayout())


if __name__ == "__main__":
    main()
