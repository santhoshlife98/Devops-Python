import requests, json
import sys
import os
import uuid

####################################### TOKEN GENERATION #######################################
token_url = "https://idp.xxxxx.xxxxx.com/sso/token"

redirect_uri = "http://localhost:5000"

authorization_code = raw_input('Enter the code: ')

data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': redirect_uri}
print "Requesting id token"

header = {
     "Content-Type":"application/json",
     "Authorization":"Basic xxxxxxx",
     "Accept":"application/json",
     "Accept-Charset":"UTF-8",
     "SVC.NAME":"xxxxxxx",
     "SVC.ENV":"xxx"
}

access_token_response = requests.post(token_url, json=data, headers=header)

#print access_token_response
print access_token_response.text

# we can now use the access_token as much as we want to access protected resources.
tokens = json.loads(access_token_response.text)
id_token = tokens['id_token']
print "#######################################################################################"
print "id token: " + id_token
print "#######################################################################################"
####################################### TOKEN GENERATION #######################################

####################################### TOKEN VALIDATION #######################################
validate_url = "https://idp.xxxxx.xxxxx.com/xxxx/token/validate"

iamdata = {'accessToken': id_token}

iamheader = {
     "Content-Type":"application/json",
     "Accept":"application/json",
     "Accept-Charset":"UTF-8"
}

iam_token_response = requests.post(validate_url, json=iamdata, headers=iamheader)

#print iam_token_response
#print iam_token_response.text

iamtoken = json.loads(iam_token_response.text)
iam_token = iamtoken['iamToken']
prinId = iamtoken['principalId']
uname = iamtoken['username']
print "#######################################################################################"
print "iam token: " + iam_token
print "#######################################################################################"
####################################### TOKEN VALIDATION #######################################

######################################### FIND ROLES ###########################################
role_url = "https://xxx.com/xxx/yyy/xxxx/role"

param = {
     "principalId": prinId,
     "realmId": "HomeOfficeRealm"
}

c = str(uuid.uuid1())

roleheader = {
     "Content-Type":"application/json",
     "Accept":"application/json",
     "Accept-Charset":"UTF-8",
     "WM_SVC.ENV":"stg",
     "WM_QOS.CORRELATION_ID":c
}

iam_role_response = requests.get(role_url, params=param, headers=roleheader)

#print iam_role_response
#print iam_role_response.text

print "#######################################################################################"
print uname.upper() + " " + "is part of following groups"
print "-----------------------------------------------"
roleresp = json.loads(iam_role_response.text)
for role in roleresp['payload']['dtoList']:
    print role['name']
print "#######################################################################################"
######################################### FIND ROLES ###########################################
