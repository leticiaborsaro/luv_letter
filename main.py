import pygame

# CONSTANTS
bg_color = (255, 191, 192)
width = 800
height = 600

# SETUP (GENERIC)
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption('My love <3')

#class Button:
  #  def __init__(self, x, y, width, height, text=''):
     #   self.x = x
      #  self.y = y
      #  self.width = width
      #  self.height = height
      #  self.text = text
      #  self.font = pygame.font.SysFont('Arial', 20)


def main_screen():

    # fonte do texto
    font = pygame.font.SysFont('Arial', 40)
    text = font.render('You have 1 new message', True, (0, 0, 0))
    # centralizar o texto na tela
    rect = text.get_rect(center=(width / 2, height / 2))
    screen.blit(text, rect)

    # imagem
    luv_letter = pygame.image.load('luv_letter.png')
    luv_letter = pygame.transform.scale(luv_letter, (120, 120))
    rect2 = luv_letter.get_rect(center=(width / 2, (height / 2 ) - 50))
    screen.blit(luv_letter, rect2)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(bg_color)

    # here is the game
    main_screen()



    pygame.display.flip()
    clock.tick(60)

