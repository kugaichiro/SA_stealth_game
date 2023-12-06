from pygame.locals import *
import pygame
import sys

import prototype.game.parts


def main():
    pygame.init()  # Pygameを初期化
    screen = pygame.display.set_mode((400, 330))  # 画面を作成
    pygame.display.set_caption("Pygame sample app")  # タイトルを作成

    running = True
    # メインループ
    while running:
        screen.fill((0, 0, 0))  # 画面を黒で塗りつぶす

        # 画像を描画
        # ---------------  1.画像を読み込む  --------------------------

        # 普通に画像を表示する方法
        img1 = pygame.image.load(r"C:\Users\irhi8\PycharmProjects\pythonProject\SA_project\prototype\system-data\picture\human.jpg")

        # 一部の色を透明にする
        """img2 = pygame.image.load("img2.jpg").convert()
        colorkey = img2.get_at((0, 0))
        img2.set_colorkey(colorkey, RLEACCEL)"""

        # 画像の大きさを変える
        """img3 = pygame.image.load("img3.jpg")
        img3 = pygame.transform.scale(img3, (200, 130))  # 200 * 130に画像を縮小"""

        # ---------------  2.画像を表示  --------------------------
        screen.blit(img1, (20, 20))
        #screen.blit(img2, (150, 20))
        #screen.blit(img3, (20, 170))

        pygame.display.update()  # 描画処理を実行
        for event in pygame.event.get():
            if event.type == QUIT:  # 終了イベント
                running = False
                pygame.quit()  # pygameのウィンドウを閉じる
                sys.exit()  # システム終了


if __name__ == "__main__":
    main()
