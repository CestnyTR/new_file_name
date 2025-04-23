import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import platform

def open_folder(path):
    try:
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.call(["open", path])
        else:  # Linux
            subprocess.call(["xdg-open", path])
    except Exception as e:
        print(f"Klasör açılamadı: {path}\nHata: {e}")

def rename_files_in_folder():
    folder_path = filedialog.askdirectory(title="Bir klasör seçin")
    if not folder_path:
        messagebox.showwarning("Uyarı", "Hiçbir klasör seçilmedi.")
        return

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            rnd_number = str(random.randint(100000, 999999))
            name, extension = os.path.splitext(file)
            new_file_name = rnd_number + " " + name + extension
            new_file_path = os.path.join(dirpath, new_file_name)
            try:
                os.rename(file_path, new_file_path)
            except Exception as e:
                messagebox.showerror("Hata", f"Bir dosya yeniden adlandırılamadı: {file}\n{str(e)}")
                return

    messagebox.showinfo("Başarılı", "Tüm dosyalar başarıyla yeniden adlandırıldı.")
    open_folder(folder_path)  # İşlemden sonra klasörü aç

# Ana pencere
root = tk.Tk()
root.title("Dosya Yeniden Adlandırıcı")
root.geometry("400x200")

# Arayüz öğeleri
label = tk.Label(root, text="Bir klasör seçin ve içindeki dosyaları yeniden adlandırın.", wraplength=350)
label.pack(pady=20)

btn_select_folder = tk.Button(root, text="Klasör Seç ve Dosyaları Yeniden Adlandır", command=rename_files_in_folder)
btn_select_folder.pack(pady=10)

btn_quit = tk.Button(root, text="Çıkış", command=root.quit)
btn_quit.pack(pady=10)

# Döngüyü başlat
root.mainloop()
