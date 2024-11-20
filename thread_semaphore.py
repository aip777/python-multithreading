import threading
import uuid
import queue
import sqlite_db
con = threading.Semaphore(5)

def producer(my_queue):
    customer_info = ['Name', 'Email', 'Age', 'Address', 'Phone Number']
    student_range = input("How many students? Input Type(int): ")
    length = int(student_range)
    for i in range(length):
        customer_data = [str(uuid.uuid4())]
        for item in customer_info:
            _input_data = input(f'Enter your {item}: ')
            print(" ")
            customer_data.append(_input_data)
            # my_queue.put(_input_data)
        my_queue.put(customer_data)
    my_queue.put(None)

def consumer(my_queue):
    while True:
        item = my_queue.get()
        if not item:
            break
        # inset data in database
        con.acquire()
        print(item)
        sqlite_db.insert_data(item)
        con.release()

queue = queue.Queue()
t1 =  threading.Thread(target=producer, args=(queue,))
t2 = threading.Thread(target=consumer, args=(queue,))
t1.start()
t2.start()

