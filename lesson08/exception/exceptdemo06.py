h = int(input('請輸入身高:'))
w = int(input('請輸入體重:'))
try:
    bmi = w / (h/100)**2
    if bmi < 18 or bmi > 23:
        raise Exception('BMI 不合格: ' + str(bmi))
except Exception as e:
    print(e)
else:
    print(bmi)