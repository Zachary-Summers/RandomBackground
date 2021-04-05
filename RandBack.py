#randBackground
import pygame, math, sys, random, time, pyautogui
w,h=pyautogui.size()
multiplier=int(input())
w=(w//10)*multiplier
h=(h//10)*multiplier
pygame.init()

#variable stuff

screen=pygame.display.set_mode((w,h))
screenshot=0
def newBack(colors=None):
    for i in range(h):
            for e in range(w):
                if colors==None:
                    pygame.draw.circle(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(e,i),1)
                elif colors[0]=="g":
                    gray=random.randint(0,255)
                    pygame.draw.circle(screen,(gray,gray,gray),(e,i),1)
                else:
                    pygame.draw.circle(screen,random.choice(colors),(e,i),1)
newBack()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LALT:
                newBack()
            elif event.key==pygame.K_b:#black and white
                newBack(((255,255,255),(0,0,0)))
            elif event.key==pygame.K_g:#grauscale
                newBack("gray")
            elif event.key==pygame.K_v:#vivid
                newBack(((255,0,0),(0,255,255),(255,255,0),(255,255,255),(0,0,0),(0,255,0),(0,0,255)))
            elif event.key==pygame.K_f:#steriopyically feminie colors
                newBack(((255,192,203),(75,0,130)))
            elif event.key==pygame.K_i:#steriopyically feminie colors
                pygame.image.save(screen, "{}.jpeg".format(screenshot))
                screenshot+=1
    pygame.display.update()