'''
Основные запросы:
all, get, filter
Фильтры:
1. С одним параметром filter
Post.objects.filter(name='Пост про уров')
2. Все, но с исключением exclude
Post.objects.exclude(name='Пост про уров')
3. С несколькими параметрами
Post.objects.filter(
        name='Пост про уров',
        text='Уроды бывают разные, особенно конченные, так вот один из них такой'
        )
4. Можно применять любые запросы к полученному QuerySet последовательно через переменные
u = Post.objects.filter(name='Пост про уров')
some = u.filter(text='Уроды бывают разные, особенно конченные, так вот один из них такой')
или в одну строку:
Post.objects.filter(name='Пост про уров').filter(text='Уроды бывают разные, особенно конченные, так вот один из них такой')
Post.objects.filter(name='Пост про уров').exclude(text='Текстик, которого нет')

Сложные фильтры
1. Со сравнением
Найти все посты с рейтингом больше трёх
Post.objects.filter(rating__gt=3)
Найти все посты с рейтингом меньше трёх
Post.objects.filter(rating__lt=3)
Найти все посты с рейтингом больше или равно трём
Post.objects.filter(rating__gte=3)
Найти все посты с рейтингом меньше или равно трём
Post.objects.filter(rating__lte=3)
2. Посты с рейтингом 2 или 3
Post.objects.filter(rating__gte=2, rating__lte=3)
или:
Post.objects.filter(rating__in=[2,3])
3. Посты, текст которого начинается на "Уроды бывают ..."
Post.objects.filter(text__startswith='Уроды бывают')
4. Посты, в имени которых есть фрагмент "про"
Post.objects.filter(name__contains='про')
5. Посты с датой создания меньше какого-то
import datetime
some_date=datetime.datetime(year=2000, month=1, day=1)
Post.objects.filter(create__gt=some_date)
Ещё вариант с some_date
Post.objects.filter(create__in=[some_date])
или так
Post.objects.filter(create__year=2000, create__month=1, create__day=1)
ещё можно вот так
Post.objects.filter(create__year=2000, create__month=1, create__day__gt=1)

6. Запросы к связанным моделям
cat = Category.objects.get(name='Категорийцы')
Post.objects.filter(category=cat)
или
Post.objects.filter(category__name='Категорийцы')
Если имя категории начинается через 'Кат'
Post.objects.filter(category__name__startswith='Кат')
Если имя категории заканичивается через 'ых'
Post.objects.filter(category__name__endswith='ых')


'''