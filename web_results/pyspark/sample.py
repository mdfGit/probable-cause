from __future__ import print_function
import sys
from pyspark import SparkContext

if __name__ == "__main__":

	file = sc.textFile("hdfs://ip-10-0-0-7:9000/user/test.txt")
	counts = file.flatMap(lambda line: line.split(" "))\
	       .map(lambda word: (word, 1))\
	       .reduceByKey(lambda a, b: a + b)
	res = counts.collect()
	for val in res:
		print val