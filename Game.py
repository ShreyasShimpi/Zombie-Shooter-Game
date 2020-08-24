import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First game")

walkRight = [pygame.image.load('files/R1.png'), pygame.image.load('files/R2.png'), pygame.image.load('files/R3.png'),
             pygame.image.load('files/R4.png'), pygame.image.load('files/R5.png'), pygame.image.load('files/R6.png'),
             pygame.image.load('files/R7.png'), pygame.image.load('files/R8.png'), pygame.image.load('files/R9.png')]
walkLeft = [pygame.image.load('files/L1.png'), pygame.image.load('files/L2.png'), pygame.image.load('files/L3.png'),
            pygame.image.load('files/L4.png'), pygame.image.load('files/L5.png'), pygame.image.load('files/L6.png'),
            pygame.image.load('files/L7.png'), pygame.image.load('files/L8.png'), pygame.image.load('files/L9.png')]
bg = pygame.image.load('files/bg.jpg')
char = pygame.image.load('files/standing.png')

clock = pygame.time.Clock()


class player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = 5
        self.isJump = False
        self.jumpcount = 10
        self.left = False
        self.right = False
        self.walkcount = 0
        self.standing = True
        self.box = (self.x + 20, self.y + 10, 28, 56)

    def draw(self, win):
        if self.walkcount >= 27:
            self.walkcount = 0
        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkcount // 3], (self.x, self.y))
                self.walkcount += 1
            elif self.right:
                win.blit(walkRight[self.walkcount // 3], (self.x, self.y))
                self.walkcount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        self.box = (self.x + 20, self.y + 10, 28, 56)
        # pygame.draw.rect(win, (0, 0, 0), self.box, 2)

    def hit(self):
        self.x = 60
        self.y = 410
        self.isJump = False
        self.jumpcount = 10
        self.walkcount = 0
        font1 = pygame.font.SysFont('comicsans', 100, True)
        text1 = font1.render("-5", 1, (255, 0, 0))
        win.blit(text1, (250 - (text1.get_width() // 2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301


class enemy:
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, w, h, end):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = 2
        self.end = end
        self.path = [self.x, self.end]
        self.walkcount = 0
        self.health = 10
        self.visible = True
        self.box = (self.x + 20, self.y, 28, 60)
        self.bar = (self.x + 20, self.y - 4, 28, 4)

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkcount + 1 >= 33:
                self.walkcount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkcount // 3], (self.x, self.y))
                self.walkcount += 1
            else:
                win.blit(self.walkLeft[self.walkcount // 3], (self.x, self.y))
                self.walkcount += 1

            self.box = (self.x + 20, self.y, 28, 60)
            # pygame.draw.rect(win, (255, 0, 0), self.box, 2)
            self.bar = (self.x + 20, self.y - 4, (28 * self.health // 10), 4)
            pygame.draw.rect(win, (255, 0, 0), self.bar)
        else:
            self.x = 300
            self.y = 410
            self.walkcount = 0
            self.health = 10
            self.box = (self.x + 20, self.y, 28, 60)
            self.bar = (self.x + 20, self.y - 4, 28, 4)
            pygame.time.delay(2000)
            self.visible = True

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 2
        else:
            self.visible = False


class gun:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redraw():
    win.blit(bg, (0, 0))
    text = font.render("score: " + str(score), 1, (0, 0, 0))
    win.blit(text, (390, 10))
    pygame.draw.rect(win, (50, 0, 0), (0, 461, 500, 100))
    player.draw(win)
    enemy1.draw(win)

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# Main Loop
font = pygame.font.SysFont('comicsans', 30, True)
player = player(50, 400, 64, 64)
enemies = []
enemy1 = enemy(100, 404, 64, 64, 450)
enemies.append(enemy1)
shoot = 0
score = 0
bullets = []
facing = 0

run = True
while run:
    clock.tick(27)

    if shoot > 0:
        shoot += 1
    if shoot > 3:
        shoot = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_RIGHT] and player.x < (500 - player.w):
        player.x += player.vel
        player.right = True
        player.left = False
        player.standing = False
    else:
        player.standing = True
        player.walkcount = 0

    if not player.isJump:
        if keys[pygame.K_UP]:
            player.isJump = True
            player.left = False
            player.right = False
            player.walkcount = 0
    else:
        if player.jumpcount >= -10:
            neg = 1
            if player.jumpcount < 0:
                neg = -1
            player.y -= player.jumpcount ** 2 * 0.4 * neg
            player.jumpcount -= 1

        else:
            player.isJump = False
            player.jumpcount = 10

    # Bulllet hit enemy
    for bullet in bullets:
        if bullet.y - bullet.radius < enemy1.box[1] + enemy1.box[3] and bullet.y + bullet.radius > enemy1.box[1]:
            if bullet.x + bullet.radius < enemy1.box[0] + enemy1.box[2] and bullet.x - bullet.radius > enemy1.box[0]:
                enemy1.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if 500 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if keys[pygame.K_SPACE] and shoot == 0:
        if player.left:
            facing = -1
        elif player.right:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                gun(round(player.x + player.w // 2), round(player.y + player.h // 2), 5, (255, 0, 0), facing))
        shoot = 1

    # Enemy hit player
    if player.box[1] < enemy1.box[1] + enemy1.box[3] and player.box[1] + player.box[3] > enemy1.box[1]:
        if player.box[0] < enemy1.box[0] + enemy1.box[2] and player.box[0] + player.box[2] > enemy1.box[0]:
            player.hit()
            score -= 5

    redraw()

pygame.quit()
