global i
i = 1
def knapSack(kapasite, agirlik, deger, n):
    # baslangic sarti
    global i
    list = []
    if n == 0 or kapasite == 0:
        return 0
    # Eger agirlik kapasiteden buyukse alma
    if (agirlik[n - 1] > kapasite):
        i += 1

        return knapSack(kapasite, agirlik, deger, n - 1)
    # Max degeri dondur
    else:
        list.append(i)
        print(list)
        return max(
            deger[n - 1] +
            knapSack(kapasite - agirlik[n - 1], agirlik, deger, n - 1),
            knapSack(kapasite, agirlik, deger, n - 1))


# Main
deger = [20, 30, 60, 10, 40, 10, 30, 40, 80, 70]
agirlik = [2, 5, 10, 5, 3, 1, 3, 4, 5, 7]
kapasite = 16
n = len(deger)
print(knapSack(kapasite, agirlik, deger, n))