# import requests

# url = "https://gigachat.devices.sberbank.ru/api/v1/models"

# payload={}
# headers = {
#   'Accept': 'application/json',
#   'Authorization': 'Bearer eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.qpY5Hlpts6uoOL2T9YQ1zJbSUKBwDdVShxvmOkgcg3H8wi6vLMqwIVJia8dL6MvqqMM87ivwDlIHS9OMtUe7BBqYBhq0tYiF8WAHeSAaE5EqRViEs-UQZiTLxBLO7RRmdu6BzkUSoxSdBx8DDShRkM37zZWbkcat7ecJBpABwD6O6mHiFoI8QeA15WJErxmOlZSq0WXOktkmEVR3j6MA3kpYNiJXWPUZnSPgwx0MfU31bdPBPOI5xQezrDf3tumeaTGY9lzf-kXn0j7hXMvIli9ofb-1hJNJbOsiHd1oLzrS9bZIdQEqmmxK4hygmghV4LfXw-Bwr4iafOSl7Tp35w.t3EzL7nGM1QncqihEOXSwg.NCvIizDr1e2ZQcWvd1lZbMvZZrHr23NKtC6QKov0CjlyeV-8SOOSTdxPcM4Qm7QsSygoAfpYRkUgAnGdaBB9DR78m9X4QbRrwI2y2tCt_IdTcbgIoVMfR9Hid2t6qsctGGqY9yDlSvMGV7x6mu7N6m6juB7YQFINIcIR3g753g6CGR2ZhXbiPmIhfsD7U4NZZEZfv9LwQ0Cmw-Q6L2iVxN4zGZw6DD1HZlLHY1YVLcgQubZVOIY0ac551RwZ_z1XNqMZHca1pmahzU1ATh3A_BODVydDDTKppAxMmH44QzcnxV9_ZtnwSrl-HDnwei5jB29a2S8n2x6eOE8RaL6EPqc2LSkmjBOFIOAbAQjMCSiSiWprP7gWI922J8JrN-6ipB5hpdRsfZT7PPG_KzWhLAsYT23ogoMK_Hskwr_aWPBRL6HYj_ctQX6PkUYa_46EMhLrrIIFHL6YP3oEaNO1CP9JT_wZK8CKrJ2xB-GPHgvtI2XxRW9YPVaM35TbeFT-4RtwXmkoQycyw7IWnbJzTua2LAxcpbEX-CfjaIyl8uNeBqmD-mzuF1tOKArl9Gop05SebbXd7AC9LKgy__OjWZfgUA79Y1aSVOquEmSdG1BpccbO20z4EUJV4NX7xgyJTXjGD6ncrWTMheia-stwLFgBkSHZ-tqDkXY8VOrPwMsmx2KEKCQaSZFc-OCPMgIFZc3Buv0rtbbudY0k4EntSRQM-zyJ1yIe133JGn8nPBw.LLQM54DJ_5n9wXsb6NfwhwIlE1kMgaKmLii_1nU7v_I'
# }

# response = requests.request("GET", url, headers=headers, data=payload, verify=False)

# print(response.text)
import requests
import json
#NGRkMThmZjItYTExYi00NjU0LWI1NzYtOTY3YTA4MzI5ZjRhOjJkNWVjYzQ5LWQ1YjctNDNiMy1iMmYwLTdlZTE5YjdlMmU0OQ==

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload={
  'scope': 'GIGACHAT_API_PERS'
}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'RqUID': '7101aae4-1b8c-42bf-ba7b-e2469856888e',
  'Authorization': 'Basic NGRkMThmZjItYTExYi00NjU0LWI1NzYtOTY3YTA4MzI5ZjRhOjJkNWVjYzQ5LWQ1YjctNDNiMy1iMmYwLTdlZTE5YjdlMmU0OQ=='
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
access_token = json.loads(response.text)['access_token']
print(response.text)

# url = 'https://gigachat.devices.sberbank.ru/api/v1/chat/completions'
# s = requests.Session()

