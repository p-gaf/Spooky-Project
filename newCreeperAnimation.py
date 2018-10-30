import gui
import time

baseMediaPath=pickAFolder()
setMediaPath(baseMediaPath)

icon1=gui.Icon(baseMediaPath+"creeper_0.png")
icon2=gui.Icon(baseMediaPath+"creeper_1.png")
icon3=gui.Icon(baseMediaPath+"creeper_2.png")
icon4=gui.Icon(baseMediaPath+"creeper_3.png")
#create output list
output=[]
output.append(icon1)
output.append(icon2)
output.append(icon3)
output.append(icon4)
#attach the output to frames variable
#add gui window
window=gui.Display("Animation",400,400)
def startAnimation(x,y):
  while true:
    window.add(output[1],x,y)
    window.remove(output[0])
    time.sleep(1)
    window.add(output[2],x,y)
    window.remove(output[1])
    time.sleep(1)
    window.add(output[3],x,y)
    window.remove(output[2])
    time.sleep(1)
    window.add(output[0],x,y)
    window.remove(output[3])
    time.sleep(1)
  


#seperate functions for adding next frame
def showFrame(window, output, n):
  window.add(output[n], 0, 0)
  
def removeFrame(window, output, n):
  window.remove(output[n])

def showNextFrame():
  global window, output, currentFrame, totalFrames
  
  #increment current frame, but wrap around to 0 if >= totalFrames
  currentFrame = (currentFrame + 1) % totalFrames
  
  #show the new frame, it'll render on top of the old one
  showFrame(window, output, currentFrame)
  
  #remove the old one from underneath
  removeFrame(window, output, currentFrame - 1)

#frame variablres
totalFrames=4
currentFrame=0
#animation running program
animationTimer=Timer(83,showNextFrame(),[],True)