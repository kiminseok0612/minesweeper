import pygame
import os
import random
block_size=32
board_size=10
board_img=[
    [0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0],
    ]
board=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ]
def show_dig_space(y,x):
    if board_img[y][x]==2:
        return
    board_img[y][x]=2
    if board[y][x]!=0:
        return
    if y+1<10:
        show_dig_space(y+1,x)
    if y-1>=0:
        show_dig_space(y-1,x)
    if x+1<10:
        show_dig_space(y,x+1)
    if x-1>=0:
        show_dig_space(y,x-1)
    
pygame.init()
screen=pygame.display.set_mode((320,320))
pygame.display.set_caption("지뢰찾기")
file_path=os.path.dirname(__file__)
image_path=os.path.join(file_path,("image"))
clock=pygame.time.Clock()
background_img=[
    pygame.image.load(os.path.join(image_path,"background1.png")),
    pygame.image.load(os.path.join(image_path,"background2.png")),
    pygame.image.load(os.path.join(image_path,"background3.png")),
    ]
mine_img=pygame.image.load(os.path.join(image_path,"mine.png"))
pointer_img=pygame.image.load(os.path.join(image_path,"pointer.png"))
flag_img=pygame.image.load(os.path.join(image_path,"flag.png"))
num_img=[
    pygame.image.load(os.path.join(image_path,"num1.png")),
    pygame.image.load(os.path.join(image_path,"num2.png")),
    pygame.image.load(os.path.join(image_path,"num3.png")),
    pygame.image.load(os.path.join(image_path,"num4.png")),
    pygame.image.load(os.path.join(image_path,"num5.png")),
    pygame.image.load(os.path.join(image_path,"num6.png")),
    pygame.image.load(os.path.join(image_path,"num7.png")),
    pygame.image.load(os.path.join(image_path,"num8.png")),
    ]
pointer_x_pos=0
pointer_y_pos=0
flag=[]
flag_check=False
do_dig=False
for i in range(10):
    while True:
        mine_x=random.randint(0,9)
        mine_y=random.randint(0,9)
        if board[mine_y][mine_x]==0:
            board[mine_y][mine_x]=-1
            for y in range(-1,2):
                for x in range(-1,2):
                    if (mine_y+y>=0 and mine_y+y<10) and (mine_x+x>=0 and mine_x+x<10) and board[mine_y+y][mine_x+x]!=-1:
                        board[mine_y+y][mine_x+x]+=1
            break

run=True
while run:
    fps=clock.tick(24)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            break
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                if pointer_y_pos+1<=9:
                    pointer_y_pos+=1
            if event.key==pygame.K_UP:
                if pointer_y_pos-1>=0:
                    pointer_y_pos-=1
            if event.key==pygame.K_RIGHT:
                if pointer_x_pos+1<=9:
                    pointer_x_pos+=1
            if event.key==pygame.K_LEFT:
                if pointer_x_pos-1>=0:
                    pointer_x_pos-=1
            if event.key==pygame.K_f:
                flag_check=True
            if event.key==pygame.K_d:
                do_dig=True

    if do_dig:
        if [pointer_x_pos,pointer_y_pos] in flag:
            flag.remove([pointer_x_pos,pointer_y_pos])
        if board[pointer_y_pos][pointer_x_pos]==-1:
            run=False
        else:
            show_dig_space(pointer_y_pos,pointer_x_pos)
        do_dig=False

    if flag_check:
        if [pointer_x_pos,pointer_y_pos] not in flag:
            flag.append([pointer_x_pos,pointer_y_pos])
        else:
            flag.remove([pointer_x_pos,pointer_y_pos])
        flag_check=False

    for i in range(board_size):
        for j in range(board_size):
            screen.blit(background_img[board_img[i][j]],(j*block_size,i*block_size))
            if board[i][j]!=0 and board_img[i][j]==2:
                screen.blit(num_img[board[i][j]-1],(j*block_size,i*block_size))
    for f in flag:
        screen.blit(flag_img,(f[0]*block_size,f[1]*block_size))
    screen.blit(pointer_img,(pointer_x_pos*block_size,pointer_y_pos*block_size))
    pygame.display.update()
    cnt=0
    for i in range(10):
        for j in range(10):
            if board_img[i][j]!=2:
                cnt+=1
    if cnt==10:
        run=False

for i in range(10):
    for j in range(10):
        if board[i][j]==-1:
            screen.blit(mine_img,(j*block_size,i*block_size))
pygame.display.update()
pygame.time.delay(3000)

pygame.quit()
