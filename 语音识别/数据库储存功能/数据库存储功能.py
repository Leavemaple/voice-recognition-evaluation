#Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。


#首先是自己产生参数
#URL方式：params = {"EngineModelType":"16k_0","ChannelNum":1,"ResTextFormat":0,"SourceType":0,"Url":"http://ttsgz-1255628450.cos.ap-guangzhou.myqcloud.com/20190813/cbf318cd-273e-4b7c-bab0-50a1885c9b96.wav"}
#录音文件方式：params = {"EngineModelType":"16k_0","ChannelNum":1,"ResTextFormat":0,"SourceType":1,"Data":base64Wav,"DataLen":dataLen}

#然后会返回一个数据 {"RequestId": "d33d2dd0-a3a6-4cfc-bb53-f33c754a13e3", "Data": {"TaskId": 737083613}}

#最后我们会查询，返回一个数据 {"Data": {"Status": 2, "StatusStr": "success", "Result": "[0:0.000,0:1.540]  梅赛德斯奔驰。\n", "TaskId": 737083613, "ErrorMsg": "", "ResultDetail": null}, "RequestId": "4f87d14f-8b0f-4970-b517-eaf8c5df2e9d"}

import sqlite3
conn = sqlite3.connect('test.db')

print("数据库已生成！")
cursor = conn.cursor()

#执行一条SQL语句，创建voice表:
cursor.execute('create table user (id varchar(20) primary key, voice varchar(20))')

#插入一条记录
cursor.execute('insert into user (id, voice) values (\'1\', \'梅赛德斯奔驰\')')

print("数据已插入成功！")

cursor.close()
conn.commit()
conn.close()