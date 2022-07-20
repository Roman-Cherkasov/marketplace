import requests

# # GET
response_get = requests.get('http://127.0.0.1:5000/get_user_data')
print("get_result =", response_get.status_code)


# POST
# requests.post('http://127.0.0.1:5000/registration', data={key: value}, json={key: value}, args)
json = {
    'login': 'master_yoda',
    'password': 'Do_or_do_not._There_is_no_try'
}
json2 = {
    'login': 'batman',
    'password': 'nananana'
}

# response_post = requests.post(
#     'http://127.0.0.1:5000/registration',
#     json=json2
# )

# print("post_result =", response_post.status_code)
# print("post_result =", response_post.status_code)



# if res:
#     print('Response OK')
# else:
#     print('Response Failed')
# print(res.status_code)
# print(res.text)
