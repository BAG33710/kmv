# Коллекционные типы данных и циклы

## Аннотация

Данный проект позволит изучить такие коллекционные типы данных, как кортежи, списки, словари и множества, работу с ними, а также циклы while и for.


### Задание 1

Необходимо внутри  цикла **while** организовать всю работу. Для этого необходимо:
1. Задать лимит очереди - 4 человека.
2. Дать возможность до достижения лимита делать два действия:
- добавлять пациента в очередь;
- смотреть текущую очередь.
3. Очередь можно организовать через строку. Между собой людей можно разделять запятой с пробелом.
Например - `Иванов А.С., Петров К.В., Сидорова Г.У.`. Очередь пусть будет заканчиваться последним введенным пациентов в очередь, как в примере. Без добавления лишних знаков препинания.
4. Пусть пользователю до достижения лимита на каждой итерации цикла предлагается две опции для ввода с клавиатуры:
    ```
    ----
    Введите:
     - 1, если хотите добавить пациента в очередь;
     - 2, если хотите посмотреть текущую очередь.
    ----
    ```
   При этом пусть черточек будет штук 50, больше будет видно отделение инпутов от ввода.
5. При выборе опции 1 пусть пользователь вводит ФИО пациента, которого нужно добавить:
    ```
    Введите ФИО пациента: 
    ```
   После двоеточия пусть будет пробел, а то введенное ФИО будет слепляться.
6. При выборе опции 2 пусть пользователь видит текущую очередь в следующем виде (не забудь пробел после запятой):
    ```
    Текущая очередь - Иванов А.С., Петров К.В., Сидорова Г.У.
    ```
7. Когда лимит достигнут пусть пользователь видит сформировавшуюся очередь, как в пункте 6.
8. И еще пусть все выводы НЕ РАЗДЕЛЯЮТСЯ между собой лишней пустой строчкой, а идут друг за другом на следующей строчке.


### Задание 2

**break** - это кажется то, что тебе нужно для прерывания заполнения очереди. Что же нужно будет сделать дальше.

Последующие изменения/правки добавляются к предыдущему коду (то есть учитываются все пункты от 1 до 8 из Задания 1).
1. После ввода ФИО пациента с клавиатуры, нужно приводить его в следующий вид - первая буква фамилии, имени и отчества - должны быть с большой буквы,
в случае инициалов - большие буквы. Пример - Иванов Александр Сергеевич, Иванов А.С.
2. Добавить опцию 3 в ввод с клавиатуры:
    ```
    ...
     - 3, если хотите прекратить работу программы и посмотреть получившуюся очередь.
    ...
    ```
3. При выборе опции 3 пусть цикл прерывается и перед завершением программы показывается текущая очередь (см. пункт 6 Задания 1).
4. Если очередь была заполнена до лимита, то перед последним показом очереди пусть показывается фраза "Очередь наполнена!", а потом уже сама очередь:
    ```
    Очередь наполнена!
    Текущая очередь - Иванов А.С., Петров К.В., Сидорова Г.У., Киров А.А.
    ```
5. В случае, если очередь пустая, то каждый раз когда ее нужно вывести на экран, надо выводить фразу
   ```
   Очередь пустая!
   ```

P.S. Если программа завершена раньше заполнения лимита, то фразу "Очередь наполнена!" выводить не надо!

### Задание 3

Теперь необходимо заменить строки на **множества** и добавить новый функционал уже с учетом **множеств**. Нужно записать себе необходимые пункты и обязательно перечитать их **ВСЕ** перед тем, как приступать к решению.

1. Вместо строки нужно использовать **множество**. Надо не забыть поменять механизм добавления с учетом него.
2. Вместо счетчика в условии цикла использовать длину **множества**. То есть сравнивать с лимитом длину текущей очереди.
3. Добавить опцию для удаления в ввод с клавиатуры.
    ```
    ...
     - 1, если хотите добавить пациента в очередь;
     - 2, если хотите удалить пациента из очереди;
     - 3, если хотите посмотреть текущую очередь;
     - 4, если хотите прекратить работу программы и посмотреть получившуюся очередь.
    ...
    ```
4. В пункте выше удаление обозначено, как опция 2. В случае выбора опции 2, необходимо просить ввести ФИО пациента, которого необходимо удалить.
    ```
    Введите ФИО пациента, которого надо удалить из очереди: 
    ```
    После двоеточия нужно не забыть пробел.
5. Если такого пациента нет в очереди, то нужно выдать предупреждение пользователю:
    ```
    Такого пациента нет в очереди!
    ```
    Если же есть, то удалить из нее.
