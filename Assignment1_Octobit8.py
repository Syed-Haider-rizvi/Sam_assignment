

# import pandas as pd
# df = pd.read_csv("D:\Assignment1_Octobit8Env\data1.csv")
# saved_column_cook = df.cookTime
# saved_column_prep = df.prepTime
# saved_column_ingredients = df.ingredients
#
#
#
# for data in saved_column_cook:
#     strDemo = str(data)
#     strDemo = strDemo.replace('PT', '')
#     print(strDemo + ',')

# for data in saved_column_prep:
#     strDemo = str(data)
#     print(strDemo.replace('PT', ''))
#
# key = False
# list = []
# for data in saved_column_ingredients:
#     if 'beef' in data:
#         key = True
#         list.append(data)
# print(list)


# cookTime = []


from pyspark.sql import SparkSession

logFile = "D:\Assignment1_Octobit8Env\data1.csv"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('beef')).count()
numBs = logData.filter(logData.value.contains('PT')).count()

print("Lines with beef: %i, lines with PT: %i" % (numAs, numBs))

spark.stop()


