import pyaudio,wave
import base64
from test_ex import test

import init_oral_process

class Record():

    def __init__(self):
        # 定义音频数据参数
        self.CHUNK = 1024  # 块
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2  # 渠道
        self.RATE = 44100  # 率
        self.RECORD_SECONDS = 2
        self.WAVE_OUTPUT_FILENAME = "hello.mp3"
        self.testword = "hello"
        self.SessionId = 'test_'
        self.RefText = "hello"

    def recording(self):
        p = pyaudio.PyAudio()

        # 打开数据流
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        print("& Start Recording & :")

        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("#### done recording ####")

        # 停止数据流
        stream.stop_stream()
        stream.close()

        # 关闭 PyAudio
        p.terminate()

        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        self.database(self.WAVE_OUTPUT_FILENAME)

    def database(self,file):
        print("文件地址：",file)
        with open(file,mode='rb') as f:
            base64_data = base64.b64encode(f.read()).decode()
            #base64_data ='aGVsbG8='
        print("base64编码：",base64_data[:20])
        '''self.params = {'Action': 'KeywordEvaluate', 'Version': '2018-07-24', 'SeqId': 1, 'IsEnd': 1, 'VoiceFileType': 3,
                  'VoiceEncodeType': 1, 'UserVoiceData': self.base64_data,
                  'SessionId': '12345', 'SoeAppId': 'default',
                  'Keywords': [{"RefText": self.testword, 'EvalMode': 0, 'ServerType': 0, 'ScoreCoeff': 1.0}]}
        test(self.params)
        '''
        #初始化音频信息
        init_oral_process.init_oral_process(self.SessionId,self.RefText,base64_data)



