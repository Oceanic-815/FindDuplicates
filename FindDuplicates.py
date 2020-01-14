import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Find duplicates")
        self.master.geometry("900x600")
        self.master.state('zoomed')
        self.pack()  # show
        self.create_widgets()

    def create_widgets(self):
        #  Creating panels to place GUI components there
        self.panel2 = tk.Frame(bg='#d7d8f0', bd=2)
        self.panel2.pack(side=tk.TOP, fill=tk.X)
        self.text_in_panel2 = tk.Label(self.panel2, bg='#d7d8e0', text="Где искать: ")
        self.text_in_panel2.pack(side=tk.LEFT)
        self.panel = tk.Frame(bg='#d7d8e0', bd=2)
        self.panel.pack(side=tk.TOP, fill='both')

        # Loading images for buttons
        self.do_btn_img = tk.PhotoImage(file='do.gif')
        self.hlp_btn_img = tk.PhotoImage(file='hlp.gif')
        self.exit_img = tk.PhotoImage(file='exit.gif')

        #  Creating field to enter a path
        self.enter_path = ttk.Entry(self.panel2)
        self.enter_path.pack(fill='x')

        #  Creating two Tree views
        self.tree1 = ttk.Treeview(self.panel, columns=("Имя", "Путь", "Размер"), height=15, show='headings')
        self.tree1.column('Имя', width=100, anchor='w')  # (id, width, align)
        self.tree1.column('Путь', width=700, anchor='w')
        self.tree1.column('Размер', width=100, anchor='w')
        self.tree1.heading("Имя", text="Имя")  # Naming columns
        self.tree1.heading("Путь", text="Путь")
        self.tree1.heading("Размер", text="Размер")
        self.tree1.pack(side=tk.LEFT, fill='both', expand=True)
        self.tree2 = ttk.Treeview(self.panel, columns=("Имя", "Путь", "Размер"), height=15, show='headings')
        self.tree2.column('Имя', width=100, anchor='w')  # (id, width, align)
        self.tree2.column('Путь', width=700, anchor='w')
        self.tree2.column('Размер', width=100, anchor='w')
        self.tree2.heading("Имя", text="Имя")  # Naming columns
        self.tree2.heading("Путь", text="Путь")
        self.tree2.heading("Размер", text="Размер")
        self.tree2.pack(side=tk.LEFT, fill='both', expand=True)

        #  Creating buttons
        srch = tk.Button(self, text='Поиск', command=self.do_search, bd=0, compound=tk.TOP, image=self.do_btn_img)
        srch.pack(side=tk.LEFT, pady=5, padx=5)
        hlp_btn = tk.Button(self, text='Что это?', command=self.do_help, bd=0, compound=tk.TOP, image=self.hlp_btn_img)
        hlp_btn.pack(side=tk.LEFT)
        quit = tk.Button(self, text="Выйти", command=self.master.destroy, bd=0, compound=tk.TOP, image=self.exit_img)
        quit.pack(side=tk.LEFT)


    def open_instruction(self):  # Call class with instructions window
        Child()

    def do_search(self):  # Start searching of duplicates
        print("Output")

    def do_help(self):
        self.open_instruction()  # Call function where class Child is created


class Child(tk.Toplevel):  # creates a child window with short instruction
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        hlp_txt = "Программа находит повторяющиеся фотографии и видео\n по указанному пути.\n\n Обнаружение одинаковых " \
                  "файлов происходит не только\n по их именам, но и по MD5 или размеру \n(еще не определился).\n\n" \
                  "Чтобы начать поиск, нужно ввести путь до папки, которую\n нужно просканировать на наличие дубликатов" \
                  " и нажать\n кнопку 'Поиск'. После того, как программа просканирует \n содержимое указанной папки, " \
                  "будут показаны все \nдубликаты и их пути расположения на диске."
        self.title("Краткая справка")
        self.geometry("500x400+500+200")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        hlp_lab = tk.Label(self, text=hlp_txt, bd=1, font="Times 14", justify=tk.CENTER)
        hlp_lab.pack()
        pan_hlp = tk.Frame(bd=1)
        pan_hlp.pack(side=tk.BOTTOM, fill=tk.X)
        close_hlp = tk.Button(self, text="Закрыть", fg="black", command=self.destroy)
        close_hlp.pack(side=tk.BOTTOM)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
