import gui
import timer
import random

window = None
fadeRectangle = None
frameTimer = None

isRectangleFading = False
howFaded = None

carvedPumpkin = None
questionIcon = None
musicSound = None

isPumpkinCarved = False

#Setup, make everything exist.
def setup():
  global window, frameTimer, fadeRectangle, carvedPumpkin, questionIcon, musicSound
  
  cleanup()

  setMediaPath(pickAFolder())
  window = gui.Display("Minecard", 640,480)
  
  baseState = gui.Icon(getMediaPath("baseState.jpg"),640,480)
  window.add(baseState, 0, 0)
  
  carvedPumpkin = gui.Icon(getMediaPath("croppedPumpkinCarved.png"),640,480)
  
  pumpkinHitbox = gui.Rectangle(103,272,190,334,gui.Color(0,0,0,0),true,0)
  pumpkinHitbox.onMouseDown(carvePumpkin)
  pumpkinHitbox.onMouseEnter(questionOn)
  pumpkinHitbox.onMouseExit(questionOff)
  window.add(pumpkinHitbox)
  
  fadeRectangle = gui.Rectangle(0,0,640,480,gui.Color(0,0,0,255),true,0)
  fadeRectangle.onMouseEnter(fadeInRectangle)
  window.add(fadeRectangle)
  
  questionIcon = gui.Icon(getMediaPath("question.png"), 50, 50)
  
  frameTimer = timer.Timer(1000/60, update, [], true)
  frameTimer.start()
  musicSound = makeAndPlay(getMediaPath("minecraftmusic.wav"))
  
  #Todo: music stuff. 
  #Make a timer for music that runs every time the music ends
  #Start it on the fade click
  #Keep track of the same sound file so we can stop it and or start it later.

#Delete everything and make sure we're working from a clean slate.
#Todo: if anything gets added to setup, make sure to clean it up here!
def cleanup():
  global window, frameTimer, fadeRectangle, musicSound
  
  if frameTimer:
    frameTimer.stop()
  frameTimer = None
  
  if fadeRectangle:
    window.remove(fadeRectangle)
  fadeRectangle = None
  
  if not musicSound == None:
    stopPlaying(musicSound)
  
  window = None

#Starts the fade
def fadeInRectangle(x,y):
  global isRectangleFading, howFaded
  if isRectangleFading == False:
    makeAndPlay(getMediaPath("thunder1.wav"))
    isRectangleFading = True
    howFaded = 120
    fadeRectangle.setColor(gui.Color(0,0,0,255))

def carvePumpkin(x,y):
  global window, carvedPumpkin, isPumpkinCarved, questionIcon
  window.remove(questionIcon)
  window.add(carvedPumpkin)
  isPumpkinCarved = True
  
def questionOn(x,y):
  global window, questionIcon, isPumpkinCarved
  if(isPumpkinCarved == False):
    window.add(questionIcon,125,225)

def questionOff(x,y):
  global window, questionIcon
  
  window.remove(questionIcon)

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
      

#make and play function to be activated when a function is clicked on
def makeAndPlay(file):
  sound=makeSound(file)
  play(sound)
  return sound

def monsterClick(x,y):
  #two functions inside, one to play sound, and one to animate
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
#creeper=gui.Icon(,random.randInt(0,640),random.randInt(0,480))
#zombie=gui.Icon(,random.randInt(0,640),random.randInt(0,480))
#skeleton=gui.Icon(,random.randInt(0,640),random.randInt(0,480))
#testcomment

setup()
