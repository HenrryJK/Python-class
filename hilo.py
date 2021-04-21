import threading
import time


def mensaje(texto):
    print("Este es un texto : " + texto)
    time.sleep(5)


if __name__ == '__main__':
    thread = threading.Thread(target=mensaje, args=("DAD",))
    thread.start()
    thread.join()

    print("Ciclo V")
