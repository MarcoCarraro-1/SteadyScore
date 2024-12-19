import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, ttk
from PIL import Image, ImageTk
import api

root = tk.Tk()
username = ""
password = ""
font="Roboto"
button_style = {'width': 20, 'height': 2, 'bg': "#4CAF50", 'fg': "white", 'font': ('Roboto', 12, 'bold'), 'bd': 0, 'relief': 'flat'}
label_style = {'font': ('Roboto', 16), 'fill':'white'}
entry_style = {'width': 50, 'bg':"white",  'font': ('Roboto', 16), 'bd': 1, 'relief': 'flat', 'highlightthickness': 0}
text_style = {'font': ("Roboto", 24, "bold"), 'fill': "white"}
subject = ""
argument = ""
num_questions = 0
school_level = ""
question_type = ""
difficulty = ""
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
bg_image = Image.open("background.jpg") 
bg_image = bg_image.resize((sc_width, sc_height), Image.LANCZOS) 
bg_photo = ImageTk.PhotoImage(bg_image)
gif = Image.open("loading.gif")  # Percorso della tua GIF
gif_frames = []
try:
    while True:
        gif.seek(len(gif_frames))  # Sposta al frame successivo
        gif_frames.append(ImageTk.PhotoImage(gif.copy()))  # Copia il frame attuale
except EOFError:
    pass  # Fine dei frame



def greet_user():
    messagebox.showinfo("Welcome", "Hi and welcome to SteadyScore!")

def animate_gif(canvas, gif_frames, x, y, delay, current_frame=0):
    frame = gif_frames[current_frame]
    canvas.itemconfig(gif_id, image=frame)  # Aggiorna l'immagine del canvas
    next_frame = (current_frame + 1) % len(gif_frames)  # Ciclo dei frame
    canvas.after(delay, animate_gif, canvas, gif_frames, x, y, delay, next_frame)

