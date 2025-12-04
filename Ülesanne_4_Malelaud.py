import tkinter as tk

def joonista_maja():
    root = tk.Tk()
    root.title("Malelaud")

    counter = 0
    laius = 400
    kõrgus = 400
    canvas = tk.Canvas(root, width=laius, height=kõrgus, bg="white")
    canvas.pack()


    while counter < 8:
        for rida in range(8):
            for veerg in range(8):
                x1 = veerg * 50
                y1 = rida * 50
                x2 = x1 + 50
                y2 = y1 + 50
                if (rida + veerg) % 2 == 0:
                    värv = "white"
                else:
                    värv = "black"
                canvas.create_rectangle(x1, y1, x2, y2, fill=värv)
        counter += 1
    
    root.mainloop()

joonista_maja()