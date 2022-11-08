import itertools


def sum_solution(cozumler):
    deger, kg = 0, 0
    for block in cozumler:
        deger += block[0]
        kg += block[1]

    return deger, kg


def canta(kapasite, blocks):

    cozumler = []
    for count in range(len(blocks) + 1):
        for cozum in itertools.combinations(blocks, count):
            deger, kg = sum_solution(cozum)
            if kg <= kapasite:
                cozumler.append((deger, kg, cozum))

    cozumler.sort(reverse=True, key=lambda x: x[0])
    return cozumler


cozumler = canta(16, [(20, 2), (30, 5), (60, 10), (10, 5), (40, 3), (10, 1),
                      (30, 3), (40, 4), (80, 5), (70, 7)])
cozum = cozumler[0]
print(f"Max Deger:  {cozum[0]}  Agirlik: {cozum[1]} Icerik:  {cozum[2]}")

print(f"Deger  Agirlik Icerik")
for cozum in cozumler:
    print(f"{cozum[0]:5d} {cozum[1]:6d} {cozum[2]}")
