import tkinter as tk
from tkinter import messagebox

class WorkoutGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Personalized Workout Generator")

        
        self.label1 = tk.Label(root, text="Select Fitness Level:", font=("Arial", 14))
        self.label1.pack(pady=10)
        
        self.fitness_level = tk.StringVar(value="Beginner")
        fitness_levels = ["Beginner", "Intermediate", "Advanced"]
        for level in fitness_levels:
            tk.Radiobutton(root, text=level, variable=self.fitness_level, value=level, font=("Arial", 12)).pack(anchor=tk.W)
        
        self.label2 = tk.Label(root, text="Select Fitness Goal:", font=("Arial", 14))
        self.label2.pack(pady=10)
        
        self.fitness_goal = tk.StringVar(value="Strength")
        fitness_goals = ["Strength", "Cardio", "Flexibility"]
        for goal in fitness_goals:
            tk.Radiobutton(root, text=goal, variable=self.fitness_goal, value=goal, font=("Arial", 12)).pack(anchor=tk.W)

        self.generate_button = tk.Button(root, text="Generate Workout", font=("Arial", 14), command=self.generate_workout)
        self.generate_button.pack(pady=20)
        
        self.workout_display = tk.Text(root, height=10, width=50, font=("Arial", 12))
        self.workout_display.pack(pady=20)
    
    def generate_workout(self):
        level = self.fitness_level.get()
        goal = self.fitness_goal.get()
        
        
        workouts = {
            "Beginner": {
                "Strength": [
                    "Push-ups: 3 sets of 10 reps",
                    "Squats: 3 sets of 15 reps",
                    "Dumbbell Press: 3 sets of 12 reps"
                ],
                "Cardio": [
                    "Jumping Jacks: 3 sets of 30 seconds",
                    "Running: 15 minutes",
                    "High Knees: 3 sets of 30 seconds"
                ],
                "Flexibility": [
                    "Forward Bend: 3 sets of 30 seconds",
                    "Quad Stretch: 3 sets of 30 seconds",
                    "Shoulder Stretch: 3 sets of 30 seconds"
                ]
            },
            "Intermediate": {
                "Strength": [
                    "Pull-ups: 3 sets of 8 reps",
                    "Lunges: 3 sets of 12 reps each leg",
                    "Bench Press: 3 sets of 10 reps"
                ],
                "Cardio": [
                    "Burpees: 3 sets of 15 reps",
                    "Cycling: 30 minutes",
                    "Mountain Climbers: 3 sets of 45 seconds"
                ],
                "Flexibility": [
                    "Hamstring Stretch: 3 sets of 45 seconds",
                    "Hip Flexor Stretch: 3 sets of 45 seconds",
                    "Triceps Stretch: 3 sets of 45 seconds"
                ]
            },
            "Advanced": {
                "Strength": [
                    "Deadlifts: 3 sets of 8 reps",
                    "Pistol Squats: 3 sets of 6 reps each leg",
                    "Overhead Press: 3 sets of 8 reps"
                ],
                "Cardio": [
                    "Sprint Intervals: 20 minutes",
                    "Rowing: 30 minutes",
                    "Box Jumps: 3 sets of 20 reps"
                ],
                "Flexibility": [
                    "Pigeon Pose: 3 sets of 60 seconds",
                    "Cobra Stretch: 3 sets of 60 seconds",
                    "Seated Forward Bend: 3 sets of 60 seconds"
                ]
            }
        }

        workout_plan = workouts[level][goal]
        workout_text = f"Workout Plan for {level} {goal}:\n\n"
        workout_text += "\n".join(workout_plan)
        
        self.workout_display.delete("1.0", tk.END)
        self.workout_display.insert(tk.END, workout_text)
        messagebox.showinfo("Workout Generated", "Your workout plan has been generated!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkoutGenerator(root)
    root.mainloop()
