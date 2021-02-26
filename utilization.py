import psutil
import time
while 1:
	cpuPercent = psutil.cpu_percent(interval=20)
	ramPercentr = psutil.virtual_memory().percent
	print "CPU utilization:" , cpuPercent, ", Memory utilization:",  ramPercentr
	time.sleep(10)