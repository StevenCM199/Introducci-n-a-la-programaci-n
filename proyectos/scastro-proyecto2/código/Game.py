import sys, pygame
import random                       
from pygame.locals import *
from math import *


pygame.mixer.pre_init (44100,16,8,4096)
pygame.init()

ANCHO  = 1380
ALTO = 800
PANTALLA = pygame.display.set_mode((ANCHO,ALTO))
FPS    = pygame.time.Clock()


blanco = (255,255,255)
pygame.display.set_caption('PyDeathRace')

pista1 = pygame.transform.scale(pygame.image.load('media/nivel1Pista.png').convert_alpha(),(ANCHO,ALTO))#Las imagenes de la carretera para cada nivel
pista2 = pygame.transform.scale(pygame.image.load('media/nivel2Pista.png').convert_alpha(),(ANCHO,ALTO))
pista3 = pygame.transform.scale(pygame.image.load('media/nivel3Pista.png').convert_alpha(),(ANCHO,ALTO))

pts = pygame.transform.scale(pygame.image.load('media/puntos.png').convert_alpha(),(270,240)) #La imagen del cuadro de los puntos

todos_los_sprites = pygame.sprite.Group()
font_name = pygame.font.match_font('arial')

#Estas son las variables de los niveles, controlan todos los objetos que deben dibujarse para cada nivel
lvl1 = True
lvl2 = False
lvl3 = False

#La musica de fondo de los tres niveles
if lvl1 == True:
    pygame.mixer.music.load ("media/track1.ogg")
    pygame.mixer.music.set_volume (0.5)
    pygame.mixer.music.play (-1)

if lvl2 == True:
    pygame.mixer.music.load ("media/track2.ogg")
    pygame.mixer.music.set_volume (0.5)
    pygame.mixer.music.play (-1)

if lvl3 == True:
    pygame.mixer.music.load ("media/track3.ogg")
    pygame.mixer.music.set_volume (0.5)
    pygame.mixer.music.play (-1)

#La funcion de la puntuacion y el tiempo
def draw_text(surf,text,size,x,y): 
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface,text_rect)
    
# La clase del carro del jugador
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        start_pos = (73, 370)           
        start_angle = 90
        self.x     = start_pos[0]
        self.y     = start_pos[1]
        self.angle = start_angle
        self.speed = 0
        
        self.image = pygame.transform.scale(pygame.image.load("media/Car.png").convert_alpha(), (48, 48))
        self.rect = self.image.get_rect().inflate(-8,-8)


#Se cambian las coordenadas de aparicion segun el nivel en el que se encuentre
        if lvl2 == True:
            self.x = 725
            self.y = 78
            self.angle = 0

        if lvl3 == True:
            self.x = 1324
            self.y = 346
            self.angle = -90
            
            
#Funcion del movimiento del carro                                                                  
    def move(self): 
        keys = pygame.key.get_pressed()
                                        
        self.forward_speed = 0.5          
        self.rearward_speed = 0.2
        self.max_speed = 5
        self.max_reverse = -5

        if keys[K_a] or keys[K_LEFT]:
            self.angle += self.speed
        if keys[K_d] or keys[K_RIGHT]:
            self.angle -= self.speed
        if keys[K_w] or keys[K_UP]:
            self.speed += self.forward_speed
        if keys[K_s] or keys[K_DOWN]:
            self.speed -= self.rearward_speed

# limitador de velocidad
        if self.speed > self.max_speed: 
            self.speed = self.max_speed

        if self.speed < self.max_reverse:
            self.speed = self.max_reverse


        self.angle %= 359
        
# Bordes del juego, el carro no puede salir de los bordes
        if self.x < 0:
            self.x = 1
        if self.x > 1380:
            self.x = 1379
        if self.y < 0:
            self.y = 1
        if self.y > 800:
            self.y = 799


        self.x += self.speed * cos(radians(self.angle))    
        self.y -= self.speed * sin(radians(self.angle))

