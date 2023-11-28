import sys
import pygame
from pygame.locals import *

### 定数
WIDTH = 640
HEIGHT = 400
MESSAGE = "Hello World"
MIN_SIZE = 8
MAX_SIZE = 113

### モジュール初期化
pygame.init()

### 画面設定
surface = pygame.display.set_mode((WIDTH, HEIGHT))

### 文字設定
fonts = []
for size in range(MIN_SIZE, MAX_SIZE):
    fonts.append(pygame.font.Font("/Windows/Fonts/meiryo.ttc", size))

for size in range(MAX_SIZE, MIN_SIZE, -1):
    fonts.append(pygame.font.Font("/Windows/Fonts/meiryo.ttc", size))

### 無限ループ
while True:

    ### 文字リスト分ループ
    for font in fonts:

        ### 文字列設定(リスト)
        text = font.render(MESSAGE, True, (255, 255, 255))

        ### 文字列サイズ取得
        pos = font.size(MESSAGE)

        ### ベース画面初期化
        surface.fill((0, 0, 0))

        ### テキスト画面表示
        surface.blit(text, (int((WIDTH - pos[0]) / 2), int((HEIGHT - pos[1]) / 2)))

        ### 画面更新
        pygame.display.update()

        ### 一定時間停止
        pygame.time.wait(50)

        ### イベント処理
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                ### 終了処理
                pygame.quit()
                sys.exit()
