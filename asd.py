import pygame as pg
from time import time


def showAnimation(sc_text, pos, alpha):
    sc_text.set_alpha(alpha)
    screen.blit(sc_text, pos)
    pg.display.update()


def showText(action):
    font = pg.font.SysFont('arial', Font)
    text = ''
    splitaction = action.split(' ')
    lines = 0

    for i in range(len(splitaction)):
        text += splitaction[i] + ' '
        sc_text = font.render(text + splitaction[i + 1], True, (255, 255, 255))
        pos = sc_text.get_rect(center=(width // 2, 0))
        if i == len(splitaction) - 2:
            mainTexts.append([sc_text, pos, time(), 0])
            lines += 1
            break
        elif pos.left < margin or pos.right > width - margin:
            sc_text = font.render(text, True, (255, 255, 255))
            pos = sc_text.get_rect(center=(width // 2, 0))
            mainTexts.append([sc_text, pos, time(), 0])

            lines += 1
            text = ''

    y = actionArea.h // (lines + 1)
    for i in range(len(mainTexts)):
        mainTexts[i][1] = mainTexts[i][0].get_rect(center=(width // 2, actionArea.y + (y * (i + 1))))

    if lines != 1:
        if lines % 2 == 0:
            a, b = (len(mainTexts) // 2 - 1, len(mainTexts) // 2)
            center = [mainTexts[a][1].y, mainTexts[b][1].y]
            x=True
            c = center[0] + (center[1] - center[0]) // 2
            mainTexts[a][1].y = c - (rowMargin // 2)
            mainTexts[b][1].y = c + (rowMargin // 2)
            while True:
                if x:
                    a = b
                    b += 1
                else:
                    b = a
                    a -= 1
                if x and b > len(mainTexts) - 1:
                    x = False
                    a = lines // 2 - 2
                    b = lines // 2 - 1
                elif not x and a < 0:
                    break
                center = [mainTexts[a][1].y, mainTexts[b][1].y]
                if center[1] - center[0] > rowMargin:

                    if x:
                        mainTexts[b][1].y = center[0] + rowMargin
                    else:
                        mainTexts[a][1].y = center[1] - rowMargin
                else:
                    break


def UI(action, variants):
    screen.fill((0, 0, 0))
    showText(action)
    pg.display.update()


def choose(variants, variant):
    for i in variants:
        pass


with open('js.json', 'r', encoding='utf8') as f:
    js = eval(f.read())
    scene = '1'
    width = 600
    height = 600
    margin = 50
    rowMargin = 35
    Font = 20
    mainTexts = []

    pg.init()
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('quest')

    actionArea = pg.draw.rect(screen, (55, 55, 55), (margin, margin, width - (margin * 2), height // 2 - margin // 2))

    pg.time.Clock().tick(60)
    keys = pg.key.get_pressed()
    mx, my = pg.mouse.get_pos()

    UI(js[scene]['a'], js[scene]['v'])

    run = True
    while run:
        pg.draw.rect(screen, (55, 55, 55),
                                  (margin, margin, width - (margin * 2), height // 2 - margin // 2), width=2)

        for i in mainTexts:
            timer = time()
            if timer - i[2] >= 0.02:
                i[3] += 5
                showAnimation(i[0], i[1], i[3])
                i[2] = timer
            if i[3] >= 100:
                mainTexts.remove(i)

        for e in pg.event.get():
            if e.type == pg.QUIT:
                run = False

pg.quit()
