#地址链接：https://cloud.tencent.com/document/product/1093/35731
#调用腾讯云API的使用方法
#以下分别是通过语音 URL和本地语音上传请求方式的 demo，以及轮询接口查询识别结果，来帮助客户快速接入。

#通过语音 URL 方式请求
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models
import base64

#音频 URL 方式
try:
    #此处<Your SecretId><Your SecretKey>需要替换成客户自己的账号信息
    cred = credential.Credential("Your SecretId", "Your SecretKey")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "asr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.signMethod = "TC3-HMAC-SHA256"
    client = asr_client.AsrClient(cred, "ap-shanghai", clientProfile)
    req = models.CreateRecTaskRequest()
    params = {"EngineModelType":"16k_0","ChannelNum":1,"ResTextFormat":0,"SourceType":0,"Url":"http://ttsgz-1255628450.cos.ap-guangzhou.myqcloud.com/20190813/cbf318cd-273e-4b7c-bab0-50a1885c9b96.wav"}
    req._deserialize(params)
    resp = client.CreateRecTask(req)
    print(resp.to_json_string())
    #windows 系统使用下面一行替换上面一行
    #print(resp.to_json_string().decode('UTF-8').encode('GBK') )

except TencentCloudSDKException as err:
    print(err)

