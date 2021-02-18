import pygame, ui

def drawPixel(pixelSize, pixelRed, pixelGreen, pixelBlue):
    x, y = pygame.mouse.get_pos()
    if x < drawingField:
        pygame.draw.rect(screen, (pixelRed, pixelGreen, pixelBlue), (x-int(pixelSize/2), y-int(pixelSize/2), pixelSize, pixelSize))


#### pixel size functions ####
def incrPixelSize():
    global pixelSize
    pixelSize += 1

def decrPixelSize():
    global pixelSize
    if pixelSize > 0:
        pixelSize -= 1

#### color functions ####
def incrPixelRed():
    global pixelRed
    if pixelRed < 255:
        pixelRed += 1

def decrPixelRed():
    global pixelRed
    if pixelRed > 0:
        pixelRed -= 1

def incrPixelGreen():
    global pixelGreen
    if pixelRed < 255:
        pixelGreen += 1

def decrPixelGreen():
    global pixelGreen
    if pixelGreen > 0:
        pixelGreen -= 1

def incrPixelBlue():
    global pixelBlue
    if pixelRed < 255:
        pixelBlue += 1

def decrPixelBlue():
    global pixelBlue
    if pixelBlue > 0:
        pixelBlue -= 1

if __name__ == "__main__":
    
    pygame.init()
    hud = ui.ui()

    drawingField = 600
    settings = 300
    screen = pygame.display.set_mode((drawingField+settings, 600))

    global pixelSize
    pixelSize = 1
    
    #### pixel size ####
    hud.addButton("pixelSizeM", screen, "-", 22, 14, drawingField+50, 50, 50, 50, (100, 100, 100), (200, 200, 200), decrPixelSize)
    hud.addLable("pixelSize", screen, f"{pixelSize}", 40, 16, drawingField+100, 50, 100, 50, (200, 200, 200), (0, 0, 0))
    hud.addButton("pixelSizeP", screen, "+", 20, 14, settings+drawingField-100, 50, 50, 50, (100, 100, 100), (200, 200, 200), incrPixelSize)

    global pixelRed
    pixelRed = 255

    #### pixel red ####
    hud.addLable("Red", screen, "R: ", 20, 16, drawingField+25, 150, 50, 50, (200, 200, 200), (0, 0, 0))
    hud.addButton("pixelRedM", screen, "-", 22, 14, drawingField+75, 150, 50, 50, (100, 100, 100), (200, 200, 200), decrPixelRed)
    hud.addLable("pixelRedVal", screen, f"{pixelRed}", 40, 16, drawingField+125, 150, 100, 50, (200, 200, 200), (0, 0, 0))
    hud.addButton("pixelRedP", screen, "+", 20, 14, settings+drawingField-75, 150, 50, 50, (100, 100, 100), (200, 200, 200), incrPixelRed)

    global pixelGreen
    pixelGreen = 255

    #### pixel Green ####
    hud.addLable("Green", screen, "G: ", 20, 16, drawingField+25, 250, 50, 50, (200, 200, 200), (0, 0, 0))
    hud.addButton("pixelGreenM", screen, "-", 22, 14, drawingField+75, 250, 50, 50, (100, 100, 100), (200, 200, 200), decrPixelGreen)
    hud.addLable("pixelGreenVal", screen, f"{pixelGreen}", 40, 16, drawingField+125, 250, 100, 50, (200, 200, 200), (0, 0, 0))
    hud.addButton("pixelGreenP", screen, "+", 20, 14, settings+drawingField-75, 250, 50, 50, (100, 100, 100), (200, 200, 200), incrPixelGreen)

    global pixelBlue
    pixelBlue = 255

    #### pixel Blue ####
    hud.addLable("Blue", screen, "B: ", 20, 16, drawingField+25, 350, 50, 50, (200, 200, 200), (0, 0, 0))
    hud.addButton("pixelBlueM", screen, "-", 22, 14, drawingField+75, 350, 50, 50, (100, 100, 100), (200, 200, 200), decrPixelBlue)
    hud.addLable("pixelBlueVal", screen, f"{pixelBlue}", 40, 16, drawingField+125, 350, 100, 50, (200, 200, 200), (0, 0, 0))
    hud.addButton("pixelBlueP", screen, "+", 20, 14, settings+drawingField-75, 350, 50, 50, (100, 100, 100), (200, 200, 200), incrPixelBlue)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exit()
        
        pygame.draw.rect(screen, (255, 255, 255), (drawingField, 0, settings, 600))

        mouseL = pygame.mouse.get_pressed()[0]
        if mouseL: drawPixel(pixelSize, pixelRed, pixelGreen, pixelBlue)

        hud.lables["pixelSize"].changeText(f"{pixelSize}")

        hud.lables["pixelRedVal"].changeText(f"{pixelRed}")
        hud.lables["pixelGreenVal"].changeText(f"{pixelGreen}")
        hud.lables["pixelBlueVal"].changeText(f"{pixelBlue}")

        hud.updateElements(mouseL)
        pygame.display.update()