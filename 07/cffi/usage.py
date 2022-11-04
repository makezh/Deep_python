import cffi


def ABI():
    ffi = cffi.FFI()
    lib = ffi.dlopen('./libchain.so')
    ffi.cdef('''
    long long **createMatrix(int dim);
    long long **multiply(long long **matrix1, long long **matrix2, long long dim);
    long long **chain_multiply(int count_of_matrix, int dim);
    ''')

    res = lib.chain_multiply(5000, 100)
    print(res)


def main():
    if __name__ == "__main__":
        ABI()


main()
