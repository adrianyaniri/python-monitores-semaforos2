import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S',
                    level=logging.INFO)

colaCaja = []
clientes = []
maxClientes = 3
semaforoCajero = threading.Semaphore()


class Cliente(threading.Thread):
    def __int__(self):
        super().__init__()

    def entrarAlSuper(self):
        if len(clientes) > maxClientes:
            logging.info('mucha gente, me voy a casa')
        clientes.append(1)
        time.sleep(2)
        logging.info('comprando')

    def run(self):
        # while True:
        self.entrarAlSuper()
        colaCaja.append(1)
        time.sleep(2)
        logging.info('voy a la caja')
        semaforoCajero.acquire()


class Cajero(threading.Thread):
    def __int__(self):
        super().__init__()

    def run(self):
        while True:
             while len(colaCaja) == 0:
                colaCaja.pop(0)
                logging.info('atendiendo')
                semaforoCajero.acquire()
                time.sleep(2)
                logging.info('termine de antender')
        logging.info('me fui a dormir')

# agregar fun espera con random


cajero = Cajero()


cajero.start()
for i in range(5):
    Cliente(i).start()
