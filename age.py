driving = input('請問你開過車嗎:')
age = input('請問你的年齡是?:')
if driving == '有':
    if int(age) >= 18 :
        print('你通過測試了')
        raise SystemExit
    else :
        print('你違規上路了')       
elif driving == '沒有':
     if int(age) >= 18 :
        print('你可以去考駕照喔')
     else :
         print('再等等', 18-int(age),'年，你就可以考駕照了')
else :
    print('只能輸入有或沒有')
"# age" 
