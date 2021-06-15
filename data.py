import tkinter as tk

def main(root):
    btnLihat = tk.Button(root, text="Lihat Data", height=5, width=35)
    btnLihat.grid(row=2, column=2)

    btnTambah = tk.Button(root, text="Tambah Data", height=5, width=40)
    btnTambah.grid(row=2, column=3)

root = tk.Tk()
root.title(('Data Mahasiswa'))
root.geometry('500x350')

main(root)
root.mainloop()