import json

import requests

print("************************************GET****************************************************")
'''resp = requests.get("https://reqres.in/api/users?page=2")
# get response
print(resp.status_code)
respCode = resp.status_code
assert respCode == 200, "Expected response code is 200"
print(resp.json())'''

#print(resp.text)
#print(resp.content)
#print(resp)
#print(type(resp))
#print(dir(resp))

# Validate response
resp = requests.get("https://reqres.in/api/users?page=2")
print(resp.json())
jasonresp = resp.json()
print(jasonresp['total_pages'])
assert jasonresp['total_pages']==2, "total pages not matched"

print(jasonresp["data"][1]["email"])
assert (jasonresp["data"][1]["email"])
assert (jasonresp["data"][1]["email"]).endswith("@reqres.in"), "Email format is wrong"
assert (jasonresp["data"][1]["email"]).startswith("lindsay"), "Wrong email id "
print(jasonresp["data"][3]["last_name"])
assert (jasonresp["data"][4]["id"])!= None,"id should not be null"
print(jasonresp["data"][2]["first_name"])
assert (jasonresp["data"][2]["first_name"])!= None,"first_name should be null"
print(jasonresp["support"]["url"])

print("************************************POST****************************************************")

dictionary ={
    "name": "Bansari",
    "job": "QA Engineer"
}
resp = requests.post("https://reqres.in/api/users",data=dictionary)
print(resp)
print(resp.json())
print(resp.json()['createdAt'])
assert resp.json()['name'] == 'Bansari'
assert resp.json()['id'] != None

print("***************PASS jason through file dynemically*****************")

dictdata = open("data.json","r").read()
resp = requests.post("https://reqres.in/api/users",data=json.loads(dictdata))
print(resp)
print(resp.json())
print(resp.json()['id'])
assert resp.json()['name'] == 'Bansari'
assert resp.json()['id'] != None
print(resp.headers)
print(resp.headers.get("Content-Type"))

print("***************POST generates token*****************")

dictionary ={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

resp = requests.post("https://reqres.in/api/register",data=dictionary)
print(resp)
print(resp.json())
print(resp.json()['token'])


print("************************************PUT****************************************************")
dictionary ={
    "name": "morpheus",
    "job": "zion resident"
}

resp = requests.put("https://reqres.in/api/users/2",data=dictionary)
print(resp)
print(resp.json())
print(resp.json()['job'])
assert resp.json()['job'] == 'zion resident'

print("************************************PATCH****************************************************")
dictionary ={
    "job": "QA Engineer"
}

resp = requests.put("https://reqres.in/api/users/2",data=dictionary)
print(resp)
print(resp.json())
print(resp.json()['job'])
assert resp.json()['job'] == 'QA Engineer'

print("************************************DELETE****************************************************")

resp = requests.delete("https://reqres.in/api/users/3")
print(resp.status_code)
assert resp.status_code == 204, "Deletion Failed"

print("************************************Delayed response****************************************************")

resp = requests.get("https://reqres.in/api/users?delay=2")
print(resp.status_code)

print("************************************Authentication****************************************************")

resp = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=('admin','admin'))
print(resp.status_code)
assert resp.status_code == 200, "Authentication Failed"


URL = ''
token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImR"
headers = {'Authorization': "Bearer {}".format(token)}
response = requests.post(URL, headers=headers)
print(response.json())




