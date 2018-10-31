import gui
import timer
import random


#Initialize global variables for future reference.
window = None
fadeRectangle = None
frameTimer = None

isRectangleFading = False
howFaded = None

houseOpen = None
isDoorOpen = False

carvedPumpkin = None
questionIcon = None
pumpkinHitbox = None
musicSound = None

textShown = False

output = []

isPumpkinCarved = False

creeperAnimating = False
creeperFrame = 0
creeperX = None
creeperY = None
creeperFrameDelay = 0

#Sorry for the excessive object oriented code here, I wanted to do this effect and had no idea how else to do it. -Brendan.
class Particle:
  global window
  
  #Classwide variable, contains a list of all currently extant objects of class Particle.
  particles = []
  
  #__init__: Create a new particle and set up the internal variables, as well as adding it to Particle.particles.
  #Arguments:
    #initX, type Int: The initial X position of the particle
    #initY, type Int: The initial Y position of the particle
    #initXVel, type Float: The initial velocity of the particle on the X axis.
    #initYVel, type Float: The initial velocity of the particle on the Y axis.
    #imageName, type String: The name of the image file in the media path.
  #Returns:
    #self, type Particle
  def __init__(self, initX, initY, initXVel, initYVel, imageName):
    self.x = initX
    self.y = initY
    self.xVel = initXVel
    self.yVel = initYVel
    self.yAccel = random.randint(8,12)/10.0
    
    #Keep track of how long the particle has been alive
    self.timeAlive = 0
    
    #Keep an internal reference to an icon and add it later
    self.icon = gui.Icon(getMediaPath(imageName))
    window.add(self.icon, self.x, self.y)
    
    #Add this particle to a class list of all particles.
    Particle.particles.append(self)
    
  #update: Update the position and icon of the particle.
  #Arguments:
    #None
  #Returns:
    #None
  def update(self):
    #Don't Let unnecessary particles stay around,
    #delete particles that have been around for half
    #a second.
    if self.timeAlive <= 30:
      #Get rid of the icon where it last was
      window.remove(self.icon)
    
      #Do some math to find the current velocities and positions.
      self.yVel = self.yVel + self.yAccel
      self.x = self.x + self.xVel
      self.y = self.y + self.yVel
    
      #Add our icon back in the new position.
      window.add(self.icon, int(self.x), int(self.y))
      
      self.timeAlive = self.timeAlive + 1
    #If it's been around for that long, remove it from
    #the window and from the list of extant particles.
    elif self.timeAlive > 30:
      window.remove(self.icon)
      Particle.particles.remove(self)
      
  
  #getParticles: A class method to return the list of particles, for encapsulation reasons.
  #Arguments:
    #None
  #Returns:
    #Particle.particles, type list of Particle
  @classmethod
  def getParticles(cls):
    return Particle.particles

#setup: Initialize all of the variables, icons, objects, and lists that the rest of the program will need, as well
#as setting up the event handlers for later.
#Arguments:
  #None
#Returns:
  #None
def setup():
  global window, frameTimer, fadeRectangle, carvedPumpkin, questionIcon, pumpkinHitbox, text, musicSound, icon1, creeperX, creeperY, houseOpen, output
  
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
  
  houseOpen = gui.Icon(getMediaPath("lightOnFixed.png"),640,480)
  
  doorHitbox = gui.Rectangle(395,233,479,275,gui.Color(0,0,0,0),true,0)
  doorHitbox.onMouseDown(openDoor)
  doorHitbox.onMouseEnter(questionOn2)
  doorHitbox.onMouseExit(questionOff)
  window.add(doorHitbox)
  
  icon1=gui.Icon(getMediaPath("creeper_0.png"))
  icon2=gui.Icon(getMediaPath("creeper_1.png"))
  icon3=gui.Icon(getMediaPath("creeper_2.png"))
  icon4=gui.Icon(getMediaPath("creeper_3.png"))
  #create output list
  output.append(icon1)
  output.append(icon2)
  output.append(icon3)
  output.append(icon4)
  #creeper coordinates
  creeperX=400
  creeperY=270

  window.remove(icon2)
  window.remove(icon3)
  window.remove(icon4)
  window.add(icon1,creeperX,creeperY)
  icon1.onMouseDown(startCreeperAnimation)

  fadeRectangle = gui.Rectangle(0,0,640,480,gui.Color(0,0,0,255),true,0)
  fadeRectangle.onMouseEnter(fadeInRectangle)
  window.add(fadeRectangle)
  
  questionIcon = gui.Icon(getMediaPath("question.png"), 50, 50)
  
  text = gui.Icon(getMediaPath("text.png"), 500, 57)
  
  frameTimer = timer.Timer(1000/60, update, [], true)
  frameTimer.start()
  musicSound = makeAndPlay(getMediaPath("minecraftmusic.wav"))
  
  #add creeper
  
#Description: Sets the creeper animation running.
#Arguments: x,y- Location of click
#Returns: None
def startCreeperAnimation(x,y): 
  global creeperX, creeperY, creeperAnimating
  if creeperAnimating == False:
    creeperAnimating = True

#cleanup: Reset all of the variables and delete instances to objects that no longer exist.
#Arguments:
  #None
