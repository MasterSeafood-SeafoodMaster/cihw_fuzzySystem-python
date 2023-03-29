import numpy as np
import math

def getSquare(path):
	f = open(path, 'r')
	lines = f.readlines()
	car_pos = lines.pop(0).replace("\n", "").split(",")
	start = lines.pop(0).replace("\n", "").split(",")
	end = lines.pop(0).replace("\n", "").split(",")

	square = []
	for line in lines:
		l = line.replace("\n", "")
		square.append(l.split(","))

	square = np.array(square, dtype=np.float)
	car_pos = np.array(car_pos, dtype=np.float)
	endline = np.array([start,end], dtype=np.float)

	return square, car_pos, endline

def nextPos(x, y, ang, theta):
	r_ang = math.radians(ang)
	r_theta = math.radians(theta)

	nx = x + math.cos( math.radians(ang+theta) ) + (math.sin( math.radians(theta) )*math.sin( math.radians(ang) ))
	ny = y + math.sin( math.radians(ang+theta) ) - (math.sin( math.radians(theta) )*math.cos( math.radians(ang) ))

	nang = math.radians(ang) - math.asin( (math.sin( math.radians(theta) )*2)/6 )
	nang = nang*(180/math.pi)

	#print(nx-x, ny-y, nang)

	return np.array([nx, ny, nang], dtype=np.float)

def draw_sensors(x, y, angle, walls):

    # Calculate the positions of the three sensors
    front_sensor = np.array([x, y]) + 50 * np.array([math.cos(math.radians(angle)), math.sin(math.radians(angle))])
    left_sensor = np.array([x, y]) + 50 * np.array([math.cos(math.radians(angle + 45)), math.sin(math.radians(angle + 45))])
    right_sensor = np.array([x, y]) + 50 * np.array([math.cos(math.radians(angle - 45)), math.sin(math.radians(angle - 45))])

    # Calculate the distances from each sensor to the nearest wall
    front_distances = np.sqrt(np.sum((walls - front_sensor) ** 2, axis=1))
    left_distances = np.sqrt(np.sum((walls - left_sensor) ** 2, axis=1))
    right_distances = np.sqrt(np.sum((walls - right_sensor) ** 2, axis=1))

    print(front_sensor, left_sensor, right_sensor)

    return front_sensor, left_sensor, right_sensor, front_distances.min(), left_distances.min(), right_distances.min()


def intersection(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x4 - x3, y4 - y3
    t = (dx2 * (y3 - y1) + dy2 * (x1 - x3)) / denom
    x, y = x1 + t * dx1, y1 + t * dy1
    return x, y


def inBox(x, y):
	return 18 <= x <= 30 and 37 <= y <= 40