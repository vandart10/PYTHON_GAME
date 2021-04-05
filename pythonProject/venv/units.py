import unittest
import sys
from abc import ABC, abstractmethod

start_pos_x = 0
start_pos_y = 0
kol = 0


class CWarrior:
    health = 0
    power = 0
    speed_x = 0
    speed_y = 0
    x = 0
    y = 0

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self, warrior):
        pass

    @abstractmethod
    def death(self):
        pass


class CSpell:
    coord_x = 0
    coord_y = 0
    radius = 0


class CRageSpell(CSpell):
    coord_x = 0
    coord_y = 0
    radius = 0
    damage = 0

    def rage(self, *warriors):
        pass


class CHealSpell(CSpell):
    coord_x = 0
    coord_y = 0
    radius = 0
    heal = 0

    def healing(self, *warriors):
        pass


class CSpeedSpell(CSpell):
    coord_x = 0
    coord_y = 0
    radius = 0
    speed = 0

    def fast(self, *warriors):
        pass


class CWizard(CWarrior):

    speed_x = 10
    speed_y = 0
    power = 25
    health = 100
    x = start_pos_x
    y = start_pos_y

    def __init__(self):
        pass

    def produce(self):
        f = CSkeletonFactory()
        return f.create(self.x, self.y)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def attack(self, warrior):
        warrior.health -= self.power
        if warrior.health <= 0:
            warrior.death()

    def death(self):
        del self


class CRam(CWarrior):
    speed_x = 10
    speed_y = 0
    power = 0
    health = 1000
    x = start_pos_x
    y = start_pos_y

    def __init__(self):
        pass

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def attack(self, warrior):
        warrior.health -= self.power
        if warrior.health <= 0:
            warrior.death()

    def death(self):
        fact = CKamikazeFactory()
        fact.create()
        fact.create()
        del self


class CKamikaze(CWarrior):
    speed_x = 100
    speed_y = 0
    power = 100
    __health = 1
    x = start_pos_x
    y = start_pos_y

    def __init__(self):
        pass

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def attack(self, warrior):
        warrior.health -= self.power
        if warrior.health <= 0:
            warrior.death()

    def death(self):
        del self


class CArcher(CWarrior):
    speed_x = 2
    speed_y = 0
    power = 20
    health = 50
    x = start_pos_x
    y = start_pos_y

    def __init__(self):
        pass

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def attack(self, warrior):
        warrior.health -= self.power
        if warrior.health <= 0:
            warrior.death()

    def death(self):
        del self


class CHorseman(CWarrior):
    speed_x = 50
    speed_y = 0
    power = 50
    health = 100
    x = start_pos_x
    y = start_pos_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def attack(self, warrior):
        warrior.health -= self.power
        if warrior.health <= 0:
            warrior.death()

    def death(self):
        del self


class CInfantry(CWarrior):
    speed_x = 25
    speed_y = 0
    power = 60
    health = 90
    x = start_pos_x
    y = start_pos_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def attack(self, warrior):
        warrior.health -= self.power
        if warrior.health <= 0:
            warrior.death()

    def death(self):
        del self


class CSkeleton(CWarrior):
    speed_x = 25
    speed_y = 0
    power = 10
    health = 1
    x = start_pos_x
    y = start_pos_y

    def __init__(self, st_x, st_y):
        self.x = st_x
        self.y = st_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def attack(self, warrior):
        warrior.health -= self.power
        if warrior.health <= 0:
            warrior.death()

    def death(self):
        del self


class CWarriorFactory:
    @abstractmethod
    def create(self):
        pass


class CSpellFactory:
    @abstractmethod
    def create(self):
        pass


class CSkeletonFactory:
    def create(self, x, y):
        return CSkeleton(x, y)


class CInfantryFactory(CWarriorFactory):
    def create(self):
        return CInfantry()


class CKamikazeFactory(CWarriorFactory):
    def create(self):
        return CKamikaze()


class CHorsemanFactory(CWarriorFactory):
    def create(self):
        return CHorseman()


class CArcherFactory(CWarriorFactory):
    def create(self):
        return CArcher()


class CRamFactory(CWarriorFactory):
    def create(self):
        return CRam()


class CWizardFactory(CWarriorFactory):
    def create(self):
        return CWizard()


class CRageSpellFactory(CSpell):
    def create(self):
        return CRageSpell()


class CSpeedSpellFactory(CSpell):
    def create(self):
        return CSpeedSpellFactory()


class CHealSpellFactory(CSpell):
    def create(self):
        return CHealSpellFactory()