#Returns:
  #None
def cleanup():
  global window, frameTimer, fadeRectangle, isPumpkinCarved, isRectangleFading, carvedPumpkin, pumpkinHitbox, questionIcon, musicSound, output, isDoorOpen, creeperFrame, textShown, creeperAnimating
  
  isPumpkinCarved = False
  isRectangleFading = False
  isDoorOpen = False
  creeperAnimating = False
  creeperFrame = 0
  textShown = False
  
  if frameTimer:
    frameTimer.stop()
  frameTimer = None
  
  if fadeRectangle:
    window.remove(fadeRectangle)
  fadeRectangle = None
  
  if carvedPumpkin:
    window.remove(carvedPumpkin)
  carvedPumpkin = None
  
  if pumpkinHitbox:
    window.remove(pumpkinHitbox)
  pumpkinHitbox = None
  
  if questionIcon:
    window.remove(questionIcon)
  questionIcon = None
  if not musicSound == None:
    stopPlaying(musicSound)
  
  output = []

  window = None

#fadeInRectangle: Starts the initial fadein and plays the thunder sound, also initializes the fading rectangle to the
#correct initial settings.
#Arguments:
  #x, x coordinate of click
  #y, y coordinate of click
#Returns:
  #None
def fadeInRectangle(x,y):
  global isRectangleFading, howFaded
  if isRectangleFading == False:
    makeAndPlay(getMediaPath("thunder1.wav"))
    isRectangleFading = True
    howFaded = 120
    fadeRectangle.setColor(gui.Color(0,0,0,255))

#carvePumpkin: Changes the pumpkins state to carved, as well as creating four particles to display
#Arguments:
  #x, x coordinate of click
  #y, y coordinate of click
#Returns:
  #None
def carvePumpkin(x,y):
  global window, carvedPumpkin, isPumpkinCarved, questionIcon
  if(isPumpkinCarved == False):
    makeAndPlay(getMediaPath("pumpkinHit.wav"))
    window.remove(questionIcon)
    window.add(carvedPumpkin)
    isPumpkinCarved = True
  #Create four particles with slightly different x and y velocities to start with.
  #Each starts at the location of click, then moves downward.
  #Each uses the same image file, particle.png.
  Particle(x+103,y+272,random.randint(-30,-10)/10.0,random.randint(-10,-1),"particle.png")
  Particle(x+103,y+272,random.randint(-30,-10)/10.0,random.randint(-10,-1),"particle.png")
  Particle(x+103,y+272,random.randint(10,30)/10.0,random.randint(-10,-1),"particle.png")
  Particle(x+103,y+272,random.randint(10,30)/10.0,random.randint(-10,-1),"particle.png")

#openDoor: Switches the state of the house to lit and door opened.
#Arguments:
  #x, x coordinate of click
  #y, y coordinate of click
#Returns:
  #None
def openDoor(x,y):
  global window, houseOpen, isDoorOpen, questionIcon
  if(isDoorOpen == False):
    makeAndPlay(getMediaPath("doorOpen.wav"))
    window.remove(questionIcon)
    window.add(houseOpen)
    isDoorOpen = True

#questionOn: Shows a questionmark icon over the pumpkin and plays a ding sound.
#Arguments:
  #x, x coordinate of click
  #y, y coordinate of click
#Returns:
  #None
def questionOn(x,y):
  global window, questionIcon, isPumpkinCarved
  if(isPumpkinCarved == False):
    window.add(questionIcon,125,225)
    makeAndPlay(getMediaPath("questionSound.wav"))

#questionOn: Shows a questionmark icon over the door and plays a ding sound.
#Arguments:
  #x, x coordinate of click
  #y, y coordinate of click
#Returns:
  #None
def questionOn2(x,y):
  global window, questionIcon, isDoorOpen
  if(isDoorOpen == False):
    window.add(questionIcon, 410, 180)
    makeAndPlay(getMediaPath("questionSound.wav"))


def questionOff(x,y):
  global window, questionIcon
  
  window.remove(questionIcon)
  

#This runs every frame and checks for things that need to happen, then makes them happen
def update():
  global fadeRectangle, isRectangleFading, isDoorOpen, isPumpkinCarved, howFaded, window, text, creeperAnimating, creeperFrame, creeperX, creeperY, output, creeperFrameDelay, textShown
  
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
  
  #Check to make sure other elements have been clicked before showing text
  if isDoorOpen == true and isPumpkinCarved == true:
    if textShown == False:
      window.add(text, 80, 85)
      textShown = True
    
  #Change the creeper animation.
  if creeperAnimating == True:
    if creeperFrameDelay <= 0:
      lastCreeperFrame = creeperFrame
      creeperFrame=(creeperFrame+1)%4
      window.add(output[creeperFrame],creeperX,creeperY)
      window.remove(output[lastCreeperFrame])
      creeperFrameDelay = 4
    else:
      creeperFrameDelay = creeperFrameDelay-1
  #Run the update() function of every particle that exists currently.
  for particle in Particle.getParticles():
    particle.update()

#make and play function to be activated when a function is clicked on
def makeAndPlay(file):
  sound=makeSound(file)
  play(sound)
  return sound

setup()
