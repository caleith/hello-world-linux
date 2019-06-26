import getpass
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

junos_hosts = ["172.25.11.1"]

for ip in junos_hosts:
	dev = Device(host=ip, user="lab", password="lab123")
	try:
		dev.open()

		config = Config(dev)
		config.lock()

		config.load(path="snmp.conf", merge=True)

		config.pdiff()
		config.commit()
		config.unlock()

		dev.close()
	except:
		print("\n*** Connection rror ***\n")


