from dataclasses import dataclass
from enum import Enum
from uuid import uuid4

from abc import ABC, abstractmethod


@dataclass
class SimpleSVGAttribute:
    name: str
    value: str

    def __repr__(self) -> str:
        return f"""{self.name}="{self.value}" """


class Group:

    def __init__(self, name, offset=None):
        self.name = name
        self.parent = None
        if self.name is None:
            self.name = str(uuid4())
        self.__children = []
        self.__attrs = []
        self.offset = offset
        if offset is None:
            self.offset = (0, 0)
    
    def add_child(self, child):
        if hasattr(child, "write"):
            self.__children.append(child)
            child.parent = self
    
    def add_attr(self, attribute):
        self.__attrs.append(attribute)

    def write(self, output_fp):
        output_fp.write(f"""<g id="{self.name}" transform="translate({self.offset[0]}, {self.offset[1]})" {" ".join(map(str, self.__attrs))}>\n""")
        self._write_children(output_fp)
        output_fp.write("</g>\n")
    
    def _write_children(self, output_fp):
        for child in self.__children:
            child.write(output_fp)


class Page(Group):

    def __init__(self, name=None, material_dimensions=(10, 10)):
        Group.__init__(self, name=name, offset=None)
        self.material_dimensions = material_dimensions

    def write(self, output_fp):
        output_fp.write(f"""<svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink" x="0" y="0"
                width="{self.material_dimensions[0]}mm"
                height="{self.material_dimensions[1]}mm"
                viewBox="0, 0, {self.material_dimensions[0]},
                {self.material_dimensions[1]}">\n""")
        self._write_children(output_fp)
        output_fp.write("""</svg>\n""")
        output_fp.flush()


class NotchSide(Enum):
    inside_left = "inside_left"
    outside_left = "outside_left"
    inside_right = "inside_right"
    outside_right = "outside_right"
    inside_top = "inside_top"
    outside_top = "outside_top"
    inside_bottom = "inside_bottom"
    outside_bottom = "outside_bottom"


class Orientation(Enum):
    h = "horizontal"
    v = "vertical"


class Path:

    def __init__(self):
        self._ops = []

    def move_to(self, x, y):
        self._ops.append(f"M {x},{y}")

    def move_by(self, x, y):
        self._ops.append(f"m {x},{y}")

    def line_to(self, x, y):
        self._ops.append(f"m {x},{y}")

    def line_to(self, x, y):
        self._ops.append(f"L {x},{y}")

    def line_by(self, x, y):
        self._ops.append(f"l {x},{y}")

    def hline_to(self, l):
        self._ops.append(f"H {l}")

    def hline_by(self, l):
        self._ops.append(f"h {l}")

    def vline_to(self, l):
        self._ops.append(f"V {l}")

    def vline_by(self, l):
        self._ops.append(f"v {l}")
    
    def __repr__(self) -> str:
        return " ".join(self._ops)


class NotchedBox(Group):

    def __init__(self, name=None, width=0, height=0, notch_sides=None, notch_depth=10, min_notch_len=10, max_notch_len=40):
        Group.__init__(self, name=name, offset=None)
        self.width = width
        self.height = height
        self.notch_sides = notch_sides
        if self.notch_sides is None:
            self.notch_sides = []
        self.min_notch_len = min_notch_len
        self.max_notch_len = max_notch_len
        self.notch_depth = notch_depth

    def write(self, output_fp):
        for side in ["left", "top", "right", "bottom"]:
            if getattr(NotchSide, f"inside_{side}") in self.notch_sides:
                p = determine_notches(
                        length=self.height,
                        inside=True, 
                        min_notch_len=self.min_notch_len,
                        max_notch_len=self.max_notch_len,
                        notch_depth=self.notch_depth,
                        orientation=(Orientation.v if side in ["left", "right"] else Orientation.h),
                )
            elif getattr(NotchSide, f"outside_{side}") in self.notch_sides:
                p = determine_notches(
                        length=self.height if side in ["left", "right"] else self.width,
                        inside=True, 
                        min_notch_len=self.min_notch_len,
                        max_notch_len=self.max_notch_len,
                        notch_depth=self.notch_depth,
                        orientation=(Orientation.v if side in ["left", "right"] else Orientation.h),
                )
            else:
                p = Path()
                p.move_to(0, 0)
                if side in ["left", "right"]:
                    p.line_to(0, self.height)
                else:
                    p.line_to(self.width, 0)
            output_fp.write(f"""<path id="{self.name}2" d="{p}" transform="translate({self.width if side == "right" else 0}, {self.height if side == "bottom" else 0})" />\n""")
        self._write_children(output_fp)


def _horv(x, y, orientation):
    if orientation == Orientation.h:
        return (x, y)
    return (y, x)

def determine_notches(length:int=100, inside:bool=True, min_notch_len:int=4, max_notch_len:int=30, notch_depth:int=10, tabs:bool=True, orientation:Orientation=Orientation.h):
    p = Path()
    current_notch = 0
    if inside:
        current_notch = notch_depth
    p.move_to(*_horv(0, current_notch, orientation))
    ns = list(range(min_notch_len, max_notch_len+1))
    ns.reverse()
    notch_count = 0
    for notch_size in ns:
        remain = length % notch_size
        notch_count = int(length / notch_size)
        if remain == 0 and notch_count % 2 == 1:
            break
    print(f" {notch_size}mm x {notch_count}")
    current_position = 0
    for notch in range(0, notch_count):
        current_position += notch_size
        p.line_to(*_horv(current_position, current_notch, orientation))
        current_notch = 0 if current_notch == notch_depth else notch_depth
        if notch != notch_count - 1:
            p.line_to(*_horv(current_position, current_notch, orientation))
    return p
