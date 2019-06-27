
import getpass
import yaml
import sys

from pprint import pprint

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import *
from jinja2 import Template

# ----------------------------------------------------------------
# from jnpr.junos.utils.sw import SW
# sw = SW(dev)
# ok = sw.install(package=r'<FILE_NAME>',progress=update_progress)
# def update_progress(dev, report) # report - FILE
#    print dev.hostname, '> ', report
# ----------------------------------------------------------------

# timout for working connection
Device.auto_probe=5

# list of hosts
junos_hosts = ["vMX-1","vMX-2"]

# get password
pw=getpass.getpass()

# main loop
for host in junos_hosts:
	# read params
	with open(host + ".yml", "r") as yml_var:
		data = yaml.load(yml_var.read(), Loader=yaml.FullLoader)
	# read template
	with open("snmp.j2", "r") as j2_var:
		t_format = j2_var.read()

	template = Template(t_format)
	# render configuration
	myConfig = template.render(data)

	print ("\nResults for device " + host + "\n-------------------")

	# show template
	print(myConfig)

	try:
		dev = Device(host=host, user="lab", password=pw)
		dev.open()
		# set timeout
		dev.timeout = 10
		# start configuration
		config = Config(dev)
		config.lock()
		config.load(myConfig, merge=True, formt="text")
		# show | compare
		config.pdiff()
		# commit configuration
		config.commit()
		config.unlock()
		dev.close()
	# exceptions
	except ProbeError as e:
		print("Dead box!")
	except LockError as e:
		print("The config database was locked!")
	except ConnectTimeoutError as e:
		print ("Connection time out!")
