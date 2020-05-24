"""
输入：身高和体重值
处理：计算BM1值，并根据BMI指标分类找到合适类别
输出：打印指标分类信息
"""

input_height = float(input('身高(m)：'))
input_weight = float(input('体重(kg)：'))
bmi = input_weight / pow(input_height, 2)

if bmi < 18.5:
    inlandClass = '偏瘦'
elif 18.5 <= bmi < 25:
    inlandClass = '正常'
elif 25 <= bmi < 30:
    inlandClass = '偏胖'
else:
    inlandClass = '肥胖'

if bmi < 18.5:
    internationalClass = '偏瘦'
elif 18.5 <= bmi < 24:
    internationalClass = '正常'
elif 24 <= bmi < 28:
    internationalClass = '偏胖'
else:
    internationalClass = '肥胖'

print('BMI值：{:.2f}\n国际BMI：{}\n国内BMI：{}'.format(bmi, internationalClass, inlandClass))
