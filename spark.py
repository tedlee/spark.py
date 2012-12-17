#!/usr/bin/env python
# coding: utf-8

import optparse

def main():

	options, arguments = optparse.OptionParser().parse_args()
	if len(arguments) > 1:

		arguments = map(int, arguments) # Convert arguments to integers
		bars = ["▁","▂","▃","▄","▅","▆","▇"] 
		spark_string = ""

		smallest_spark = 0
		smallest_spark = min(arguments)
		distance = max(arguments) - smallest_spark # Find the delta between largest and smallest values
		steps = distance / float(len(bars) - 1) or 1

		for i in arguments:
			spark_string += bars[int(round((i - smallest_spark) / steps))]
		
		print spark_string

	else:

		print "\n################################"
		print "This is spark.\n"
		print "*How to use spark*"
		print "Run: spark.py [numbers seperated by spaces]"
		print "Ex:"
		print "    spark.py 13 37 42 65 69"
		print "################################\n"

if __name__ == "__main__":
	main()