# headers = {
#   'Accept': 'application/json',
#   'Authorization': 'Bearer eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.qpY5Hlpts6uoOL2T9YQ1zJbSUKBwDdVShxvmOkgcg3H8wi6vLMqwIVJia8dL6MvqqMM87ivwDlIHS9OMtUe7BBqYBhq0tYiF8WAHeSAaE5EqRViEs-UQZiTLxBLO7RRmdu6BzkUSoxSdBx8DDShRkM37zZWbkcat7ecJBpABwD6O6mHiFoI8QeA15WJErxmOlZSq0WXOktkmEVR3j6MA3kpYNiJXWPUZnSPgwx0MfU31bdPBPOI5xQezrDf3tumeaTGY9lzf-kXn0j7hXMvIli9ofb-1hJNJbOsiHd1oLzrS9bZIdQEqmmxK4hygmghV4LfXw-Bwr4iafOSl7Tp35w.t3EzL7nGM1QncqihEOXSwg.NCvIizDr1e2ZQcWvd1lZbMvZZrHr23NKtC6QKov0CjlyeV-8SOOSTdxPcM4Qm7QsSygoAfpYRkUgAnGdaBB9DR78m9X4QbRrwI2y2tCt_IdTcbgIoVMfR9Hid2t6qsctGGqY9yDlSvMGV7x6mu7N6m6juB7YQFINIcIR3g753g6CGR2ZhXbiPmIhfsD7U4NZZEZfv9LwQ0Cmw-Q6L2iVxN4zGZw6DD1HZlLHY1YVLcgQubZVOIY0ac551RwZ_z1XNqMZHca1pmahzU1ATh3A_BODVydDDTKppAxMmH44QzcnxV9_ZtnwSrl-HDnwei5jB29a2S8n2x6eOE8RaL6EPqc2LSkmjBOFIOAbAQjMCSiSiWprP7gWI922J8JrN-6ipB5hpdRsfZT7PPG_KzWhLAsYT23ogoMK_Hskwr_aWPBRL6HYj_ctQX6PkUYa_46EMhLrrIIFHL6YP3oEaNO1CP9JT_wZK8CKrJ2xB-GPHgvtI2XxRW9YPVaM35TbeFT-4RtwXmkoQycyw7IWnbJzTua2LAxcpbEX-CfjaIyl8uNeBqmD-mzuF1tOKArl9Gop05SebbXd7AC9LKgy__OjWZfgUA79Y1aSVOquEmSdG1BpccbO20z4EUJV4NX7xgyJTXjGD6ncrWTMheia-stwLFgBkSHZ-tqDkXY8VOrPwMsmx2KEKCQaSZFc-OCPMgIFZc3Buv0rtbbudY0k4EntSRQM-zyJ1yIe133JGn8nPBw.LLQM54DJ_5n9wXsb6NfwhwIlE1kMgaKmLii_1nU7v_I',
#   'Content-Type': 'application/json'
# }

# payload ={
#     "model": "GigaChat",
#     "messages": [
#         {'content': 'Мяч, в зависимости от вида спорта, может иметь разную форму. Например:\n\n1. **Футбольный мяч** — имеет сферическую форму с покрышкой из синтетической кожи и наполнителем из латексной пены или полиуретана.\n2. **Волейбольный мяч** — также сферический, но обычно имеет более мягкую покрышку и меньший вес по сравнению с футбольным.\n3. **Баскетбольный мяч** — сферический, но с покрышкой из кожи или синтетического материала и внутренним наполнением из резины или бутила.\n4. **Теннисный мяч** — чаще всего имеет форму, близкую к сферической, но с более мягкой поверхностью и более плотным наполнителем.\n\nОднако, в целом, мячи имеют форму, близкую к сферической, так как это обеспечивает наилучшую аэродинамику и удобство игры.', 'role': 'assistant'},
#     {
#       "role": "user",
#       "content": "Сократи прошлый ответ"
#     }
#     ],
#     "stream": False,
#     "repetition_penalty": 1
# }

# r = s.post(url, headers=headers, data=json.dumps(payload), verify=False)

# data = json.loads(r.content)
# answer = data['choices'][0]['message']['content']
# add_to_messages = data['choices'][0]['message']

# print(answer)
# print(add_to_messages)