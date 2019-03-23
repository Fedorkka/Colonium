import pygame
from tkinter import *


class Chip:
    def __init__(self, coord, level, player):
        self.coord = coord
        self.level = level
        self.player = player

    def level_up(self, k):

        self.level += k
        if self.level == 4:
            self.reaction()

    def reaction(self):
        self.level = 0
        c_player = self.player
        self.player = 0
        if self.coord[0] < 7:
            game_field[self.coord[0] + 1][self.coord[1]].player = c_player
            game_field[self.coord[0] + 1][self.coord[1]].level_up(1)

        if self.coord[0] > 0:
            game_field[self.coord[0] - 1][self.coord[1]].player = c_player
            game_field[self.coord[0] - 1][self.coord[1]].level_up(1)

        if self.coord[1] > 0:
            game_field[self.coord[0]][self.coord[1] - 1].player = c_player
            game_field[self.coord[0]][self.coord[1] - 1].level_up(1)

        if self.coord[1] < 7:
            game_field[self.coord[0]][self.coord[1] + 1].player = c_player
            game_field[self.coord[0]][self.coord[1] + 1].level_up(1)


def new_game():
    for i in range(8):
        game_field.append([])
        for z in range(8):
            game_field[i].append(Chip([i, z], 0, 0))
    if players == 2:
        game_field[1][1].player = 1
        game_field[1][6].player = 2
        game_field[1][1].level_up(3)
        game_field[1][6].level_up(3)
    if players == 3:
        game_field[1][1].player = 1
        game_field[1][6].player = 2
        game_field[6][1].player = 3
        game_field[1][1].level_up(3)
        game_field[1][6].level_up(3)
        game_field[6][1].level_up(3)
    if players == 4:
        game_field[1][1].player = 1
        game_field[1][6].player = 2
        game_field[6][1].player = 3
        game_field[6][6].player = 4
        game_field[1][1].level_up(3)
        game_field[1][6].level_up(3)
        game_field[6][1].level_up(3)
        game_field[6][6].level_up(3)

    for i in range(3):
        images.append([])
        for z in range(players):
            images[i].append(
                pygame.image.load(
                    "../Colonium/gameData/Chips/image_part_" + str(i + 1) + str(z + 1) +
                    ".png"))
    for i in range(11):
        playlist.append("../Colonium/gameData/Music/m"+str(i+1)+".mp3")





def draw():
    for i in range(8):
        for z in range(8):
            if game_field[i][z].player != 0 and game_field[i][z].level != 0:
                p = game_field[i][z].player
                lv = game_field[i][z].level
                res = images[lv - 1][p - 1]
                screen.blit(res, (i * 50 + l * (i + 1), z * 50 + l * (z + 1)))
            if game_field[i][z].player == player:
                screen.blit(surf, (i * 50 + l * (i + 1), z * 50 + l * (z + 1)))
            x, y = pygame.mouse.get_pos()
            if (i * 50 + l * (i + 1) <= x <= i * 50 + l * (i + 1) + 50) \
                    and (z * 50 + l * (z + 1) <= y <= z * 50 + l * (z + 1) + 50) \
                    and game_field[i][z].player == player:
                surf.fill((255,200,0))
                screen.blit(surf, (i * 50 + l * (i + 1), z * 50 + l * (z + 1)))
                surf.fill((0,0,0))


    for i in range(9):
        pygame.draw.line(screen, (100, 100, 100), [i * 50 + l * i, 0], [i * 50 + l * i, 400 + l * 9], 2)
        pygame.draw.line(screen, (100, 100, 100), [0, i * 50 + l * i], [400 + l * 9, i * 50 + l * i], 2)


def turn(player):
    player += 1
    if player == players + 1:
        player = 1
    return player


def players_quantity(k, root):
    global players
    players = k
    root.destroy()


def test():
    global players
    try:
        players += 0
    except NameError:
        quit()

def main_menu():
    root = Tk()
    root.geometry("400x400")
    l = Label(root, text="Colonium", font="Arial 30").place(x=120, y=50)
    b2 = Button(root, text="2 Players", font="Arial 20", command=lambda: players_quantity(2, root)).place(x=135, y=125)
    b3 = Button(root, text="3 Players", font="Arial 20", command=lambda: players_quantity(3, root)).place(x=135, y=200)
    b4 = Button(root, text="4 Players", font="Arial 20", command=lambda: players_quantity(4, root)).place(x=135, y=275)
    root.mainloop()
    test()

def new_track():
    global tr
    tr += 1
    if tr == 11:
        tr = 0
    pygame.mixer.music.load(playlist[tr])
    pygame.mixer.music.play()



game_field = []
images = []
playlist = []
l = 2
player = 1

main_menu()
new_game()

surf = pygame.Surface((50, 50))
surf.set_alpha(50)
size = (400 + l * 9, 400 + l * 9)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Colonium")
done = False
clock = pygame.time.Clock()
pygame.mixer.init()
tr= -1
pygame.mixer.music.set_endevent(pygame.USEREVENT)
new_track()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.USEREVENT:
            new_track()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                new_track()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i in range(8):
                for z in range(8):
                    if (i * 50 + l * (i + 1) <= x <= i * 50 + l * (i + 1) + 50) \
                            and (z * 50 + l * (z + 1) <= y <= z * 50 + l * (z + 1) + 50) \
                            and game_field[i][z].player == player:
                        game_field[i][z].level_up(1)
                        player = turn(player)
    screen.fill((255, 255, 255))
    draw()
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
