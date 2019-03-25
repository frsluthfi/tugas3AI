import csv
import statistics
from math import *
from operator import itemgetter

#Melakukan input data train dan memasukannya ke dalam array multidimensi arrTrain
with open('DataTrain_Tugas3_AI.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0
    arrTrain = []
    i = 0
    for row in reader:
        if line_count == 0:
            line_count += 1
        else:
            i+=1
            arrTemp = []
            arrTemp.append(float(row[1]))
            arrTemp.append(float(row[2]))
            arrTemp.append(float(row[3]))
            arrTemp.append(float(row[4]))
            arrTemp.append(float(row[5]))
            arrTemp.append(float(row[6]))
            arrTrain.append(arrTemp)

    #Melakukan input data test dan menasukannya ke dalam array multidimensi arrTest
    with open('DataTest_Tugas3_AI.csv') as csvfile2:
        reader = csv.reader(csvfile2)
        line_count = 0
        arrTest = []
        j = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
            else:
                j+=1
                arrTemp = []
                arrTemp.append(float(row[1]))
                arrTemp.append(float(row[2]))
                arrTemp.append(float(row[3]))
                arrTemp.append(float(row[4]))
                arrTemp.append(float(row[5]))
                arrTest.append(arrTemp)
        #Mendefinisikan nilai K
        k = 3
        #Mendifinisikan variabel i yang digunakan sebagai variabel perulangan seluruh data Test
        i = 0
        #arrVal digunakan untuk menampung hasil pengelompokkan
        arrVal = []
        while(i<200):
            #Variabel j digunakan sebagai variabel perulangan seluruh data Train
            j = 0
            #arrMath menampung hasil perhitungan jarak data train dan data test, serta kelompok pada data train
            arrMath = []
            #arrLazy digunakan untuk menampung nilai hasil pengolompokkan berdasarkan arrayMath yang telah diurutkan
            arrLazy = []
            while(j<800):
                arrTemp = []
                #variabel result diisi dengan hasil perhitungan jarak
                #Sqrt dapat digan abs ketika ingin merubah metode perhitungan dari Euclidean ke Manhattan
                result = sqrt((arrTest[i][0]-arrTrain[j][0])**2+(arrTest[i][1]-arrTrain[j][1])**2+(arrTest[i][2]-arrTrain[j][2])**2+(arrTest[i][3]-arrTrain[j][3])**2+(arrTest[i][4]-arrTrain[j][4])**2)
                arrTemp.append(result)
                arrTemp.append(arrTrain[j][5])
                arrMath.append(arrTemp)
                j+=1
            arrMath.sort(key=lambda x: x[0])
            #arrCoba digunakan untuk memotong arrMath, mengambil nilai teratas.
            arrCoba = arrMath[:-(800-k)]
            for b in range(k):
                arrLazy.append(arrCoba[b][1])
            arrLazy.sort(key=lambda x: x)
            if((arrLazy[0] == arrLazy[1]) or (arrLazy[0] == arrLazy[2]) or (arrLazy[1] == arrLazy[2])):
                arrVal.append(statistics.mode(arrLazy))
            else:
                arrVal.append(arrLazy[0])            
            i+=1
        #digunakan untuk menampilkan hasil
        for i in arrVal:
             print(i)

        #digunakan untuk memasukkan hasil ke dalam file 'TebakanTugas3.csv'
        with open('TebakanTugas3.csv','w') as file:
            for i in range(200):
                file.write('%d' % arrVal[i])
                file.write('\n')