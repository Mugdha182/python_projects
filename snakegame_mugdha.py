import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game in tkinter")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=400, height=400, bg="green")
        self.canvas.pack()

        self.score_label = tk.Label(root, text="Score: 0", font=("Times New Roman", 14))
        self.score_label.pack()

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game, state=tk.DISABLED)
        self.restart_button.pack()

        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.food = self.place_food()
        self.direction = "Down"
        self.game_running = True
        self.score = 0

        self.root.bind("<KeyPress>", self.change_direction)
        self.game_loop()

    def place_food(self):
        while True:
            x = random.randint(0, 19) * 20
            y = random.randint(0, 19) * 20
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            new_direction = event.keysym
            if (self.direction == "Up" and new_direction != "Down") or \
               (self.direction == "Down" and new_direction != "Up") or \
               (self.direction == "Left" and new_direction != "Right") or \
               (self.direction == "Right" and new_direction != "Left"):
                self.direction = new_direction

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            new_head = (head_x, head_y - 20)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 20)
        elif self.direction == "Left":
            new_head = (head_x - 20, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 20, head_y)

        self.snake = [new_head] + self.snake[:-1]

    def check_collision(self):
        head_x, head_y = self.snake[0]
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400 or len(self.snake) != len(set(self.snake)):
            self.game_running = False
            self.canvas.create_text(200, 200, text="Game Over!!", fill="red", font=("Arial", 26))
            self.restart_button.config(state=tk.NORMAL)

    def check_food(self):
        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.place_food()
            self.score += 10
            self.score_label.config(text=f"Score: {self.score}")

    def game_loop(self):
        if self.game_running:
            self.canvas.delete(tk.ALL)
            self.move_snake()
            self.check_collision()
            self.check_food()
            self.draw_objects()
            self.root.after(200, self.game_loop)  

    def draw_objects(self):
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="yellow")
        food_x, food_y = self.food
        self.canvas.create_rectangle(food_x, food_y, food_x + 20, food_y + 20, fill="red")

    def restart_game(self):
        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.food = self.place_food()
        self.direction = "Down"
        self.game_running = True
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.restart_button.config(state=tk.DISABLED)
        self.game_loop()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
