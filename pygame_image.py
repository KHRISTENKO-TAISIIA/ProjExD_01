import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg1_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(pg.image.load("ex01/fig/pg_bg.jpg"), True, False)
    bg3_img = pg.transform.flip(bg2_img, False, True)
    kk_img = pg.transform.flip(pg.image.load("ex01/fig/3.png"), True, False)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]
    bg = [bg1_img, bg2_img, bg3_img]

    tmr = 0

    while True:
        tmr = tmr + 1
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%1600
        for i in range(2):
            screen.blit(bg[i], [i*1600-x, 0])
        screen.blit(kk_imgs[tmr%2], [300, 200])
        pg.display.update()
        clock.tick(300)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()