length = 160;
channel_thickness = 6;
channel_height = 16;
width = 40;
thickness = 4;
stop_height = 44;
support_depth = 20;

// calculated
plate_width = width - 2 - channel_thickness * 2;


translate([-20, -125, 0]) {
    difference() {
        union() {
            // base
            cube([width, length, thickness]);
            // sides
           translate([0, 0, thickness])
           cube([channel_thickness, length, channel_height]);
           translate([width-channel_thickness, 0, thickness])
           cube([channel_thickness, length, channel_height]);
            
            // channel tops
           translate([width - channel_thickness * 2, 0, channel_height+thickness])
           cube([channel_thickness * 2, length, thickness]);
           translate([0, 0, channel_height+thickness])
           cube([channel_thickness * 2, length, thickness]);
           
            // static-stop
            //   fill
            translate([0, 0, thickness]) {
                cube([width, support_depth+(thickness*2), channel_height+thickness]);
            }
            translate([0, 0, channel_height+thickness]) {
                //   side-supports
                translate([0, support_depth, thickness])
                cube([channel_thickness, channel_thickness, stop_height]);
                translate([width-channel_thickness, support_depth, thickness])
                cube([channel_thickness, channel_thickness, stop_height]);

                //    backing
                translate([0, support_depth + thickness, thickness])
                cube([width, thickness, stop_height]);
                //    legs
                difference() {
                    translate([0, 0, thickness])
                    cube([channel_thickness, support_depth, stop_height]);
                    rotate([-24, 0, 0])
                    translate([-1, -29, 0])
                    cube([channel_thickness * 2, support_depth+thickness, stop_height * 2]);
                }
                difference() {
                    translate([width-channel_thickness, 0, thickness])
                    cube([channel_thickness, support_depth, stop_height]);
                    rotate([-24, 0, 0])
                    translate([33, -29, 0])
                    cube([channel_thickness * 2, support_depth+thickness, stop_height * 2]);
                }
                //   center support
                difference() {
                    union() {
                        translate([(width/2) - (channel_thickness/2), support_depth, thickness])
                        cube([channel_thickness, channel_thickness, stop_height]);
                        translate([17, 0, thickness])
                        cube([channel_thickness, support_depth, stop_height]);
                    }
                    rotate([-24, 0, 0])
                    translate([(width/2) - (channel_thickness/2)-1, -26, 0])
                    cube([channel_thickness+2, support_depth + thickness, stop_height * 2]);
                }  
            }      
        }
        // screw slide
        translate([width/2 - 3.5, thickness*4 + support_depth, -1])
        cube([7, length-(thickness * 6 + support_depth), 8]);
    }
}


// plate
translate([30, 24, 0])
difference() {
    cube([plate_width, plate_width, channel_height-2]);
    translate([plate_width/2, plate_width/2, -1])
    cylinder(h=channel_height, d=9);
    translate([plate_width/2, plate_width/2, 8])
    cylinder(h=channel_height, d=11);
}




// adjustable stop
translate([30, -30, -14]) {    
    difference() {
        union() {
            translate([0, 0, channel_height+thickness*2])
            cube([width, support_depth+thickness*2, thickness*3]);
            translate([0, 0, channel_height+thickness * 2]) {
                //   side-supports
                translate([0, support_depth, thickness])
                cube([channel_thickness, channel_thickness, stop_height]);
                translate([width-channel_thickness, support_depth, thickness])
                cube([channel_thickness, channel_thickness, stop_height]);

                //    backing
                translate([0, support_depth + thickness, thickness])
                cube([width, thickness, stop_height]);
                //    legs
                difference() {
                    translate([0, 0, thickness])
                    cube([channel_thickness, support_depth, stop_height]);
                    rotate([-24, 0, 0])
                    translate([-1, -29, 0])
                    cube([channel_thickness * 2, support_depth+thickness, stop_height * 2]);
                }
                difference() {
                    translate([width-channel_thickness, 0, thickness])
                    cube([channel_thickness, support_depth, stop_height]);
                    rotate([-24, 0, 0])
                    translate([33, -29, 0])
                    cube([channel_thickness * 2, support_depth+thickness, stop_height * 2]);
                }  
            }
        }
        translate([width/2, (support_depth+thickness)/2, 0])
        cylinder(h=stop_height, d=8);
    }
}
    
