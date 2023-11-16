def test (name,age):
    print(name,age)
test("Tom",69)

#參數名稱前加*使其為任意數量
def func1(*a):
    for i in a:
        print(i)
func1(2,6,9)
#輸出其加減後的值
def calculation(a, b):
    return(a+b,a-b)
res = calculation(40, 10)
print(res)
#輸出預設參數
def showEmployee(name, salary=9000):
    print('123')
    print("姓名:",name,"薪資:",salary)
showEmployee("Tom", 12000)
#未給薪資 套用預設值9000
showEmployee("Jerry")