


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

