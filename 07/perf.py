import time
from main import chain_mul

NUM_MATRICES = 5000
DIM_MATRICES = 100


def main():
    if __name__ == "__main__":
        print("====== python ======")
        start_py = time.time()
        chain_mul(NUM_MATRICES, DIM_MATRICES)
        end_py = time.time()
        print(f"Time of execution of python matmul implementation is {end_py - start_py} seconds\n")

        print("====== C ======")


main()
