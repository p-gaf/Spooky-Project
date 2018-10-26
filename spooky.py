import gui
import timer
import random

window = None
fadeRectangle = None
frameTimer = None

def setup():
  global window, frameTimer

  setMediaPath(pickAFolder())
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

def monsterClick(x,y):
  #two functions inside, one to play sound, and one to animate
  #Include a file extension
  makeAndPlay(file)
  #Add an animation function
#create frames for creeper gif
def createIconsForCreeper(suffix):
  output=[]
  for i in range(0,51):
    filename="frame_0"+str(i)+"_delay-0.05s.gif"
    icon=gui.Icon(filename,300)
    output.append(icon)
    
    
 


#Insert icons into gui window, 
zombie=gui.Icon(,random.randInt(0,640),random.randInt(0,480))
skeleton=gui.Icon(,random.randInt(0,640),random.randInt(0,480))


setup()