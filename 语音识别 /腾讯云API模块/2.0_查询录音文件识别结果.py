#通过上面两个文件的获取类似{"RequestId": "d33d2dd0-a3a6-4cfc-bb53-f33c754a13e3", "Data": {"TaskId": 737083613}}

#根据TaskId编码进行结果的查询

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models
try:
    #此处<Your SecretId><Your SecretKey>需要替换成客户自己的账号信息
    cred = credential.Credential("AKIDLSKLzxNoNgnhR0jEyRfcIn7JGyThDNzP", "MUEl25tfDoKfy70ddXIm0FI8iy54nJhq")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "asr.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = asr_client.AsrClient(cred, "ap-shanghai", clientProfile)

    req = models.DescribeTaskStatusRequest()
    params = '{"TaskId":737083613}'
    req.from_json_string(params)

    resp = client.DescribeTaskStatus(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)



'''
运行后的结果如下，能识别“梅赛德斯奔驰”语句
{"Data": {"Status": 2, "StatusStr": "success", "Result": "[0:0.000,0:1.540]  梅赛德斯奔驰。\n", "TaskId": 737083613, "ErrorMsg": "", "ResultDetail": null}, "RequestId": "4f87d14f-8b0f-4970-b517-eaf8c5df2e9d"}
'''