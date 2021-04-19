#!/bin/bash
sudo date -s "20:00:00"
while true
do
	sleep 5
	./cooler
	#uptime >>output.txt
	#date >>output.txt
	#sleep 5
done
