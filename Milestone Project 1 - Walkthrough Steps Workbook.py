


# Milestone Project 1: Walkthrough Steps Workbook
# 
# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[1]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# In[2]:


test_board =['#','X','X','X','X','X','X','X','X','X']*10
display_board(test_board)


# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[3]:


def player_input():
    
    marker=''
    while marker!='X' and marker!='O':
        marker = input('player1,choose O or X:').upper()
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return(player1,player2)    


# **TEST Step 2:** run the function to make sure it returns the desired output

# In[4]:


player1_marker,player2_marker=player_input()


# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[5]:


def place_marker(board, marker, position):
    
    board[position]=marker


# **TEST Step 3:** run the place marker function using test parameters and display the modified board

# In[6]:


place_marker(test_board,'$',9           )
display_board(test_board)


# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[8]:


def win_check(board, mark):
    return( (mark==board[1]==board[2]==board[3]) or
    (mark==board[4]==board[5]==board[6]) or        
    (mark==board[7]==board[8]==board[9])or        
    (mark==board[1]==board[5]==board[9]) or       
    (mark==board[1]==board[4]==board[7]) or      
    (mark==board[2]==board[5]==board[8]) or        
    (mark==board[3]==board[6]==board[9]) or            
    (mark==board[3]==board[5]==board[7]))
       
    
        
        
        
    


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# In[9]:


win_check(test_board,'X')


# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[10]:


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[11]:


def space_check(board, position):
    return board[position]==''
    


# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[12]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True        


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[13]:


def player_choice(board):
    
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('enter the position between 1 to 9'))
        
    return position


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[14]:


def replay():
    
    choice=input('play again? Enter yes or no')
    return choice == 'yes'


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[16]:


print('Welcome to "TIC TAC TOE!" "')

while True:
    
    the_board=['']*10
    player1_mark,player2_mark=player_input()
    turn=choose_first()
    print(turn + 'will go first')
    play_game = input(print('ready to play y or n'))
    if play_game=='y':
        game_on=True
    else:
        game_on=False

    while game_on:
        if turn=='player1':
            
            display_board(the_board)
            
            position=player_choice(the_board)
            
            place_marker(the_board,player1_mark,position)
            
            if win_check(the_board,player1_mark):
                display_board(the_board)
                print('player 1 has won')
                game_on=False
            
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    break
                    
                else:
                    turn='player2'
            
            
        
        else:
            
            
            display_board(the_board)
            
            position=player_choice(the_board)
            
            place_marker(the_board,player2_mark,position)
            
            if win_check(the_board,player2_mark):
                display_board(the_board)
                print('player 2 has won')
                game_on=False
            
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    break
                    
                else:
                    turn='player1'
            
            
            

            
    if not replay():
        break


# ## Good Job!
