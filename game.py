# Import libraries
import pygame
import os
import utils
import csv
import numpy as np

# Initialize field variables
clickMultiplier = 1
money = 0
incrementMoney = 0
item1Cost = 100
item2Cost = 500
item3Cost = 50
item4Cost = 1000
x = 0
y = 0

# Window position
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
pygame.init()


class Main_Game():
    def __init__(self):
        # Creates our window
        self.window = pygame.display.set_mode((1540, 920), pygame.NOFRAME)
        self.surface = pygame.display.get_surface()
        pygame.display.flip()
        pygame.display.set_caption("Monster Clicker")
        icon = pygame.image.load('web.jpg')
        pygame.display.set_icon(icon)

        # Initialize game images
        self.forest = pygame.image.load("forest.png").convert_alpha()
        self.forest = pygame.transform.rotozoom(self.forest, 0, 1.15)
        self.forest_rect = self.forest.get_rect(
            center=((self.surface.get_width() / 2), self.surface.get_height() / 2))

        self.brickwall = pygame.image.load("brickwall.png").convert_alpha()
        self.brickwall = pygame.transform.rotozoom(self.brickwall, 0, 1.85)
        self.brickwall_rect = self.brickwall.get_rect(
            center=((self.surface.get_width() / 2.25), self.surface.get_height() / 2.15))

        self.shopkeeper = pygame.image.load("shopkeeper.png").convert_alpha()
        self.shopkeeper = pygame.transform.rotozoom(self.shopkeeper, 0, 0.7)
        self.shopkeeper_rect = self.shopkeeper.get_rect(
            topleft=((self.surface.get_width() / 2.5), (self.surface.get_height() / 3)))

        self.table = pygame.image.load("table.png").convert_alpha()
        self.table = pygame.transform.rotozoom(self.table, 0, 0.6)
        self.table_rect = self.table.get_rect(
            topleft=((self.surface.get_width() / 3.75), (self.surface.get_height() / 2.05)))

        self.monster = pygame.image.load("m1.png").convert_alpha()
        self.monster = pygame.transform.rotozoom(self.monster, 0, 0.7)
        self.monster_rect = self.monster.get_rect(
            topleft=((self.surface.get_width() / 2.45), (self.surface.get_height() / 2.3)))

        self.shopButton = pygame.image.load("shop.png").convert_alpha()
        self.shopButton = pygame.transform.rotozoom(self.shopButton, 0, 0.03)
        self.shopButton_rect = self.shopButton.get_rect(
            topleft=((self.surface.get_width() / 1.09), (self.surface.get_height() / 1.15)))

        self.backButton = pygame.image.load("back.png").convert_alpha()
        self.backButton = pygame.transform.rotozoom(self.backButton, 0, 0.03)
        self.backButton_rect = self.backButton.get_rect(
            topleft=((self.surface.get_width() / 115), (self.surface.get_height() / 1.15)))

        self.icon1 = pygame.image.load("icon1.png").convert_alpha()
        self.icon1 = pygame.transform.rotozoom(self.icon1, 0, 0.5)
        self.icon1_rect = self.icon1.get_rect(
            topleft=((self.surface.get_width() / 3.5), (self.surface.get_height() / 6)))

        self.icon2 = pygame.image.load("icon2.png").convert_alpha()
        self.icon2 = pygame.transform.rotozoom(self.icon2, 0, 0.5)
        self.icon2_rect = self.icon2.get_rect(
            topleft=((self.surface.get_width() / 1.5), (self.surface.get_height() / 6)))

        self.icon3 = pygame.image.load("icon3.png").convert_alpha()
        self.icon3 = pygame.transform.rotozoom(self.icon3, 0, 0.5)
        self.icon3_rect = self.icon3.get_rect(
            topleft=((self.surface.get_width() / 3.5), (self.surface.get_height() / 2.2)))

        self.icon4 = pygame.image.load("icon4.png").convert_alpha()
        self.icon4 = pygame.transform.rotozoom(self.icon4, 0, 0.5)
        self.icon4_rect = self.icon4.get_rect(
            topleft=((self.surface.get_width() / 1.5), (self.surface.get_height() / 2.2)))

        self.startButton = pygame.image.load("startButton.png").convert_alpha()
        self.startButton = pygame.transform.rotozoom(self.startButton, 0, 1)
        self.startButton_rect = self.startButton.get_rect(
            topleft=((self.surface.get_width() / 2.5), (self.surface.get_height() / 2.32)))

        self.loadSaveButton = pygame.image.load("loadSaveButton.png").convert_alpha()
        self.loadSaveButton = pygame.transform.rotozoom(self.loadSaveButton, 0, 1)
        self.loadSaveButton_rect = self.loadSaveButton.get_rect(
            topleft=((self.surface.get_width() / 2.5), (self.surface.get_height() / 1.80)))

        self.exitGameButton = pygame.image.load("exitGameButton.png").convert_alpha()
        self.exitGameButton = pygame.transform.rotozoom(self.exitGameButton, 0, 1)
        self.exitGameButton_rect = self.exitGameButton.get_rect(
            topleft=((self.surface.get_width() / 2.5), (self.surface.get_height() / 1.47)))

        self.saveGameButton = pygame.image.load("saveGameButton.png").convert_alpha()
        self.saveGameButton = pygame.transform.rotozoom(self.saveGameButton, 0, 1)
        self.saveGameButton_rect = self.saveGameButton.get_rect(
            topleft=((self.surface.get_width() / 2.5), (self.surface.get_height() / 1.80)))

        self.continueButton = pygame.image.load("continueButton.png").convert_alpha()
        self.continueButton = pygame.transform.rotozoom(self.continueButton, 0, 1)
        self.continueButton_rect = self.continueButton.get_rect(
            topleft=((self.surface.get_width() / 2.5), (self.surface.get_height() / 2.32)))

        self.myFont = pygame.font.SysFont("monospace", 20)

    def startMenu(self):
        # Our main loops, keeping the game going.
        global clickMultiplier
        global money
        global item1Cost
        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.exitGameButton_rect.collidepoint(event.pos):
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.startButton_rect.collidepoint(event.pos):
                    menu = False
                    self.adventureScene()
                if event.type == pygame.MOUSEBUTTONDOWN and self.loadSaveButton_rect.collidepoint(event.pos):
                    clickMultiplier, money, item1Cost, item3Cost = np.loadtxt('save.csv', delimiter=',', unpack=True)
                    menu = False
                    self.adventureScene()

                self.window.fill((255, 255, 255))
                self.startText = utils.getFont(size=60, style="bold").render("Monster Clicker", True,
                                                                             utils.black)
                self.window.blit(self.startText, (self.surface.get_width() / 3.5, self.surface.get_height() / 3.02))
                self.window.blit(self.startButton, self.startButton_rect)
                self.window.blit(self.loadSaveButton, self.loadSaveButton_rect)
                self.window.blit(self.exitGameButton, self.exitGameButton_rect)
                pygame.display.update()

    def pause(self):
        # Function that keeps track of the pause menu
        global clickMultiplier
        global money
        global item1Cost
        global csv_writer
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.exitGameButton_rect.collidepoint(event.pos):
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print('game unpaused')
                        pause = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.continueButton_rect.collidepoint(event.pos):
                    print('game unpaused')
                    pause = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.saveGameButton_rect.collidepoint(event.pos):
                    with open('save.csv', 'w') as savedVariables:
                        csv_writer = csv.writer(savedVariables)
                        csv_writer.writerow([clickMultiplier, money, item1Cost, item3Cost])
                        savedVariables.close()

                self.window.fill((169, 169, 169))
                self.pauseText = utils.getFont(size=60, style="bold").render("Game Paused", True,
                                                                             utils.black)
                self.window.blit(self.pauseText, (self.surface.get_width() / 3.02, self.surface.get_height() / 3.02))
                self.window.blit(self.continueButton, self.continueButton_rect)
                self.window.blit(self.saveGameButton, self.saveGameButton_rect)
                self.window.blit(self.exitGameButton, self.exitGameButton_rect)
                pygame.display.update()

    def adventureScene(self):
        # Function that keeps track of the main adventure menu
        global money
        global incrementMoney
        global clickMultiplier
        mainGame = True
        while mainGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print('game paused')
                        self.pause()
                if event.type == pygame.MOUSEBUTTONDOWN and self.monster_rect.collidepoint(event.pos):
                    print(money)
                    money = money + clickMultiplier
                if event.type == pygame.MOUSEBUTTONDOWN and self.shopButton_rect.collidepoint(event.pos):
                    mainGame = False
                    self.gameShop()

            money += incrementMoney
            self.window.blit(self.forest, self.forest_rect)
            self.window.blit(self.monster, self.monster_rect)
            self.window.blit(self.shopButton, self.shopButton_rect)
            self.scoreText = self.myFont.render("Your money = " + str(int(money)) + "$", 1, (255, 255, 255))
            self.window.blit(self.scoreText, (self.surface.get_width() / 80, self.surface.get_height() / 70))
            pygame.display.update()
            pygame.display.flip()

    def gameShop(self):
        # Function that keeps track of the game shop menu
        global item1Cost
        global item2Cost
        global item3Cost
        global item4Cost
        global money
        global incrementMoney
        global clickMultiplier
        shop = True
        while shop:
            self.window.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print('game paused')
                        self.pause()
                if event.type == pygame.MOUSEBUTTONDOWN and self.backButton_rect.collidepoint(event.pos):
                    shop = False
                    self.adventureScene()
                if event.type == pygame.MOUSEBUTTONDOWN and self.icon1_rect.collidepoint(
                        event.pos) and money >= item1Cost:
                    clickMultiplier = clickMultiplier + 1
                    money = money - item1Cost
                if event.type == pygame.MOUSEBUTTONDOWN and self.icon2_rect.collidepoint(
                        event.pos) and money >= item2Cost:
                    item1Cost = item1Cost * 0.90
                    item3Cost = item3Cost * 0.90
                    money = money - item2Cost
                if event.type == pygame.MOUSEBUTTONDOWN and self.icon3_rect.collidepoint(
                        event.pos) and money >= item3Cost:
                    incrementMoney = incrementMoney + 0.01
                    money = money - item3Cost
                if event.type == pygame.MOUSEBUTTONDOWN and self.icon4_rect.collidepoint(
                        event.pos) and money >= item4Cost:
                    money = money - item4Cost

            money += incrementMoney
            self.window.blit(self.brickwall, self.brickwall_rect)
            self.window.blit(self.shopkeeper, self.shopkeeper_rect)
            self.window.blit(self.table, self.table_rect)
            self.window.blit(self.backButton, self.backButton_rect)

            # Icon1 configuration
            self.window.blit(self.icon1, self.icon1_rect)
            self.icon1Text = utils.getFont(size=20, style="bold").render("Extra Clicks", True,
                                                                         utils.black)
            self.window.blit(self.icon1Text, (self.surface.get_width() / 3.95, self.surface.get_height() / 7.17))
            self.icon1TextCost = utils.getFont(size=22, style="").render(str(int(item1Cost)) + '$', True,
                                                                         utils.black)
            self.window.blit(self.icon1TextCost, (self.surface.get_width() / 3.43, self.surface.get_height() / 4.1))

            # Icon2 configuration
            self.window.blit(self.icon2, self.icon2_rect)
            self.icon2Text = utils.getFont(size=20, style="bold").render("Cost Down", True,
                                                                             utils.black)
            self.window.blit(self.icon2Text, (self.surface.get_width() / 1.55, self.surface.get_height() / 7.17))
            self.icon2TextCost = utils.getFont(size=22, style="").render(str(int(item2Cost)) + '$', True,
                                                                         utils.black)
            self.window.blit(self.icon2TextCost, (self.surface.get_width() / 1.489, self.surface.get_height() / 4.1))

            # Icon3 configuration
            self.window.blit(self.icon3, self.icon3_rect)
            self.icon3Text = utils.getFont(size=20, style="bold").render("Passive Income", True,
                                                                         utils.black)
            self.window.blit(self.icon3Text, (self.surface.get_width() / 4.05, self.surface.get_height() / 2.35))
            self.icon3TextCost = utils.getFont(size=22, style="").render(str(int(item3Cost)) + '$', True,
                                                                         utils.black)
            self.window.blit(self.icon3TextCost, (self.surface.get_width() / 3.38, self.surface.get_height() / 1.88))

            # Icon4 configuration
            self.window.blit(self.icon4, self.icon4_rect)
            self.icon4Text = utils.getFont(size=20, style="bold").render("Next Level", True,
                                                                         utils.black)
            self.window.blit(self.icon4Text, (self.surface.get_width() / 1.56, self.surface.get_height() / 2.348))
            self.icon4TextCost = utils.getFont(size=22, style="").render(str(int(item4Cost)) + '$', True,
                                                                         utils.black)
            self.window.blit(self.icon4TextCost, (self.surface.get_width() / 1.499, self.surface.get_height() / 1.88))

            self.scoreText = self.myFont.render("Your money = " + str(int(money)) + "$", 1, (255, 255, 255))
            self.window.blit(self.scoreText, (self.surface.get_width() / 80, self.surface.get_height() / 70))
            pygame.display.update()
        pygame.quit()

# Calls our game to start
game = Main_Game()
game.startMenu()
