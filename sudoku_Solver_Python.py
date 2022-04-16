
from tkinter import *
from PIL import Image, ImageTk

input_display = []



def display():
    
    root = Tk()
    root.title("Sudoku Solver")
    canvas = Canvas(root,width=504,height=550)
    canvas.grid(columnspan=1)

    grid_pic = Image.open('/Users/jkaruntzos/Documents/blank-sudoku-grid.png')
    grid_pic = ImageTk.PhotoImage(grid_pic)
    grid_label = Label(image=grid_pic)
    grid_label.image = grid_pic
    grid_label.place(x=0,y=0)

    

    #0,0 => 20,12
    entries = []
    xC = 20
    yC = 12
    for b in range(81):
        if b % 9 == 0 and b != 0:
            yC+=55
            xC = 20
        entry = Entry(root, width=1, bd=1,font = ("Arial",25))
        entry.place(x=xC,y=yC)
        entries.append(entry)
        
        xC+=55

        
    #--------------------#
    def clear(entries):
        for entry in entries:
            entry.delete(0,END)
    
    def button(entries):
        ans = []
        for entry in entries:
            e = entry.get()
            if e == "":
                ans.append("0")
            else:
                ans.append(e)
            
        b = []
        i = 9
        for r in range(9):
            row = ans[(r*i):(r*i)+9]
            b.append(row)

        solve(b)

        r = 0
        c = 0
        for entry in entries:
            if entry.get() == "":
                entry.insert(0,b[r][c])
            c+=1
            if c == 9:
                c = 0
                r+=1
        
    #---------------------#

    solve_button = Button(root, width=20, text = "Solve", command=lambda:button(entries)).place(x = 165, y = 520)
    clear_button = Button(root, width=10, text = "Clear", command=lambda:clear(entries)).place(x=400,y=520)
    
    
    root.mainloop()



board = []

def get_Board():
    lines = []
    for i in range(9):
        lines = input().split()
        r = 0
        for line in lines:
            l = line.split(",")
            board.append(l)

def print_Board(b):
    for r in range(9):
        for c in range(9):
            print("|"+b[r][c], end = "")
            if c == 2 or c == 5 or c == 8:
                print("| ",end = " ")
        print("")
        if r == 2 or r == 5:
            print("  ")

#Returns true if there is a conflict w/ the coord value in its 3x3 square
def in_Square_Conflict(b, coord, t):
    row = coord[0]
    col = coord[1]
    r = 0
    c = 0
    
    if row <= 2:
        r = 0
    elif row >= 6:
        r = 6
    else:
        r = 3

    if col <= 2:
        c = 0
    elif col >= 6:
        c = 6
    else:
        c = 3


    for x in range(3):
        for y in range(3):
            if x != row and y != col:
                if b[r][c+y] == t:
                    return True

        r += 1

    return False



#Returns true if there is a conflict w/ the coord value in its
#horizontal or vertical lines
def in_Line_Conflict(b, coord, t):
    row = coord[0]
    col = coord[1]

    #HORIZONTAL
    for c in range(9):
        if b[row][c] == t and c != col:
            return True
        
    #VERTICAL
    for r in range(9):
        if b[r][col] == t and r != row:
            return True
            
    return False


def conflict(b, coord, t):
    if in_Line_Conflict(b, coord,t) == False and in_Square_Conflict(b, coord,t) == False:
        return False
    return True


def solve(b):

    box = next_Blank(b)
    
    if box == [-1,-1]:
        return b

    for i in range(9):
        val = str(i+1)
        if conflict(b, box, val) == False:
            b[int(box[0])][int(box[1])] = val
            if solve(b) != -1:
                return solve(b)
        b[int(box[0])][int(box[1])] = "0"

    return -1
                


#Returns the coordinates of the next empty space
def next_Blank(b):
    blank = [-1,-1]
    for r in range(9):
        for c in range(9):
            if b[r][c] == "0":
                blank = [r,c]
                return blank
    return blank
    


def main():
    get_Board()
    solve(board)
    print_Board(b)


display()
#main()
