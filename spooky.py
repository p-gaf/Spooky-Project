import gui


window = None

def setup():
  global window
  window = gui.Display("Minecard", 640,480)

#make and play function to be activated when a function is clicked on
def makeAndPlay(file):
  sound=makeSound(file)
  play(sound)

  
