package by.shapiro.strings;

public class Main {
    public static void main(String[] args) {
        String txt = "абракадра";
        String pat = "абр";

        int q = 101;
        RabinKarp.search(pat, txt, q);
        System.out.println("Кол-во найденных подстрок:");
        RabinKarp.count(true);
        System.out.println("Случайное простое число:");
        System.out.println(RabinKarp.longRandomPrimeNumber());
    }
}
