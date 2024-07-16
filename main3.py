import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head(20))
#присваиваем уникальные значения столбца whoAmI в переменную-список unique_values
unique_values=data['whoAmI'].unique() 
#создаем новую переменную-DataFrame со столбцами из списка unique_values c нулевыми значениями
one_hot_data=pd.DataFrame(data=0,index=data.index,columns=unique_values)
#перебираем по списку unique_values исходный DataFrame "data" и пишем в соответствующие ячейки 
# Dataframe "one_hot_data" значения "1" 
for value in unique_values:
    one_hot_data.loc[data['whoAmI']==value, value]=1
print('\n',one_hot_data)