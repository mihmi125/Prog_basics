import tkinter as tk

def Paide_lipp():
    root = tk.Tk()
    root.title("Paide lipp")
    W, H = 600, 375
    
    c = tk.Canvas(root, width=W, height=H, bg='white')
    c.pack()
    ROHELINE = "green"
    VALGE = "white"

    # Koordinaatide arvutamine
    x1_3 = W // 3      # 1/3 laiusest
    h_pool = H // 2    # 1/2 kõrgusest
    r_h = h_pool // 3  # Riba kõrguse pool
    y_start = h_pool - r_h / 2
    y_lõpp = h_pool + r_h / 2

    c.create_rectangle(0, 0, x1_3, H, fill=ROHELINE, outline="")        # Roheline vasak külg
    
    c.create_rectangle(0, y_start, x1_3, y_lõpp, fill=VALGE, outline="")     # Valge riba vasakul
    c.create_rectangle(x1_3, y_start, W, y_lõpp, fill=ROHELINE, outline="")  # Roheline riba paremal

    root.mainloop()

Paide_lipp()