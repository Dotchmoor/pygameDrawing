import pygame

class ui():
    def __init__(self, font="Italic", fontSize=30):
        pygame.font.init()
        self.uiFont = pygame.font.SysFont(font, fontSize)

        self.buttons = {}
        self.lables = {}
    
    def addButton(self, name, screen, text, textRelPosX, textRelPosY, x, y, width, height, backgroundColor, textColor, linkedFunction):
        self.buttons[name] = button(self.uiFont, screen, text, textRelPosX, textRelPosY, x, y, width, height, backgroundColor, textColor, linkedFunction)

    def addLable(self, name, screen, text, textRelPosX, textRelPosY, x, y, width, height, backgroundColor, textColor):
        self.lables[name] = lable(self.uiFont, screen, text, textRelPosX, textRelPosY, x, y, width, height, backgroundColor, textColor)

    def updateElements(self, mouseLeftClick):
        self.updateButtons(mouseLeftClick)
        for key, val in self.lables.items():
            val.paint()
    	
    def updateButtons(self, mouseLeftClick):
        for key, val in self.buttons.items():
            val.paint()
            
            if mouseLeftClick:
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseX > val.x and mouseX < val.x+val.width and mouseY > val.y and mouseY < val.y+val.height:
                    if val.released == True:
                        val.isClicked()
                        val.released = False
            else:
                if val.released == False:
                    val.onRelease()
                    val.released = True
                    val.backgroundColor = val.backgroundOGColor

class uiElement():
    def __init__(self, font, screen, text="", textRelPosX=0, textRelPosY=0, x=0, y=0, width=20, height=20, backgroundColor=[100, 100, 100], textColor=[0, 0, 0]):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.backgroundOGColor = backgroundColor
        self.backgroundColor = backgroundColor
        self.text = text
        self.textColor = textColor
        self.textRelPosX = textRelPosX
        self.textRelPosY = textRelPosY
        self.font = font
        self.textSurface = font.render(text, False, textColor)

    def paint(self):
        pygame.draw.rect(self.screen, self.backgroundColor, (self.x, self.y, self.width, self.height))
        self.screen.blit(self.textSurface, (self.x+self.textRelPosX, self.y+self.textRelPosY))
    
    def changeText(self, newText):
        self.textSurface = self.font.render(newText, False, self.textColor)

class button(uiElement):
    def __init__(self, font, screen, text, textRelPosX, textRelPosY, x, y, width, height, backgroundColor, textColor, function):
        super().__init__(font, screen, text, textRelPosX, textRelPosY, x, y, width, height, backgroundColor,  textColor)
        
        self.linkedFunction = function
        self.released = True

    def isClicked(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseX >= self.x and mouseX < self.x + self.width and mouseY >= self.y and mouseY <= self.y + self.height:
            newR, newG, newB = self.backgroundColor[0]+30, self.backgroundColor[1]+30, self.backgroundColor[2]+30
            if newR > 255: newR = 255
            if newG > 255: newG = 255
            if newB > 255: newB = 255
            self.backgroundColor = [newR, newG, newB]

    def onRelease(self):
        self.linkedFunction()

class lable(uiElement):
    def __init__(self, font, screen, text, textRelPosX, textRelPosY, x, y, width, height, backgroundColor,  textColor):
        super().__init__(font, screen, text, textRelPosX, textRelPosY, x, y, width, height, backgroundColor,  textColor)
        