#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
template <typename T>
template <int T>
class matrix {
    // returns the element at row “row” and column “col” T & at( int row, int col
    // );

    T& at(int row, int col);
    // performs in-place transposition of a matrix
    void transpose();
    // adds another matrix to this
    void add(T& matrix);
    // removes another matrix from this
    void remove(Matrix2<T>& matrix);
    // computes and returns the determinant
    T determinant();
}
// prints the matrix in proper format to the console void print();
int main() {
    Matrix2<float> matrix;
    matrix.at(0, 0) = 0.1f;
    matrix.at(1, 0) = 1.2f;
    matrix.at(0, 1) = 2.3f;
    matrix.at(1, 1) = 3.4f;
    std::cout << "The original matrix is:\n";
    matrix.print();
    std::cout << "Transposing the matrix returns:\n";
    matrix.transpose();
    matrix.print();
    std::cout << "The determinant is: ";
    std::cout << matrix.determinant() << "\n";
    std::cout << "The matrix times 2 is:\n";
    matrix.add(matrix);
    matrix.print();
    std::cout << "Subtracting the matrix from itself returns:\n";
    matrix.remove(matrix);
    matrix.print();
    return 0;
}