6. Остальной функционал нужно оставить таким же, как в предыдущем задании.
7. С учетом замены строки на множество вывод текущей очереди будет выглядеть следующим образом:
    ```
    Текущая очередь - {'Иванов А.С.', 'Петров К.В.', 'Сидорова Г.У.', 'Киров А.А.'}
    ```
    Править его не нужно!

### Задание 4

Кажется **список** уже можно использовать для добавления или удаления элементов по порядковому номеру в нем, для этого можно использовать **индексы**.
Пора зафиксировать для себя перечень дел. В этих заданиях главное не забывать перечитывать **ВСЕ** пункты перед выполнением.
1. Заменить **множество** на **список** и переписать весь функционал, связанный с добавлением и удалением из него. 
2. При выборе опции 1 (добавить пациента в очередь) необходимо спрашивать куда пользователь хочет добавить пациента - в конец или другую часть очереди:
    ```
    ----
    Введите:
     - 1, если хотите добавить пациента в конец очереди;
     - 2, если хотите добавить пациента в начало или середину очереди.
    ----
    ```
    2.1. После выбора ЛЮБОЙ подопции, необходимо запросить ФИО на добавление (при этом не забыть оставить обработку (корректность записи ФИО) из прошлого задания):
    ```
    Введите ФИО пациента: 
    ```
    2.2. Если такой пациент уже есть в очереди, то нужно выдавать фразу:
    ```
    Такой пациент уже есть в очереди!
    ```
    2.3. Если пациента нет в очереди и была выбрана подопция 1, то нужно просто добавить в конец очереди.\
    2.4. Если пациента нет в очереди и была выбрана подопция 2, то нужно спросить в какое место в очереди надо вставить пациента. При этом все пациенты с этого места и дальше сьедут вправо.
    ```
    Введите на какое место очереди хотите вставить пациента: 
    ```
    Надо не забыть, что порядковый номер и **индекс** все же не совсем одно и тоже.
3. При выборе опции 2 (удалить пациента из очереди) необходимо спрашивать, как пользователь хочет удалить - по ФИО или порядковому номеру:
    ```
    ----
    Введите:
     - 1, если хотите удалить пациента по ФИО;
     - 2, если хотите удалить пациента по его номеру в очереди.
    ----
    ```
    3.1. После выбора подопции 1, необходимо запросить ФИО на удаление (при этом обработку ФИО никто не отменял):
    ```
    Введите ФИО пациента: 
    ```
    3.2. Если такого пациента нет в очереди, то надо выдавать надпись (при этом программа не должна завершать работу):
    ```
    Такого пациента нет в очереди!
    ```
    3.3. После выбора подопции 2, необходимо запросить порядковый номер в очереди, который надо почистить:
    ```
    Введите порядковый номер человека в очереди: 
    ```
    3.4. Если такого порядкового номера нет в очереди, то нужно выдавать ту же фразу, как и в пункте 3.2., программа при этом должна продолжать работу.
4. Остальной функционал нужно оставить таким же, как в предыдущей версии кода (предыдущем задании).
5. С учетом замены множества на список вывод текущей очереди будет выглядеть следующим образом:
    ```
    Текущая очередь - ['Иванов А.С.', 'Петров К.В.', 'Сидорова Г.У.', 'Киров А.А.']
    ```
    Править его не нужно!

### Задание 5

Пора переходить на **словари**. 
Похоже нужно сделать следующее (при этом перед реализацией нужно будет прочитать **ВСЕ** пункты для общей картины):
1. Заменить **список** на **словарь** и переписать весь функционал, связанный с добавлением и удалением из него.
2. Не реализовывать старый функционал, лежащий под опциями 2 и 3 в Задании 4.
3. Теперь при выборе опции 1 (добавить пациента в очередь) необходимо спрашивать время и ФИО пациента, пусть пользователь вводит их через запятую и пробел.
(Подсказка метод **split** для строк.) Он должен помочь разделить время и ФИО. При этом также необходимо не забыть оставить обработку для ФИО. Пример инпута:
    ```
    Введите время и ФИО пациента (через запятую и пробел - "08:00, Иванов А.А."): 
    ```
    3.1. Если время уже есть в ключах словаря, то надо выдавать фразу:
    ```
    Это время уже занято!
    ```
    3.2. Если ФИО пациента уже есть в значениях словаря, то надо выдавать фразу:
    ```
    Такой пациент уже есть в очереди!
    ```
    3.3. В остальных случаях можно добавлять в словарь, **ключ** - время, **значение** - ФИО.
