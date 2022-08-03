marks_a6 = '2022_07_18_SonyA6000_g201b20445_f002'
marks_rx = '2022_07_18_SonyRX1RM2_g201b20445_f002'

def dataProof (file):
    originalFile = file + '.marks' 
    resultFile = file + 'result.marks'
    f1 = open(originalFile, 'r')
    f2 = open(resultFile, 'w')

    for line in f1:
        temp = line.strip().split(' ')
        temp[0] = "2022"
        
        for i in range(1, 6):
            if temp[i][0] == '0':
                var =  ' '+ temp[i][1:]
                temp[i] = var
                print(temp)
        f2.write(' '.join(temp)+'\n')
    f1.close()
    f2.close()

dataProof(marks_a6)
dataProof(marks_rx)

rinex = '2022_07_18_g201b20445_f002_.22o'
marks_a6 = '2022_07_18_SonyA6000_g201b20445_f002result'
marks_rx = '2022_07_18_SonyRX1RM2_g201b20445_f002result'

def dataClean (file1, file2):
    f1 = open(file1 + '.obs', 'r')
    f2 = open(file2 + '.marks', 'r')
    resultFile = file1 + 'result.obs'
    f3 = open(resultFile, 'w')

    marks = f2.readlines()
    print(marks)
    for line in f1:
        if line[2:(len(line))] not in marks:
            f3.write(line)
     
         
    f1.close()
    f2.close()
    f3.close()

dataClean(rinex, marks_a6)