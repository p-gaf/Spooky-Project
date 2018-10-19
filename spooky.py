import gui


window = None

def setup():
  global window
  window = gui.Display("Minecard", 640,480)

#make and play function to be activated when a function is clicked on
def makeAndPlay(file):
  sound=makeSound(file)
  play(sound)
def monsterClick(x,y):
  #two functions inside, one to play sound, and one to animate
  #Include a file extension
  makeAndPlay(file)
  #Add an animation function

  
