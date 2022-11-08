import java.util.Scanner;

public class compare {
    public static void binarySearch(int array[], int search) {

        int size = array.length;
        int low = 0;
        int high = size - 1;
        int count = 0;

        while (low <= high) {
            int mid = (low + high) / 2;
            // Değer ortanca mı diye kontrol eder
            if (array[mid] == search) {
                System.out.println("The element is found at " + mid);
                break;
                // Aranan değer ortanca değerden büyükse sol yarı görmezden gelinir.
            } else if (array[mid] < search) {
                low = mid + 1;
                // Aranan değer ortanca değerden küçükse sağ yarı görmezden gelinir.
            } else {
                high = mid - 1;
            }
            count++;
        }
        System.out.println("The number of comparisons: " + count);

        if (low > high) {
            System.out.println("The element is not found");
        }
    }

    public static void interpolationSearch(int array[], int search) {

        int size = array.length;
        int low = 0;
        int high = size - 1;
        int count = 0;

        while (low <= high) {
            int mid = low + (high - low) * (search - array[low]) / (array[high] - array[low]);
            // Elemanın bulunması durumu
            if (array[mid] == search) {
                System.out.println("The element is found at " + mid);
                break;
                // Aranan değer büyükse listenin sağ yarısında kalır
            } else if (array[mid] < search) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
            count++;
        }
        System.out.println("The number of comparisons: " + count);

        if (low > high) {
            System.out.println("The element is not found");
        }
    }

    public static void linearSearch(int array[], int search) {
        int size = array.length;
        int i;

        // Listenin başından başlanarak değer aranır
        for (i = 0; i < size; i++) {
            if (array[i] == search) {
                System.out.println("The element is found at " + i);
                break;
            }
        }
        System.out.println("The number of comparisons: " + (i + 1));
        // Tüm liste dolaşılıp eleman bulunamazsa uyarı mesajı yazdırılır
        if (size == i)
            System.out.println("The element is not found");
    }

    public static void jumpSearch(int array[], int search) {
        int size = array.length;
        int step = (int) Math.floor(Math.sqrt(size));
        int prev = 0;
        int count = 0;

        // Listenin başından başlanarak değer aranır
        while (array[Math.min(step, size) - 1] < search) {
            prev = step;
            step += (int) Math.floor(Math.sqrt(size));
            if (prev >= size)
                break;
            count++;
        }

        // Listenin sonuna kadar dolaşılır
        while (array[prev] < search) {
            prev++;
            if (prev == Math.min(step, size))
                break;
            count++;
        }
        System.out.println("The number of comparisons: " + count);

        // Eleman bulunamazsa uyarı mesajı yazdırılır
        if (array[prev] == search)
            System.out.println("The element is found at " + prev);
        else
            System.out.println("The element is not found");
    }

    public static void main(String[] args) {
        int[] array1 = { 45, 67, 89, 90, 123, 456, 567, 678, 789, 890, 901 };
        int[] array2 = { 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 };

        Scanner input = new Scanner(System.in);
        System.out.print("Dizide hangi elemanı arıyorsunuz?: ");
        int search = input.nextInt();

        System.out.println("Nasıl aramak istiyorsunuz?");
        System.out.println("1. Binary search");
        System.out.println("2. Interpolasyon search");
        System.out.println("3. Linear search");
        System.out.println("4. Jump search");

        int choice = input.nextInt();
        input.close();

        switch (choice) {
            case 1:
                System.out.println("Eşit olmayan dağılımlı dizide arama yapılıyor...");
                binarySearch(array1, search);
                System.out.println("Eşit dağılımlı dizide arama yapılıyor...");
                binarySearch(array2, search);
                break;

            case 2:
                System.out.println("Eşit olmayan dağılımlı dizide arama yapılıyor...");
                interpolationSearch(array1, search);
                System.out.println("Eşit dağılımlı dizide arama yapılıyor...");
                interpolationSearch(array2, search);
                break;

            case 3:
                System.out.println("Eşit olmayan dağılımlı dizide arama yapılıyor...");
                linearSearch(array1, search);
                System.out.println("Eşit dağılımlı dizide arama yapılıyor...");
                linearSearch(array2, search);
                break;

            case 4:
                System.out.println("Eşit olmayan dağılımlı dizide arama yapılıyor...");
                jumpSearch(array1, search);
                System.out.println("Eşit dağılımlı dizide arama yapılıyor...");
                jumpSearch(array2, search);
                break;

            default:
                System.out.println("Yanlış seçim yaptınız.");
                break;
        }
    }
}