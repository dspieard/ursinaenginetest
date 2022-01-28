from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def update():
    if held_keys['left mouse']:
        axe.active()
    else:
        axe.passive()

def input(key):
    if enemy:
        if key == 'left mouse down' and distance(player, enemy) < 2:
            if enemy.hovered:
                destroy(enemy)

class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'grass',
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.lime
        )
    

class Axe(Entity):
    def __init__(self):
        super().__init__(
            model= "assets/axe2.obj", 
            parent=camera.ui, 
            position = (.3, -.2), 
            scale=0.2, 
            rotation= Vec3(270,45,0),
            collider = 'box'
        )

    def active(self):
        self.rotation = Vec3(250,45,20)
        position = (.3, -.2)

    def passive(self):
        self.rotation = Vec3(290,45,0)
        position = (.5, -.4)

class Enemy(Button):
    def __init__(self):
        super().__init__(
            model= 'assets/basicCharacter.fbx', 
            parent=scene,
            scale=0.2,
            position= (10,0,10),
            color = color.white,
            texture = 'assets/skin_orc.png',
            collider = 'box',
            health = 5  
            )
    


app = Ursina()
axe= Axe()
enemy = Enemy()

sky=Sky()

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x, 0, z))

player = FirstPersonController()

app.run()
