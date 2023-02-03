
// cam
translate([0, 40, 0]) {
    difference() {
        union() {
            // shaft
            cylinder(10, 8, 8, $fn=128, center=false);
            translate([0, 0, 3]) {
                // cam
                cylinder(4, 10, 10, $fn=128, center=false);
            }
        }
        
        // hollow
        translate([0, 0, 2]) {
            cylinder(18, 5, 5, $fn=128, center=false);
        }
        
        // keyhole
        translate([0, 0, -1]) {
            intersection() {
                translate([-1.5, -5, 0]) {
                    cube([3,10,10], center=false);
                }
                cylinder(4, 4, 4, $fn=64, center=false);
            }
        }

        
        translate([10.25, -2, -2]) {
            rotate([0,0,45]){
                cube([3,3,14], center=false);
            }
        }
        translate([0, 8, -2]) {
            rotate([0,0,45]){
                cube([3,3,14], center=false);
            }
        }
        translate([-11.98, -30, -2]) {
            cube([4,60,30], center=false);
        }
    }
}


// box is 52mm x 92mm x 12mm


// cam_holder
translate([0, -50, 0]) {
    difference() {
        // holder box
        cube([146, 70, 12], center=false);
        translate([35, 35, 2.2]) {
            // cam opening
            cylinder(10, 11, 11, $fn=128, center=false);
        }
        translate([42, 8, -2]) {
            // module home
            cube([95,54,30], center=false);
        }
        // spring opening
        translate([6, 8, 4]) {
            cube([14,54,14], center=false);
            translate([12, 24, 0]) {
                cube([8,6,14], center=false);
            }
        }
    }
    translate([35, 35, 2.2]) {
        difference() {
            // cam spindle
            translate([0, 0, -2.2]) {
                cylinder(9, 4, 4, $fn=128, center=false);
            }
            translate([0, 0, 2.2]) {
                cylinder(8, 3, 3, $fn=128, center=false);
            }
        }
    }
}
