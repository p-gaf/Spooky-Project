from gui import *
from timer import *
#create frames for creeper gif
def createIconsForCreeper():
  output=[]
  for i in range(0,51):
    filename="frame_"+str(i)+"_delay-0.05s.gif"
    icon=Icon(filename)
    output.append(icon)
  return output
  
def showFrame(display, frames, n):
  display.add(frames[n], 0, 0)
  
def removeFrame(display, frames, n):
  display.remove(frames[n])

def showNextFrame():
  global window, frames, currentFrame, totalFrames
  
  #increment current frame, but wrap around to 0 if >= totalFrames
  currentFrame = (currentFrame + 1) % totalFrames
  
  #show the new frame, it'll render on top of the old one
  showFrame(window, frames, currentFrame)
  
  #remove the old one from underneath
  removeFrame(window, frames, currentFrame - 1)

# make the JES media libraries know where to look
baseMediaPath = pickAFolder()
setMediaPath(baseMediaPath)

totalFrames=50
currentFrame=0

frames= createIconsForCreeper()
window= Display("creeper",400,400)

animationTimer=Timer(83,showNextFrame,[],True)
