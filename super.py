import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S',
                    level=logging.INFO)

colaCaja = []
clientes = []
maxClientes = 3
semaforoCliente = threading.Semaphore()
semaforoCajero = threading.Semaphore()


class Cliente(threading.Thread):
    def __int__(self):
        super().__init__()

    def entrarAlSuper(self):

        if len(clientes) > maxClientes:
            logging.info('mucha gente, me voy a casa')
        semaforoCliente.acquire()
        clientes.append(self)
        time.sleep(2)
        logging.info('voy a la caja')
        colaCaja.append(self)

    def run(self):
        while True:
            self.entrarAlSuper()
            time.sleep(2)
            semaforoCliente.release()


class Cajero(threading.Thread):
    def __int__(self):
        super().__init__()

    def run(self):
        while True:
            if len(colaCaja) > 0:
                semaforoCajero.acquire()
                colaCaja.pop(0)
                logging.info('atendiendo')
                semaforoCliente.release()
                time.sleep(2)
                logging.info('termine de antender')
            semaforoCajero.release()
            logging.info('me fui a dormir')


cajero: Cajero = Cajero()


cajero.start()

for i in range(clientes):
    Cliente(i).start()
