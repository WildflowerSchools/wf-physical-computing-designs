# Physical Computing Designs

This is all of the hardware designs created to support the classroom technology. Software used to create these designs:

- [Wings3D](http://www.wings3d.com) create initial models and exported to STL
- [Prusa Slicer](https://www.prusa3d.com/page/prusaslicer_424/) import STL files and slice for printing. Exports to gcode.
- [Graphic](https://www.graphic.com/mac/) for tray designs, exports to SVG (mac only).


## Cameras/Raspberry Pi's

### pi-rig-v0003 (last version - deployed in dahlia 2022)

This design went back to the idea that the PI should be static and attached to the wall with the camera board mounted on an arm off of it. It is kind of a basket that is affixed to the wall. A sled is attached to the PI board and slid into the basket. The camera is mounted on an arm.

- [camera-full-set-v001.3mf](camera-cases/camera-full-set-v001.3mf) slicer file used for layot on 3D printer. Contains 2 full sets of case with all parts. Includes an extra arm as they tend to get lost if not careful.
- [pi-rig-v0003.wings](camera-cases/pi-rig-v0003.wings) wings3D file of the case.
- [pi-rig-v0003.stl](camera-cases/pi-rig-v0003.stl) STL export
- [cam-bracket-v0001.wings](camera-cases/cam-bracket-v0001.wings) wings3D file of the camera arm
- [cam-case-v004.wings](camera-cases/cam-case-v004.wings) wings3D file of the camera holder
- [cam-bracket-v0001.stl](camera-cases/cam-bracket-v0001.stl) STL export
- [rig-nail-jig-v2.wings](camera-cases/rig-nail-jig-v2.wings) wings3D file of the wall attachement that holds case on wall.
- [rig-nail-jig-v2.stl](camera-cases/rig-nail-jig-v2.stl) STL export

This was printed in grey PLA but was then painted white to match the walls of the classroom. Future prints should be white. A [Prusa Mini+](https://www.prusa3d.com/product/original-prusa-mini-semi-assembled-3d-printer-4/) was used to print all the models.


### Other

Files in [camera-cases/archived](camera-cases/archived/) are a smattering of earlier designs and ideas.


## Sensors for Shoes and Teachers

Files in [shoe-teacher-sensor-cases](shoe-teacher-sensor-cases/) are all of the radio pendant and shoe attachement dsigns, none of which are used any longer. Preserved for posteriety.


## Trays

### Gen3 practical life tray small

prototype tray for next generation trays. [gen-3-pltray-small](trays/gen-3-pltray-small).

These parts would be sent to [Ponoko](https://www.ponoko.com/login?redirect=%2F) to be laser cut. These should be modified for larger tray sizes.

- [all.idraw](trays/gen-3-pltray-small/all.idraw) Graphic file that has all of the laser cut pieces
- [gen-3-pltray-small-base.svg](trays/gen-3-pltray-small/gen-3-pltray-small-base.svg) SVG file on the base of the tray, the very bottom, with a hole for inserting the electronics module.
- [gen-3-pltray-small-Bottom.svg](trays/gen-3-pltray-small/gen-3-pltray-small-Bottom.svg) SVG file on the bottom of the tray, the upper bottom.
- [gen-3-pltray-small-Sides.svg](trays/gen-3-pltray-small/gen-3-pltray-small-Sides.svg) SVG file on the sides of the tray.

Base and bottom should be done in Amber Bamboo Plywood 2.7mm thickness. Sides in Amber Bamboo Plywood 6.7mm thickness.

These parts are 3D printed.
- [tray-module-alt01-v0001.3mf](trays/tray-module-alt01-v0001.3mf) slicer file for latest interation of the module.
- [tray-module-alt01-v0001.wings](trays/tray-module-alt01-v0001.wings) wings3D file for the design
- [tray-module-alt01-v0001.stl](trays/tray-module-alt01-v0001.stl) STL export
- [cam-lock.scad](trays/cam-lock.scad) OpenSCAD file for the test models of the cam-lock piece, that would hold in the module. Has not been printed or tested yet.
- [cam-lock.stl](trays/cam-lock.stl) STL export


### Other

A script was started to generate trays of different sizes using python [generate-tray.py](trays/generate-tray.py). It wasn't completed.

Files in [trays/archive](trays/archive/) are older tray designs that are no longer in use.