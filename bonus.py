from pip._vendor.distlib.compat import raw_input

i = int(raw_input('请输入本月利润:\n'))
if i <= 10000:
    bonus = i*0.1
elif i <= 20000:
    bonus = 10000*0.1 + (i-10000)*0.75
print(float(bonus))