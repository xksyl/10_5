import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]


    time_start = time.time()
    for filename in filenames:
        read_info(filename)
    l_t = time.time() - time_start
    print(f"Время выполнения линейного вызова: {l_t:.6f} секунд")


    time_start = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    m_t = time.time() - time_start
    print(f"Время выполнения многопроцессного вызова: {m_t:.6f} секунд")