#Dibuja el carro en la pantalla tomando en cuenta su rotacion
    def render(self): 
        self.rotcar   = pygame.transform.rotate(self.image, self.angle)
        self.rotcar_rect = self.rotcar.get_rect(center = (self.x, self.y))
        PANTALLA.blit(self.rotcar, self.rotcar_rect)

#Metodo del carro para disparar balas
    def disparar(self): 
        global balas 
        bullet = Bullet(self.x,self.y)
        balas.add(bullet)
        todos_los_sprites.add(bullet)


        
class Bullet(pygame.sprite.Sprite): #Clase de la bala
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        car = Car() 
        self.image = pygame.transform.scale(pygame.image.load("media/bala.png").convert_alpha(),(15,15))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.speed = 10
        self.time = 2
        self.angle = car.angle

#Esta funcion se encarga del movimiento de la bala
    def update(self):

        self.rect.x += self.speed * cos(radians(self.angle))    
        self.rect.y -= self.speed * sin(radians(self.angle))      

#La bala desaparece cuando sale de la pantalla
        if  self.rect.x < 0 or self.rect.x > 1380:
            self.kill()
            
        if self.rect.y < 0 or self.rect.y > 800:
            self.kill()

#Esta es la clase de los limites del nivel 1, entiendase limites como la parte exterior a la carretera
class Nivel1(pygame.sprite.Sprite): 
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('media/nivel1Limites.png').convert_alpha(),(ANCHO,ALTO))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    
#Limites del nivel 2
class Nivel2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('media/nivel2Limites.png').convert_alpha(),(ANCHO,ALTO))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#Bordes del nivel 2, estos "bordes" son la pared de llantas por la que el carro rebota si choca contra ellas
class Bor2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('media/nivel2Bordes.png').convert_alpha(),(ANCHO,ALTO))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#Limites del nivel 3
class Nivel3(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('media/nivel3Limites.png').convert_alpha(),(ANCHO,ALTO))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#Bordes del nivel 3
class Bor3(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('media/nivel3Bordes.png').convert_alpha(),(ANCHO,ALTO))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#Clase de los conos
class Cono(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load("media/cono.png").convert_alpha(),(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#Clase de las rocas
class Roca(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load("media/roca.png").convert_alpha(),(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y  
#Clase de las manchas
class Mancha(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load("media/mancha.png").convert_alpha(),(40,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#Clase de los dummy vehicles   
class Dummies(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load("media/bot1.png").convert_alpha(), (48, 48))
        self.rect = self.image.get_rect().inflate(-8,-8)
        self.rect.x = random.randint(50,100)
        self.rect.y = random.randint(370,430) 
        self.speed = random.randint(3,7)       
        self.angle = 360

        #Variables de movimiento
        self.up = True 
        self.down = False
        self.left = False
        self.right = False 

        if lvl2 == True: #Coordenadas de los dummies en el nivel 2
            self.rect.x = random.randint(660,720)
            self.rect.y = random.randint(50,100)

        if lvl3 == True:
            self.rect.x = random.randint(1230,1315) #Coordenadas de los dummies en el nivel 3
            self.rect.y = random.randint(400,550)
            self.image = pygame.transform.scale(pygame.image.load("media/bot.png").convert_alpha(), (48, 48)) #Tengo que cambiarle la imagen debido a un problema con las rotaciones
            
            self.up = False 
            self.down = True
            self.left = False
            self.right = False 
        

    
    #Movimiento constante de los dummies
    def update(self): 
        if self.up:
            self.rect.y -=self.speed
        if self.down:
            self.rect.y +=self.speed
        if self.right:
            self.rect.x += self.speed
        if self.left:
            self.rect.x -= self.speed
            
        self.angle %= 359 

     ###MOVIMIENTO NIVEL 1 esta es la "inteligencia artificial" de los dummies en el nivel 1
        if lvl1 == True:
            if self.rect.y > 70 and self.rect.y < random.randint(72,110) and self.up:
                self.image = pygame.transform.rotate(self.image, -90)                       
                self.up = False                                                                                 
                self.right = True                                                                             
                
            if self.rect.x < 1350 and self.rect.x > random.randint(1200,1340) and self.right:
                self.image = pygame.transform.rotate(self.image, -90)
                self.right = False
                self.down = True
                
            if self.rect.y > 640 and self.rect.y < random.randint(641,800) and self.down:
                self.image = pygame.transform.rotate(self.image, -90)
                self.down = False
                self.left = True
                
            if self.rect.x > 70 and self.rect.x < random.randint(70,130) and self.left:
                self.image = pygame.transform.rotate(self.image, -90)
                self.left = False
                self.up = True
                
    ###MOVIMIENTO NIVEL 2  
        if lvl2 == True:
            if self.rect.x < 1350 and self.rect.x > random.randint(1200,1400) and self.right:
                self.image = pygame.transform.rotate(self.image, -90)
                self.right = False
                self.down = True
                
            if self.rect.y > 670 and self.rect.y < random.randint(670,800) and self.down:
                self.image = pygame.transform.rotate(self.image, -90)
                self.down = False
                self.left = True
                
            if self.rect.x < 1000 and self.rect.x > random.randint(900,1030) and self.rect.y > 300 and self.left:
                self.image = pygame.transform.rotate(self.image, -90)
                self.left = False
                self.up = True

            if self.rect.y < 300 and self.rect.y > random.randint(220,380) and self.rect.x > 600 and self.up:
                self.image = pygame.transform.rotate(self.image, 90)
                self.up = False
                self.left = True

            if self.rect.x < 380 and self.rect.x > random.randint(300,420) and self.left:
                self.image = pygame.transform.rotate(self.image, 90)
                self.left = False
                self.down = True
                
            if self.rect.y > 640 and self.rect.y < random.randint(640,750) and self.rect.x < 380 and self.down:
                self.image = pygame.transform.rotate(self.image, -90)
                self.down = False
                self.left = True

            if self.rect.x < 100 and self.rect.x > random.randint(40,120) and self.left:
                self.image = pygame.transform.rotate(self.image, -90)
                self.left = False
                self.up = True

            if self.rect.y < 120 and self.rect.y < random.randint(30,120) and self.up:
                self.image = pygame.transform.rotate(self.image, -90)
                self.up = False
                self.right = True
                
    ###MOVIMIENTO NIVEL 3
        if lvl3 == True:
            if self.rect.x < 1400 and self.rect.x > random.randint(1200,1400) and self.right:
                self.image = pygame.transform.rotate(self.image, -90)
                self.right = False
                self.down = True
                
            if self.rect.y > 680 and self.rect.y < random.randint(680,800) and self.down: 
                self.image = pygame.transform.rotate(self.image, -90)
                self.down = False
                self.left = True
                
            if self.rect.x < 1100 and self.rect.x > random.randint(900,1030) and self.rect.y > 600 and self.left: 
                self.image = pygame.transform.rotate(self.image, -90)
                self.left = False
                self.up = True

            if self.rect.y < 230 and self.rect.y > random.randint(150,227) and self.rect.x > 400 and self.up: 
                self.image = pygame.transform.rotate(self.image, 90)
                self.up = False
                self.left = True

            if self.rect.x < 700 and self.rect.x > random.randint(600,700) and self.rect.y < 680 and self.left: 
                self.image = pygame.transform.rotate(self.image, 90)
                self.left = False
                self.down = True

            if self.rect.x < 100 and self.rect.x > random.randint(40,100) and self.left: 
                self.image = pygame.transform.rotate(self.image, -90)
                self.left = False
                self.up = True

            if self.rect.y < 500 and self.rect.y > random.randint(420,500) and self.rect.x < 100 and self.up: 
                self.image = pygame.transform.rotate(self.image, -90)
                self.up = False
                self.right = True

            if self.rect.x > 460 and self.rect.x < random.randint(460,520) and self.rect.y > 280 and self.right: 
                self.image = pygame.transform.rotate(self.image, 90)
                self.right = False
                self.up = True

            if self.rect.y < 300 and self.rect.y > random.randint(300,400) and self.rect.x < 90 and self.left: 
                self.image = pygame.transform.rotate(self.image, -90)
                self.left = False
                self.up = True

            if self.rect.y < 60 and self.rect.y > random.randint(10,60) and self.rect.x < 100 and self.up: 
                self.image = pygame.transform.rotate(self.image, -90)
                self.up = False
                self.right = True
  

  #Funcion del loop del juego

def main():
    #Aqui defino todas las instancias de clase a utilizar
    car1 = Car()
    bala = Bullet(car1.x,car1.y)

    jugadores = pygame.sprite.Group()
    jugadores.add(car1)
    
    global balas
    balas = pygame.sprite.Group()

        ###MANCHAS
    manchas = pygame.sprite.Group()
    
    mancha1 = Mancha(680,40)
    mancha2 = Mancha(500,650)
    mancha3 = Mancha(900,320)
    mancha4 = Mancha(460,320)
    mancha5 = Mancha(1190,680)
    mancha6 = Mancha(300,650)
    mancha7 = Mancha(450,330)

        ###CONOS
    conos = pygame.sprite.Group()
    
    cono1 = Cono(1150,600)
    cono2 = Cono(180,600)
    cono3 = Cono(180,140)
    cono4 = Cono(1160,150)
    cono5 = Cono(180,150)
    cono6 = Cono(180,200)
    cono7 = Cono(180,250)
    cono8 = Cono(1190,490)
    cono9 = Cono(1190,540)
    cono10 = Cono(1190,590)
    cono11 = Cono(1040,270)
    cono12 = Cono(55,740)
    cono13 = Cono(55,450)
    cono14 = Cono(260,190)
    cono15 = Cono(410,80)
    cono16 = Cono(936,15)
    
        ###ROCAS
    rocas = pygame.sprite.Group()
    
    roca1 = Roca(40,30)
    roca2 = Roca(1320,30)
    roca3 = Roca(1320, 740)
    roca4 = Roca(40,740)
    roca5 = Roca(670,206)
    roca6 = Roca(40,30)
    roca7 = Roca(1330,30)
    
        ###MAPA    
    mapa = pygame.sprite.Group()
    
    nivel1 = Nivel1(0,0)
    nivel2 = Nivel2(0,0)
    nivel3 = Nivel3(0,0)

        ###BORDES
    bordes = pygame.sprite.Group()
    
    bor2 = Bor2(0,0)
    bor3 = Bor3(0,0)
    
        ###INSTANCIAS DE NIVEL, si la variable del nivel es True, le paso a dibujar todos sus correspondientes objetos
    if lvl1 == True:
        mapa.add(nivel1)
        conos.add(cono1,cono2,cono3,cono4)
        rocas.add(roca1,roca2,roca3,roca4)
        manchas.add(mancha1,mancha2)
        
        
    if lvl2 == True:
        mapa.add(nivel2)
        bordes.add(bor2)
        conos.add(cono5,cono6,cono7,cono8,cono9,cono10)
        rocas.add(roca1,roca2,roca3, roca4)
        manchas.add(mancha3,mancha4)

    if lvl3 == True:
        mapa.add(nivel3)
        bordes.add(bor3)
        conos.add(cono11,cono12,cono13,cono14,cono15,cono16)
        rocas.add(roca5,roca6,roca7)
        manchas.add(mancha5,mancha6,mancha7)
        
        ###ENEMIGOS
    enemigos = pygame.sprite.Group()
    for i in range(20):
        bot = Dummies()
        todos_los_sprites.add(bot)
        enemigos.add(bot)
        
        global tiempo
        tiempo = 180
        score = 0
        point = 0


        ###---------------------LOOP PRINCIPAL---------------------###   
    while True:
        
    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == K_SPACE:
                    car1.disparar()
        
        #La hitbox del carro
        car1.rect.x = car1.x-20
        car1.rect.y = car1.y-20

        #Las variables de la meta y el checkpoint de las pistas
        #Tengo que hacerles un check y una meta para cada nivel ya que tienen ubicaciones diferentes
        meta = pygame.Rect(40,350,171,40)
        check = pygame.Rect(1150,350,171,40)

        
        if pygame.Rect.colliderect(car1.rect,check) and lvl1 == True:
            point +=1

    
        if point > 0:
            if  pygame.Rect.colliderect(car1.rect,meta) and lvl1 == True:
                score += 1000
                point = 0

        #Meta del nivel 2
        meta2 = pygame.Rect(700,32,40,171)
        check2 = pygame.Rect(719,284,40,171)

        
        if pygame.Rect.colliderect(car1.rect,check2) and lvl2 == True:
            point +=1

    
        if point > 0:
            if  pygame.Rect.colliderect(car1.rect,meta2) and lvl2 == True:
                score += 1500
                point = 0

        meta3 = pygame.Rect(1240,320,120,50)
        check3 = pygame.Rect(322,435,40,130)

        #Meta del nivel 3
        if pygame.Rect.colliderect(car1.rect,check3) and lvl3 == True:
            point +=1

    
        if point > 0:
            if  pygame.Rect.colliderect(car1.rect,meta3) and lvl3 == True:
                score += 2000
                point = 0
        
        #Lista de todas las colisiones
        if pygame.sprite.groupcollide(enemigos,balas,True,True): 
            score += 100

        if pygame.sprite.groupcollide(jugadores,conos,False,True): 
            score -= 100 #Si choca con el cono, el cono desaparece y se restan 100 puntos

        if pygame.sprite.groupcollide(jugadores,rocas,False,False): 
            car1.speed *=-2 #Si choca con una roca, el carro rebota en la dirección contraria

        if pygame.sprite.groupcollide(jugadores,manchas,False,False):
            car1.speed *= 0.50 #Si choca con una mancha, la velocidad del carro disminuye

        if pygame.sprite.collide_mask(car1,nivel1) and lvl1 == True:
            car1.speed *= 0.70 #Si sale de la pista el carro disminuye la velocidad
            score -=1
            
        if pygame.sprite.collide_mask(car1,bor2) and lvl2 == True:
            car1.speed *= -2 #Si choca con las llantas el carro rebota

        if pygame.sprite.collide_mask(car1,nivel2) and lvl2 == True:
            car1.speed *= 0.70
            score -=5

        if pygame.sprite.collide_mask(car1,bor3) and lvl3 == True:
            car1.speed *= -2
            
        if pygame.sprite.collide_mask(car1,nivel3) and lvl3 == True:
            car1.speed *= 0.70
            score -=10


        bala.update()
        car1.move()
        car1.render()

        todos_los_sprites.update()

        pygame.display.update()
        
        tiempo = int(185 - (pygame.time.get_ticks()/1000))
        
        #Mando a dibujar la carretera de cada nivel segun el estado de su variable
        if lvl1 == True:
            PANTALLA.blit(pista1,(0,0))
            
        if lvl2 == True:
            PANTALLA.blit(pista2,(0,0))
            
        if lvl3 == True:
            PANTALLA.blit(pista3,(0,0))
            

        mapa.draw(PANTALLA)
        bordes.draw(PANTALLA)
        
        todos_los_sprites.draw(PANTALLA)
        
        rocas.draw(PANTALLA)
        manchas.draw(PANTALLA)
        conos.draw(PANTALLA)

        #Este es el cuadro de la puntuacion para cada nivel
        #Tengo que darle valores diferentes para las diferentes ubicaciones que tiene el cuadro segun el nivel
        if lvl1 ==  True:
            PANTALLA.blit(pts,(600,150))
            draw_text(PANTALLA, str(tiempo), 27,790,215)
            draw_text(PANTALLA, str(score), 27, 790,265)

        if lvl2 == True:
            PANTALLA.blit(pts,(500,360))    
            draw_text(PANTALLA, str(tiempo), 27,690,423)
            draw_text(PANTALLA, str(score), 27, 705,475)
            
        if lvl3 == True:
            PANTALLA.blit(pts,(100,260))
            draw_text(PANTALLA, str(tiempo), 27,290,324)
            draw_text(PANTALLA, str(score), 27, 305,377)
        

     
        FPS.tick(100) #El juego va a 100 FPS

if __name__ == '__main__': main()
