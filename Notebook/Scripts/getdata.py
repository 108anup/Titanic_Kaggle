import numpy as np
import csv as csv

csv_file_object = csv.reader(open("../csv/train.csv","rb"))
header = csv_file_object.next()

data = list(csv_file_object)
data = np.array(data)
print data