import re

def line():
    print("-" * 70)

# 1. Ekstraksi ID Transaksi
print("1. Ekstraksi ID Transaksi")
text = "Pembayaran untuk pesanan #INV-2026-08912 telah berhasil diverifikasi pada pukul 14.30 WIB."
pattern = r"INV-\d{4}-\d+"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 2. Ekstraksi Nominal Harga (Rupiah)
print("2. Ekstraksi Nominal Harga (Rupiah)")
text = "Total belanjaan Anda adalah Rp 450.000 dengan diskon promo sebesar Rp 50.000."
pattern = r"Rp\s?\d{1,3}(?:\.\d{3})*"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 3. Masking Nomor Kartu Kredit
print("3. Masking Nomor Kartu Kredit")
text = "Transaksi menggunakan kartu kredit 4532-1234-5678-9012 telah disetujui."
pattern = r"(\d{4})-(\d{4})-(\d{4})-(\d{4})"
masked = re.sub(pattern, r"XXXX-XXXX-XXXX-\4", text)
print("Pattern :", pattern)
print("Hasil   :", masked)
line()

# 4. Validasi Kode Promo/Voucher
print("4. Validasi Kode Promo/Voucher")
text = "Gunakan kode promo HEMAT50K atau DISKON100 untuk mendapatkan potongan harga."
pattern = r"\b[A-Z]{2,}\d+[A-Z]*\b"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 5. Identifikasi Metode Pembayaran (E-Wallet/Bank)
print("5. Identifikasi Metode Pembayaran (E-Wallet/Bank)")
text = "Metode pembayaran yang dipilih: Transfer Bank BCA (VA: 88012345678)."
pattern = r"(Transfer Bank \w+|OVO|GoPay|Dana|ShopeePay|LinkAja).*?(?:VA:\s*(\d+))?\)"
m = re.search(pattern, text)
print("Pattern :", pattern)
print("Hasil   : Metode =", m.group(1), "| VA =", m.group(2))
line()

# 6. Ekstraksi Kode SKU Produk
print("6. Ekstraksi Kode SKU Produk")
text = "Produk Sepatu Lari Kategori A [SKU: SHO-RUN-2026-BLK] tersisa 3 unit."
pattern = r"SKU:\s*([\w-]+)"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 7. Deteksi Persentase Diskon
print("7. Deteksi Persentase Diskon")
text = "Dapatkan diskon hingga 70% untuk produk kecantikan dan diskon ekstra 5% bagi member."
pattern = r"\d+%"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 8. Ekstraksi Dimensi Produk
print("8. Ekstraksi Dimensi Produk")
text = "Ukuran paket: 30x20x15 cm dengan berat total 1.5 kg."
pattern = r"\d+x\d+x\d+\s*cm"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 9. Deteksi Berat Produk
print("9. Deteksi Berat Produk")
text = "Berat bersih item ini adalah 500gr, sedangkan berat packing sekitar 0.75kg."
pattern = r"\d+(?:\.\d+)?\s?(?:gr|kg|g)\b"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 10. Parsing Varian Warna dan Ukuran
print("10. Parsing Varian Warna dan Ukuran")
text = "Kaos Polos Cotton 30s - Warna: Merah Cabai - Size: XL."
pattern = r"Warna:\s*([\w\s]+?)\s*-\s*Size:\s*(\w+)"
m = re.search(pattern, text)
print("Pattern :", pattern)
print("Hasil   : Warna =", m.group(1), "| Size =", m.group(2))
line()

