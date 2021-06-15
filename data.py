import tkinter as tk

kolom = 'Nama', 'NIM', 'Prodi', 'Nilai'

def ambil_data(inputData):
    for input in inputData:
        data = input[0]
        text  = input[1].get()
        label3 = tk.Label(root, text= data)
        label3.pack()
        
        label2 = tk.Label(root, text=text)        
        label2.pack()

def input_data(root, kolom):
    inputData = []
    for data in kolom:
        baris = tk.Frame(root)

        lblText = tk.Label(baris, width=15, text=data, anchor='w')

        input = tk.Entry(baris)
        baris.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        lblText.pack(side=tk.LEFT)
        input.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        inputData.append((data, input))
    return inputData

if __name__ == '__main__':
    root = tk.Tk()
    ents = input_data(root, kolom)
    root.bind('<Return>', (lambda event, e=ents: ambil_data(e)))   
    b1 = tk.Button(root, text='Tambah Data',
                  command=(lambda e=ents: ambil_data(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
