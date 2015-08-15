
import matplotlib.pyplot as pyplot
from math import sin, cos, degrees, pi

class ParticleViewer:

	def __init__(self):
		self.figure = pyplot.figure()
		self.axes = self.figure.gca()
		pyplot.xlabel("X")
		pyplot.ylabel("Y")
		self.xbounds = [0,1]
		self.ybounds = [0,1]

	def clear(self):
		self.axes.cla()

	def add_landmark(self, x, y, color='g', radius=4.0):
		c=pyplot.Circle((x,y),radius,color=color)
		self.axes.add_artist(c)

	def add_landmarks(self, landmarks, colors=['r', 'g', 'b', 'y']):
		for landmark, color in zip(landmarks, colors):
			self.add_landmark(landmark[1], landmark[0], color)

	def add_measurement(self, robot, measurement=0.0, color='r', length=200):
		lx = [robot.x, robot.x + (length * cos(robot.orientation + measurement))]
		ly = [robot.y, robot.y + (length * sin(robot.orientation + measurement))]
		l = pyplot.Line2D(lx, ly, linewidth=1, color=color)
		self.axes.add_artist(l)

	def add_measurements(self, robot, measurements, colors=['r', 'g', 'b', 'y'], length=200):
		for measurement, color in zip(measurements, colors):
			self.add_measurement(robot, measurement, color, length)

	def add_particle(self, x, y, orientation=0.0, radius=1.0, color='k'):
		c=pyplot.Circle((x,y),radius,color=color)
		lw = 1.5 * radius
		lh = 0.5 * radius
		x_offset = (lh / 2.0) * sin(orientation)
		y_offset = (lh / 2.0) * cos(orientation)
		l = pyplot.Rectangle((x + x_offset, y - y_offset), lw ,lh, degrees(orientation))
		self.axes.add_artist(c)
		self.axes.add_artist(l)

	def add_particles(self, p, weights=[]):
		if weights:
			for robot, size in zip(p, weights):
				self.add_particle(robot.x, robot.y, robot.orientation, size / 4.0)
		else:
			for robot in p:
				self.add_particle(robot.x, robot.y, robot.orientation)

	def set_bounds(self, x_tuple, y_tuple):
		self.xbounds = list(x_tuple)
		self.ybounds = list(y_tuple)

	def show(self):
		self.axes.set_xlim(self.xbounds)
		self.axes.set_ylim(self.ybounds)
		self.axes.set_aspect('equal', adjustable='box')
		self.figure.show()


class WeightsViewer:

	def __init__(self):
		self.figure = pyplot.figure()
		self.axes = self.figure.gca()
		pyplot.xlabel("Index")
		pyplot.ylabel("Weight")

	def showWeights(self, weights):
		self.axes.plot(weights, 'bs')
		self.figure.show()


