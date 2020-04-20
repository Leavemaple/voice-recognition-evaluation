import pyaudio,wave

class Record():
    def __init__(self):
        # 定义音频数据参数
        self.CHUNK = 1024  # 块
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2  # 渠道
        self.RATE = 44100  # 率
        self.RECORD_SECONDS = 2
        self.WAVE_OUTPUT_FILENAME = "hello.mp3"

    def recording(self):
        p = pyaudio.PyAudio()

        # 打开数据流
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        print("& 录音开始 & :")

        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("#### 录音结束 ####")

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

        #————————————————————————————————————————————————————————#
'''
使用录音模块
'''
#创建录音对象
r = Record()

#使用录音对象的录音方法
r.recording()
