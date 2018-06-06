import sys, pygame
import random                       #Antes que nada importar todos los modulos que vamos a usar
from pygame.locals import *
from math import *


#Tenemos que iniciar el modulo de pygame, luego de hacer esto definimos algunas variables generales para poder usarlas a traves
#de todo el codigo sin necesidad de llamarlas cada vez que las vayamos a usar.
pygame.init()

ANCHO  = 1380
ALTO = 800
PANTALLA = pygame.display.set_mode((ANCHO,ALTO))
FPS    = pygame.time.Clock()

blanco = (255,255,255)

pygame.display.set_caption('PyDeathRace')

#Aqui declaro la imagen de la pista, la podria declarar en otro lado pero lo hago aqui mas que todo por cuestion de orden y comodidad 
pista = pygame.transform.scale(pygame.image.load('pista.jpg').convert(),(ANCHO,ALTO))

#Definir el grupo de todos los sprites, lo hago aqui para que no me genere conflictos del tipo "referenciar antes de declarar"
todos_los_sprites = pygame.sprite.Group()

#La letra que vamos a usar para la puntuacion.
font_name = pygame.font.match_font('arial')


#Definimos el metodo para dibujar el texto y le pasamos todos los atributos a utilizar
#Use una letra generica como Arial para asegurarme de que pueda ejecutarse bien en cualquier computadora
def draw_text(surf,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface,text_rect)
    
    
    
#La clase Car, esta es la clase del jugador, notar el hecho de que para inicializarlo como sprite se le pasa
#pygame.sprite.Sprite y para llamar una instancia tengo que escribir el metodo "super().__init__(self)" de lo contrario el modulo no lo reconoce
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        start_pos = (73, 370)           #Le paso algunos atributos que son necesarios para recrear la fisica de aceleracion del carro
        start_angle = 90
        self.x     = start_pos[0]
        self.y     = start_pos[1]
        self.angle = start_angle
        self.speed = 0

        self.image = pygame.transform.scale(pygame.image.load("Car.png").convert_alpha(), (48, 48))
        self.rect = self.image.get_rect().inflate(-8,-8) #Al rectangulo tengo que pasarle el metodo inflate porque la hitbox es demasiado grande por si sola
                                                                          #Entiendase hitbox como el rectangulo del sprite


        
    def move(self): #Este metodo se encargara del movimiento del carro
        keys = pygame.key.get_pressed() #Defino esto por cuestion de comodidad, para no decir lo mismo 5 veces
                                        
        self.forward_speed = 0.5            #Algunas variables para la velocidad/aceleracion
        self.rearward_speed = 0.2
        self.max_speed = 5
        self.max_reverse = -5
        #Estos son los controles del carro, el carro adaptara los valores de velocidad especificados arriba y
        #los modificara a sus coordenadas en x e y
        if keys[K_a] or keys[K_LEFT]:
            self.angle += self.speed
        if keys[K_d] or keys[K_RIGHT]:
            self.angle -= self.speed
        if keys[K_w] or keys[K_UP]:
            self.speed += self.forward_speed
        if keys[K_s] or keys[K_DOWN]:
            self.speed -= self.rearward_speed

        if keys[K_SPACE]: #Cada vez que presione espacio el carro dispara
            self.disparar()

        if self.speed > self.max_speed: #Tengo que ponerle un limitador a la velocidad del carro, de lo contrario el carro acelerara o
            self.speed = self.max_speed # hara marcha atras infinitamente.

        if self.speed < self.max_reverse:
            self.speed = self.max_reverse


        #Esto es para que el angulo del carro nunca sea mayor a 359 grados, de esta manera no habra overflow y
        #el carro no se volvera loco
        self.angle %= 359


        #Se dibujan las coordenadas del carro como valores de un seno y un coseno, gracias a esto el carro puede rotar y asimilar la fisica de un carro en la vida real
        self.x += self.speed * cos(radians(self.angle))    #la coordenada en x es el valor de la velocidad multiplicado por el coseno del angulo en radianes
        self.y -= self.speed * sin(radians(self.angle))  #la coordenada en y es el valor de la velocidad multiplicado por el seno del angulo en radianes
        
        #hay que pasarle el valor del angulo en radianes porque pygame no trabaja con grados

        #Verificar que el carro no salga de la pista
        #Compruebo que el carro no pueda salir de estas coordenadas        
        if self.x < 40:
            self.x = 41
        if self.x > 1335:
            self.x = 1334
        if self.y < 43:
            self.y = 44
        if self.y > 750:
            self.y = 749
     

    def render(self): #Se dibuja el carro en pantalla segun el rectangulo del sprite luego de haberlo rotado
        self.rotcar   = pygame.transform.rotate(self.image, self.angle)
        self.rotcar_rect = self.rotcar.get_rect(center = (self.x, self.y))
        PANTALLA.blit(self.rotcar, self.rotcar_rect)

    def disparar(self): #El metodo disparar se encarga de crear una bala nueva y añadirla al grupo "balas" cada vez que se presiona espacio
        global balas #Tengo que crear una variable global para las balas, de lo contrario no puedo llamarlas ya que hay un problema con el orden de mis clases
        bullet = Bullet(self.x,self.y)
        balas.add(bullet)
        todos_los_sprites.add(bullet)


        
