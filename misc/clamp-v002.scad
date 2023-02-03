length = 160;
thickness = 3;
channel_height = 16;
width = 40;

wedge_depth = 38;
wedge_height = 44;

overhang = (width - thickness * 2 - 8) / 2;

module wedge(h=5, w=overhang-thickness, l=8) {
    CubePoints = [
      [  0,  0,  0 ],  //0
      [  0,  0,  h ],  //1
      [  0,  l,  0 ],  //2
      [  w,  0,  0 ],  //3
      [  w,  0,  h ],  //4
      [  w,  l,  0 ]   //5
    ];
    CubeFaces = [
      [0,2,5,3],  // bottom
      [1,0,3,4],  // front
      [5,2,1,4],  // top
      [0,1,2],    // right
      [3,5,4]     // left
    ];
    polyhedron( CubePoints, CubeFaces );
}


translate([20, -125, 0]) {
    difference() {
        union() {
            // base
            cube([width, length, thickness]);
            // sides
            translate([0, 0, thickness])
            cube([thickness, length, channel_height]);
            translate([width-thickness, 0, thickness])
            cube([thickness, length, channel_height]);
            

            for(i = [0:1:length/8-1]) {
                translate([thickness, i*8, thickness])
                wedge();
                translate([width-overhang, i*8, thickness])
                wedge();
            }
            // channel tops
            translate([0, 0, channel_height+thickness])
            cube([width, length, thickness]);
        }
        // screw slide
        translate([width/2 - 3.5, thickness * 2, -1])
        cube([7, length-(thickness * 4), channel_height]);
        // screw slide
        translate([width/2 - 6, thickness * 2, channel_height])
        cube([12, length-(thickness * 4), channel_height]);
    }
}


// sled
translate([-20, 10, 0]) {
    difference() {
        union() {
            // base
            cube([width-2-thickness*2, 24, thickness]);
            translate([overhang-thickness, 0, thickness])
            cube([12, 24, channel_height - 6]);
            for(i = [0:1:2]) {
                translate([0, i*8, thickness])
                wedge();
                translate([width-overhang-2-thickness, i*8, thickness])
                wedge();
            }
         }
         translate([(width-2-thickness*2)/2, 12, -1])
         cylinder(h=30, r=4, center=true);
    }
}


// clamp-face
translate([-20-thickness, -40, 0])
difference() {
    union() {
        cube([width, wedge_depth, thickness * 2]);
        translate([0, 0, thickness * 2])
        cube([width, thickness, wedge_height]);

        translate([0, -thickness, thickness * 2 + wedge_height/2])
        cube([width, thickness, wedge_height/2]);

        translate([0, thickness, thickness * 2])
        wedge(h=wedge_height, w=thickness*2, l=wedge_depth-thickness);
        translate([width-thickness*2, thickness, thickness * 2])
        wedge(h=wedge_height, w=thickness*2, l=wedge_depth-thickness);
    }
    translate([width/2, width/2, -1])
    cylinder(h=30, r=4, center=true);
}