def create_rounded_entry(canvas, x, y, width, height, entry_style, radius=20, bg_color="#FFFFFF", outline_color="#4CAF50", password=False):
    # Disegna un rettangolo arrotondato
    id_oval_top_left = canvas.create_oval(x - width // 2, y - height // 2, x - width // 2 + radius * 2, y - height // 2 + radius * 2, fill=bg_color, outline=outline_color)
    id_oval_top_right = canvas.create_oval(x + width // 2 - radius * 2, y - height // 2, x + width // 2, y - height // 2 + radius * 2, fill=bg_color, outline=outline_color)
    id_oval_bottom_left = canvas.create_oval(x - width // 2, y + height // 2 - radius * 2, x - width // 2 + radius * 2, y + height // 2, fill=bg_color, outline=outline_color)
    id_oval_bottom_right = canvas.create_oval(x + width // 2 - radius * 2, y + height // 2 - radius * 2, x + width // 2, y + height // 2, fill=bg_color, outline=outline_color)
    id_rect_top = canvas.create_rectangle(x - width // 2 + radius, y - height // 2, x + width // 2 - radius, y - height // 2 + radius, fill=bg_color, outline=outline_color)
    id_rect_bottom = canvas.create_rectangle(x - width // 2 + radius, y + height // 2 - radius, x + width // 2 - radius, y + height // 2, fill=bg_color, outline=outline_color)
    id_rect_center = canvas.create_rectangle(x - width // 2, y - height // 2 + radius, x + width // 2, y + height // 2 - radius, fill=bg_color, outline=outline_color)

    # Crea l'Entry sopra il rettangolo
    if(password):
        entry = tk.Entry(canvas.master, **entry_style, show='*')
    else:
        entry = tk.Entry(canvas.master, **entry_style)
    canvas.create_window(x, y, window=entry, width=width - 10, height=height - 10)  # Padding interno
    return entry


def show_login():
    global username, password
    root.title("Login")
    root.geometry(f"{sc_width}x{sc_height}")
    root.config(bg="#f0f0f0")

    canvas = tk.Canvas(root, width=sc_width, height=sc_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    
    canvas.create_text(sc_width/2, 50, text="Login", font=("Roboto", 24, "bold"), fill="white")
    
    canvas.create_text(sc_width/2, 150, text="Username", **text_style)
    username_entry = create_rounded_entry(canvas, sc_width/2, 200, 300, 50, entry_style, radius=20, bg_color="#FFFFFF", outline_color="#FFFFFF")
    #username_entry = tk.Entry(root, **entry_style)
    #username_entry.pack(pady=10, padx=10)
    #canvas.create_window(sc_width/2, 200, window=username_entry, width=250)

    canvas.create_text(sc_width/2, 270, text="Password", **text_style)
    password_entry = create_rounded_entry(canvas, sc_width/2, 320, 300, 50, entry_style, radius=20, bg_color="#FFFFFF", outline_color="#FFFFFF", password=True)
    #password_entry = tk.Entry(root, show="*", **entry_style) 
    #password_entry.pack(pady=10, padx=10)
    #canvas.create_window(sc_width/2, 320, window=password_entry, width=250)

    def save_credentials():
        global username, password
        username = username_entry.get()
        password = password_entry.get()
        print(f"Username: {username}")
        print(f"Password: {password}")
        login()

    login_button = tk.Button(root, text="Login", command=save_credentials, **button_style)
    login_button.pack(pady=10)
    canvas.create_window(sc_width/2, 400, window=login_button)

    root.bind("<Return>", lambda: save_credentials())

def login():

    if username == "marco" and password == "marco":
        #messagebox.showinfo("Login", "Accesso riuscito!")
        show_main_page()
    else:
        messagebox.showerror("Login", "Username or password incorrect!"+username+password)

def open_exercise_options():
    dialog = Toplevel(root)
    dialog.title("Let's Exercise!")
    dialog.geometry("300x200")
    dialog.config(bg="#f0f0f0")

    def option_selected(option):
        dialog.destroy()
        print("this option"+option)
        if(option == "New Test from Scratch"):
            show_form()
    
    tk.Button(dialog, text="New Test from Scratch", command=lambda: option_selected("New Test from Scratch"), **button_style).pack(pady=10)
    tk.Button(dialog, text="New Test from Slides", command=lambda: option_selected("New Test from Slides"), **button_style).pack(pady=10)
    tk.Button(dialog, text="New Test from Notes", command=lambda: option_selected("New Test from Notes"), **button_style).pack(pady=10)

def show_form():
    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=sc_width, height=sc_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    canvas.create_text(sc_width/2, 50, text="Fill the form!", font=("Roboto", 24, "bold"), fill="white")

    canvas.create_text(sc_width/2, 100, text="Subject", font=("Roboto", 24, "bold"), fill="white")
    subject_entry = create_rounded_entry(canvas, sc_width/2, 150, 300, 50, entry_style, radius=20, bg_color="#FFFFFF", outline_color="#FFFFFF")
    #tk.Label(root, text="Subject:", **label_style).pack(pady=5)
    #subject_entry = tk.Entry(root, **entry_style)
    #subject_entry.pack(pady=10, padx=10)
    #canvas.create_window(sc_width/2, 150, window=subject_entry, width=250)

    canvas.create_text(sc_width/2, 200, text="Argument", font=("Roboto", 24, "bold"), fill="white")
    argument_entry = create_rounded_entry(canvas, sc_width/2, 250, 300, 50, entry_style, radius=20, bg_color="#FFFFFF", outline_color="#FFFFFF")
    #tk.Label(root, text="Argument:", **label_style).pack(pady=5)
    #argument_entry = tk.Entry(root, **entry_style)
    #argument_entry.pack(pady=10, padx=10)
    #canvas.create_window(sc_width/2, 250, window=argument_entry, width=250)

    canvas.create_text(sc_width/2, 300, text="Number of Questions:", font=("Roboto", 24, "bold"), fill="white")
    num_questions_entry = create_rounded_entry(canvas, sc_width/2, 350, 300, 50, entry_style, radius=20, bg_color="#FFFFFF", outline_color="#FFFFFF")
    #tk.Label(root, text="Number of Questions:", **label_style).pack(pady=5)
    #num_questions_entry = tk.Entry(root, **entry_style)
    #num_questions_entry.pack(pady=10, padx=10)
    #canvas.create_window(sc_width/2, 350, window=num_questions_entry, width=250)

    canvas.create_text(sc_width/2, 400, text="School Level", font=("Roboto", 24, "bold"), fill="white")
    #tk.Label(root, text="School Level:", **label_style).pack(pady=5)
    school_level_var = ttk.Combobox(root, values=["Middle School", "High School", "University"])
    school_level_var.pack(pady=5)
    canvas.create_window(sc_width/2, 450, window=school_level_var, width=250)

    canvas.create_text(sc_width/2, 500, text="Question Type:", font=("Roboto", 24, "bold"), fill="white")
    #tk.Label(root, text="Question Type:", **label_style).pack(pady=5)
    question_type_var = ttk.Combobox(root, values=["Multiple Choice", "Open-ended", "True/False"])
    question_type_var.pack(pady=5)
    canvas.create_window(sc_width/2, 550, window=question_type_var, width=250)

    canvas.create_text(sc_width/2, 600, text="Difficulty:", font=("Roboto", 24, "bold"), fill="white")
    #tk.Label(root, text="Difficulty:", **label_style).pack(pady=5)
    difficulty_var = ttk.Combobox(root, values=["Easy", "Medium", "Hard"])
    difficulty_var.pack(pady=5)
    canvas.create_window(sc_width/2, 650, window=difficulty_var, width=250)

    def submit_form():
        global subject, argument, num_questions, school_level, question_type, difficulty

        subject = subject_entry.get()
        argument = argument_entry.get()
        num_questions = int(num_questions_entry.get())
        school_level = school_level_var.get()
        question_type = question_type_var.get()
        difficulty = difficulty_var.get()

        print(f"Subject: {subject}")
        print(f"Argument: {argument}")
        print(f"Number of Questions: {num_questions}")
        print(f"School Level: {school_level}")
        print(f"Question Type: {question_type}")
        print(f"Difficulty: {difficulty}")

        send_arguments()


    submit_button = tk.Button(root, text="Submit", command=submit_form, **button_style)
    submit_button.pack(pady=20)
    canvas.create_window(sc_width/2, 700, window=submit_button)


def send_arguments():
    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=sc_width, height=sc_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    canvas.create_text(sc_width/2, sc_height/2 - 100, text="Elaborating your test...", font=("Roboto", 24, "bold"), fill="white")

    global gif_id
    gif_id = canvas.create_image(sc_width / 2, sc_height / 2 + 50, image=gif_frames[0], anchor="center")

    animate_gif(canvas, gif_frames, sc_width / 2, sc_height / 2 + 50, 100)

    root.after(1000, lambda: api.send_info_gpt(subject, argument, num_questions, school_level, question_type, difficulty, canvas, be_ready))

def be_ready(canvas, questions):
    ready_button = tk.Button(root, text="Start!", command=lambda: do_test(canvas, questions), **button_style)
    canvas.create_window(sc_width/2, sc_height - 150, window=ready_button)

def do_test(canvas, questions):
    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=sc_width, height=sc_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    canvas.create_text(sc_width/2, 50, text="Test yourself!", font=("Roboto", 28, "bold"), fill="white")
    canvas.create_text(sc_width/2, sc_height/2 - 100, text=questions[0], font=("Roboto", 16), fill="white")
    q_entry = create_rounded_entry(canvas, sc_width/2, sc_height/2 + 150, 700, 300, entry_style, radius=20, bg_color="#FFFFFF", outline_color="#FFFFFF")

def show_main_page():
    for widget in root.winfo_children():
        widget.destroy()
    
    #tk.Label(root, text="Welcome to SteadyScore " + username + "!", **label_style).pack(pady=20)
    canvas = tk.Canvas(root, width=sc_width, height=sc_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    canvas.create_text(sc_width/2, 50, text="Welcome to SteadyScore " + username + "!", font=("Roboto", 24, "bold"), fill="white")
    exercise_button = tk.Button(root, text="Let's Exercise!", command=open_exercise_options, **button_style)
    exercise_button.pack(pady=20)
    exit_button = tk.Button(root, text="Exit", command=root.quit, **button_style)
    canvas.create_window(sc_width/2, 100, window=exercise_button)
    canvas.create_window(sc_width/2, 200, window=exit_button)

show_login()
root.mainloop()