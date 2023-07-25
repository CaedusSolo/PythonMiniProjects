import tkinter as tk 
import random 

class TicTacToe:
    def __init__(self):
        self.current_player = random.choice(["circle","cross"]) 
        self.num_turns = 0 
        self.is_box_filled = {(i, j): False for i in range(3) for j in range(3)}
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.root = tk.Tk()
        self.root.geometry("700x680")
        self.root.config(padx=20,pady=20,bg="white")
        self.root.resizable(False,False)
        self.root.title("Tic Tac Toe")

        self.ttt_label = tk.Label(self.root,bg="white",fg="black",
                                  text="Tic Tac Toe",font=("poppins",25,"bold"),
                                  anchor="center")
        self.ttt_label.grid(row=0,column=0)
        self.root.columnconfigure(0,weight=1)

        self.frame = tk.Frame(self.root,bg="white")
        self.frame.grid(row=1,column=0)

        self.canvas = tk.Canvas(self.frame,bg="white",highlightthickness=0,width=650,height=550)
        self.canvas.grid(row=0,column=0)
        self.board_img_path = tk.PhotoImage(file="Tkinter\\Tkinter Tic Tac Toe\\images\\board.png")
        self.board_img = self.canvas.create_image((330,270),image=self.board_img_path)

        self.turn_label = tk.Label(self.root,bg="white",fg="black",font=("poppins",23,"bold"),
                                   text=f"It's {self.current_player}'s turn.",anchor="center")
        self.turn_label.grid(row=2,column=0,sticky="s")
        self.canvas.bind("<Button-1>",self.handle_click)
        self.root.mainloop()


    def draw_symbol(self,x_cor,y_cor): 

        row = int(y_cor / (self.canvas.winfo_height() / 3))
        col = int(x_cor / (self.canvas.winfo_width() / 3))

        if self.is_box_filled[(row, col)] == False:
            cell_width = self.canvas.winfo_width() / 3 
            cell_height = self.canvas.winfo_height() / 3 
            x_center = (col * cell_width) + (cell_width / 2) - 20
            y_center = (row * cell_height) + (cell_height / 2) - 30

            if self.current_player == "cross":
                label = tk.Label(self.canvas,text="X",font=("poppins",50,"bold"),bg="white",fg="black",
                                highlightthickness=0,padx=5)
                label.place(x=x_center,y=y_center)
                self.board[row][col] = "X"
                self.is_box_filled[(row, col)] = True 
                
            else:
                label = tk.Label(self.canvas,text="O",font=("poppins",50,"bold"),bg="white",fg="black",
                                highlightthickness=0,padx=5)
                label.place(x=x_center,y=y_center)
                self.board[row][col] = "O"
                self.is_box_filled[(row, col)] = True 


            winner = self.check_winner()
            if winner:
                self.display_winner(winner)
            elif self.num_turns == 8:
                self.display_winner("draw")
            else:
                self.num_turns += 1
                self.current_player = "cross" if self.current_player == "circle" else "circle"
                self.turn_label.config(text=f"It's {self.current_player}'s turn.")

        else:
            return


    def handle_click(self,event):
        x = event.x 
        y = event.y
        self.draw_symbol(x,y)


    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return row[0]

        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] and self.board[0][column] is not None:
                return self.board[0][column] 
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]
        
        return None 


    def display_winner(self,winner):
        if winner == "draw":
            self.turn_label.config(text="It's a draw!")
        else:
            self.turn_label.config(text=f"{winner} wins!")

        self.ttt_label.config(text="GAME OVER") 
        self.canvas.unbind("<Button-1>")


game = TicTacToe()
