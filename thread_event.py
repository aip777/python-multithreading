import threading
e = threading.Event()

def first_task(data):
    print("This is first task", data)
    e.set()

def second_task(data):
    e.wait()
    if e.is_set():
        print("Second task is running", data)
    e.clear()
data = {'a': 1, 'b': 2, 'c': 3}
t1 = threading.Thread(target=first_task(data))
t2 = threading.Thread(target=second_task(data))
t1.start()
t2.start()
print(e.is_set())