# 11. Ekstraksi Nomor Resi Pengiriman
print("11. Ekstraksi Nomor Resi Pengiriman")
text = "Paket Anda telah dikirim via JNE dengan no resi JNE102938475661."
pattern = r"\b[A-Z]{2,5}\d{6,}\b"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 12. Deteksi Kode Pos Indonesia
print("12. Deteksi Kode Pos Indonesia")
text = "Alamat tujuan pengiriman: Jl. Mawar No. 12, Jakarta Selatan, 12410."
pattern = r"\b\d{5}\b"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 13. Sanitasi Nomor Telepon Kurir/Pelanggan
print("13. Sanitasi Nomor Telepon Kurir/Pelanggan")
text = "Hubungi kurir di 0812-3456-7890 atau +6281298765432 jika kendala."
pattern = r"(?:\+62|0)8\d{2,3}[-\s]?\d{3,4}[-\s]?\d{3,4}"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 14. Ekstraksi Nama Kurir/Ekspedisi
print("14. Ekstraksi Nama Kurir/Ekspedisi")
text = "Pengiriman menggunakan opsi SiCepat REG (Estimasi 2-3 hari)."
pattern = r"\b(JNE|SiCepat|J&T|AnterAja|Ninja Express|GoSend|GrabExpress|Pos Indonesia|Wahana|Lion Parcel)\b"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 15. Parsing Estimasi Waktu Pengiriman
print("15. Parsing Estimasi Waktu Pengiriman")
text = "Estimasi barang sampai ke lokasi tujuan adalah 2-4 hari kerja."
pattern = r"\d+-\d+\s*hari(?:\s*kerja)?"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 16. Validasi Email Pelanggan
print("16. Validasi Email Pelanggan")
text = "Konfirmasi pesanan telah dikirim ke email pembeli: user_123@gmail.com."
pattern = r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 17. Ekstraksi Username Sosial Media
print("17. Ekstraksi Username Sosial Media")
text = "Follow Instagram kami di @tokopediaseru dan TikTok @tokopedia_official."
pattern = r"@\w+"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 18. Filter Kata Kasar/Spam di Ulasan
print("18. Filter Kata Kasar/Spam di Ulasan")
text = "Barang jelek banget, penipu ini seller ajg penipuan."
kata_kasar = ["anjing", "ajg", "bangsat", "goblok", "tolol", "penipu", "penipuan", "kontol", "memek", "bego"]
pattern = r"\b(" + "|".join(kata_kasar) + r")\b"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text, flags=re.IGNORECASE))
line()

# 19. Deteksi URL/Link Luar yang Dilarang di Chat
print("19. Deteksi URL/Link Luar yang Dilarang di Chat")
text = "Silakan transaksi langsung di website kami www.tokoku-murah.com ya kak."
pattern = r"(https?://[^\s\]\)]+|www\.[^\s\]\)]+)"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 20. Ekstraksi Mention ID Pelanggan
print("20. Ekstraksi Mention ID Pelanggan")
text = "Customer Support membalas tiket pertanyaan dari customer ID: CUST-9921."
pattern = r"CUST-\d+"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 21. Ekstraksi Nilai Rating
print("21. Ekstraksi Nilai Rating")
text = "Produk ini mendapatkan ulasan 4.8 dari 5 bintang berdasarkan 250 pembeli."
pattern = r"(\d+(?:\.\d+)?)\s*dari\s*(\d+)\s*bintang"
m = re.search(pattern, text)
print("Pattern :", pattern)
print("Hasil   : Rating =", m.group(1), "/", m.group(2))
line()

# 22. Deteksi Hashtag Promosi
print("22. Deteksi Hashtag Promosi")
text = "Beli baju baru di promo #FlashSale99 dan #BajuMurah sekarang!"
pattern = r"#\w+"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 23. Menghapus Tag HTML dari Deskripsi Produk
print("23. Menghapus Tag HTML dari Deskripsi Produk")
text = "<p>Bahan <b>Katun Premium</b> adem dan nyaman.</p>"
pattern = r"<[^>]+>"
cleaned = re.sub(pattern, "", text)
print("Pattern :", pattern)
print("Hasil   :", cleaned)
line()

# 24. Ekstraksi Tanggal Ulasan
print("24. Ekstraksi Tanggal Ulasan")
text = "Ulasan ditulis oleh Ahmad pada tanggal 12/08/2026."
pattern = r"\d{2}/\d{2}/\d{4}"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 25. Deteksi Sentimen Kata Kunci Positif
print("25. Deteksi Sentimen Kata Kunci Positif")
text = "Pengiriman sangat cepat, kualitas ori dan seller ramah!"
kata_positif = ["cepat", "ori", "ramah", "bagus", "puas", "recommended", "mantap", "memuaskan"]
pattern = r"\b(" + "|".join(kata_positif) + r")\b"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text, flags=re.IGNORECASE))
line()

# 26. Ekstraksi Alamat IP Pengguna
print("26. Ekstraksi Alamat IP Pengguna")
text = "Aktivitas login mencurigakan terdeteksi dari IP 192.168.1.105 pada lokasi Jakarta."
pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 27. Parsing Log Waktu Server
print("27. Parsing Log Waktu Server")
text = "[2026-09-02 08:30:15] ERROR: Gagal memproses transaksi ID 992."
pattern = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 28. Ekstraksi HTTP Status Code
print("28. Ekstraksi HTTP Status Code")
text = "API Payment Gateway merespons dengan status POST /checkout HTTP/1.1 200 OK."
pattern = r"(GET|POST|PUT|DELETE)\s+(\S+)\s+HTTP/[\d.]+\s+(\d{3})"
m = re.search(pattern, text)
print("Pattern :", pattern)
print("Hasil   : Method =", m.group(1), "| Path =", m.group(2), "| Status =", m.group(3))
line()

