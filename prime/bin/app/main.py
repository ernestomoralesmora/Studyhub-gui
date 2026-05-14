import tkinter as tk
from tkinter import messagebox, ttk
from task_manager import TaskManager


class StudyHubGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("StudyHub Task Manager")
        self.root.geometry("760x560")
        self.root.resizable(False, False)

        self.bg_color = "#2c3e50"
        self.frame_color = "#34495e"
        self.button_color = "#3498db"
        self.list_bg = "#ecf0f1"

        self.root.configure(bg=self.bg_color)

        self.manager = TaskManager()

        self.create_widgets()
        self.refresh_task_list()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="StudyHub Task Manager",
            font=("Helvetica", 20, "bold"),
            bg=self.bg_color,
            fg="white"
        )
        title.pack(pady=15)

        self.stats_label = tk.Label(
            self.root,
            text="Tasks: 0 | Completed: 0",
            font=("Arial", 11),
            bg=self.bg_color,
            fg="white"
        )
        self.stats_label.pack(pady=5)

        input_frame = tk.Frame(
            self.root,
            bg=self.frame_color,
            padx=12,
            pady=12
        )
        input_frame.pack(pady=10)

        tk.Label(
            input_frame,
            text="Task:",
            bg=self.frame_color,
            fg="white",
            font=("Arial", 11)
        ).grid(row=0, column=0, padx=6, pady=4)

        self.task_entry = tk.Entry(
            input_frame,
            width=32,
            font=("Arial", 11)
        )
        self.task_entry.grid(row=0, column=1, padx=6, pady=4)

        tk.Label(
            input_frame,
            text="Priority:",
            bg=self.frame_color,
            fg="white",
            font=("Arial", 11)
        ).grid(row=0, column=2, padx=6, pady=4)

        self.priority_var = tk.StringVar()
        self.priority_combo = ttk.Combobox(
            input_frame,
            textvariable=self.priority_var,
            values=["Low", "Medium", "High"],
            width=10,
            state="readonly",
            font=("Arial", 10)
        )
        self.priority_combo.grid(row=0, column=3, padx=6, pady=4)
        self.priority_combo.current(1)

        add_button = tk.Button(
            input_frame,
            text="Add Task",
            bg="#2ecc71",
            fg="white",
            width=12,
            font=("Arial", 11, "bold"),
            command=self.add_task
        )
        add_button.grid(row=0, column=4, padx=8, pady=4)

        list_frame = tk.Frame(self.root, bg=self.bg_color)
        list_frame.pack(pady=10)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox = tk.Listbox(
            list_frame,
            width=82,
            height=16,
            font=("Arial", 11),
            bg=self.list_bg,
            yscrollcommand=scrollbar.set,
            selectbackground="#5dade2",
            activestyle="none"
        )
        self.task_listbox.pack(side=tk.LEFT)

        scrollbar.config(command=self.task_listbox.yview)

        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=14)

        complete_button = tk.Button(
            button_frame,
            text="Mark Complete / Undo",
            bg=self.button_color,
            fg="white",
            width=20,
            font=("Arial", 11),
            command=self.toggle_task
        )
        complete_button.grid(row=0, column=0, padx=10)

        delete_button = tk.Button(
            button_frame,
            text="Delete Task",
            bg="#e74c3c",
            fg="white",
            width=15,
            font=("Arial", 11),
            command=self.delete_task
        )
        delete_button.grid(row=0, column=1, padx=10)

        refresh_button = tk.Button(
            button_frame,
            text="Refresh",
            bg="#9b59b6",
            fg="white",
            width=12,
            font=("Arial", 11),
            command=self.refresh_task_list
        )
        refresh_button.grid(row=0, column=2, padx=10)

    def add_task(self):
        text = self.task_entry.get().strip()
        priority = self.priority_var.get()

        if not text:
            messagebox.showwarning("Warning", "Please enter a task.")
            return

        self.manager.add_task(text, priority)
        self.task_entry.delete(0, tk.END)
        self.priority_combo.current(1)
        self.refresh_task_list()

    def delete_task(self):
        selected = self.task_listbox.curselection()

        if not selected:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            return

        tasks = self.get_sorted_tasks()
        selected_index = selected[0]
        selected_task = tasks[selected_index]

        original_tasks = self.manager.get_tasks()
        original_index = original_tasks.index(selected_task)

        self.manager.delete_task(original_index)
        self.refresh_task_list()

    def toggle_task(self):
        selected = self.task_listbox.curselection()

        if not selected:
            messagebox.showwarning("Warning", "Please select a task.")
            return

        tasks = self.get_sorted_tasks()
        selected_index = selected[0]
        selected_task = tasks[selected_index]

        original_tasks = self.manager.get_tasks()
        original_index = original_tasks.index(selected_task)

        self.manager.toggle_complete(original_index)
        self.refresh_task_list()

    def get_sorted_tasks(self):
        return sorted(
            self.manager.get_tasks(),
            key=lambda t: {"High": 0, "Medium": 1, "Low": 2}[t["priority"]]
        )

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)

        tasks = self.get_sorted_tasks()

        if not tasks:
            self.task_listbox.insert(tk.END, "No tasks available.")
            self.stats_label.config(text="Tasks: 0 | Completed: 0")
            return

        for i, task in enumerate(tasks):
            status = "✔" if task["completed"] else "○"
            text = f"{status} {task['text']}  (Priority: {task['priority']})"
            self.task_listbox.insert(tk.END, text)

            if task["priority"] == "High":
                self.task_listbox.itemconfig(i, {"bg": "#ffdddd", "fg": "red"})
            elif task["priority"] == "Medium":
                self.task_listbox.itemconfig(i, {"bg": "#fff3cd", "fg": "orange"})
            else:
                self.task_listbox.itemconfig(i, {"bg": "#ddffdd", "fg": "green"})

            if task["completed"]:
                self.task_listbox.itemconfig(i, {"fg": "#555555"})

        total = len(tasks)
        completed = sum(1 for task in tasks if task["completed"])
        self.stats_label.config(text=f"Tasks: {total} | Completed: {completed}")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudyHubGUI(root)
    root.mainloop()