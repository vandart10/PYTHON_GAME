import units
import pygame
import random
import time
import sys
import os

pygame.init()


screen = pygame.display.set_mode((2000, 4000), pygame.FULLSCREEN)

xx_s = pygame.display.get_window_size()[0]
yy_s = pygame.display.get_window_size()[1]

x = xx_s / 4
y = yy_s / 4

ttt = pygame.Surface((xx_s, yy_s))
img = pygame.image.load('astr.jpg')
ttt.blit(img, (0, 0))
screen.blit(ttt, (0, 0))

fbutton = pygame.Surface((x, y))
sbutton = pygame.Surface((x, y))
tbutton = pygame.Surface((x, y))
fbutton.fill((123, 5, 5))
sbutton.fill((123, 200, 200))
tbutton.fill((255, 255, 255))

f = pygame.font.SysFont('elephant', 47)

x1 = (xx_s - 3 * x) / 4
y1 = (yy_s / 2 - y) / 2
screen.blit(fbutton, (x1, y1))
t1 = f.render('SPEED MODE', False, (123, 200, 200))
screen.blit(t1, (x1, y1))

x2 = xx_s - (xx_s - 3 * x) / 4 - x
y2 = (yy_s / 2 - y) / 2
screen.blit(sbutton, (x2, y2))
t2 = f.render('SCORE MODE', False, (123, 5, 5))
screen.blit(t2, (x2, y2))

x3 = (xx_s - x) / 2
y3 = yy_s / 2 + (yy_s / 2 - y) / 2
screen.blit(tbutton, (x3, y3))
t3 = f.render('KEY MODE', False, (163, 20, 210))
screen.blit(t3, (x3, y3))

pygame.display.update()
mode = 0


process = True
while not mode and process:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            process = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            coord = pygame.mouse.get_pos()
            if x1 <= coord[0] <= x1 + x and y1 <= coord[1] <= y1 + y:
                mode = 1
                print(1)
                break
            if x2 <= coord[0] <= x2 + x and y2 <= coord[1] <= y2 + y:
                mode = 2
                print(2)
                break
            if x3 <= coord[0] <= x3 + x and y3 <= coord[1] <= y3 + y:
                mode = 3
                print(3)
                break

#print(pygame.font.get_fonts())
if not process:
    pygame.quit()
x_sz = 40
y_sz = 40

if mode == 2:

    screen.fill((255, 255, 255))
    ttt = pygame.Surface((xx_s, yy_s))
    img = pygame.image.load('astr.jpg')
    ttt.blit(img, (0, 0))
    screen.blit(ttt, (0, 0))
    pygame.display.update()
    fon = pygame.font.SysFont('franklingothicmedium', 30)
    s1 = fon.render('YOU CAN TAP _space_ TO INCREASE THE NUMBER OF POINTS PER CLICK OK??', False, (255, 10, 10))
    s2 = fon.render('YOU CAN TAP _s_ TO SPEED UP THE APPEARANCE OF THE SQUARES ON THE SCREEN YOU KNOW Im SAYIN' + '\'', False, (255, 10, 10))
    s3 = fon.render('I THINK YOU ALSO CAN TAP _w_ TO NARROW THE BOUNDARIES OF APPEARANCE OF THE SQUARES', False, (255, 10, 10))
    screen.blit(s1, (xx_s / 40, yy_s / 40))
    screen.blit(s2, (xx_s / 40, 4 * yy_s / 40))
    screen.blit(s3, (xx_s / 40, 8 * yy_s / 40))
    process = True
    ok = pygame.Surface((x, y))
    ok.fill((100, 100, 100))
    screen.blit(ok, (xx_s / 3, yy_s - yy_s / 3))
    scc = fon.render('I GOT IT', False, (200, 200, 200))
    screen.blit(scc, (xx_s / 3 + x / 3, yy_s - yy_s / 4 + y / 6))
    pygame.display.update()
    while process:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                process = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                coord = pygame.mouse.get_pos()
                if xx_s / 3 + x / 3 <= coord[0] <= xx_s / 3 + x / 3 + x and yy_s - yy_s / 4 + y / 6 <= coord[1] <= yy_s - yy_s / 4 + y / 6 + y:
                    process = False

else:
    screen.fill((255, 255, 255))

background = pygame.Surface((xx_s, yy_s))
img = pygame.image.load('phn.jpg')
background.blit(img, (0, 0))

del_obj = pygame.Surface((x_sz, y_sz))
del_obj.fill((9, 255, 255))

if mode == 3:
    x_sz *= 4
    y_sz *= 4

#franklingothicmedium
#sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic
#bodoniblack
#elephant
#chiller
#freestylescript
#frenchscript
#bauhaus93

font = pygame.font.SysFont('chiller', 50)
score = 0.0
sc_k = 1
speed = 1.5

