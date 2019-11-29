import json
from botocore.vendored import requests
import os
import ssl

DSSC_URL = "https://" + os.environ['DSSC_URL']
DSSC_USER = os.environ['DSSC_USER']
DSSC_PSW = os.environ['DSSC_PSW']
AWS_ECR_ACCESS = os.environ['AWS_ECR_ACCESS']
AWS_ECR_SECRET = os.environ['AWS_ECR_SECRET']
scan_id = 'v1'


def get_token(userid, password):
    # print("----- Generating Token ----- "+userid)
    payload = {'user': {'userID': DSSC_USER, 'password': DSSC_PSW}}
    
    r = requests.post(DSSC_URL + '/api/sessions', json=payload, verify=False)
    # print(r)
    z = json.loads(r.text)
    # print(z['token'])
    return z


def get_scan(token, id):
    # print("----- Get Scan Data for "+id+" -----")
    headers = {
        'authorization': "Bearer " + token,
        'content-type': "application/json",
    }
    r = requests.get(DSSC_URL + '/api/scans/' + id, headers=headers, verify=False)

    x = json.loads(r.text)
    # print(x['id'])


def generate_request(token, SCAN_REGISTRY, SCAN_REPOSITORY, SCAN_TAG, AWS_REGION):
    # print("----- Generating Request -----")
    payload = {}
    if scan_id:
        # print("scan ID Not Empty ")
        payload['id'] = scan_id

    payload['name'] = "Event Based trigger from AWS ECR"
    payload['source'] = {}
    payload['source']['credentials'] = {}
    payload['source']['credentials']['aws'] = {}
    payload['source']['type'] = "docker"
    payload['source']['registry'] = SCAN_REGISTRY
    payload['source']['repository'] = SCAN_REPOSITORY
    payload['source']['tag'] = SCAN_TAG
    payload['source']['credentials']['aws']['region'] = AWS_REGION
    payload['source']['credentials']['aws']['accessKeyID'] = AWS_ECR_ACCESS
    payload['source']['credentials']['aws']['secretAccessKey'] = AWS_ECR_SECRET
    # print(payload)
    headers = {
        'authorization': "Bearer " + token,
        'content-type': "application/json",
    }
    r = requests.post(DSSC_URL + '/api/scans', json=payload, headers=headers, verify=False)

    # print(r)
    x = json.loads(r.text)
    # print(x)
    print(x['id'])
    return x['id']


def lambda_handler(event, context):
    print(event)
    # TODO implement

    if str(event['detail']['action-type']) == 'PUSH':
        SCAN_REGISTRY = str(event['account']) + ".dkr.ecr." + str(event['region']) + ".amazonaws.com"
        SCAN_REPOSITORY = str(event['detail']['repository-name'])
        SCAN_TAG = str(event['detail']['image-tag'])
        AWS_REGION = str(event['region'])
        token = get_token(DSSC_USER, DSSC_PSW)

        scan_id = generate_request(token['token'], SCAN_REGISTRY, SCAN_REPOSITORY, SCAN_TAG, AWS_REGION)
        get_scan(token['token'], scan_id)

    print("scan completed")