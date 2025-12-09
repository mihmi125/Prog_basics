import tkinter as tk

def vicsekFractals():
    root = tk.Tk()
    root.title("Vicseki Fraktaal")

    laius = 400
    kõrgus = 400
    canvas = tk.Canvas(root, width=laius, height=kõrgus, bg="white")
    canvas.pack()

    current_depth = 0

    def draw_vicsek_fast(x, y, size, depth, update_every=3000, counter=[0]):
        if depth == 0:
            canvas.create_rectangle(x, y, x + size, y + size, fill="black", outline="black")
            counter[0] += 1

            if counter[0] % update_every == 0:
                canvas.update()

        else:
            new_size = size / 3
            draw_vicsek_fast(x, y, new_size, depth - 1)
            draw_vicsek_fast(x + 2 * new_size, y, new_size, depth - 1)
            draw_vicsek_fast(x + new_size, y + new_size, new_size, depth - 1)
            draw_vicsek_fast(x, y + 2 * new_size, new_size, depth - 1)
            draw_vicsek_fast(x + 2 * new_size, y + 2 * new_size, new_size, depth - 1)

    def keys(event):
        nonlocal current_depth
        if event.char.isdigit():
            depth = int(event.char)
            if 0 <= depth <= 9:
                current_depth = depth
                canvas.delete("all")
                draw_vicsek_fast(0, 0, laius, current_depth)
                canvas.update()
        print(f"Sügavus: {current_depth}")

    root.bind("<Key>", keys)
    draw_vicsek_fast(0, 0, laius, current_depth)
    root.mainloop()

vicsekFractals()
