from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("White")
        self.score=0
        with open("high_score.txt") as sc:
            self.high_score=int(sc.read())
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
        # self.chk_score()
    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align="center", font=("Arial,24,normal"))

    def inr_scr(self):
        with open ("high_score.txt","w") as sc:
            sc.write(f"{self.high_score}")        
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0 
        self.update_score()
        self.inr_scr()         
    def update_score(self):
        self.clear()
        self.write(f"SCORES = {self.score} High Score: {self.high_score}",align="center", font=("Arial,24,normal"))

    def increase_score(self):
        self.score +=1   
        self.update_score()         
        
        
    