# Тестовое задание для greenatom 
# Разработка сервиса для загрузки медиа-файлов

Содержание
1. Общие положения	1
2. Требования к заданию	1
2.1. Общие требования	1
2.2. Функциональное описание	1


    1. Общие положения
Документ определяет тестовое задание для соискателя на вакансию стажер-разработчик Python.
    2. Требования к заданию
        2.1. Общие требования
Для разработки требуется использовать Python версии 3.6 и выше.
Приложение должно функционировать в среде ОС Linux (CentOS, Ubuntu, AstraLinux на усмотрение соискателя).
Требуется использовать библиотеку FastApi (https://fastapi.tiangolo.com).
В качестве базы данных следует использовать Postgres актуальной версии.
Требуется предоставить ссылку и доступ к репозиторию кода, к примеру GitHub.
        2.2. Функциональное описание
Требуется реализовать веб-сервис в соответствии с интерфейсом, определенным в таблице Таблица 1.

Название
Метод
Описание
/frame/
POST
На вход подаются изображения в формате jpeg. 
Количество передаваемых файлов может быть от 1 до 15.
Результат работы функции соответствует стандартному для HTTP коду.
Функция сохраняет переданные файлы в папку /data/<дата в формате YYYYMMDD>/ с именами <GUID>.jpg и фиксирует в базе данных в таблице inbox со структурой <код запроса> | <имя сохраненного файла> | <дата / время регистрации>
/frame/<код запроса>
GET
На вход подается код запроса.
На выходе возвращается список соответствующих коду запроса изображений в формате JSON, включая дату и время регистрации и имена файлов
/frame/<код запроса>
DELETE
На вход подается код запроса.
Функция удаляет данные по запросу из базы данных и соответствующие файлы изображений и папки /data/.
Опционально требуется реализовать аутентификацию веб-сервиса для ограничения доступа, к примеру, с применением OAuth.
