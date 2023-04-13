import tkinter as tk


class FullNameApp:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Midterm Exam Problem 2")
        self.root.geometry("500x350")

        self.label0 = tk.Label(self.root, text="My Full name")
        self.label1 = tk.Label(self.root, text="Enter Given Name:")
        self.entry1 = tk.Entry(self.root)
        self.label2 = tk.Label(self.root, text="Enter Middle Name:")
        self.entry2 = tk.Entry(self.root)
        self.label3 = tk.Label(self.root, text="Enter Last Name:")
        self.entry3 = tk.Entry(self.root)
        self.button = tk.Button(self.root, text="Show Full Name", command=self.show_full_name)
        self.label4 = tk.Label(self.root, text="My Full Name is:")
        self.entry4 = tk.Entry(self.root, state="readonly")

        self.label0.grid(row=0, column=4, padx=20, pady=11)
        self.label1.grid(row=1, column=3, padx=10, pady=3)
        self.entry1.grid(row=1, column=4, padx=20, pady=11)
        self.label2.grid(row=2, column=3, padx=20, pady=11)
        self.entry2.grid(row=2, column=4, padx=20, pady=11)
        self.label3.grid(row=3, column=3, padx=20, pady=11)
        self.entry3.grid(row=3, column=4, padx=20, pady=11)
        self.button.grid(row=4, column=3, columnspan=3, padx=10, pady=10)
        self.label4.grid(row=5, column=3, padx=20, pady=11)
        self.entry4.grid(row=5, column=4, padx=20, pady=11)

    def show_full_name(self):
        given_name = self.entry1.get()
        middle_name = self.entry2.get()
        last_name = self.entry3.get()
        full_name = f"{given_name} {middle_name} {last_name}"
        self.entry4.config(state="normal")
        self.entry4.delete(0, tk.END)
        self.entry4.insert(0, full_name)
        self.entry4.config(state="readonly")

    def run(self):
        self.root.mainloop()


app = FullNameApp()
app.run()