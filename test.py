import csv

# this file contains 3 different tests I created to get a better understanding of the data

def test1():
    # this test determines how often ships of a particular vesseltype carried a particular type of cargo
    # for example, for ships of vesseltype 2 there were:
        # 117 instances of handling (discharging and/or loading) cargo type 1
        # 112 instances of handling cargo type 2
        # 0 instances of handling cargo type 3
        # 12 instances of handling cargo type 4

    # reason for conducting this test: if a particular vesseltype can be strongly correlated with a particular
    # type of cargo, we can use the vesseltype to predict the kind of cargo a ship is carrying
    count = 0
    vesseldwt = 3
    vesseltype = 4
    discharge1 = 5
    load1 = 6
    discharge2 = 7
    load2 = 8
    discharge3 = 9
    load3 = 10
    discharge4 = 11
    load4 = 12
    typedict = {}
    with open('VesselData.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if count == 0:
                count += 1
                continue
            if row[vesseltype] not in typedict:
                typedict[row[vesseltype]] = [0, 0, 0, 0]
            tranship1 = int(row[discharge1]) + int(row[load1])
            tranship2 = int(row[discharge2]) + int(row[load2])
            tranship3 = int(row[discharge3]) + int(row[load3])
            tranship4 = int(row[discharge4]) + int(row[load4])
            typedict[row[vesseltype]][0] += (tranship1 > 0)
            typedict[row[vesseltype]][1] += (tranship2 > 0)
            typedict[row[vesseltype]][2] += (tranship3 > 0)
            typedict[row[vesseltype]][3] += (tranship4 > 0)
    for key in typedict.keys():
        print(key, typedict[key])

def test2():
    # this test determined how often a particular ship handled more than 1 type of cargo
    # this occurred only 0.18% of the time, so it is almost always correct to predict that if a ship carries
    # a certain type of cargo, then that is the only type of cargo it carries
    count = 0
    vesseldwt = 3
    vesseltype = 4
    discharge1 = 5
    load1 = 6
    discharge2 = 7
    load2 = 8
    discharge3 = 9
    load3 = 10
    discharge4 = 11
    load4 = 12
    diff = 0
    with open('VesselData.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if count == 0:
                count += 1
                continue
            tranship1 = int(row[discharge1]) + int(row[load1])
            tranship2 = int(row[discharge2]) + int(row[load2])
            tranship3 = int(row[discharge3]) + int(row[load3])
            tranship4 = int(row[discharge4]) + int(row[load4])
            diff += (((tranship1 > 0) + (tranship2 > 0) + (tranship3 > 0) + (tranship4 > 0)) > 1)
            count += 1
    print(diff/(count - 1))

def test3():
    # this test determined the ratio of weight of cargo handled to vesseldwt, for each vesseltype
    # for example, for vesseltype 5, the average ratio of cargo weight handled to vesseldwt is ~0.3757

    # reason for conducting this test: if we can find a strong correlation between the ships weight and the
    # weight of the cargo handled, we can predict the weight of cargo handled by multiplying the ship's weight by
    # a coefficient
    count = 0
    vesseldwt = 3
    vesseltype = 4
    discharge1 = 5
    load1 = 6
    discharge2 = 7
    load2 = 8
    discharge3 = 9
    load3 = 10
    discharge4 = 11
    load4 = 12
    typedict = {}
    with open('VesselData.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if count == 0:
                count += 1
                continue
            if row[vesseltype] not in typedict:
                typedict[row[vesseltype]] = []
            if not row[vesseldwt]:
                continue
            dwt = int(row[vesseldwt])
            tranship1 = int(row[discharge1]) + int(row[load1])
            tranship2 = int(row[discharge2]) + int(row[load2])
            tranship3 = int(row[discharge3]) + int(row[load3])
            tranship4 = int(row[discharge4]) + int(row[load4])
            transwt = tranship1 + tranship2 + tranship3 + tranship4
            typedict[row[vesseltype]].append(transwt/dwt)
    for key in typedict.keys():
        lst = typedict[key]
        sum = 0
        for num in lst:
            sum += num
        typedict[key] = sum/len(lst)
        print(key, typedict[key])

# to sum up, my approach was to find of if/how the vesseltype and vesseldwt determined which type of cargo a particular
# ship would handle, and how much of it.
# given more time, I would test the following hypotheses:

    # if the time between earliesteta and latesteta spans multiple days, then the transshipments are spread
    # over multiple days, which could mean that there are multiple transshipments, which could mean that there are
    # multiple cargo types that need to be transshipped separately

    # particular vesselids can be matched with particular cargo types or weights