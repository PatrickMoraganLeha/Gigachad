# напиши здесь код создания и управления картой
class Mapmanager(): 
    """Управление картой""" 
    def __init__(self): 
        self.colors =[
            (0.5,0.2,0.35,1),
            (0.8,0.5,0.2,1),
            (0.3,0.2,0.2,1),
            (0.2,0.3,0.0,1)
        ]
        self.model = 'block' 
        self.texture = 'block.png' 
        self.block = loader.loadModel(self.model) 
        self.block.setTexture(loader.loadTexture(self.texture)) 
        self.color = (0.2, 0.2, 0.35, 1) 
        self.startNew() 
        self.addBlock((0,10,0)) 
        self.startNew()
    def startNew(self): 
        self.land = render.attachNewNode("Land")
         
    def addBlock(self,position): 
        self.block = loader.loadModel(self.model) 
        self.block.setTexture(loader.loadTexture(self.texture)) 
        self.block.setPos(position) 
        self.block.setColor(self.color) 
        self.block.reparentTo(self.land)
        self.color=self.getColor(int(position[2]))
        self.block.setColor(self.color)


    def getColor(self,z):
        
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors)-1]
        
    
    
    def clear(self):
        self.land.removeNode()
        self.startNew()
    def loadLand(self,filename):
        #создает карту земли из текстого файла возврощяет ее размеры
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line=line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x,y,z0))
                    x +=1
                y +=1