class Test(unittest.TestCase):
    wizwarrior = CWizard()
    ramwarrior = CRam()
    arwarrior = CArcher()
    kamwarrior = CKamikaze()
    horwarrior = CHorseman()
    #scwarrior = CSkeleton()
    cinf = CInfantry()

    def test__CWizard__health(self):
        self.assertEqual(self.wizwarrior.health, CWizard.health)
        self.assertIsNotNone(self.wizwarrior)

    def test__CRam__health(self):
        self.assertEqual(self.ramwarrior.health, CRam.health)
        self.assertIsNotNone(self.ramwarrior)

    def test__CArcher__health(self):
        self.assertEqual(self.arwarrior.health, CArcher.health)
        self.assertIsNotNone(self.arwarrior)

    def test__CKam__health(self):
        self.assertEqual(self.kamwarrior.health, CKamikaze.health)
        self.assertIsNotNone(self.kamwarrior)

    def test__CHor__health(self):
        self.assertEqual(self.horwarrior.health, CHorseman.health)
        self.assertIsNotNone(self.horwarrior)

    def test__CInf__health(self):
        self.assertEqual(self.cinf.health, CInfantry.health)
        self.assertIsNotNone(self.cinf)

    def test__fact(self):
        cr = CWizardFactory()
        r = cr.create()
        self.assertEqual(r.health, self.wizwarrior.health)
        self.assertIsNotNone(r)

    def test__create(self):
        c = CHorseman()
        k = CKamikaze()
        c.attack(k)
        self.assertEqual(k.health, -50)


if __name__ == "__main__":
    unittest.main()


import pygame
import pygame.freetype
import random

# Just a ball that falls down
class Ball(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((32, 32))
        self.image.set_colorkey((0, 0, 0))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, pygame.Color('orange'), self.rect.center, 15)
        self.pos = pygame.Vector2(random.randint(0, 200), -10)
        self.rect.center = self.pos
        self.direction = pygame.Vector2(0, 0.1)

    def update(self, events, dt):
        self.direction += pygame.Vector2(0, 0.02)
        self.pos += self.direction * dt
        self.rect.center = self.pos
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):
            self.kill()

# The actual game. Well, actually, it does nothing but switching back to the cutscene
class Game(pygame.sprite.Sprite):
    def __init__(self, font):
        super().__init__()
        self.switch = None
        self.image = pygame.display.get_surface().copy()
        self.image.fill(pygame.Color('darkred'))
        font.render_to(self.image, (10, 30), 'playing a game...', fgcolor=pygame.Color('orange'))
        self.rect = self.image.get_rect()

    def update(self, events, dt):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.switch:
                    self.switch()

# the scripted cutscene
class Cutscene(pygame.sprite.Sprite):
    def __init__(self, font):
        super().__init__()
        self.font = font
        self.switch = None
        self.image = pygame.display.get_surface().copy()
        self.back_colors = {-1: pygame.Color('grey12'), 1: pygame.Color('black')}
        self.back_color = 1
        self.background()
        self.rect = self.image.get_rect()
        # we keep track of time to know when to do what action
        self.timer = 0
        self.sprites = pygame.sprite.Group()
        # we keep this list of actions, so after 500ms we create the first ball etc
        # after 3 seconds, we change the background color etc.
        # after 4 seconds, we start all over again
        self.org_actions = [
            (500, lambda: Ball(self.sprites)),
            (600, lambda: Ball(self.sprites)),
            (1000, lambda: Ball(self.sprites)),
            (2000, lambda: Ball(self.sprites)),
            (2100, lambda: Ball(self.sprites)),
            (2400, lambda: Ball(self.sprites)),
            (3000, lambda: self.switch_background()),
            (3200, lambda: Ball(self.sprites)),
            (4000, lambda: self.reset_timer())
        ]
        self.actions = self.org_actions

    def reset_timer(self):
        self.timer = 0
        self.actions = self.org_actions

    def switch_background(self):
        self.back_color *= -1

    def background(self):
        self.image.fill(self.back_colors[self.back_color])
        self.font.render_to(self.image, (10, 30), 'press [ESC] to quit', fgcolor=pygame.Color('white'))

    def update(self, events, dt):
        # we switch to a different scene when the player presses ESC
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.switch:
                    self.switch()

        # keep track of time
        self.timer += dt

        # do all actions
        for action in [action for action in self.actions if action[0] <= self.timer]:
            action[1]()

        # remove all actions that are in the past
        self.actions = [action for action in self.actions if action[0] > self.timer]

        # update our own sprites and draw stuff
        self.sprites.update(events, dt)
        self.background()
        self.sprites.draw(self.image)


def main():
    font = pygame.freetype.SysFont(None, 20)
    font.origin = True
    screen = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()
    scene = pygame.sprite.GroupSingle()

    game = Game(font)
    cutscene = Cutscene(font)
    game.switch = lambda: scene.add(cutscene)
    cutscene.switch = lambda: scene.add(game)
    scene.add(cutscene)
    dt = 0

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
        screen.fill((200,200,200))
        scene.draw(screen)
        pygame.display.update()
        scene.update(events, dt)
        dt = clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    main()