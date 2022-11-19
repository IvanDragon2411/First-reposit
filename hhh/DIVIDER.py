result = []
def divider(a, b):
 if a < b:
  raise ValueError
 if b > 100:
  raise IndexError
 return a/b


data = {10: 2, 2: 5, "123": 4, 18: 0, 14: 15, 8: 4}
for key in data:
 try:
  res = divider(key, data[key])
 except ValueError:
  print('Число 1 не делитса на число 2')

 except IndexError:
  print('Число 2 > 100')


 except Exception as error:
  print('Что-то пошло не так')
 else:
  result.append(res)

print(result)