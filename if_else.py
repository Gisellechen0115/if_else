#if跟else一分兩路 只能各有一個
age = input('請輸入年齡：')
age = int(age)
if (age>=20):
    print('你可以投票了')
else:
    print('你還不可以投票')

#else if一分多路，縮寫成 elif，可以很多個
# and or
age = input('請輸入年齡：')
age = int(age)
if age < 13 :
    print('國小')
elif age >= 13 and age <18 :
    print('國高中')
elif age >=18 and age < 22 :
    print('大學')
else : 
    print('社會')


#x練習題 
weight = input('請輸入體重(公斤)：')
height = input('請輸入身高(公分)：') 
bmi = float(weight) / float(height)** 2 * 10000
bmi = int(bmi)
if bmi < 18.5 :
    print('體重過輕')
elif bmi >= 18.5  and bmi < 24  :
    print('你的BMI值', bmi , '體重正常')
elif bmi >= 24  and bmi < 27  :
    print('你的BMI值:', bmi ,'體重過重')
elif bmi >= 27  and bmi < 30  :
    print('你的BMI值:', bmi ,'輕度肥胖')
elif bmi >= 30  and bmi < 35  :
    print('你的BMI值:', bmi ,'中度肥胖')
else:
     print('你的BMI值:', bmi ,'重度肥胖')
     
     
     