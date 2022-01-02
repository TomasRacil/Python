import multiprocessing

result=[]

#def calc_square(numbers, result, v):
#def calc_square(numbers, q):
    #v.value = 5.67
def calc_square(numbers):
    global result

    for idx, n in enumerate(numbers):

        #result[idx] = n*n
        #q.put(n*n)
        result.append(n*n)


    print(f"Inside of process {result}")

if __name__ == "__main__":
    numbers = [2,3,5]

    # result = multiprocessing.Array('i',3)
    # v = multiprocessing.Value('d', 0.0) 
    # p = multiprocessing.Process(target=calc_square, args=(numbers, result, v))
    # q=multiprocessing.Queue()
    # p = multiprocessing.Process(target=calc_square, args=(numbers, q))
    p = multiprocessing.Process(target=calc_square, args=(numbers,))

    p.start()
    p.join()

    #print(result[:])
    #print(v.value)
    #while q.empty() is not False:
        #print(q.get())
    print(f"Outside of process {str(result)}")
    