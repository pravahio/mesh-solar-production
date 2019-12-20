import time
import threading

from mesh_solar_power_production.main import MeshSolarPowerProduction

geospace = [
    '/in/delhi'
]

def main():

    c = MeshSolarPowerProduction('rpc.pravah.io:5555')

    feed = c.subscribe(geospace)
    print('Subscribed to ' + str(geospace))

    threading.Thread(target=fetch_data, args=(feed,)).start()

def fetch_data(feed):
    for m, c in feed:
        #pass
        print(m)

if '__main__' == __name__:
    main()