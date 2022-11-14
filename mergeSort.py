import random


def mergeSort(arr):
    if len(arr) > 1:

        # dizinin ortasını bulalım
        mid = len(arr) // 2

        # Elemanların sol alt gruba ayrılması
        L = arr[:mid]

        # Elemanların sağ alt gruba ayrılması
        R = arr[mid:]

        # Sol yarıyı sıralayalım
        mergeSort(L)

        # Sağ yarıyı sıralayalım
        mergeSort(R)

        i = j = k = 0

        # Sol ve sağ alt grupları birleştirelim
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Boşta eleman kalmadığını kontrol et
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Listeyi yazdıralım


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def randArr():
    size = 10
    arr = [random.randint(0, 100) for i in range(size)]

    return arr


if __name__ == '__main__':
    arr = randArr()
    print("Random dizi", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Kucukten buyuge siralama: ", end="\n")
    printList(arr)
    print("Buyukten kucuge siralama: ", end="\n")
    printList(arr[::-1])