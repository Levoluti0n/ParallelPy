import threading


def matrix_multiply_worker(A, B, result, row_start, row_end, barrier,
                           thread_id):
    print(f"Thread {thread_id} is starting computation...")
    num_cols_B = len(B[0])
    num_cols_A = len(A[0])

    for i in range(row_start, row_end):
        for j in range(num_cols_B):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(num_cols_A))

    print(
        f"Thread {thread_id} has completed its rows {row_start}-{row_end - 1} and is waiting at the barrier..."
    )
    barrier.wait()
    print(f"Thread {thread_id} passed the barrier and completed.")


def create_matrix(rows, cols, fill_value=0):
    return [[fill_value for _ in range(cols)] for _ in range(rows)]


N = 6
P = 6
M = 6

A = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18],
     [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30],
     [31, 32, 33, 34, 35, 36]]

B = [[6, 5, 4, 3, 2, 1], [12, 11, 10, 9, 8, 7], [18, 17, 16, 15, 14, 13],
     [24, 23, 22, 21, 20, 19], [30, 29, 28, 27, 26, 25],
     [36, 35, 34, 33, 32, 31]]

result = create_matrix(N, M)

num_threads = 3
rows_per_thread = N // num_threads

barrier = threading.Barrier(num_threads)

threads = []
for thread_id in range(num_threads):
    row_start = thread_id * rows_per_thread
    row_end = (thread_id +
               1) * rows_per_thread if thread_id != num_threads - 1 else N
    thread = threading.Thread(target=matrix_multiply_worker,
                              args=(A, B, result, row_start, row_end, barrier,
                                    thread_id))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nResultant Matrix:")
for row in result:
    print(row)
