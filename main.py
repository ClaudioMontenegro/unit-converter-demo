from customtkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("My Unit Converter")


app = App()
set_appearance_mode("dark")


def label_from_to(value):
    lblfrom.configure(text=f"{option_box1.get()}/{option_box3.get()}")
    lblto.configure(text=f"{option_box2.get()}/{option_box4.get()}")


def calculate_unit():
    valor = float(entry1.get())
    de = option_box1.get()
    para = option_box2.get()

    fatores = {
        'pg_to_pg': 1,
        'pg_to_ng': 1e3,
        'pg_to_μg': 1e6,
        'pg_to_mg': 1e9,
        'pg_to_g': 1e12,
        'ng_to_pg': 1e-3,
        'ng_to_ng': 1,
        'ng_to_μg': 1e3,
        'ng_to_mg': 1e6,
        'ng_to_g': 1e9,
        'μg_to_pg': 1e-6,
        'μg_to_ng': 1e-3,
        'μg_to_μg': 1,
        'μg_to_mg': 1e3,
        'μg_to_g': 1e6,
        'mg_to_pg': 1e-9,
        'mg_to_ng': 1e-6,
        'mg_to_μg': 1e-3,
        'mg_to_mg': 1,
        'mg_to_g': 1e3,
        'g_to_pg': 1e-12,
        'g_to_ng': 1e-9,
        'g_to_μg': 1e-6,
        'g_to_mg': 1e-3,
        'g_to_g': 1
    }

    key_ = f"{de}_to_{para}"
    vol1 = option_box3.get()
    vol2 = option_box4.get()
    result = valor / fatores[key_]

    if vol1 == vol2:
        result = result * 1
    elif vol1 == 'µL' and vol2 == 'mL':
        result = result * 10e4
    elif vol1 == 'µL' and vol2 == 'L':
        result = result * 10e7
    elif vol1 == 'mL' and vol2 == 'µL':
        result = result/10e2
    elif vol1 == 'mL' and vol2 == 'L':
        result = result * 10e4
    elif vol1 == 'L' and vol2 == 'µL':
        result = result/10e5
    elif vol1 == 'L' and vol2 == 'mL':
        result = result/10e2

    entry2.delete(0, 'end')
    entry2.insert(END, f"{result}")


# Buttons
b_calculate = CTkButton(master=app,
                        text="Calculate",
                        corner_radius=20,
                        height=10,
                        width=20,
                        font=("Arial Baltic", 13, "bold"),
                        command=calculate_unit)
b_calculate.place(relx=0.5, rely=0.5, anchor="center")

# Label
lbl1 = CTkLabel(master=app, text="Is equal to", font=("Arial Baltic", 14, "bold"))
lbl1.place(relx=0.2, rely=0.35, anchor="center")

lblfrom = CTkLabel(master=app, text="From", font=("Arial Baltic", 14, "bold"))
lblfrom.place(relx=0.71, rely=0.20, anchor="center")

lblto = CTkLabel(master=app, text="To", font=("Arial Baltic", 14, "bold"))
lblto.place(relx=0.7, rely=0.35, anchor="center")

# Entries
entry1 = CTkEntry(master=app,
                  width=60,
                  height=10,
                  justify='center')
entry1.insert(END, "0")
entry1.place(relx=0.5, rely=0.20, anchor="center")
entry2 = CTkEntry(master=app,
                  width=60,
                  height=10,
                  justify='center')
entry2.place(relx=0.5, rely=0.35, anchor="center")


# Boxes
values_list = ['pg', 'ng', 'μg', 'mg', 'g']
option_box1 = CTkOptionMenu(master=app, values=values_list,
                            variable=StringVar(value="From"),
                            width=20,
                            command=label_from_to)
option_box1.place(relx=0.3, rely=0.7, anchor="center")
option_box2 = CTkOptionMenu(master=app, values=values_list,
                            variable=StringVar(value="To"),
                            width=20,
                            command=label_from_to)
option_box2.place(relx=0.7, rely=0.7, anchor="center")
option_box3 = CTkOptionMenu(master=app,
                            values=["µL", "mL", "L"],
                            variable=StringVar(value="Vol.I"),
                            width=20,
                            command=label_from_to)
option_box3.place(relx=0.3, rely=0.9, anchor="center")
option_box4 = CTkOptionMenu(master=app,
                            values=["µL", "mL", "L"],
                            variable=StringVar(value="Vol.II"),
                            width=20,
                            command=label_from_to)
option_box4.place(relx=0.7, rely=0.9, anchor="center")


app.mainloop()
