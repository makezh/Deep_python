#include "printf.h"
#include "main.h"
#include "stdlib.h"


long long **createMatrix(int dim) {
    long long **matrix = (long long **) malloc(dim * sizeof(long long *));
    for (int i = 0; i < dim; i++) {
        matrix[i] = (long long *) malloc(dim * sizeof(long long));
        for (int j = 0; j < dim; j++) {
            matrix[i][j] = rand() % 100;
        }
    }
    return matrix;
}


long long **multiply(long long **matrix1, long long **matrix2, long long dim) {
    long long **result = (long long **) malloc(dim * sizeof(long long *));
    for (int i = 0; i < dim; i++) {
        result[i] = (long long *) malloc(dim * sizeof(long long));
        for (int j = 0; j < dim; j++) {
            result[i][j] = 0;
            for (int k = 0; k < dim; k++) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }
    return result;
}


long long **chain_multiply(int count_of_matrix, int dim) {
    long long **matrix = createMatrix(dim);
    for (int i = 0; i < count_of_matrix - 1; i++) {
        long long **matrix2 = createMatrix(dim);
        matrix = multiply(matrix, matrix2, dim);
        free(matrix2);
    }
    return matrix;
}

