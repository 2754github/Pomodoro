import pygame
from pygame.locals import *
import sys
import math
from time import sleep

args=sys.argv

SCREEN_SIZE=(300, 100)
WORK=int(args[1])
BREAK=int(args[2])

pygame.init()
screen=pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Pomodoro Timer")

exit_button=pygame.Rect(255,73,42,25)

sysfont=pygame.font.SysFont(None,20)
text1=sysfont.render("Work time is {0} minutes".format(WORK),True,(0,0,0))
text2=sysfont.render("Break time is {0} minutes".format(BREAK),True,(0,0,0))
text3=sysfont.render("EXIT",True,(0,0,0))

pygame.mixer.init()
alarm=pygame.mixer.Sound("alarm.wav")
powerdown=pygame.mixer.Sound("powerdown.wav")

WORK*=60
BREAK*=60

clock=pygame.time.Clock()
S=-math.pi/2
T=2*math.pi/WORK
s=-math.pi/2
t=2*math.pi/BREAK

while True:
	screen.fill((255,255,255))
	pygame.draw.arc(screen,(200,255,200),(0,0,100,100),0,2*math.pi,10)
	pygame.draw.arc(screen,(255,200,200),(10,10,80,80),0,2*math.pi,10)
	pygame.draw.rect(screen,(200,200,200),exit_button)

	screen.blit(text1,(120,35))
	screen.blit(text2,(120,55))
	screen.blit(text3,(260,80))

	time_passed_seconds=clock.tick(60)/1000

	S+=T*time_passed_seconds
	if S<3/2*math.pi:
		pygame.draw.arc(screen,(0,255,0),(0,0,100,100),math.pi/2,-S,10)
		pygame.draw.arc(screen,(255,0,0),(10,10,80,80),0,2*math.pi,10)
	elif 3/2*math.pi<S<3/2*math.pi+0.1:
		alarm.play()
	else:
		s+=t*time_passed_seconds
		pygame.draw.arc(screen,(255,0,0),(10,10,80,80),math.pi/2,-s,10)
		if s>=3/2*math.pi:
			alarm.play()
			s=-math.pi/2
			S=-math.pi/2

	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if exit_button.collidepoint(event.pos):
				powerdown.play()
				sleep(1)
				sys.exit()
