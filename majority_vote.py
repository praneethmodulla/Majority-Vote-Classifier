import sys

def main():
    train = [] 
    with open(trainFile) as input:
        num = 0
        for line in input:
            if num != 0 :
                l = line.split('\t')
                l[-1] = l[-1].strip()
                train.append(l)
            num += 1
    count1 = 0
    count0 = 0
    totalTrainData = 0
    for i in train:
        totalTrainData += 1
        if i[-1] == '1':
            count1 += 1
        elif i[-1] == '0':
            count0 += 1
    
    predict = ''
    if count1 >= count0 :
        predict = '1'
    else :
        predict = '0'
    
    trainingLabels = open("train.txt", "w")
    metricsFile = open("metrics.txt", "w")

    errorTrain = 0
    for k in train:
        trainingLabels.write(predict + "\n")
        if predict != k[-1]:
            errorTrain += 1
    
    trainingErrorRate = errorTrain/totalTrainData

    test = []
    with open(testFile) as testInput:
        number = 0
        for line in testInput:
            if number != 0:
                ln = line.split('\t')
                ln[-1] = ln[-1].strip()
                test.append(ln)
            number += 1

    countErrors = 0
    countTotal = 0

    testLabels = open("test.txt", "w")
    for j in test:
        countTotal += 1
        testLabels.write(predict + "\n")
        if predict != j[-1]:
            countErrors += 1
    
    errorRate = countErrors/countTotal
    metricsFile.write(f"error(train): {trainingErrorRate}\n")
    metricsFile.write(f"error(test): {errorRate}")

if __name__ == "__main__":
    trainFile = sys.argv[1]
    testFile = sys.argv[2]
    print(f"The training file is : {trainFile}")
    print(f"The testing file is : {testFile}")
    main()