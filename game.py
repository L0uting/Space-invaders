import pygame
import random
vaisseau=[(1,40)]
pygame.init()
pygame.font.init() 
pygame.mixer.init()
clock = pygame.time.Clock()
tire = pygame.mixer.Sound("Assets/tire.mp3")
tire.set_volume(0.1)
boom = pygame.mixer.Sound("Assets/boom.mp3")
boom.set_volume(3)
level = pygame.mixer.Sound("Assets/level.wav")
level.set_volume(3)
fin_vague_joue = False   
end = pygame.mixer.Sound("Assets/end.wav")
end.set_volume(0.3)
pygame.mixer.music.load("Assets/son.mp3")
display=(900,1072)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) 
TAILLE = 16
font = pygame.font.Font("Assets/ttf/PixelCode.ttf", 40)
hitbox="oui"
k=49
score=0
tick = 0
murs=[]
enemis_xy = [ 
    (1, 10),
    (1, 20),
    (1, 30),
    (11, 10),
    (11, 20),
    (11, 30),
    (21, 10),
    (21, 20),
    (21, 30),
    (31, 10),
    (31, 20),
    (31, 30),
    (41, 10),
    (41, 20),
    (41, 30),
]

enemis=[]
for x,y in enemis_xy:
   rect = pygame.Rect(x * TAILLE, (y * TAILLE)-100, 115, 90)
   enemis.append(rect)

   

direction = 1
projectiles = []

screen = pygame.display.set_mode((display))
monster_img = pygame.image.load("Assets/monstre2.png").convert_alpha()
monster2_img = pygame.image.load("Assets/monstre1.png").convert_alpha()
gal = pygame.image.load("Assets/galaxy.png").convert_alpha()
gal = pygame.transform.scale(gal, (1920, 1080))
vaissea=pygame.image.load("Assets/vaisseau.png").convert_alpha()
vaissea = pygame.transform.scale(vaissea, (100,100))
monster_img = pygame.transform.scale(monster_img, (130,100))
monster2_img = pygame.transform.scale(monster2_img, (130,100))
expl = pygame.image.load("Assets/expl.png").convert_alpha()
expl = pygame.transform.scale(expl, (130,100))
def color(x, y, color):
   screen.fill(color, (x*16, y*16, 16, 16))
def draw_vaisseau():
   global tick
   for x,y in vaisseau:
       screen.blit(vaissea, ((x*16)-45, y*16))
   for x,y in projectiles:
        color(x, y, (255, 0, 0))
   for ennemi    in enemis: 
        if tick % 40 < 20:
            screen.blit(monster_img, (ennemi.x-4, ennemi.y - 12))
        else:
            screen.blit(monster2_img, (ennemi.x-4, ennemi.y - 6))
direction = 1 
bord_gauche = 1
bord_droit = 112
d=130
n=2
def respawn():
   global d, n ,fin_vague_joue
   global enemis, enemis_xy 
   if len(enemis)==0:
      if not fin_vague_joue:
            end.play()
            fin_vague_joue = True


      
   
      d-=1
      round_font = pygame.font.Font("Assets/ttf/PixelCode.ttf", 150)
      texte = round_font.render(f"ROUND {n}", True, (255, 0, 0))
      texte_rect = texte.get_rect(center=(screen.get_width()//2, 200))
      screen.blit(texte, texte_rect)
      round_font = pygame.font.Font("Assets/ttf/PixelCode.ttf", 50)
      texte2 = round_font.render(f"INCOMING: {d}", True, (255, 0, 0))
      texte_rect = texte2.get_rect(center=(screen.get_width()//2, 300))
      screen.blit(texte2, texte_rect)

      if d<=0:
         level.play()


         enemis_xy = [ 
            (1, 10),
            (1, 20),
            (1, 30),
            (11, 10),
            (11, 20),
            (11, 30),
            (21, 10),
            (21, 20),
            (21, 30),
            (31, 10),
            (31, 20),
            (31, 30),
            (41, 10),
            (41, 20),
            (41, 30),
         ]

         enemis=[]
         for x,y in enemis_xy:
            rect = pygame.Rect(x * TAILLE, (y * TAILLE)-100, 115, 90)
            enemis.append(rect)
         d=130
         n+=1
         fin_vague_joue = False 

def debug():
   global tick,n
   for ennemi in enemis:
      pygame.draw.rect(screen, (255, 0, 0), ennemi, 1) 
   texte=font.render(f"ticks: {tick} ", True, (255, 255, 255))
   screen.blit(texte, (10, 10))
   
def deplacement_enemis():
    global direction
  
    x,y=display
    if len(enemis) == 0:
        return


    for ennemi in enemis:
        ennemi.x += direction


    toucher_bord = False
    for ennemi in enemis:
        if ennemi.right >= x and direction == 1:  
            toucher_bord = True
            break
        elif ennemi.left <= 0 and direction == -1:  
            toucher_bord = True
            break


    if toucher_bord:
        direction *= -1
        for ennemi in enemis:
            ennemi.y += 55
   

def deplacement():
   global score
   x1,y1=display
  
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
   if x>=x1/16:
      vaisseau[0]=( (x1/16)-1,y)
   if y<=45:
      vaisseau[0]= (x,46)
   if y>=60:
      vaisseau[0]= (x,60)
  
   texte1=font.render(f"score:{score}", True, (0, 0, 255))
   screen.blit(texte1, (x1-230,10))

def shoot():
   global score
   global k

   if k>10:
    keys = pygame.key.get_pressed()
    x, y = vaisseau[0]
    if keys[pygame.K_SPACE]:
        k=0
        
        projectiles.append((x, y))
        tire.play()
   
   for x, y in projectiles:
      for ennemi in enemis:
         if ennemi.collidepoint(x * 16, y * 16):
               projectiles.remove((x, y))
          
               enemis.remove(ennemi)
               screen.blit(expl, (ennemi.x-4, ennemi.y - 6))
               boom.play()
               score+=10
               

  
  
def move_projectiles():
   global tick
   for i in range(len(projectiles)):
      x, y = projectiles[i]
      if tick % 1== 0:
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
      #screen.blit(gal, (1,1))
      if hitbox=="oui":
       debug()
      deplacement()
      shoot()
      respawn()
      draw_vaisseau()
      move_projectiles()
      deplacement_enemis()
 
      pygame.display.flip()
      k+=1
      tick += 1
      
      
  pygame.quit()
main()
      
 