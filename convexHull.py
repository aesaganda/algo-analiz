# koordinatların x ve y olarak tanımlanması için oluşturulan sınıf
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def Left_index(points):
    '''
	En soldaki noktanın bulunması için
    x koordinatlarına göre sıralama yapılır
	'''
    minn = 0
    for i in range(1, len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn


# Bu fonksiyon 3 nokta arasındaki yönü bulur
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - \
     (q.x - p.x) * (r.y - q.y)

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def convexHull(points, n):

    # Üç noktadan az varsa programdan çık
    if n < 3:
        return

    # Soldaki noktaların bulunması
    l = Left_index(points)

    hull = []
    p = l
    q = 0
    while (True):

        # Bulunan noktayı sonuca ekle
        hull.append(p)

        q = (p + 1) % n

        for i in range(n):
            if (orientation(points[p], points[i], points[q]) == 2):
                q = i

        p = q

        # İlk noktaya gelince döngüden çık
        if (p == l):
            break

    # Sonucu yazdır
    for each in hull:
        print('(', points[each].x, ',', points[each].y, ')')


points = []
points.append(Point(1, 5))
points.append(Point(2, 8))
points.append(Point(2, 9))
points.append(Point(3, 10))
points.append(Point(3, 1))
points.append(Point(4, 6))
points.append(Point(4, 8))
points.append(Point(9, 5))
points.append(Point(10, 4))

convexHull(points, len(points))