import requests as re

user_email = input("Please enter an email to find twitter account of: ")
print("\n ################################################### \n")
###########################################################################################################################################

####REQUEST 1###

url = "https://twitter.com/i/api/1.1/onboarding/task.json?flow_name=password_reset"
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
headers= {"Host":"twitter.com","Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA","X-Guest-Token":"1520620748909744130","Content-Length":"284"}

json = {"input_flow_data":{"requested_variant":"eyJwbGF0Zm9ybSI6IlJ3ZWIifQ==","flow_context":{"debug_overrides":{},"start_location":{"location":"manual_link"}}},"subtask_versions":{"contacts_live_sync_permission_prompt":0,"email_verification":1,"topics_selector":1,"wait_spinner":1,"cta":4}}

res = re.post(url,headers=headers,json=json)

#print(res.text)

flow_token = res.text.split('"flow_token":"')[1]
flow_token = flow_token.split('"')[0]
print("Flow token is: "+flow_token)

###########################################################################################################################################
####REQUEST 2###

url2= "https://twitter.com/i/api/1.1/onboarding/task.json"
headers2={"Host":"twitter.com","Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA","X-Guest-Token":"1520620748909744130","Content-Length":"810"}

json2={"flow_token":flow_token,"subtask_inputs":[{"subtask_id":"PwrJsInstrumentationSubtask","js_instrumentation":{"response":"{\"rf\":{\"ae449d12e1b1c679d368ba4b7de2602abfafb4b47c6cd59f23837950caa7843f\":252,\"a27a0b1e01bc5010abdcbd20a485288718fb12712143abe6b76d94bff5de3821\":174,\"ac783862866afe2c42a120cdbf546185795d40233ffe91fb6aad5b40de15b873\":-239,\"de9da9540e297f4e43f17b72ddc3ae7a323170f200afc9874788452dabbb3d7e\":86},\"s\":\"9ZQuIX2V-qDnQx8QPUzTU72RA378eIYKi3Ckhh0mnmYOW6o5YBscLKe8Lt6yKJdbGsi_JAoEiSdbFVjgkCjLy7K1wnuuC8Em2HX9rUodzJQOdvyYfK_7dUCgSYFrfjo6C9jBQI1M5HpqEt2jMrSEkFpphLEDvBCgjeJKBzTK60LsunIx70mZ_Pzu9pMZteqRp8vW-0kIR3JctNw6FlbbIeeFe-jzfFMBWW2jTheIQ_eHgKFZWjXRlW6DXOMk1zlyh-AZDQZweBHYnIzsqPkVeXIG3PAcz5u9NLZpRWtmqufam05amxtiQO9KvhfEy_T4Fn7l0M9WY4QuaXWNax1oQgAAAX-yhWUl\"}","link":"next_link"}}]}

res2 = re.post(url2,headers=headers2,json=json2)
#print(res2.text)

flow_token_2 = res2.text.split('"flow_token":"')[1]
flow_token_2 = flow_token_2.split('"')[0]

print(flow_token_2)
###########################################################################################################################################

####REQUEST 3###

url3 = "https://twitter.com/i/api/1.1/onboarding/task.json"

headers3 = {"Host":"twitter.com",
"X-Csrf-Token":"5a6bf4da2965d7dec5e21bfc76b00a0a",
"Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
"Content-Type":"application/json",
"X-Guest-Token":"1520620748909744130",
"Content-Length":"195"}

json3 = {"flow_token":flow_token_2,"subtask_inputs":[{"subtask_id":"PasswordResetBegin","enter_text":{"text":user_email,"link":"next_link"}}]}
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
res_3 = re.post(url3,headers=headers3,json=json3)

#print(res_3.text)
#(res_3.text)

if("Sorry, we could not find your account." in res_3.text):
    print("\nThere is no twitter account linked to this email!")
elif("You’ll need to wait before you can try again. We do this when we notice suspicious activity.\n\nGet help with account access issues."):
    print("\nOops! Wait for sometime...")
else:
    print("\nThere exists an account linked with this email")
