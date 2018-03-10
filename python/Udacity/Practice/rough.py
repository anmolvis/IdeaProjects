import matplotlib.pylot as plt
import csv
def trip_duration(filename):
    with open(filename,"r") as f:
        reader = csv.DictReader(f)
        list_dur = []
        for row in reader:
            dur = float(row["duration"])
            list_dur.append(dur)
        print(list_dur)
        %matplotlib inline
        pyl.hist(list_dur)
        pyl.title("Trip Duration")
        pyl.xlabel("Duration")
        pyl.show()
trip_duration("NYC-2016-Summary.csv")
