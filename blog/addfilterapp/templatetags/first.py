from django import template

register = template.Library() # Создаём функцию для подключения шаблонов

def capitalize(inputstr): # Имитируем фильтр шаблола capfirst
    return inputstr.capitalize()

def supertxt(inputstr): # Чтобы "главная страница" фильтр изменял в "ГлАвНаЯ СтРаНиЦа"
    '''
    result = []
    for i in range(len(inputstr)):
        letter = inputstr[i]
        if i % 2 == 0:
            letter = letter.upper()
        result.append(letter)
    return ''.join(result)
    или так:'''
    return ''.join([sign.upper() if i % 2 == 0 else sign for i, sign in enumerate(inputstr)])

register.filter('capitalize', capitalize)
register.filter('sup', supertxt)