class Bullet(pygame.sprite.Sprite): #Inicializo la clase de la bala y le doy todos los atributos que va a usar 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        car = Car() #Tengo que llamar una instancia de la clase Car porque quiero que el valor del angulo de la bala sea el mismo que el del carro
        self.image = pygame.transform.scale(pygame.image.load("bala.png").convert_alpha(),(15,15))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.speed = 10
        self.time = 2
        self.angle = car.angle


    def update(self):

        self.rect.x += self.speed * cos(radians(self.angle))    #Igualo la posicion de la bala con respecto de la posicion del carro para que la bala siempre salga
        self.rect.y -= self.speed * sin(radians(self.angle))      #donde esta ubicado el carro
        
   
        # Si la bala alcanza el borde de la pantalla, desaparece, esto para ahorrar memoria
        if  self.rect.x < 0 or self.rect.x > 1380:
            self.kill()

        if self.rect.y < 0 or self.rect.y > 800:
            self.kill()
    

            


class Dummies(pygame.sprite.Sprite):
    def __init__(self): #Inicializo la clase de los dummy vehicles
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load("bot.png").convert_alpha(), (48, 48))
        self.rect = self.image.get_rect().inflate(-8,-8)
        self.rect.x = random.randint(50,100)
        self.rect.y = random.randint(370,430) #Los dummies tienen coordenadas de spawn y velocidades determinadas por valores aleatorios
        self.speed = random.randint(3,7)        # de esta manera me aseguro de que todas las trayectorias sean diferentes, por lo tanto los dummies no pasaran apelotados en la carretera
        self.angle = 0
        
        self.up = True #Estas variables me seran muy utiles mas abajo
        self.down = False
        self.left = False
        self.right = False 
    

    def update(self): #Defino las variables de arriba como variables de movimiento
        if self.up:
            self.rect.y -=self.speed
        if self.down:
            self.rect.y +=self.speed
        if self.right:
            self.rect.x += self.speed
        if self.left:
            self.rect.x -= self.speed
            
        self.angle %= 359 #Compruebo que el angulo de los dummies nunca sea mayor a 359

        #Esta es la trayectoria, o, la inteligencia artificial, por asi decirlo, de los dummies
        #Basicamente la logica es asi:

        #Si el dummy esta entre "x" coordenada e "y" coordenada, moverse en una direccion determinada
            
        if self.rect.y > 70 and self.rect.y < random.randint(72,110) and self.up:
            self.image = pygame.transform.rotate(self.image, -90)                       #Por ejemplo aqui, si la coordenada "y" del dummy es mayor que 70, menor que un numero al azar entre
            self.up = False                                                                                 #72 y 110, y esta actualmente moviendose hacia arriba, entonces el dummy pasara a moverse a la derecha
            self.right = True                                                                                #esto es manejado por la manipulacion de las variables que declare arriba
            
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

        #Esta logica cuatro veces, una por direccion, generando un ciclo que simula el movimiento de los dummies a traves de la pista





