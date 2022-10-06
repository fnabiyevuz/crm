# import requests
# import json
# url = "http://notify.eskiz.uz/api/message/sms/send-batch"
#
# payload = json.dumps({
#     "messages": [
#         {"user_sms_id": "1", "to": 998999002806, "text": "eto test"},
#         {"user_sms_id": "2", "to": 998999002806, "text": "eto test 2"}],
#     "from": "4546",
#     "dispatch_id": 123
# })
# headers = {
#     'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9ub3RpZnkuZXNraXoudXpcL2FwaVwvYXV0aFwvcmVmcmVzaCIsImlhdCI6MTYyMzE2MDQ2OCwiZXhwIjoxNjI1NzUyNDg2LCJuYmYiOjE2MjMxNjA0ODYsImp0aSI6Imo4eWJpREhmcFFwSHJCSFQiLCJzdWIiOjQ4NiwicHJ2IjoiODdlMGFmMWVmOWZkMTU4MTJmZGVjOTcxNTNhMTRlMGIwNDc1NDZhYSJ9.qm3UIr39aB1Xd14Ike_NgVEE5S3nES_5bHZPO-SDJ8s'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)

import requests

url = "http://notify.eskiz.uz/api/message/sms/send-batch"

payload = "{\r\n    \"messages\": [\r\n        {\"user_sms_id\":\"vash-sms-id-1\",\"to\": 998999002806, \"text\": \"eto test\"},\r\n        {\"user_sms_id\":\"vash-sms-id-2\",\"to\": 998999002806, \"text\": \"eto test 2\"}\r\n    ],\r\n    \"from\": \"4546\",\r\n    \"dispatch_id\": 123\r\n}"
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9ub3RpZnkuZXNraXoudXpcL2FwaVwvYXV0aFwvcmVmcmVzaCIsImlhdCI6MTYyMzE2MDQ2OCwiZXhwIjoxNjI1NzUyNDg2LCJuYmYiOjE2MjMxNjA0ODYsImp0aSI6Imo4eWJpREhmcFFwSHJCSFQiLCJzdWIiOjQ4NiwicHJ2IjoiODdlMGFmMWVmOWZkMTU4MTJmZGVjOTcxNTNhMTRlMGIwNDc1NDZhYSJ9.qm3UIr39aB1Xd14Ike_NgVEE5S3nES_5bHZPO-SDJ8s'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)