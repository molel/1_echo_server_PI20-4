# Лабораторная работа "Эхо-сервер" по Практикуму по программированию

### Цель работы

Познакомиться с приемами работы с сетевыми сокетами в языке программирования Python.

### Задания для самостоятельного выполнения

1. Модифицируйте код сервера таким образом, чтобы при разрыве соединения клиентом он продолжал слушать данный порт и, таким образом, был доступен для повторного подключения.

![screenshot](/screenshots/1.png)

2. Модифицируйте код клиента и сервера таким образом, чтобы номер порта и имя хоста (для клиента) они спрашивали у пользователя. Реализовать безопасный ввод данных и значения по умолчанию.

![screenshot](/screenshots/2.png)

3. Модифицировать код сервера таким образом, чтобы все служебные сообщения выводились не в консоль, а в специальный лог-файл.

![screenshot](/screenshots/3.png)

4. Модифицируйте код сервера таким образом, чтобы он автоматически изменял номер порта, если он уже занят. Сервер должен выводить в консоль номер порта, который он слушает.

![screenshot](/screenshots/4.png)

5. Реализовать сервер идентификации. Сервер должен принимать соединения от клиента и проверять, известен ли ему уже этот клиент (по IP-адресу). Если известен, то поприветствовать его по имени. Если неизвестен, то запросить у пользователя имя и записать его в файл. Файл хранить в произвольном формате.
6. Реализовать сервер аутентификации. Похоже на предыдущее задание, но вместе с именем пользователя сервер отслеживает и проверяет пароли. Дополнительные баллы за безопасное хранение паролей. Дополнительные баллы за поддержание сессии на основе токена наподобие cookies

![screenshot](/screenshots/5-6.1.png)
![screenshot](/screenshots/5-6.2.png)
![screenshot](/screenshots/5-6.3.png)


7. Напишите вспомогательные функции, которые реализуют отправку и принятие текстовых сообщений в сокет. Функция отправки должна дополнять сообщение заголовком фиксированной длины, в котором содержится информация о длине сообщения. Функция принятия должна читать сообщение с учетом заголовка. В дополнении реализуйте преобразование строки в байтовый массив и обратно в этих же функциях. Дополнително оценивается, если эти функции будут реализованы как унаследованное расширение класса socket библиотеки socket.

![screenshot](/screenshots/7.png)

8. Дополните код клиента и сервера таким образом, чтобы они могли посылать друг другу множественные сообщения один в ответ на другое.

![screenshot](/screenshots/8.png)


## Контрольные вопросы
1. Чем отличаются клиентские и серверные сокеты?
Клиентские сокеты грубо можно сравнить с конечными аппаратами телефонной сети, а серверные — с коммутаторами

2. Как можно передавать через сокеты текстовую информацию?
С помощью преобразования текстовый переменных в массив байтов

3. Какие операции с сокетами блокируют выполнение программы?
  a. Операция ввода
  b. Выходная отправки
  c. Принять соединение
  d. Операция исходящего соединения

4. Что такое неблокирующие сокеты?
В случае неблокирующих сокетов функция чтения проверяет, есть ли данные в буфере, и если есть - сразу возвращает, если нет, то она не ждет и также сразу возвращает, что прочитано 0 байт.

5. В чем преимущества и недостатки использования TCP по сравнению с UDP?
  a. Надежность: в этом случае предпочтительнее будет протокол TCP, за счет подтверждения получения данных, повторной отправки в случае необходимости, а также использованию такого инструмента как тайм-аут. Протокол UDP такого инструментария не имеет, а потому при получении отправленные данные могут приходить не полностью;
  b. Упорядоченность: опять будет предпочтительнее TCP, поскольку этот протокол гарантирует передачу пакетов данных именно в том порядке, в котором они были отправлены. В случае с UDP такой порядок не соблюдается;
  c. Скорость: здесь уже лидировать будет UDP, так как более тяжеловесному TCP-протоколу будет требоваться больше времени для установки соединения, подтверждения получения, повторной отправки данных и т.д. ;
  d. Метод передачи данных: в случае с TCP данные передаются потоково, границы фрагментов данных не имеют обозначения. В случае с UDP данные передаются в виде датаграмм – проверка пакетов на целостность осуществляется принимающей стороной только в случае получения сообщения. Также пакеты данных имеют определенные обозначения границ;

6. Какие системные вызовы, связанные с сокетами используются только на стороне сервера?
  a. socket
  b. bind
  c. listen
  d. accept

7. На каком уровне модели OSI работают сокеты?
Когда мы создаем сокет (socket - гнездо), мы получаем возможность доступа к нужному нам уровню OSI. Ну а дальше мы можем использовать соответствующие вызовы для взаимодействия с ним. Сокеты устроены таким образом, что они могут взаимодействовать с ОС на любом уровне OSI, скрывая ту часть реализации, которой мы не интересуемся

