import pygame

pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Tic Tac Toe")
p=[[1,2,3],[1,4,7],[1,5,9],[3,6,9],[7,8,9],[3,5,7],[2,5,8],[4,5,6]]
p1_list=[]
p2_list=[]
p1_count=p2_count=0
font=pygame.font.Font("freesansbold.ttf",32)
s=[1,2,3,4,5,6,7,8,9]

def check(A,B):
    count1=count2=0
    for i in range(len(p)):
        for j in range(3):
            if p[i][j] in A:
                count1+=1
            if p[i][j] in B:
                count2+=1
        if count1==3:
            print("P1")
        elif count2==3:
            print("P2")
        else:
            return 'v'

r=True
while r:
    screen.fill((128,128,128))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            r=False
        if p1_count>p2_count:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    p2_list.append(1)
                elif event.key==pygame.K_2:
                    p2_list.append(2)
                elif event.key==pygame.K_3:
                    p2_list.append(3)
                elif event.key==pygame.K_4:
                    p2_list.append(4)
                elif event.key==pygame.K_5:
                    p2_list.append(5)
                elif event.key==pygame.K_6:
                    p2_list.append(6)
                elif event.key==pygame.K_7:
                    p2_list.append(7)
                elif event.key==pygame.K_8:
                    p2_list.append(8)
                elif event.key==pygame.K_9:
                    p2_list.append(9)
            if event.type==pygame.KEYUP: 
                if event.key in s:
                    p2_count+=1
            if p2_count>=3:
                check(p1_list,p2_list)
        else:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    p1_list.append(1)
                elif event.key==pygame.K_2:
                    p1_list.append(2)
                elif event.key==pygame.K_3:
                    p1_list.append(3)
                elif event.key==pygame.K_4:
                    p1_list.append(4)
                elif event.key==pygame.K_5:
                    p1_list.append(5)
                elif event.key==pygame.K_6:
                    p1_list.append(6)
                elif event.key==pygame.K_7:
                    p1_list.append(7)
                elif event.key==pygame.K_8:
                    p1_list.append(8)
                elif event.key==pygame.K_9:
                    p1_list.append(9)
            if event.type==pygame.KEYUP: 
                if event.key in s:
                    p1_count+=1
            if p1_count>=3:
                if check(p1_list,p2_list)=='v':
                    r=True
                else:
                    r=False
    pygame.display.update()