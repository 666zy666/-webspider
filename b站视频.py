import requests
# 视频获取
headers = {
    "referer": "https://www.bilibili.com/video/BV1aVJQzPEUb/?share_source=copy_web&vd_source=4b391b7745f04642c6b44c18f5781bc2",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
url = "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/87/24/32599182487/32599182487-1-100022.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&platform=pc&gen=playurlv3&os=alibv&og=ali&mid=0&nbs=1&trid=445b32eb07754d85aa515ee2b5fad94u&deadline=1760871499&oi=3683222232&uipk=5&upsig=b9bf5b9f996698ab197144b67ede224d&uparams=e,platform,gen,os,og,mid,nbs,trid,deadline,oi,uipk&bvc=vod&nettype=0&bw=187804&dl=0&f=u_0_0&agrr=1&buvid=350DCF5E-A1CC-0406-3069-6233EBCE337F03223infoc&build=0&orderid=0,3"

response = requests.get(url, headers=headers)
open('视频.avi',mode="wb").write(response.content)
print('video ok')
# 音频获取
headers2 = {
    "referer": "https://www.bilibili.com/video/BV1aVJQzPEUb/?share_source=copy_web&vd_source=4b391b7745f04642c6b44c18f5781bc2",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
url = "https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/87/24/32599182487/32599182487-1-30216.m4s"
params = {
    "e": "ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=",
    "nbs": "1",
    "gen": "playurlv3",
    "os": "coso1bv",
    "og": "cos",
    "mid": "0",
    "oi": "3683222232",
    "deadline": "1760875382",
    "platform": "pc",
    "uipk": "5",
    "trid": "5e7d60b0c5cc470492ce29b5b832074u",
    "upsig": "03dbc3b64660095ae6ac6cf57c5f15f7",
    "uparams": "e,nbs,gen,os,og,mid,oi,deadline,platform,uipk,trid",
    "bvc": "vod",
    "nettype": "0",
    "bw": "65740",
    "dl": "0",
    "f": "u_0_0",
    "agrr": "1",
    "buvid": "350DCF5E-A1CC-0406-3069-6233EBCE337F03223infoc",
    "build": "0",
    "orderid": "0,3"
}
res = requests.get(url, headers=headers2, params=params)
open('音频.mp3','wb').write(res.content)
print('MP3 ok')

import os
def convert_avi_to_mp4_os(input_file, output_file):
    """
    使用os.system将AVI转换为MP4
    """
    # 构建命令字符串
    command = f'ffmpeg -i "{input_file}" -c:v libx264 -c:a aac "{output_file}"'
    # 执行命令
    exit_code = os.system(command)
    if exit_code == 0:
        print(f"转换成功: {input_file} -> {output_file}")
        return True
    else:
        print(f"转换失败，错误代码: {exit_code}")
        return False


if __name__ == "__main__":
    input_file = "视频.avi"
    output_file = "output.mp4"
    convert_avi_to_mp4_os(input_file, output_file)
# 视频与音频合并
import subprocess
def merge_audio_video(video_path, audio_path, output_path):
    """
    合并MP4视频和MP3音频[^1][^3]
    :param video_path: MP4视频文件路径
    :param audio_path: MP3音频文件路径
    :param output_path: 输出文件路径
    """
    cmd = [
        'ffmpeg',
        '-y',  # 覆盖已存在文件
        '-i', video_path,  # 输入视频
        '-i', audio_path,  # 输入音频
        '-c:v', 'copy',    # 复制视频流不重新编码
        '-c:a', 'aac',     # 转码音频为AAC格式
        '-strict', '-2',   # 允许实验性编码器
        output_path
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"合并成功: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"合并失败: {e.stderr}")
        return False

# 使用示例
merge_audio_video("output.mp4", "音频.mp3", "全中国肥胖率高的城市之一，有多好吃？.mp4")
