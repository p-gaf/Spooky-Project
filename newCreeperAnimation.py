import gui
import timer

baseMediaPath=pickAFolder()
setMediaPath(baseMediaPath)

icon1=gui.Icon(baseMediaPath+"creeper_0.gif")
icon2=gui.Icon(baseMediaPath+"creeper_1.gif")
icon3=gui.Icon(baseMediaPath+"creeper_2.gif")
icon4=gui.Icon(baseMediaPath+"creeper_3.gif")

#add gui window
window=Display("Animation",400,400)
#test 
window.add(icon1,200,200)
#seperate functions for adding next frame
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


#function to delete previous frame
#function to run it all