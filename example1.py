from motion import Simulation


file = "02.jpg"
#func = lambda x: 1 / (x**5)
func = None

s = Simulation(file=file, func=func)
s.run()
s.play()
