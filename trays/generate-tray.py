import json
import logging
import os

import click

from svgops import Page, NotchedBox, Group, SimpleSVGAttribute, NotchSide

AMBER_BAMBOO_HEAVY = 6.7
AMBER_BAMBOO_MED = 2.7
AMBER_BAMBOO_LIGHT = 1.8

AMBER_BAMBOO_DIMENSIONS = (790, 384)
GAP_SIZE = 8


@click.group()
@click.pass_context
def main(ctx):
    pass

class Tray:

    def __init__(self,
                 length,
                 width,
                 height,
                 side_material_thickness=AMBER_BAMBOO_HEAVY,
                 base_material_thickness=AMBER_BAMBOO_MED,
                 material_dimensions=AMBER_BAMBOO_DIMENSIONS,
                 cavity_depth=14,
                 dpi=72,
                ):
        self.dpi = dpi
        self.length = length
        self.width = width
        self.height = height
        self.side_material_thickness = side_material_thickness
        self.base_material_thickness = base_material_thickness
        self.cavity_depth = cavity_depth
        self.material_dimensions = material_dimensions

    def apply_cut_style(self, obj):
        obj.add_attr(SimpleSVGAttribute(name="fill", value="#ffffff"))
        obj.add_attr(SimpleSVGAttribute(name="stroke", value="#000000"))
        obj.add_attr(SimpleSVGAttribute(name="stroke-width", value="1"))

    def pages(self):
        # TODO add checks for size to make sure they fit on a page, current sizes are known to fit
        # do sides
        page = Page(name="sides", material_dimensions=self.material_dimensions)
        grp_1 = Group(name="short_side_a", offset=(10, 10,))
        page.add_child(grp_1)
        grp_1.add_child(NotchedBox(width=60, height=210, notch_sides=[NotchSide.inside_left, NotchSide.inside_top, NotchSide.inside_bottom, ]))
        # grp_2 = Group(name="short_side_b", offset=(80, 10,))
        # page.add_child(grp_2)
        # grp_1.add_child(NotchedBox(width=60, height=210, notch_sides=[NotchSide.inside_left, NotchSide.inside_top, NotchSide.inside_bottom, ]))
        # grp_3 = Group(name="long_side_a", offset=(150, 10,))
        # page.add_child(grp_3)
        # grp_3.add_child(NotchedBox(width=350, height=60, notch_sides=[NotchSide.inside_left, NotchSide.outside_right, NotchSide.outside_right, ]))
        # grp_4 = Group(name="long_side_b", offset=(150, 80,))
        # page.add_child(grp_4)
        # grp_4.add_child(NotchedBox(width=350, height=60, notch_sides=[NotchSide.inside_left, NotchSide.outside_right, NotchSide.outside_right, ]))
        self.apply_cut_style(grp_1)
        # self.apply_cut_style(grp_2)
        # self.apply_cut_style(grp_3)
        # self.apply_cut_style(grp_4)
        yield page


# class NotchSide(Enum):
#     inside_left = "inside_left"
#     outside_left = "outside_left"
#     inside_right = "inside_right"
#     outside_right = "outside_right"
#     inside_top = "inside_top"
#     outside_top = "outside_top"
#     inside_bottom = "inside_bottom"
#     outside_bottom = "outside_bottom"







    def write(self, prefix):
        for page in self.pages():
            with open(f"{prefix}-{page.name}.svg", 'w') as output_fp:
                page.write(output_fp)


@main.command()
@click.pass_context
@click.option('--output', "-o", help='path to write the svg to', required=True)
def make_box(ctx, output):
    tray = Tray(400, 300, 64)
    tray.write(output)


if __name__ == '__main__':
    logger = logging.getLogger()

    logger.setLevel(os.getenv("LOG_LEVEL", logging.INFO))
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    main()
