import gui
import timer
import random

window = None
fadeRectangle = None
frameTimer = None

isRectangleFading = False
howFaded = None

#Setup, make everything exist.
def setup():
  global window, frameTimer, fadeRectangle
  
  cleanup()

  setMediaPath(pickAFolder())
  window = gui.Display("Minecard", 640,480)
  
  fadeRectangle = gui.Rectangle(0,0,640,480,gui.Color(0,0,0,255),true,0)
  fadeRectangle.onMouseDown(fadeInRectangle)
  window.add(fadeRectangle)
  
  frameTimer = timer.Timer(1000/60, update, [], true)
  frameTimer.start()
  
  #Todo: music stuff. 
  #Make a timer for music that runs every time the music ends
  #Start it on the fade click
  #Keep track of the same sound file so we can stop it and or start it later.

#Delete everything and make sure we're working from a clean slate.
#Todo: if anything gets added to setup, make sure to clean it up here!
def cleanup():
  global window, frameTimer, fadeRectangle
  
  if frameTimer:
    frameTimer.stop()
  del frameTimer
  
  if fadeRectangle:
    window.remove(fadeRectangle)
  del fadeRectangle
  
  del window

#Starts the fade
def fadeInRectangle(x,y):
  global isRectangleFading, howFaded
  if isRectangleFading == False:
    isRectangleFading = True
    howFaded = 120

#This runs every frame and checks for things that need to happen, then makes them happen
def update():
  global fadeRectangle, isRectangleFading, howFaded, window
  
  #Is our black screen fading in?
  if isRectangleFading == True:
    #If we should still be fading in, do
    if howFaded > 0:
      #Make a color based on how faded in we are
      fadeColor = gui.Color(0,0,0,(howFaded/120.0))
      fadeRectangle.setColor(fadeColor)
      #Make it more faded in
      howFaded = howFaded-1
    else:
      #We're done fading, so stop fading and delete the rectangle.
      isRectangleFading = False
      window.remove(fadeRectangle)
      del fadeRectangle
      

#make and play function to be activated when a function is clicked on
def makeAndPlay(file):
  sound=makeSound(file)
  play(sound)
  return sound

def monsterClick(x,y):
  #two functions inside, one to play sound, and one to animate
  #Include a file extension
  makeAndPlay(file)
  #Add an animation function

#Insert icons into gui window, 
#creeper=gui.Icon(,random.randInt(0,640),random.randInt(0,480))
#zombie=gui.Icon(,random.randInt(0,640),random.randInt(0,480))
#skeleton=gui.Icon(,random.randInt(0,640),random.randInt(0,480))


setup()
