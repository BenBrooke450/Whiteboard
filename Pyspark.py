


###############################################################################


#17 How to convert the first character of each element in a series to uppercase?

"""
# Suppose you have the following DataFrame
data = [("john",), ("alice",), ("bob",)]
df = spark.createDataFrame(data, ["name"])

df.show()
+-----+
| name|
+-----+
| john|
|alice|
| bob|
+-----+
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import max, count, col, rank, row_number, monotonically_increasing_id, when, upper

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

data = [("john",), ("alice",), ("bob",)]

df = spark.createDataFrame(data, ["name"])

list1 = []

for i, n in enumerate(df.collect()):
    list1.append((i + 1, n[0][0].upper() + n[0][1:]))

df = spark.createDataFrame(list1, ["number", "name"])

df.show()

+------+-----+
|number| name|
+------+-----+
|     1| John|
|     2|Alice|
|     3|  Bob|
+------+-----+







###############################################################################


#23 How to filter words that contain atleast 2 vowels from a series?

"""
df = spark.createDataFrame([('Apple',), ('Orange',), ('Plan',) , ('Python',) , ('Money',)], ['Word'])

df.show()
+------+
| Word|
+------+
| Apple|
|Orange|
| Plan|
|Python|
| Money|
+------+

"""

# Initialize Spark session
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

from pyspark.sql.functions import to_date, dayofmonth, weekofyear, dayofyear, dayofweek, col, concat, lit

df = spark.createDataFrame([('Apple',), ('Orange',), ('Plan',) , ('Python',) , ('Money',)], ['Word'])

list1 = []
vowls = ["a","e","i","o","u"]

for n in df.collect():
  t = 0
  for v in n[0].lower():
    if v in vowls:
      t = t + 1
      if t == 2:
        break
    elif len(n[0]) - 1 == t:
      list1.append((n[0],))
    else:
      t = t + 1

df = spark.createDataFrame(list1,["Letters_not_woth_two"]).show()
