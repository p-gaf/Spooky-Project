import gui
import timer


window = None
fadeRectangle = None
frameTimer = None

def setup():
  global window, frameTimer
  window = gui.Display("Minecard", 640,480)
  
  fadeRectangle = gui.Rectangle(0,0,640,480,gui.Color(0,0,0,255),true,0)
  window.add(fadeRectangle)
  
  frameTimer = timer.Timer(1000/60, update, [], true)

def update():
  pass

#make and play function to be activated when a function is clicked on
def makeAndPlay(file):
  sound=makeSound(file)
  play(sound)

  
