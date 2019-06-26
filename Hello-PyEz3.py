import getpass
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

host = None
uname = None
pw = None

if host == None:
	host=input("Hostname: ")

if uname == None:
	uname=input("Username: ")

if pw == None:
	pw=input("Password: ")

dev = Device(host=host, user=uname, password=pw, gather_facts=False)

try:
	dev.open()
except:
	print("\n*** Connection rror ***\n")

cu = Config(dev)
diff = cu.diff()


pprint (diff)
if diff:
	print("ROLLBACK")
	cu.rollback()

dev.close()


