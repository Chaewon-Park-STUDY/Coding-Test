def solution(board):
    num_first=0
    num_second=0
    for elem in board:
        for _ in elem:
            if _=="O":
                num_first+=1
            elif _=="X":
                num_second+=1
    count_num=num_first+num_second
    
    def win():
        first_win=False
        second_win=False
        if "OOO" in board:
            first_win=True
        if "XXX" in board:
            second_win=True
        for i in range(3):
            if all(board[j][i]=="O" for j in range(3)):
                first_win=True
            else:
                if all(board[j][i]=="X" for j in range(3)):
                    second_win=True
        if all(board[i][i]=="O" for i in range(3)) or all(board[j][2-j]=="O" for j in range(3)):
            first_win=True
        else:
            if all(board[i][i]=="X" for i in range(3)) or all(board[j][2-j]=="X" for j in range(3)):
                second_win=True
        return (first_win,second_win)
        
        
    if count_num%2==0:
        if num_first==num_second and not(win()[0]==True):
            return 1
        else:
            return 0
    else:
        if num_first-num_second==1 and not(win()[1]==True):
            return 1
        else:
            return 0
            