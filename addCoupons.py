import requests
import json
import time

coupons = []
add_coupons = []
cookies = {
  
}

headers = {
    'User-Agent': 'krogerco/55.0/iOS',
    'User-Time-Zone': 'America/Chicago',
    'X-Correlation-Id': '',
    'X-KROGER-TENANT': 'kroger',
    'X-KROGER-CHANNEL': 'MOBILE;IOS',
    'Accept-Language': 'en-US;q=1',
    'Authorization': '',
    'X-ApplicationAuthorizationToken':  '',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-LAF-OBJECT':'' ,

}

response = requests.get('https://mobile.kroger.com/mobilecoupons/api/v1/coupons/browse', headers=headers, cookies=cookies)
if response.status_code == 200:
    coupons.append(response.json())
    for i in coupons:
        if 'data' in i:
            for j in i['data']['categories']:
                if 'coupons' in j:
                    for k in j['coupons']:
                        add_coupons.append(k['id'])
else:
    print("Failed to retrieve coupons from Kroger API. Status code: " + str(response.status_code) + " Response: " + response.json()['error'])





for clip in add_coupons:
    headers = {
        'User-Agent': 'krogerco/55.0/iOS',
        'User-Time-Zone': 'America/Chicago',
        'X-Correlation-Id': '',
        'X-KROGER-TENANT': 'kroger',
        'X-KROGER-CHANNEL': 'MOBILE;IOS',
        'Accept-Language': 'en-US;q=1',
        'Authorization': '',
        'X-ApplicationAuthorizationToken':  '',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-LAF-OBJECT':'' ,

    }
    data = '{"action":"CLIP","couponId":"'+clip+'"}'
    dump_data = json.loads(data)

    response = requests.post('https://mobile.kroger.com/mobileatlas/v1/savings-coupons/v1/clip-unclip', headers=headers, cookies=cookies, data=data)
    print(response.text)
    if response.status_code == 200:
        print("Successfully clipped coupon " + clip)
        time.sleep(1)
    else:
        print("Failed to clip coupon " + clip)
