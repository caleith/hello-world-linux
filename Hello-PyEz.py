from pprint import pprint
from jnpr.junos import Device

dev = Device(host="172.25.11.1", user="lab", password="lab123")

try:
	dev.open()
except:
	print("\n*** Connection rror ***\n")

pprint (dev.facts)
dev.close()


