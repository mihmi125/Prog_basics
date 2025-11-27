"""Koostada programm, mis kuvab valge taustaga graafikaakna pealkirjaga “Liiklusmärk” ja joonistab (tkinteriga) 
sinna vabalt valitud liiklusmärgi (liiklusseaduses määratud liiklusmärke saab vaadata lisadest).

Mõned innustavad variandid on 112, 175, 178, 438, 712, aga ka siin võiks pigem valida midagi sellist, kus tsüklid oleksid asjakohased.

Soovi korral võib julgesti jagada pilti oma programmi tulemusest kaaskursuslastega foorumis Lippude, liiklusmärkide, majade ja 
malelaudade teosed. NB! Juhend ekraanipildi saamiseks.
"""
import tkinter as tk
def Stop_märk():
    root = tk.Tk()
    root.title("Stop märk")
    W, H = 400, 400

    c = tk.Canvas(root, width=W, height=H, bg='white')
    c.pack()
    PUNANE = "red"
    VALGE = "white"
    MUST = "black"

    c.create_polygon(   # Outer octagon
    152, 98,    # Top-Left
    248, 98,    # Top-Right
    302, 152,   # Middle-Top-Right
    302, 248,   # Middle-Bottom-Right
    248, 302,   # Bottom-Right
    152, 302,   # Bottom-Left
    98, 248,    # Middle-Bottom-Left
    98, 152,    # Middle-Top-Left

    fill=VALGE,
    outline=MUST,
    width=1
    )

    c.create_polygon(  # Inner octagon
    162, 108,   # Top-Left
    238, 108,   # Top-Right
    292, 162,   # Middle-Top-Right
    292, 238,   # Middle-Bottom-Right
    238, 292,   # Bottom-Right
    162, 292,   # Bottom-Left
    108, 238,   # Middle-Bottom-Left
    108, 162,   # Middle-Top-Left

    fill=PUNANE,
    outline=MUST,
    width=1
    )

    c.create_text(200,200, text="STOP", fill=VALGE, font=("Arial", 50, "bold"))
    root.mainloop()

Stop_märk()