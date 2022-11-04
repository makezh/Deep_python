import time
from main import chain_mul
import cffi

NUM_MATRICES = 5000
DIM_MATRICES = 100


def main():
    if __name__ == "__main__":
        print("====== python ======")
        start_py = time.time()
        chain_mul(NUM_MATRICES, DIM_MATRICES)
        end_py = time.time()
        print(f"Time of execution of python matmul implementation is {end_py - start_py} seconds\n")

        print("====== cffi ======")
        ffi = cffi.FFI()
        cffi_lib = ffi.dlopen('./cffi/libchain.so')
        ffi.cdef('''
            long long **createMatrix(int dim);
            long long **multiply(long long **matrix1, long long **matrix2, long long dim);
            long long **chain_multiply(int count_of_matrix, int dim);
            ''')

        start_cffi = time.time()
        cffi_lib.chain_multiply(NUM_MATRICES, DIM_MATRICES)
        end_cffi = time.time()
        print(f"Time of execution of cffi fibonacci implementation is {end_cffi - start_cffi} seconds")


main()
