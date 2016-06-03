"""
http://www.geeksforgeeks.org/find-two-rectangles-overlap/
"""

def doOverlap(l1,r1,l2,r2):
	if l1.x > r2.x or l2.x > r1.x:
		return False
	if l1.y < r2.y or l2.y < r1.y:
		return False
	return True





rect1_x_radius = (x2-x1)/2
rect1_y_radius = (y2-y1)/2

rect2_x_radius = (x4-x3)/2
rect2_y_radius = (y4-y3)/2

midAx = x1 + rect1_x_radius
midBx = x3 + rect2_x_radius

midAy = y1 + rect1_y_radius
midBy = y3 + rect2_y_radius

mid_dist_x = abs(midAx-midBx)
mid_dist_y = abs(midAy-midBy)

if mid_dist_x > rect1_x_radius + rect2_x_radius or mid_dist_y > rect1_y_radius + rect2_y_radius
