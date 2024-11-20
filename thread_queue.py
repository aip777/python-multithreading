import threading
import uuid
import queue
def producer(my_queue):
    customer_info = ['Name', 'Email', 'Age', 'Address', 'Phone Number']
    customer_data = [str(uuid.uuid4())]
    for item in customer_info:
        _input_data = input(f'Enter your {item}: ')
        customer_data.append(_input_data)
        my_queue.put(_input_data)
    my_queue.put(customer_data)
    my_queue.put(None)

def consumer(my_queue):
    while True:
        item = my_queue.get()
        if not item:
            break
        print(item)
queue = queue.Queue()
t1 =  threading.Thread(target=producer, args=(queue,))
t2 = threading.Thread(target=consumer, args=(queue,))
t1.start()
t2.start()
