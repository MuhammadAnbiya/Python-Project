#simple calculator
print('pilih operator apa yang ingin dipakai : ' +
      "\n1. Penambahan" +
      "\n2. Pengurangan" + 
      "\n3. Perkalian" +
      "\n4. Pembagian"
      )
operator = str(input("masukan pilihan operator : "))
angka1 = int(input("masukan angka pertama : "))
angka2 = int(input("masukan angka kedua : "))

if operator == 'penambahan':
    hasil = angka1 + angka2
elif operator == 'pengurangan':
    hasil = angka1 - angka2
elif operator == 'perkalian':
    hasil = angka1 * angka2
elif operator =='pembagian':
    hasil = angka1 / angka2
    
print(f'{operator} dari {angka1} dan {angka2} adalah {hasil}')    