4. При выборе опции 2 (удалить пациента из очереди) необходимо спрашивать время, которое нужно очистить:
    ```
    Введите время пациента, которого нужно удалить из очереди (например, 08:00 или 10:15): 
    ```
    4.1. Если такого времени нет среди ключей, то нужно выдавать фразу
    ```
    Это время не занято!
    ```
    4.2. В остальных случаях удалять время и ФИО из словаря.
5. Остальной функционал нужно оставить таким же, как в предыдущей версии кода (в предыдущем задании).
6. С учетом замены списка на словарь вывод текущей очереди будет выглядеть следующим образом:
    ```
    Текущая очередь - {'08:00': 'Иванов А.С.', '09:15': 'Петров К.В.', '10:30': 'Сидорова Г.У.', '12:50': 'Киров А.А.'}
    ```
    Править его не нужно!

### Задание 6

Теперь необходимо добавить новый цикл **for** в опцию два. А если подробнее, то:
1. При выборе опции 2 (удалить пациента из очереди) необходимо спрашивать, как пользователь хочет удалить - по времени или ФИО:
    ```
    ----
    Введите:
     - 1, если хотите удалить пациента по времени;
     - 2, если хотите удалить пациента по ФИО.
    ----
    ```
    1.1. После выбора подопции 1, необходимо запросить время на удаление:
    ```
    Введите время пациента, которого нужно удалить из очереди (например, 08:00 или 10:15): 
    ```
    1.2. Если такого времени нет среди **ключей**, то нужно выдавать фразу:
    ```
    Это время не занято!
    ```
    1.3. После выбора подопции 2, необходимо запросить ФИО или часть ФИО на удаление (при этом регистр не должен иметь значение:
    ```
    Введите ФИО (или часть ФИО) пациентов, которых хотите удалить из очереди: 
    ```
    1.4. Далее нужно с помощью цикла **for** найти те **ключи**, в значения которых входит введенная часть. При этом регистр нужно не учитывать (Иванов и иванов - должны быть одним и тем же).\
    1.5. Если таких **ключей** найдено не было, то нужно выдавать фразу:  
    ```
    Таких пациентов нет в очереди!
    ```
    1.6. Если такие **ключи** найдены, то их нужно удалить вместе с их **значениями** из словаря.
2. Остальной функционал нужно оставить таким же, как в предыдущей версии кода (в предыдущем задании).



### Дополнительное задание


Предположим, в данный момент ты сконцентрирован на изучении 3 языков: латыни, английского и python.
Для тебя они сейчас находятся в одинаковом приоритете. И ты хочешь, чтобы программа рандомно сформировала тебе расписание - 
в какой день недели следующего месяца, что тебе изучать.

Ты накидываешь себе на листочке вид, в котором ты бы хотел видеть это расписание, получается следующее:
```
|    | Пн         | Вт     | Ср         | Чт     | Пт     | Сб         | Вс         |
|----|------------|--------|------------|--------|--------|------------|------------|
|  1 | Английский | Python | Английский | Отдых  | Латынь | Отдых      | Python     |
|  2 | Английский | Python | Английский | Python | Отдых  | Английский | Английский |
|  3 | Латынь     | Отдых  | Python     | Отдых  | Латынь | Отдых      | Латынь     |
|  4 | Отдых      | Python | Латынь     | Латынь | Латынь | Латынь     | Латынь     |
```

Как же это можно реализовать в питоне... А что если представить это в таком виде:
```python
[
    ['1', 'Английский', 'Python', 'Отдых', ...],
    ['2', 'Английский', 'Python', 'Отдых', ...],
    ['3', 'Латынь', 'Отдых', 'Python', ...],
    ['4', 'Отдых', 'Python', 'Латынь', ...],
]
```

> Если тебе нужно вывести список или список списков в красивом виде, то можно использовать сторонние библиотеки.
> Например, библиотеку **tabulate**. Изучи, как она работает, там можно выводить данные в разных красивых форматах.
> 
> P.S. Лучше всего подойдёт формат ***github***.



Выглядить это должно так, чтобы у тебя получилась фиксированная таблица, где кол-во строк равно всегда 4 (примерное кол-во недель в месяце), а столбцов всегда 7 (по дням недели).

Поэтому тебе необходимо:

1. Изучить, как работает модуль **tabulate**.
2. Сформировать список, состоящий из четырех списков, описывающих одну неделю, каждый из которых включает номер недели и 7 **рандомных** выборов из списка `['Латынь', 'Английский', 'Python', 'Отдых']`.
Кажется, что для этого можно использовать два вложенных цикла **for** и модуль **random**.
3. Используя модуль **tabulate** вывести данный список списков с заголовками на экран.
4. Список с заголовками дней недель следующий - `['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']`.
5. Назвать файл с кодом этого задания - *task_dop.py* и закинуть в папку *src/* .

