import pygame
import numpy as np
import random

WIDTH = 800
HEIGHT = 500
win = pygame.display.set_mode((WIDTH,HEIGHT))

class obstacle:
	def __init__(self):
		self.x = WIDTH
		self.y = 400

class dino:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Dino Jump')
		self.dinox = 50
		self.dinoy = 400
		self.objects = []
		self.score = 0
		isJump = False
		jumpCount = 8
		clock = pygame.time.Clock()
		ispassed = False
		q = 0
		while True:

			clock.tick(180)
			pygame.time.delay(20)
			win.fill((0,0,0))
			
			if len(self.objects)<6:
				self.objects.append(obstacle())
				if len(self.objects)>1:
					self.objects[-1].x = self.objects[-2].x+random.randint(80,250)
				
			for i in range(len(self.objects)):
				self.draw(self.objects[i].x,self.objects[i].y)
			

			self.draw(self.dinox,self.dinoy)

			keys = pygame.key.get_pressed()
			
			if keys[pygame.K_SPACE]:
				isJump = True

			if isJump:
				if jumpCount >= -8:
					self.dinoy -= (jumpCount*abs(jumpCount)) * 0.5
					jumpCount -= 1
				else:
					jumpCount = 8
					isJump = False

			if self.objects[0].x <= 0:
				self.objects.pop(0)
					
			for i in range(len(self.objects)):
				self.objects[i].x -= 3
				
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			for i in range(len(self.objects)):
				if self.objects[i].x in range(self.dinox,self.dinox+10) and self.objects[i].y == self.dinoy:
					pygame.quit()

			if q%5 == 0:
				self.score += 1
				print(self.score)

			q+=1
			

			

	def draw(self,x,y):
		# win.fill((0,0,0))
		pygame.draw.rect(win,(255,0,0),(x,y,10,10))
		# pygame.draw.rect(win,(255,0,0),(self.dinox,self.dinoy,10,10))
		pygame.draw.line(win,(255,255,255),(0,410),(WIDTH,410))
		pygame.display.update()


dino()