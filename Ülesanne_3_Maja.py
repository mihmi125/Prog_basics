import tkinter as tk

def joonista_maja():
    root = tk.Tk()
    root.title("Maja")

    laius = 600
    kõrgus = 400
    canvas = tk.Canvas(root, width=laius, height=kõrgus, bg="white")
    canvas.pack()
    
    # --- Maja joonistamine ---
    
    # Värvid:
    kere_varv = "brown"
    katus_varv = "red"
    ukse_varv = "blue"
    akna_värv = "lightblue"
    
    # 1. Maja kere (Ristkülik)
    kere_x1, kere_y1 = 150, 250
    kere_x2, kere_y2 = 450, 350
    canvas.create_rectangle(kere_x1, kere_y1, kere_x2, kere_y2, fill=kere_varv)
    
    # 2. Katus (Kolmnurk)
    katuse_tipp_x, katuse_tipp_y = 300, 150
    katuse_vasak_x, katuse_vasak_y = kere_x1 - 20, kere_y1
    katuse_parem_x, katuse_parem_y = kere_x2 + 20, kere_y1
    canvas.create_polygon(katuse_tipp_x, katuse_tipp_y, 
                          katuse_vasak_x, katuse_vasak_y, 
                          katuse_parem_x, katuse_parem_y, 
                          fill=katus_varv)
    
    # 3. Uks (Ristkülik)
    ukse_laius = 40
    ukse_kõrgus = 70
    ukse_x1 = kere_x1 + (kere_x2 - kere_x1) // 2 - ukse_laius // 2
    ukse_y1 = kere_y2 - ukse_kõrgus
    ukse_x2 = ukse_x1 + ukse_laius
    ukse_y2 = kere_y2
    canvas.create_rectangle(ukse_x1, ukse_y1, ukse_x2, ukse_y2, fill=ukse_varv)

    # 4. Aken (Ristkülik)
    akna_suurus = 40
    akna_x1 = kere_x1 + 50
    akna_y1 = kere_y1 + 40
    akna_x2 = akna_x1 + akna_suurus
    akna_y2 = akna_y1 + akna_suurus
    canvas.create_rectangle(akna_x1, akna_y1, akna_x2, akna_y2, fill=akna_värv)
    
    root.mainloop()

joonista_maja()