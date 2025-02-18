def tamsayı_test(değer):
    try:
        return değer == int(değer)
    except ValueError:
        return False

print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")
print("5.Çıkış")
sayı1 = float(input("birinci sayıyı giriniz"))
sayı2 = float(input("ikinci sayıyı giriniz"))
işlem =input("işlem seçiniz")
if işlem == "1":
  if tamsayı_test(sayı1 + sayı2):
    print(int(sayı1 + sayı2))
  else:
    print(float(sayı1 + sayı2))
elif işlem == "2":
  if tamsayı_test(sayı1 - sayı2):
    print(int(sayı1 - sayı2))
  else:
    print(float(sayı1 - sayı2)) 
elif işlem == "3":
  if tamsayı_test(sayı1 * sayı2):
    print(int(sayı1 * sayı2))
  else:
    print(float(sayı1 * sayı2))   
elif işlem == "4":
  if tamsayı_test(sayı1 / sayı2):
    print(int(sayı1 / sayı2))
  else:
    print(float(sayı1 / sayı2))
else:
   print("çıkış yapılıyor")
   
