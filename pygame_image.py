import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    flipped1= pg.transform.flip(bg_img, True, False)
    kouka_img = pg.image.load("fig/3.png")
    kouka_img = pg.transform.flip(kouka_img, True, False)
    kouka_rct = kouka_img.get_rect()
    kouka_rct.center = 300, 200

    tmr = 0
    while True:
        x = tmr%3200
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        kouka_rct.move_ip((-1,0))

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kouka_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            kouka_rct.move_ip((0,+1))
        if key_lst[pg.K_LEFT]:
            kouka_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            kouka_rct.move_ip((+2,0))
        screen.blit(bg_img, [-x, 0])
        screen.blit(flipped1, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(kouka_img, kouka_rct)
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()