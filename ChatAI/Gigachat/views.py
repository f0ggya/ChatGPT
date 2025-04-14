from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import requests, json

def home(request):
    return render(request, 'home.html')

@require_http_methods(['POST'])
@csrf_exempt
def send_message(request):
    data = json.loads(request.body)
    prompt = data['prompt']
    url = 'https://gigachat.devices.sberbank.ru/api/v1/chat/completions'
    s = requests.Session()

    headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.qpY5Hlpts6uoOL2T9YQ1zJbSUKBwDdVShxvmOkgcg3H8wi6vLMqwIVJia8dL6MvqqMM87ivwDlIHS9OMtUe7BBqYBhq0tYiF8WAHeSAaE5EqRViEs-UQZiTLxBLO7RRmdu6BzkUSoxSdBx8DDShRkM37zZWbkcat7ecJBpABwD6O6mHiFoI8QeA15WJErxmOlZSq0WXOktkmEVR3j6MA3kpYNiJXWPUZnSPgwx0MfU31bdPBPOI5xQezrDf3tumeaTGY9lzf-kXn0j7hXMvIli9ofb-1hJNJbOsiHd1oLzrS9bZIdQEqmmxK4hygmghV4LfXw-Bwr4iafOSl7Tp35w.t3EzL7nGM1QncqihEOXSwg.NCvIizDr1e2ZQcWvd1lZbMvZZrHr23NKtC6QKov0CjlyeV-8SOOSTdxPcM4Qm7QsSygoAfpYRkUgAnGdaBB9DR78m9X4QbRrwI2y2tCt_IdTcbgIoVMfR9Hid2t6qsctGGqY9yDlSvMGV7x6mu7N6m6juB7YQFINIcIR3g753g6CGR2ZhXbiPmIhfsD7U4NZZEZfv9LwQ0Cmw-Q6L2iVxN4zGZw6DD1HZlLHY1YVLcgQubZVOIY0ac551RwZ_z1XNqMZHca1pmahzU1ATh3A_BODVydDDTKppAxMmH44QzcnxV9_ZtnwSrl-HDnwei5jB29a2S8n2x6eOE8RaL6EPqc2LSkmjBOFIOAbAQjMCSiSiWprP7gWI922J8JrN-6ipB5hpdRsfZT7PPG_KzWhLAsYT23ogoMK_Hskwr_aWPBRL6HYj_ctQX6PkUYa_46EMhLrrIIFHL6YP3oEaNO1CP9JT_wZK8CKrJ2xB-GPHgvtI2XxRW9YPVaM35TbeFT-4RtwXmkoQycyw7IWnbJzTua2LAxcpbEX-CfjaIyl8uNeBqmD-mzuF1tOKArl9Gop05SebbXd7AC9LKgy__OjWZfgUA79Y1aSVOquEmSdG1BpccbO20z4EUJV4NX7xgyJTXjGD6ncrWTMheia-stwLFgBkSHZ-tqDkXY8VOrPwMsmx2KEKCQaSZFc-OCPMgIFZc3Buv0rtbbudY0k4EntSRQM-zyJ1yIe133JGn8nPBw.LLQM54DJ_5n9wXsb6NfwhwIlE1kMgaKmLii_1nU7v_I',
    'Content-Type': 'application/json'
    }
    payload ={
        "model": "GigaChat",
        "messages": [
           
        {
        "role": "user",
        "content": prompt
        }
        ],
        "stream": False,
        "repetition_penalty": 1
    }
    r = s.post(url, headers=headers, data=json.dumps(payload), verify=False)
    return HttpResponse(r.content)