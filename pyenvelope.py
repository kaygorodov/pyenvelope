from shapely.geometry import MultiPoint
from shapely.affinity import rotate
import math


def get_minimum_bounding_rectangle(points):
    obj = MultiPoint(points)
    convex_hull = obj.convex_hull
    rotating_center = convex_hull.centroid
    convex_hull_points = convex_hull.exterior.coords
    min_area = None
    mbr = None
    mbr_angle = None

    for i in range(len(convex_hull_points) - 2):
        point_a = points[i]
        point_b = points[i + 1]

        opposite = point_b[1] - point_a[1]
        adjacent = point_b[0] - point_a[0]

        if adjacent == 0:
            angle = math.pi / 2
        else:
            angle = math.atan(opposite / float(adjacent))

        obj_rotated = rotate(convex_hull, -angle, origin=rotating_center,
                             use_radians=True)

        if min_area is None or obj_rotated.envelope.area < min_area:
            min_area = obj_rotated.envelope.area
            mbr = obj_rotated.envelope
            mbr_angle = angle

    # rotate back
    mbr = rotate(mbr, mbr_angle, origin=rotating_center, use_radians=True)

    # return rectangle vertices coordinates
    return list(mbr.exterior.coords)
