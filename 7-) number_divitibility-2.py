#Belirtilen başlangıç, bitiş ve adım değerine göre, aralıktaki sayıların toplamı hesaplayan program
#belirlenen değişkenlere başlangıç değeri atamak zorunludur aksi takdirde hata alırız burada result'ı i kadar arttırılır
#fakat result'ın başlangıç değeri olmadığı için neyi i kadar arttıracağını bilemez program yada result'ın int mi str mi olduğunu bilemez
#aynı zamanda işme yapılan değişken tanımlı olmalıdır biz burada result değişkenini başlangıçta tanımlayın başlangıç değeri atamazsak
#for döngüsü içerisinde tanımlanmamış bir değişken olduğundan programımız hata döndürecektir
result = 0
for i in range(0,1000,10):
    result += i
print(result)