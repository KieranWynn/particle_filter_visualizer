# Particle Filter Visualizer

This is a simple python module to enable insight into Udacity's
[Artificial Intelligence for Robotics](https://www.udacity.com/course/artificial-intelligence-for-robotics--cs373) course.
This particular example is targeted for [Lesson 3 : Particle Filters] and the problem set associated with it.

The visualizer uses matplotlib and it's pyplot API, so make sure you have this installed:

	pip install matplotlib

Then copy the particle_filter_visualizer.py file to your local working directory.
From there you can add the following code into the main loop of the provided particle_filter() method.


	from particle_filter_visualizer import ParticleViewer, WeightsViewer
	
	...
	
	show_plot = True
	
	...
	
	def particle_filter(motions, measurements, N=500):
	
	...
	
		if show_plot:
		
            # Create a matplotlib figure to view particles
            pv = ParticleViewer()
            pv.set_bounds((-30,150), (-30,150))

            # Add the landmarks to the plot
            pv.add_landmarks(landmarks)

            # Add the current particle set
            pv.add_particles(p)

            # Add the 'mean' particle
            pose = get_position(p)
            r = robot()
            r.set(*pose)
            # Display what the measurement looks like from the POV of the mean particle
            pv.add_measurements(r, measurements[t])
            # Display the figure
            pv.show()
            raw_input()
  
  
Unfortunately matplotlib is not great at realtime plotting (especially on OS X ), so the use of `raw_input()` here allows you to pause the program flow within each loop iteration to view the generated figure. Execution will continue when you hit enter in your shell running the above python script. You don't have to close each figure manually, they'll die at the end of program execution.