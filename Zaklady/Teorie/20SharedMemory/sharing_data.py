"""_summary_"""

import multiprocessing

def calc_square_using_value(numbers: list[int], results: multiprocessing.Array):
    """_summary_

    Args:
        numbers (list[int]): _description_
        q (multiprocessing.Queue): _description_
    """
    for idx, num in enumerate(numbers):
        results[idx] = (num*num)
    # print(f"Inside of process {results[:]}")

def calc_square_using_queue(numbers: list[int], que: multiprocessing.Queue):
    """_summary_

    Args:
        numbers (list[int]): _description_
        que (multiprocessing.Queue): _description_
    """
    for _, num in enumerate(numbers):
        que.put(num*num, block=True)

if __name__ == "__main__":
    nums = [2,3,5]

    res = multiprocessing.Array('i',3)
    p = multiprocessing.Process(target=calc_square_using_value, args=(nums, res))

    p.start()
    print(f"Outside of process before join {res[:]}")
    p.join()

    print(f"Outside of process {res[:]}")

    # res_queue = multiprocessing.Manager().Queue()
    # n = multiprocessing.Process(target=calc_square_using_queue, args=(nums, res_queue))
    # #p = multiprocessing.Process(target=calc_square, args=(numbers,))
    # n.start()
    # sleep(1)
    # print("Outside of process:")

    # while res_queue.empty() is not False:
    #     print(res_queue.get())

    # sleep(1)
    # n.join()
