# Diketahui Harga laptop Zaid Abdullah adalah 39.000.000, dengan masa manfaat 7 tahun dan nilai sisa setelah 7 tahun di perkirakan sebesar 4.000.000. Berapakah Nilai Aset Laptop Bapak Zaid Abdullah setelah 3 tahun?


# SusutTahunan = (39.000.000-4.000.000)/7 = 5.000.000
# Masa Pakai 3 tahun, berarti harga laptop sudah menyusut 5.000.000*3 = 15.000.000
# Nilai Aset Tersisa adalah 39.000.000 - 15.000.000 = 24.000.000


# keterangan : Harga beli, Masa manfaat dan perkiraan nilai sisa setelah masa manfaat habis tiap barang berbeda-beda. Buatlah kalkulator untuk mengakomodasi kasus diatas


# Buatlah Looping untuk mencetak nama anda sendiri seperti berikut ini : (Minimal 7 karakter, klo tidak ada boleh ditambah yang lain)

# N * * * * * *
# N U * * * * *
# N U G * * * *
# N U G R * * *
# N U G R A * *
# N U G R A H *
# N U G R A H A

# Nilai akan lebih sempurna jika nama yang di input bisa berubah-rubah


harga_laptop = int(input("Berapakah harga laptop anda : "))
tahun = int(input("Berapa lama anda menggunakan laptop terserbut : "))
masa_manfaat = int(input("Berapa Masa Manfaat setelah beberapa tahun anda gunakan : "))
lama_tahun = int(input("Tahun keberapa anda ingin mengetahui masa manfaat laptop anda : "))

susut_tahunan = (harga_laptop - masa_manfaat)/tahun
prediksi_masa_manfaaat = (susut_tahunan * lama_tahun)
aset_sisa = (harga_laptop - prediksi_masa_manfaaat)

print(f"Susut tahunan dari laptop anda adalah : {susut_tahunan}" + "\n" +
      f"Setelah masa pakai {lama_tahun} tahun, berarti harga laptop sudah menyusut {prediksi_masa_manfaaat}"+ "\n" +
      f"Nilai aset tersisa adalah {aset_sisa}")


