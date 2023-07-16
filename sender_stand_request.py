import configuration
import requests

#Тренажер GET-запрос
#Задание 1
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

#response = get_docs()
#print(response.status_code)

#Задание 2
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)
response = get_logs()
#print(response.status_code)
#print(response.headers)

#Задание 4
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count": 20})
#response = get_logs()
#print(response.status_code)
#print(response.headers)

#Задание 5
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
#response = get_users_table()
#print(response.status_code)

# POST-запрос
import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки
#response = post_new_user(data.user_body);
#print(response.status_code)
#print(response.json()) #Задание 1

#Задание 2
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids,
                            headers=data.headers)

#response = post_products_kits(data.product_ids);
#print(response.status_code)
#print(response.json())














