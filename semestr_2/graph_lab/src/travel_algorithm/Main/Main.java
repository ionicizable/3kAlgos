package travel_algorithm.Main;

import travel_algorithm.Algorithms.Algo;

public class Main {
    public static void main(String[] args) {

        Integer[][] matrix = {
            {Integer.MAX_VALUE, 4, 12, 1, 5, 15},
            {4, Integer.MAX_VALUE, 4, 15, 13, 8},
            {6, 4, Integer.MAX_VALUE, 5, 10, 2},
            {1, Integer.MAX_VALUE, 5, Integer.MAX_VALUE, Integer.MAX_VALUE, 4},
            {5, 13, 10, Integer.MAX_VALUE, Integer.MAX_VALUE, 2},
            {15, 8, 2, 4, 2, Integer.MAX_VALUE}
        };

        System.out.println("Алгоритм Флойда");
        matrix = Algo.floydAlgorithm(matrix);

        System.out.println("Алгоритм Литтла");
        Algo.littleAlgorithm(matrix);
    }
}
