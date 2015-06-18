import pygame

scr = pygame.display.set_mode((800,600))

array = [[1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1]];



def pill(x,y):
    pos_pill = (int(50 + (600/6)/2 + x*(600/6)), int(50+(400/4)/2 + y*(400/4))); 
    pygame.draw.circle(scr, (100,0,0), pos_pill, 10)
  
 
def map():
    pygame.draw.rect(scr, (100,100,100), (50,50,700,100), 0)
    pygame.draw.rect(scr, (100,100,100), (50,450,700,100), 0)
    pygame.draw.rect(scr, (100,100,100), (50,150,100,300), 0)
    pygame.draw.rect(scr, (100,100,100), (650,150,100,300), 0)

    for y in range (len(array)):
        for x in range(len(array[y])):
            if array[y][x] == 1:
                pill(x,y)
        
    

posf = (400,300)
pose1 = (425,290)
pose2 = (375,290)
posm = (375,305,50,20)
move = 1

def ghost():
    global posf
    global pose1
    global pose2
    global posm
    global move
    
    clock = pygame.time.Clock()

    posf = (posf[0]+move,posf[1])
    pygame.draw.circle(scr, (0, 0, 100), posf, 50)
    pose1= (pose1[0]+move,pose1[1])
    pygame.draw.circle(scr, (100, 100, 100), pose1, 8)
    pose2 = (pose2[0]+move,pose2[1])
    pygame.draw.circle(scr, (100, 100, 100), pose2, 8)
    posm = (posm[0]+move,posm[1],posm[2],posm[3])
    pygame.draw.arc(scr, (100, 100, 100), posm, 3.8, 5.70, 3)
    pygame.display.flip()
    if posf[0] < 50 or posf[0] > 750:
        move = -move
 
            
    clock.tick(300)

pos_pacman = (100,100)

def pacman():
    global pos_pacman
    move_pacman = {
        pygame.K_DOWN: (0, 25),
        pygame.K_UP: (0, -25),
        pygame.K_RIGHT: (25, 0),
        pygame.K_LEFT: (-25, 0)
    }
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            return
        elif e.type == pygame.KEYDOWN and e.key in move_pacman:
            if pos_pacman[0] > 50 or pos_pacman[0] < 750 or pos_pacman[1] > 50 or pos_pacman[1] < 550:
                pos_pacman = (pos_pacman [0]+move_pacman[e.key][0], pos_pacman[1]+move_pacman[e.key][1])
    pygame.draw.circle(scr, (100,100,0),pos_pacman,35)

def loop():
    while True:
        scr.fill((0,0,0));
        map()
        pacman()
        ghost()
        pygame.display.flip()

loop()
