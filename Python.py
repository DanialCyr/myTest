year = int(input('请输入年份：'))
result = "是闰年" if(year%4 == 0 and year % 100 !=0) or (year%100 == 0) else "不是闰年"
print("\n"+str(year) + result + "!")