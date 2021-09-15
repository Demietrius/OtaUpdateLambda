import json
import os

from unittest import TestCase

import boto3

from Ota import app, s3_accessor


class test_handler(TestCase):

    def test_lambda_handler(self):
        payload = {
            "resource": "/insert",
            "path": "/insert",
            "httpMethod": "POST",
            "headers": {
                "Accept-Encoding": "gzip",
                "CloudFront-Forwarded-Proto": "https",
                "CloudFront-Is-Desktop-Viewer": "false",
                "CloudFront-Is-Mobile-Viewer": "true",
                "CloudFront-Is-SmartTV-Viewer": "false",
                "CloudFront-Is-Tablet-Viewer": "false",
                "CloudFront-Viewer-Country": "US",
                "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
                "Host": "y59u0xig10.execute-api.us-east-1.amazonaws.com",
                "User-Agent": "Dalvik/1.6.0 (Linux; U; Android 10670; Labconco FreeezeZone Build/KTU84P)",
                "Via": "1.1 0b5289ed31b336bd635023da029aaff0.cloudfront.net (CloudFront)",
                "X-Amz-Cf-Id": "moDIzKAUtmk4FwSqedoTCamT0snQRsetPF9tlNrqMGDwl0olGlkpvA==",
                "X-Amzn-Trace-Id": "Root=1-6115462e-5fd048065a142c180fb1d36e",
                "X-Forwarded-For": "12.43.13.254, 130.176.67.69",
                "X-Forwarded-Port": "443",
                "X-Forwarded-Proto": "https"
            },
            "multiValueHeaders": {
                "Accept-Encoding": [
                    "gzip"
                ],
                "CloudFront-Forwarded-Proto": [
                    "https"
                ],
                "CloudFront-Is-Desktop-Viewer": [
                    "false"
                ],
                "CloudFront-Is-Mobile-Viewer": [
                    "true"
                ],
                "CloudFront-Is-SmartTV-Viewer": [
                    "false"
                ],
                "CloudFront-Is-Tablet-Viewer": [
                    "false"
                ],
                "CloudFront-Viewer-Country": [
                    "US"
                ],
                "Content-Type": [
                    "application/x-www-form-urlencoded;charset=utf-8"
                ],
                "Host": [
                    "y59u0xig10.execute-api.us-east-1.amazonaws.com"
                ],
                "User-Agent": [
                    "Dalvik/1.6.0 (Linux; U; Android 10670; Labconco FreeezeZone Build/KTU84P)"
                ],
                "Via": [
                    "1.1 0b5289ed31b336bd635023da029aaff0.cloudfront.net (CloudFront)"
                ],
                "X-Amz-Cf-Id": [
                    "moDIzKAUtmk4FwSqedoTCamT0snQRsetPF9tlNrqMGDwl0olGlkpvA=="
                ],
                "X-Amzn-Trace-Id": [
                    "Root=1-6115462e-5fd048065a142c180fb1d36e"
                ],
                "X-Forwarded-For": [
                    "12.43.13.254, 130.176.67.69"
                ],
                "X-Forwarded-Port": [
                    "443"
                ],
                "X-Forwarded-Proto": [
                    "https"
                ]
            },
            "queryStringParameters": 'null',
            "multiValueQueryStringParameters": 'null',
            "pathParameters": 'null',
            "stageVariables": 'null',
            "requestContext": {
                "resourceId": "lxquum",
                "resourcePath": "/insert",
                "httpMethod": "POST",
                "extendedRequestId": "D9fnSEIpoAMF6Ww=",
                "requestTime": "12/Aug/2021:16:02:54 +0000",
                "path": "/Prod/insert",
                "accountId": "884775804250",
                "protocol": "HTTP/1.1",
                "stage": "Prod",
                "domainPrefix": "y59u0xig10",
                "requestTimeEpoch": 1628784174491,
                "requestId": "843d88b5-5108-4e14-8dfc-9a36bc940449",
                "identity": {
                    "cognitoIdentityPoolId": 'null',
                    "accountId": 'null',
                    "cognitoIdentityId": 'null',
                    "caller": 'null',
                    "sourceIp": "12.43.13.254",
                    "principalOrgId": 'null',
                    "accessKey": 'null',
                    "cognitoAuthenticationType": 'null',
                    "cognitoAuthenticationProvider": 'null',
                    "userArn": 'null',
                    "userAgent": "Dalvik/1.6.0 (Linux; U; Android 10670; Labconco FreeezeZone Build/KTU84P)",
                    "user": 'null'
                },
                "domainName": "y59u0xig10.execute-api.us-east-1.amazonaws.com",
                "apiId": "y59u0xig10"
            },
            "body": {
                "commonParams": {
                    "view": "OTA",
                    "action": "READ",
                    "transactionId": "r339fd9"
                },
                "request": {
                    "fileName": "WA_APP_FS_vH_steris.LCC"
                }
            }
        }

        ret = app.lambda_handler(payload, "")

        assert ret["statusCode"] == 200
        assert "message" in ret["body"]
        # assert "location" in data.dict_keys()

    def test_s3(self):
        s3 = boto3.resource('s3', region_name="us-east-1")

        # bucket = 'charterandgoreplaymessages'    # name of the s3 bucket
        bucket = "ota-software-storage"
        file_key = "2021/WA_APP_FS_vH_steris.LCC"

        object = s3.Object(bucket, file_key)
        body = object.get()["Body"].read()

        pass
