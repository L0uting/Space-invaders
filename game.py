import pygame
vaisseau=[(1,40)]
pygame.init()
pygame.font.init() 
pygame.mixer.init()
clock = pygame.time.Clock()
tire = pygame.mixer.Sound("Assets/tire.mp3")
tire.set_volume(0.1)
pygame.mixer.music.load("Assets/son.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) 

k=0
tick = 0

enemis=[ 

(1, 1),
(1, 11),
(1, 21),
(11, 1),
(11, 11),
(11, 21),
(21, 1),
(21, 11),
(21, 21),
(31, 1),
(31, 11),
(31, 21),
(41, 1),
(41, 11),
(41, 21),

]
direction = 1
projectiles = []
screen = pygame.display.set_mode((900, 720))
monster_img = pygame.image.load("Assets/az.png").convert_alpha()
gal = pygame.image.load("Assets/galaxy.png").convert_alpha()
gal = pygame.transform.scale(gal, (900, 720))
vaissea=pygame.image.load("Assets/vaisseau.png").convert_alpha()
vaissea = pygame.transform.scale(vaissea, (100,100))
monster_img = pygame.transform.scale(monster_img, (100,100))

def color(x, y, color):
   screen.fill(color, (x*16, y*16, 16, 16))
def draw_vaisseau():
   for x,y in vaisseau:
       screen.blit(vaissea, ((x*16)-45, y*16))
   for x,y in projectiles:
        color(x, y, (255, 0, 0))
   for x, y in enemis:
    screen.blit(monster_img, (x*16, y*16))
direction = 1 
bord_gauche = 1
bord_droit = 50

def deplacement_enemis():
    global direction

    if len(enemis) == 0:
        return
    if tick % 20 == 0:  
        for i in range(len(enemis)):
            x, y = enemis[i]
            enemis[i] = (x + direction, y)
    toucher_bord = False
    for x, y in enemis:
        if x >= bord_droit and direction == 1:
            toucher_bord = True
            break
        elif x <= bord_gauche and direction == -1:
            toucher_bord = True
            break


    if toucher_bord:
        direction *= -1  
        for i in range(len(enemis)):
            x, y = enemis[i]


   

def deplacement():
   keys = pygame.key.get_pressed()
   x, y = vaisseau[0]
   if keys[pygame.K_q]:
    x -= 1
   if keys[pygame.K_d]:
    x += 1
   if keys[pygame.K_s]:
    y += 1
   if keys[pygame.K_z]:
    y-= 1
   vaisseau[0] = (x, y)
   if x<=0:
      vaisseau[0]= (1,y)
   if x>=55:
      vaisseau[0]= (55,y)
   if y<=30:
      vaisseau[0]= (x,31)
   if y>=42:
      vaisseau[0]= (x,41)
      
      

def shoot():
   global k
   if k>30:
    keys = pygame.key.get_pressed()
    x, y = vaisseau[0]
    if keys[pygame.K_SPACE]:
        k=0
        
        projectiles.append((x, y+1))
        tire.play()
  
  
def move_projectiles():
   global tick
   for i in range(len(projectiles)):
      x, y = projectiles[i]
      if tick % 2 == 0:
         y -= 1
      projectiles[i] = (x, y)
def main():
  global k, tick
  
  running = True
  while running:
      
      clock.tick(60)
      screen.fill((0, 0, 0))
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
      screen.blit(gal, (1,1))
      deplacement()
      shoot()
      draw_vaisseau()
      move_projectiles()
      deplacement_enemis()
      pygame.display.flip()
      k+=1
      tick += 1
      
  pygame.quit()
main()
      
 