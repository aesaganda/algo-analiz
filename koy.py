def optimalMesafe(koy: list):
    postane = int

    villageNumber = len(koy)

    for i in range(villageNumber):
        postane = i
        uzaklik = mesafeBul(postane, villageNumber)
        if max(uzaklik) == villageNumber // 2:
            break

    return postane


def mesafeBul(postane: int, villageNumber: int):
    uzaklik = list()

    for i in range(villageNumber):
        uzaklik.append(abs(postane - i))

    return uzaklik


def main():
    koy = ['1', '2', '3', '4', '5']
    postane = optimalMesafe(koy)
    print(koy[postane])


if __name__ == '__main__':
    main()