# Import libraries
import pygame
import os
import utils

# Initialize field variables
clickMultiplier = 1
money = 200
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

        self.myFont = pygame.font.SysFont("monospace", 20)

    def startMenu(self):
        # Our main loops, keeping the game going.
        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.exitGameButton_rect.collidepoint(event.pos):
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.startButton_rect.collidepoint(event.pos):
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
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        print('game unpausedlol')
                        pause = False

                self.window.fill((169, 169, 169))
                pauseText = utils.getFont(size=96, style="bold").render("Paused", True, utils.black)
                pauseTextRect = pauseText.get_rect()
                pauseTextRect.center = self.window.get_rect().center
                self.window.blit(pauseText, pauseTextRect)
                pygame.display.update()

    def adventureScene(self):
        global money
        global clickMultiplier
        mainGame = True
        while mainGame:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        print('game paused')
                        self.pause()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.monster_rect.collidepoint(event.pos):
                    print(money)
                    money = money + clickMultiplier
                if event.type == pygame.MOUSEBUTTONDOWN and self.shopButton_rect.collidepoint(event.pos):
                    mainGame = False
                    self.gameShop()

            self.window.blit(self.forest, self.forest_rect)
            self.window.blit(self.monster, self.monster_rect)
            self.window.blit(self.shopButton, self.shopButton_rect)
            self.scoreText = self.myFont.render("Your money = " + str(money) + "$", 1, (255, 255, 255))
            self.window.blit(self.scoreText, (self.surface.get_width() / 80, self.surface.get_height() / 70))
            pygame.display.update()
            pygame.display.flip()

    def gameShop(self):
        shop = True
        global money
        global clickMultiplier
        while shop:
            self.window.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        print('game paused')
                        self.pause()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.backButton_rect.collidepoint(event.pos):
                    shop = False
                    self.adventureScene()
                if event.type == pygame.MOUSEBUTTONDOWN and self.icon1_rect.collidepoint(event.pos) and money >= 100:
                    clickMultiplier = clickMultiplier + 1
                    money = money - 100

            self.window.blit(self.brickwall, self.brickwall_rect)
            self.window.blit(self.shopkeeper, self.shopkeeper_rect)
            self.window.blit(self.table, self.table_rect)
            self.window.blit(self.backButton, self.backButton_rect)
            self.window.blit(self.icon1, self.icon1_rect)
            self.scoreText = self.myFont.render("Your money = " + str(money) + "$", 1, (255, 255, 255))
            self.window.blit(self.scoreText, (self.surface.get_width() / 80, self.surface.get_height() / 70))
            pygame.display.update()

        pygame.quit()


game = Main_Game()
game.startMenu()