x = 0
y = 300
x1 = 0
y1 = 0
process = True
px = 0
py = 0
px1 = 0
py1 = 0
l = 0
u_r = 0
u_g = 0
u_b = 0
f_r = 255 - u_r
f_g = 255 - u_g
f_b = 255 - u_b
ft = time.time()
timer = 60
c_time = time.time()
streak = 0
tap_time = time.time()
flag = True
screen.fill((255, 255, 255))
minus = 50
koef = 1
kf = 1
first = False
u = False
k = 0
best = 0
let = 'a'
l = []
for i in range(97, 97 + 26):
    l.append(chr(i))

while process:
    screen.blit(background, (0, 0))
    u = False
    if not first:
        if mode < 3:
            kol = random.randint(2, 8)
            u_r = random.randint(1, 250)
            u_g = random.randint(1, 250)
            u_b = random.randint(1, 250)
            f_r = 251 - u_r
            f_g = 251 - u_g
            f_b = 251 - u_b
            x = random.uniform(0, xx_s - x_sz)
            y = random.uniform(45, yy_s - y_sz)
            del_obj.fill((u_r, u_g, u_b))
            first = True
        else:
            u_r = random.randint(1, 250)
            u_g = random.randint(1, 250)
            u_b = random.randint(1, 250)
            let = l[random.randint(0, 25)]
            f_r = 251 - u_r
            f_g = 251 - u_g
            f_b = 251 - u_b
            x = random.uniform(0, xx_s - x_sz)
            y = random.uniform(45, yy_s - y_sz)
            le = font.render(str(l[0]), False, (0, 0, 0))
            screen.blit(le, (x, y))
            pygame.display.update()
            first = True
    if flag:
        timer = 60 - time.time() + c_time
        if timer < 0.01:
            flag = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                process = False
            if mode < 3:
                if e.type == pygame.MOUSEBUTTONDOWN:
                    coord = pygame.mouse.get_pos()
                    if y <= coord[1] <= y + y_sz and x <= coord[0] <= x + x_sz:
                        if mode == 1:
                            u_r = random.randint(1, 250)
                            u_g = random.randint(1, 250)
                            u_b = random.randint(1, 250)
                            f_r = 251 - u_r
                            f_g = 251 - u_g
                            f_b = 251 - u_b
                            x = random.uniform(0, xx_s - x_sz)
                            y = random.uniform(45, yy_s - y_sz)
                            del_obj.fill((u_r, u_g, u_b))
                        score += 100 * sc_k * (streak + 1)
                        y1 = -1
                        x1 = -1
                        streak += 1
                        if not best:
                            best += 1
                        minus = 50 * sc_k * (streak + 1)
                        u = True
                        k += 1

                    else:
                        if streak > best:
                            best = streak
                        streak = 0
                        score -= minus
            if mode == 2:
                if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and score >= 200 * sc_k:
                    score -= 200 * sc_k
                    sc_k *= 1.1
                if e.type == pygame.KEYDOWN and e.key == pygame.K_s and score >= 200 * kf:
                    speed -= 0.05
                    score -= 200 * kf
                    kf *= 1.5
                if e.type == pygame.KEYDOWN and e.key == pygame.K_w and score >= 200 * koef:
                    xx_s -= 50
                    yy_s -= 50
                    score -= 200 * koef
                    koef *= 1.1
            if mode == 3 and e.type == pygame.KEYDOWN:
                fl = 0
                fl = fl or (e.key == pygame.K_q and let == 'q')
                fl = fl or (e.key == pygame.K_w and let == 'w')
                fl = fl or (e.key == pygame.K_e and let == 'e')
                fl = fl or (e.key == pygame.K_r and let == 'r')
                fl = fl or (e.key == pygame.K_t and let == 't')
                fl = fl or (e.key == pygame.K_y and let == 'y')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_u and let == 'u')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_i and let == 'i')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_o and let == 'o')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_p and let == 'p')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_a and let == 'a')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_s and let == 's')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_d and let == 'd')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_f and let == 'f')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_g and let == 'g')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_h and let == 'h')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_j and let == 'j')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_k and let == 'k')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_l and let == 'l')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_z and let == 'z')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_x and let == 'x')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_c and let == 'c')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_v and let == 'v')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_b and let == 'b')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_n and let == 'n')
                fl = fl or (e.type == pygame.KEYDOWN and e.key == pygame.K_m and let == 'm')
                if fl:
                    k += 1
                    streak += 1
                    if not best:
                        best += 1
                    u_r = random.randint(1, 250)
                    u_g = random.randint(1, 250)
                    u_b = random.randint(1, 250)
                    f_r = 251 - u_r
                    f_g = 251 - u_g
                    f_b = 251 - u_b
                    let = l[random.randint(0, 25)]
                    x = random.uniform(0, xx_s - x_sz)
                    y = random.uniform(45, yy_s - y_sz)
                else:
                    if streak > best:
                        best = streak
                    streak = 0
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    process = False

        if u:
            screen.blit(background, (0, 0))
        if mode < 3:
            screen.blit(del_obj, (x, y))
        titl = font.render('YOUR COLOR', False, (u_r, u_g, u_b))
        screen.blit(titl, (0, 0))

        if mode == 2:
            ssc = font.render('SCORE', False, (255, 10, 10))
            sc = font.render("{0:.2f}".format(score), False, (255, 10, 10))
            screen.blit(ssc, (600, 0))
            screen.blit(sc, (600, 50))

            per = font.render('Periodicity', False, (150, 100, 100))
            pper = font.render("{0:.2f}".format(speed), False, (150, 100, 100))
            screen.blit(per, (1300, 0))
            screen.blit(pper, (1300, 50))

            tiimer = font.render("{0:.2f}".format(timer), False, (0, 0, 0))
            screen.blit(tiimer, (100, 100))

        strk = font.render(str(streak), False, (110, 1, 2))
        sn = font.render('WIN STREAK', False, (110, 1, 2))
        screen.blit(sn, (1000, 0))
        screen.blit(strk, (1000, 50))

        if mode == 1 or mode == 3:
            avr = font.render('AVERAGE SPEED', False, (12, 32, 31))
            avrs = font.render("{0:.2f}".format(k / (60 - timer)), False, (150, 100, 100))
            screen.blit(avr, (400, 0))
            screen.blit(avrs, (400, 50))
            fo = pygame.font.SysFont('chiller', 50)
            tiimer = fo.render("{0:.2f}".format(timer), False, (0, 0, 0))
            screen.blit(tiimer, (700, 0))
            fff = pygame.font.SysFont(
                'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic',
                50)
            le = fff.render(str(let), False, (u_r, u_g, u_b))
            screen.blit(le, (x, y))

        lt = time.time()
        if mode == 2:
            if lt - ft >= speed or u:
                kol = random.randint(2, 8)
                u_r = random.randint(1, 250)
                u_g = random.randint(1, 250)
                u_b = random.randint(1, 250)
                f_r = 251 - u_r
                f_g = 251 - u_g
                f_b = 251 - u_b
                ft = lt
                x = random.uniform(0, xx_s - x_sz)
                y = random.uniform(45, yy_s - y_sz)
                del_obj.fill((u_r, u_g, u_b))

        #window.blit(screen, (0, 0))
        pygame.display.update()
    else:
        screen.fill((255, 255, 255))
        fff = pygame.image.load('moon.jpg')
        back = pygame.Surface((xx_s, yy_s))
        back.blit(fff, (0, 0))
        screen.blit(back, (0, 0))
        obj = pygame.Surface((400, 600))
        obj2 = pygame.Surface((400, 600))
        img = pygame.image.load('mario.jpg')
        img2 = pygame.image.load('mario2.jpg')
        obj.blit(img, (0, 0))
        obj2.blit(img2, (0, 0))
        obj.set_colorkey((255, 255, 255))
        obj2.set_colorkey((255, 255, 255))
        text = "YOU WIN (maybe)  "
        if mode == 1:
            text += "{0:.2f}".format(score)
        if mode != 2:
            avr = font.render('AVERAGE SPEED', False, (0, 0, 0))
            avrs = font.render("{0:.2f}".format(k / (60 - timer)), False, (0, 0, 0))
            screen.blit(avr, (1000, 0))
            screen.blit(avrs, (1000, 25))

        sn = font.render('WIN STREAK', False, (0, 0, 0))
        strk = font.render(str(best), False, (0, 0, 0))
        t = font.render(text, True, (0, 0, 0))
        screen.blit(t, (0, 0))
        screen.blit(sn, (xx_s - 300, 0))
        screen.blit(strk, (xx_s - 300, 50))
        process = True
        ko = 0
        t1 = time.time()
        x = 0
        y = 400
        while process:
            t = time.time()
            if t - t1 >= 0.3:
                t1 = t
                ko += 1
                fff = pygame.image.load('moon.jpg')
                screen.blit(back, (0, 0))
                if ko % 2 == 0:
                    screen.blit(obj, (x, y))
                else:
                    screen.blit(obj2, (x, y))
                x += 2
                if x == xx_s:
                    x = 0
            text = "YOU WIN (maybe)  "
            if mode == 1:
                text += "{0:.2f}".format(score)
            if mode != 2:
                avr = font.render('AVERAGE SPEED', False, (0, 0, 0))
                avrs = font.render("{0:.2f}".format(k / (60 - timer)), False, (0, 0, 0))
                screen.blit(avr, (1000, 0))
                screen.blit(avrs, (1000, 25))

            sn = font.render('WIN STREAK', False, (0, 0, 0))
            strk = font.render(str(best), False, (0, 0, 0))
            t = font.render(text, True, (0, 0, 0))
            screen.blit(t, (500, 0))
            screen.blit(sn, (xx_s - 300, 0))
            screen.blit(strk, (xx_s - 300, 50))
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    process = False
            pygame.display.update()
pygame.quit()
