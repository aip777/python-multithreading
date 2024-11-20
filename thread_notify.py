import threading
import uuid

def write():
    con.acquire()
    with open('data.txt', 'a') as file:
        customer_info = ['Name', 'Email', 'Age', 'Address', 'Phone Number']
        customer_data = [str(uuid.uuid4())]
        for item in customer_info:
            customer_data.append(input(f'Enter your {item}: '))
        file.write(str(customer_data))
    con.notify_all()
    con.release()
def read():
    con.acquire()
    with open('data.txt', 'r') as file:
        data = file.readline()
        print(data)
    con.release()

con = threading.Condition()
t1 = threading.Thread(target=write)
t2 = threading.Thread(target=read)
t1.run()
t2.run()
