# 🔀 Dosya Yeniden Adlandırıcı (new_file_name)

> Prefixes every file in a folder with a random 6-digit number — handy for shuffling file order.

Seçtiğin klasördeki tüm dosyaların adının başına **rastgele 6 haneli bir sayı** ekleyen küçük bir masaüstü aracı.
Dosyalar ada göre sıralanan cihazlarda (araç USB'si, medya oynatıcı, slayt gösterisi) **sırayı karıştırmak** için kullanışlı.

```
şarkı.mp3     →  482913 şarkı.mp3
foto_01.jpg   →  105774 foto_01.jpg
```

## Kullanım

### Windows (kurulum gerekmez)
1. [Releases](https://github.com/CestnyTR/new_file_name/releases/latest) sayfasından `new_name.exe` dosyasını indir ve çalıştır.
2. **Klasör Seç ve Dosyaları Yeniden Adlandır** butonuna bas, klasörü seç.
3. İşlem bitince klasör otomatik açılır.

### Python ile (Windows / macOS / Linux)
```bash
python new_name.py
```
Python 3 yeterli, ek paket gerekmez (Tkinter Python ile gelir).
Linux'ta Tkinter yoksa: `sudo apt install python3-tk`

## ⚠️ Dikkat
- **Alt klasörlerdeki dosyalar da** yeniden adlandırılır.
- İşlemin **geri alma özelliği yok**. Önemli dosyalarda önce yedek al.
- Aynı klasörde iki kez çalıştırırsan dosyaların başına ikinci bir sayı eklenir.

## Kendin derlemek istersen
```bash
pip install pyinstaller
pyinstaller --onefile --windowed new_name.py
```
Çıktı `dist/new_name.exe` olarak oluşur.

## Teknolojiler
Python 3 · Tkinter
