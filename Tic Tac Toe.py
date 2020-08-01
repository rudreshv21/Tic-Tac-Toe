#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output


# In[2]:


def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[3]:


def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input('Select your marker:').upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')       


# In[4]:


def place_marker(board,marker,position):
    board[position]=marker


# In[5]:


def win_check(board,marker):
    return((board[1]==board[2]==board[3]==marker)or(board[4]==board[5]==board[6]==marker)or(board[7]==board[8]==board[9]==marker)or
          (board[1]==board[4]==board[7]==marker)or(board[2]==board[5]==board[8]==marker)or(board[3]==board[6]==board[9]==marker)or
           (board[1]==board[5]==board[9]==marker)or(board[3]==board[5]==board[7]==marker))


# In[6]:


import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player1'
    else:
        return 'player2'


# In[7]:


def space_check(board,position):
    return board[position]==' '


# In[8]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[9]:


def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('enter your position 1-9:'))
    return position


# In[10]:


def replay():
    choice=input('continue yes or no:')
    return choice=='yes'


# In[ ]:


print('Welcome To Tic Tac Toe')
while True:
    board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+'will go first')
    play_game=input('Ready to play?:')
    if play_game=='yes':
        game_on=True
    else:
        game_on=False
    while game_on:
        if  turn=='player1':
            display_board(board)
            position=player_choice(board)
            place_marker(board,player1_marker,position)
            if win_check(board,player1_marker):
                display_board(board)
                print('player 1 won')
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('tie')
                    game_on=False
                else:
                    turn='player2'
        else:
            display_board(board)
            position=player_choice(board)
            place_marker(board,player2_marker,position)
            if win_check(board,player2_marker):
                display_board(board)
                print('player 2 won')
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('tie')
                    game_on=False
                else:
                    turn='player1'    
    if not replay():
        break


# In[ ]:




