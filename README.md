shopee parser purchasing history

pernah mikir gak sih gimana ya caranya buat ambil history pembelian shopee tanpa harus capek capek scroll sampe mampus?
well, ini dia solusinya! shopee parser puchasing history mengambil data history pembelian kita dan langsung meng-export nya ke file csv.

caranya (windows) : 
1. ngerti python sedikit aja (kalo udah pernah install selenium di global environment berarti gak usah install lagi ya, bisa lgsg ke step 6)
2. download & install python https://www.python.org/downloads/
3. buat folder bebas dimana aja, trus kita masuk ke dalam folder tersebut
4. pencet shift-klik kanan trus klik open powershell window here
5. ketik py -m pip install selenium
6. download main.py trus masukin ke folder yang tadi dibuat

okay sampe disini berarti kita udah install module selenium trus main.py udah ada di folder baru.
sekarang kita konfigurasi browser nya.

biar gak ribet pakai mozilla firefox ya, karna kita udah setting apps nya buat jalan di firefox.

1. download & install mozilla firefox kalo blm punya https://www.firefox.com/ 
2. login shopee 
3. buka tab baru dan ketik about:profiles 
4. sekarang buka main.py pakai notepad atau IDE terserah kalian ya
5. pada baris ke-13 ada variable 'profile_path' yang isi nya adalah root directory profiles kamu, kamu copy root directory nya dari tab about:profiles. contoh : r"\AppData\Roaming\Mozilla\Firefox\Profiles\xxxxx"

good! sekarang kita udah setting supaya apps nya buat buka browser dengan profile yang kita mau, yang shopee nya udah login.

sekarang kita tinggal setup geckodriver nya.

1. download geckodriver sesuai os https://github.com/mozilla/geckodriver/releases (untuk windows bisa download geckodriver-v.xxxx-win32.zip)
2. extract geckodriver nya di folder yang pertama kita buat
3. jadi sekarang udah 2 file di folder tadi, main.py dan geckodriver.exe
4. sekarang kembali ke main.py, pada baris ke-14 ada variable 'geckodriver_path' yang isi nya adalah path geckodriver, kalian bisa copy path nya di address bar. contoh : r"D:\shopee\geckodriver.exe"

congrats! sekarang kamu udah bisa jalanin deh!
how to run the apps :
1. tutup semua firefox
2. buka folder yang sudah dibuat tadi
3. shift+klik kanan trus klik open powershell window here
4. ketik py main.py
5. doneeee! nanti file csv nya ada di folder yang sama dengan main.py

Q&A

Q : Error NoSuchElement .ashFMQ?

A : kalo itu sih biasa nya antibot tracking nya shopee. kamu masuk ke shopee pake firefox trus nanti biasa nya kamu suruh bypass captcha nya (geser geser puzzle sih biasanya). trus jalanin lagi app nya.

Q : Pengen lebih banyak lagi datanya, kalo bisa sampe mentok!!!!

A : app nya itu di desain buat scroll sampe 400 container item aja kalo kalian mau sampe mentok berarti ganti aja variable itemTargetCount di line 34 dari 400 jadi 1000 atau lebih (gak tanggung kalo crash browser nya hehehe) dan juga semakin banyak datanya semakin lama juga app nya bekerja jadi resiko ditanggung pemenang ya

Q : Kok ada tanggal yang kosong?

A : berarti pembelian tersebut dibatalkan

Q : tapi ini produk yang dikembalikan juga masuk?

A : iya dia ngambil semua item yang ada dikolom "selesai" jadi meskipun itemnya dikembalikan, dia tetep ada disana. mungkin kedepannya bisa kita filter, tapi untuk sekarang manual dulu yaa hehe

mau tanya yang lain lain? bisa langsung DM twitter aja ya, aktif banget kok disana.
@danube_stream

future features [ kalo gak sibuk, banyak tugas kuliah >:( ] : 
- filter item yang sudah dikembalikan
- mungkin bisa filter per-bulan dan bukan per-scroll


thank you! and no AI were harmed during the process of making this program! (ada satu sih buat bikin headless mode tapi diem diem aja yaaa ssssttt)


