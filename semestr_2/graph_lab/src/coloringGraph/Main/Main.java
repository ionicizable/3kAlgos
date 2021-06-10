package coloringGraph.Main;

import coloringGraph.Classes.Graph;
import coloringGraph.Printer.MatrixPrinter;

import javax.swing.*;

public class Main extends JPanel {
    public static Graph graph;
    public static int[][] matrix = new int[0][0];

    public static void main(String[] args) throws InterruptedException {

        int[][] firstAdjacencyMatrix = {
                {0, 1, 0, 1, 0, 0, 0}, // 1
                {1, 0, 1, 0, 1, 0, 0}, // 2
                {0, 1, 0, 1, 0, 0, 1}, // 3
                {1, 0, 1, 0, 1, 0, 1}, // 4
                {0, 1, 0, 1, 0, 1, 0}, // 5
                {0, 0, 0, 0, 1, 0, 1}, // 6
                {0, 0, 1, 1, 0, 1, 0}  // 7
        };
        Graph graph = new Graph(firstAdjacencyMatrix, firstAdjacencyMatrix.length);
        graph.printGraph();
        System.out.println("Матрица инциндентности:");
        MatrixPrinter.printMatrix(graph.writeIncidenceMatrix());
        System.out.println("\nМатрица смежности:");
        MatrixPrinter.printMatrix(graph.writeAdjacencyMatrix());
        System.out.println("\nСписок смежности:");
        MatrixPrinter.printMatrix(graph.writeAdjacencyList());
        System.out.println("\nСписок рёбер:");
        MatrixPrinter.printEdgesArray(graph.writeEdges());

        System.out.println("\nВершины и рёбра:");
        MatrixPrinter.printVerticesAndEdges(graph.getVertices(), graph.writeEdges());

        System.out.println("\nЖадный алгоритм раскраски");
        graph.greedyColoring(graph.writeAdjacencyList());

        System.out.println("\nРаскраска с помощью манипуляций со строками списка смежности");
        graph.coloringByManipulatingRows(graph.writeAdjacencyMatrix());

        int[][] secondAdjacencyMatrix = {
                {0, 1, 0, 1, 0, 0, 0}, // 1
                {0, 0, 0, 0, 1, 0, 0}, // 2
                {0, 1, 0, 0, 0, 0, 1}, // 3
                {0, 0, 1, 0, 1, 0, 0}, // 4
                {0, 0, 0, 0, 0, 1, 0}, // 5
                {0, 0, 0, 0, 0, 0, 1}, // 6
                {0, 0, 1, 1, 0, 0, 0}  // 7
        };
        Graph graphTwo = new Graph(secondAdjacencyMatrix, secondAdjacencyMatrix.length);
        graphTwo.printGraph();
        System.out.println("Матрица инциндентности:");
        MatrixPrinter.printMatrix(graphTwo.writeIncidenceMatrix());
        System.out.println("\nМатрица смежности:");
        MatrixPrinter.printMatrix(graphTwo.writeAdjacencyMatrix());
        System.out.println("\nСписок смежности:");
        MatrixPrinter.printMatrix(graphTwo.writeAdjacencyList());
        System.out.println("\nСписок рёбер:");
        MatrixPrinter.printEdgesArray(graphTwo.writeEdges());

        System.out.println("\nВершины и рёбра:");
        MatrixPrinter.printVerticesAndEdges(graphTwo.getVertices(), graphTwo.writeEdges());


        System.out.println("\nПоиск в глубину");
        int indexVertexDFS = 1;
        graphTwo.depthFirstSearch(graphTwo.writeAdjacencyList(), indexVertexDFS);

        System.out.println("\nПоиск в ширину");
        int indexVertexBFS = 1;
        graphTwo.breadthFirstSearch(graphTwo.writeAdjacencyList(), indexVertexBFS);


        int[][] thirdAdjacencyMatrix = {
                {0, 1, 1, 1}, // 1
                {1, 0, 1, 1}, // 2
                {1, 1, 0, 0}, // 3
                {1, 1, 0, 0}  // 4
        };
        Graph graphThree = new Graph(thirdAdjacencyMatrix, thirdAdjacencyMatrix.length);
        System.out.println("\nВершины и рёбра:");
        MatrixPrinter.printVerticesAndEdges(graphThree.getVertices(), graphThree.writeEdges());
        System.out.println("Матрица инциндентности:");
        MatrixPrinter.printMatrix(graphThree.writeIncidenceMatrix());
        System.out.println("\nМатрица смежности:");
        MatrixPrinter.printMatrix(graphThree.writeAdjacencyMatrix());
        System.out.println("\nСписок смежности:");
        MatrixPrinter.printMatrix(graphThree.writeAdjacencyList());
        System.out.println("\nСписок рёбер:");
        MatrixPrinter.printEdgesArray(graphThree.writeEdges());
        System.out.println("\nВершины и рёбра:");
        MatrixPrinter.printVerticesAndEdges(graphThree.getVertices(), graphThree.writeEdges());

        System.out.println("Раскраска рёбер");
        graphThree.edgeColoring(graphThree.getEdges());
    }
}

