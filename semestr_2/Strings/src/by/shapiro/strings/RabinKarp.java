package by.shapiro.strings;

import java.math.BigInteger;
import java.util.Random;

public class RabinKarp
{
    // d - количество символов во входном алфавите
    public final static int d = 256;
    public static int pat_count = 0;

    static void count(boolean isPrinted){
        if(isPrinted){
            System.out.println(pat_count);
        } else {
            pat_count++;
        }
    }

    static void search(String pat, String txt, int q)
    {
        int M = pat.length();
        int N = txt.length();
        int i, j;
        int p = 0; // значение хэша для подстроки
        int t = 0; // значение хеша для входной строки
        int h = 1;

        // Значением h будет pow(d, M-1)%q
        for (i = 0; i < M-1; i++)
            h = (h*d)%q;

        // Рассчитываем значение хэша подстроки и первой области входной строки
        for (i = 0; i < M; i++)
        {
            p = (d*p + pat.charAt(i))%q;
            t = (d*t + txt.charAt(i))%q;
        }

        // Сдвигаем подстроку над входной строкой по одному символу за раз
        for (i = 0; i <= N - M; i++)
        {

            // Проверяем хэш - значения текущей области входной строки и подстроки
            // and pattern. Если хэш-значения совпадают, то проверяем далее посимвольно
            if ( p == t )
            {
                /* Проход посимвольно */
                for (j = 0; j < M; j++)
                {
                    if (txt.charAt(i+j) != pat.charAt(j))
                        break;
                }

                // Если p == t и подстрока[0...M-1] == входная строка[i, i+1, ...i+M-1]
                if (j == M)
                    System.out.println("Подстрока найдена на индексе " + i);
                    count(false);
            }

            // Рассчитываем хэш - значение следующей области входной строки: Удаляем
            // ведущий индекс, добавляем замыкающий
            if ( i < N-M )
            {
                t = (d*(t - txt.charAt(i)*h) + txt.charAt(i+M))%q;

                // При получении отрицательного t конвертируем его в положительноецццц
                if (t < 0)
                    t = (t + q);
            }
        }
    }
    public static long longRandomPrimeNumber() {
        BigInteger prime = BigInteger.probablePrime(11, new Random());
        return prime.longValue();
    }
}