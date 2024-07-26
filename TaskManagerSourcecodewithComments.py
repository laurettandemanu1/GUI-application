import tkinter as tk
from tkinter import messagebox

class TaskManager:
    """
    TaskManager class to create a task manager application using Tkinter.
    """

    def __init__(self, root):
        """
        Initialize the TaskManager with the main window and widgets.
        
        Parameters:
        root (tk.Tk): The main window of the application.
        """
        self.root = root
        self.root.title("Task Manager")
        self.tasks = []  # List to store tasks

        # Create main window widgets
        self.label = tk.Label(root, text="Task Manager", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.new_task_button = tk.Button(root, text="New Task", command=self.open_new_task_window)
        self.new_task_button.pack()

        self.view_tasks_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.view_tasks_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=self.root.destroy)
        self.exit_button.pack()

    def open_new_task_window(self):
        """
        Open a new window to enter a new task and its priority.
        """
        new_task_window = tk.Toplevel(self.root)
        new_task_window.title("New Task")

        # Create new task window widgets
        tk.Label(new_task_window, text="Enter Task:").pack()
        self.task_entry = tk.Entry(new_task_window)  # Entry widget for task
        self.task_entry.pack()

        tk.Label(new_task_window, text="Enter Priority:").pack()
        self.priority_entry = tk.Entry(new_task_window)  # Entry widget for priority
        self.priority_entry.pack()

        self.save_button = tk.Button(new_task_window, text="Save", command=self.save_task)
        self.save_button.pack()

    def save_task(self):
        """
        Save the entered task and its priority to the tasks list.
        """
        task = self.task_entry.get()  # Get task from entry widget
        priority = self.priority_entry.get()  # Get priority from entry widget

        if not task or not priority:
            messagebox.showerror("Error", "Task and Priority cannot be empty.")
            return

        try:
            priority = int(priority)  # Convert priority to integer
        except ValueError:
            messagebox.showerror("Error", "Priority must be an integer.")
            return

        self.tasks.append((task, priority))  # Append task and priority to tasks list
        messagebox.showinfo("Success", "Task saved successfully.")
        self.task_entry.delete(0, tk.END)  # Clear task entry widget
        self.priority_entry.delete(0, tk.END)  # Clear priority entry widget

    def view_tasks(self):
        """
        Open a new window to display all saved tasks sorted by priority.
        """
        view_tasks_window = tk.Toplevel(self.root)
        view_tasks_window.title("View Tasks")

        if not self.tasks:
            tk.Label(view_tasks_window, text="No tasks found.").pack()
        else:
            for task, priority in sorted(self.tasks, key=lambda x: x[1]):
                tk.Label(view_tasks_window, text=f"Task: {task}, Priority: {priority}").pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
