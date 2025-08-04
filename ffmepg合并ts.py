import os
os.chdir('film')
#m3u8文件直接合并
# rt = os.popen("ffmpeg -i filmfile_list.m3u8 -c copy xxx.mp4").read()
#生成txt文件和并
rt = os.popen('ffmpeg -f concat -safe 0 -i filmfile_list.txt -c copy output.ts').read()
print(rt)