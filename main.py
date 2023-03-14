from functools import reduce

def sonlar(sonlar):
    sonlar = [1,2,3,4,5,6]

    # Roʻyxatdagi har bir raqam ustida amallar oshirish uchun map() funksiyasidan foydalandim
    b = (input("Sonlarni nechiga kopaytiraymi,bolaymi, qoshaymi, ayiraymi qaysi amal kerak bo'lsa uning belgisini yozing: "))
    if b == "*":
        kopaytuvchi = int(input("Nechaga ko'paytirishimni hohlaysiz: "))
        amallar = list(map(lambda x: x * kopaytuvchi, sonlar))

    elif b == "/":
        boluvchi = int(input("Nechaga bo'lishimni hohlaysiz: "))
        amallar = list(map(lambda x: x // boluvchi, sonlar))

    elif b == "+":
        qoshuluvchi = int(input("Nechaga qo'shishimni hohlaysiz: "))
        amallar = list(map(lambda x: x + qoshuluvchi, sonlar))

    elif b == "-":
        ayiruvchi = int(input("Nechaga ayirishimni hohlaysiz: "))
        amallar = list(map(lambda x: x - ayiruvchi, sonlar))


    
    # Roʻyxatdan juft va toq  sonlarini topish uchun filter() funksiyasidan foydalandim

    juft = list(filter(lambda x: x % 2 == 0, sonlar))


    toq = list(filter(lambda x: x % 3 == 0, sonlar))
    # Roʻyxatdagi barcha raqamlar yigʻindisini topish uchun reduce() funksiyasidan foydalandim
    barchasi_yigindi = reduce(lambda x, y: x + y, sonlar)

    print(f"{b} amalidagi natija: ",amallar)
    print("Juft sonlar: ", juft)
    print("Toq sonlar: ", toq)
    print("Barcha raqamlar yig'indisi:", barchasi_yigindi)
sonlar([1,2,3,4,5,6])