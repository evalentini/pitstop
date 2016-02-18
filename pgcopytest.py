import psycopg2

try:
	conn=psycopg2.connect("dbname='pitstop', user='root', password='bigmoney2016'")
except:
	print "cant connect"
