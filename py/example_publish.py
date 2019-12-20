import time 
import sys
import json

from mesh_solar_power_production.main import *
from mesh_solar_power_production.defaults import State
from mesh_solar_power_production import MeshRPCException

geospace = [
	'/in/ncr'
]

def main(argv):
	m = MeshSolarPowerProduction()

	solar_data = open('solar.json', 'r').read()
	solar_json = json.loads(solar_data)

	try:
		m.registerToPublish(geospace)
	except MeshRPCException as e:
		print(e.getMessage())
		exit()
	
	for i in range(100):
		try:
			m.publish(geospace, solar_json)
			print('Publishing #' + str(i))
		except MeshRPCException as e:
			print(e.getMessage())
			exit()
		time.sleep(2)

if "__main__" == __name__:
    main(sys.argv)