# 29. Deteksi Percobaan SQL Injection di Kolom Pencarian
print("29. Deteksi Percobaan SQL Injection di Kolom Pencarian")
text = "User mencari keyword: baju pria' OR '1'='1"
pattern = r"(?i)'\s*(OR|AND)\s*'?\s*\d+\s*'?\s*=\s*'?\s*\d+\s*'?"
print("Pattern :", pattern)
print("Hasil   :", "Terdeteksi SQLi" if re.search(pattern, text) else "Aman")
line()

# 30. Parsing Slug URL Produk
print("30. Parsing Slug URL Produk")
text = "Halaman diakses: https://tokopedia.com/p/sepatu-sneakers-pria-white-edition"
pattern = r"/p/([\w-]+)"
m = re.search(pattern, text)
print("Pattern :", pattern)
print("Hasil   :", m.group(1))
line()

# 31. Deteksi Batas Waktu Bayar (Countdown/Timer)
print("31. Deteksi Batas Waktu Bayar (Countdown/Timer)")
text = "Selesaikan pembayaran Anda dalam 01:45:30 sebelum pesanan dibatalkan."
pattern = r"\b\d{2}:\d{2}:\d{2}\b"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 32. Parsing Jumlah Stok (Inventory Quantity)
print("32. Parsing Jumlah Stok (Inventory Quantity)")
text = "Stok Gudang A: 150 pcs | Stok Gudang B: 20 pcs."
pattern = r"Gudang\s+(\w+):\s*(\d+)\s*pcs"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 33. Ekstraksi Kode Rak/Lokasi Bin Gudang
print("33. Ekstraksi Kode Rak/Lokasi Bin Gudang")
text = "Ambil barang di Lokasi Rak: RAK-A3-BAY12."
pattern = r"RAK-[\w-]+"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 34. Deteksi Status Pesanan
print("34. Deteksi Status Pesanan")
text = "Pesanan #1092 berubah status dari [MENUNGGU_PAYMENT] menjadi [DISELESAIKAN]."
pattern = r"\[([A-Z_]+)\]"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 35. Parsing Berat Total & Biaya Ongkir
print("35. Parsing Berat Total & Biaya Ongkir")
text = "Berat Total: 3kg - Biaya Pengiriman: Rp 27.000."
pattern = r"Berat Total:\s*([\d.]+\s?kg).*?Biaya Pengiriman:\s*Rp\s*([\d.]+)"
m = re.search(pattern, text)
print("Pattern :", pattern)
print("Hasil   : Berat =", m.group(1), "| Ongkir = Rp", m.group(2))
line()

# 36. Membersihkan Multiple White Space pada Deskripsi
print("36. Membersihkan Multiple White Space pada Deskripsi")
text = "Baju    kaos   pria     lengan panjang."
pattern = r"\s{2,}"
cleaned = re.sub(pattern, " ", text)
print("Pattern :", pattern)
print("Hasil   :", cleaned)
line()

# 37. Ekstraksi Angka dari Format Campuran (Angka & Teks)
print("37. Ekstraksi Angka dari Format Campuran (Angka & Teks)")
text = "Paket berisi 12pcs piring, 5pcs gelas, dan 1set sendok."
pattern = r"(\d+)(pcs|set|pack|buah)"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 38. Deteksi Penggunaan EMOTICON/EMOJI Unicode
print("38. Deteksi Penggunaan EMOTICON/EMOJI Unicode")
text = "Barangnya bagus banget kak! \U0001F44D\U0001F525 Recommended seller! \u2764\uFE0F"
pattern = r"[\U0001F300-\U0001FAFF\u2600-\u27BF]"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 39. Parsing Nama dan Nilai Atribut Spesifikasi (JSON-like text)
print("39. Parsing Nama dan Nilai Atribut Spesifikasi (JSON-like text)")
text = "Spesifikasi: [RAM: 8GB], [Storage: 256GB], [Baterai: 5000mAh]"
pattern = r"\[(\w+):\s*([\w\d]+)\]"
print("Pattern :", pattern)
print("Hasil   :", re.findall(pattern, text))
line()

# 40. Normalisasi Kata Baku Singkatan Chat (Preprocessing AI)
print("40. Normalisasi Kata Baku Singkatan Chat (Preprocessing AI)")
text = "brg sdh smp dgn slmt, tq seller"
kamus = {
    "brg": "barang",
    "sdh": "sudah",
    "smp": "sampai",
    "dgn": "dengan",
    "slmt": "selamat",
    "tq": "terima kasih",
}
pattern = r"\b(" + "|".join(kamus.keys()) + r")\b"
normalized = re.sub(pattern, lambda m: kamus[m.group(0)], text)
print("Pattern :", pattern)
print("Hasil   :", normalized)
line()