def main():
    #Llamar instancias de clase para poder usarlas en el loop
    car1 = Car()
    bala = Bullet(car1.x,car1.y)
    

    #Creo los demas grupos para los sprites, esto es importante ya que si no creo los grupos, cosas tan importantes como las colisiones
    #no funcionarian

    jugadores = pygame.sprite.Group()
    jugadores.add(car1)
    
    global balas
    balas = pygame.sprite.Group()

    enemigos = pygame.sprite.Group()

    #El grupo de los dummies es diferente ya que en este caso estoy llamando a que se creen 20 instancias de la clase
    #dummy, o sea, 20 vehiculos enemigos
    for i in range(20):
        bot = Dummies()
        todos_los_sprites.add(bot)
        enemigos.add(bot)

    #Defino algunas variables que me seran de utilidad en el loop
        tiempo = 180
        score = 0
        point = 0


        ###---------------------LOOP PRINCIPAL---------------------###   
    while True:
        
        #Este evento cierra el juego.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        
  
        #Hago un seguimiento de la hitbox del carro con su sprite, tengo que hacer esto de lo contrario el
        #carro no podria colisionar
        car1.rect.x = car1.x-20
        car1.rect.y = car1.y-20

        
        #Defino las colisiones entre los sprites
        r1 = pygame.Rect(212,167,945,450)
        if pygame.Rect.colliderect(car1.rect,r1):   #Si el jugador se sale de la pista, su velocidad se disminuye y se le restan puntos
            car1.speed = 2
            score -=10

        #Estos dos rectangulos me son de ayuda para poder sumar puntos por cada vez que el jugador complete una vuelta
        meta = pygame.Rect(40,350,171,40)
        check = pygame.Rect(1150,350,171,40)

        #Funcionan asi: si el jugador hace contacto con el rectangulo "check", ubicado al otro lado de la pista con respeto a la meta, se suman numeros a la variable "point"
        
        if pygame.Rect.colliderect(car1.rect,check):
            point +=1

        #Si la variable "point" es mayor a 0 y el jugador pasa por la meta, se sumaran 1000 puntos al contador y se reiniciara la variable "point" a 0
            #Gracias a este pequeño sistema, el jugador no puede abusar de los puntos que otorgan el cruzar la meta, ya que debe dar una vuelta completa para que los puntos cuenten
        if point > 0:
            if  pygame.Rect.colliderect(car1.rect,meta):
                score += 1000
                point = 0
        
            
        if pygame.sprite.groupcollide(enemigos,balas,True,True): #Si una bala alcanza a un dummy, ambos desaparecen y suman 100 puntos al contador
            score += 100


        if tiempo == 0: #Luego de 3 minutos, el juego acaba
             pygame.quit()

        #Estos metodos se encargan de actualizar los sprites
        bala.update()
        car1.move()
        car1.render()

        todos_los_sprites.update()

        pygame.display.update()

        #Dibujo todos los elementos que estaran en pantalla

        tiempo = int(180 - (pygame.time.get_ticks()/1000)) 
        
        PANTALLA.blit(pista,(0,0))
        todos_los_sprites.draw(PANTALLA)
        draw_text(PANTALLA, str(tiempo), 40,300,265)
        draw_text(PANTALLA, str(score), 40, 300,300)

        

        #El juego va a 60 frames por segundo
        FPS.tick(60)

if __name__ == '__main__': main()
