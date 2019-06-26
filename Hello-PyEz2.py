import getpass
from pprint import pprint
from jnpr.junos import Device

host = None
uname = None
pw = None

if host == None:
	host=input("Hostname: ")

if uname == None:
	uname=input("Username: ")

if pw == None:
	pw=input("Password: ")

dev = Device(host=host, user=uname, password=pw)

try:
	dev.open()
except:
	print("\n*** Connection rror ***\n")

pprint (dev.facts)
dev.close()


