my_dyct = {'Илья':1990 , 'Кирилл' : 1987, 'Вася': 1967, 'Федя': 1976}
print('База с датами рождения',my_dyct)
print('Год рождения Кирилла',(my_dyct.get('Кирилл')))
print('Катя -',(my_dyct.get('Катя', 'Такого имени нет')))
my_dyct.update({'Катя':1995, 'Юля': 1992})
print('обновленная база',my_dyct)
t=my_dyct.pop('Вася')
print('Самый возрастной был Вася, рожденный в ',t, 'году. Он удален из списка')
print ('обновленная база данных',my_dyct)

my_set = {0,1,1,0,'Tomato', 2, 'Tomato', 2.567, 'True', 'False'}
print(my_set)
my_set.update({'Морковка', 'Манго', 346})
print(my_set)
my_set.discard('Tomato')
print(my_set)