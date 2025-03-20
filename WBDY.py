import requests
from lxml import etree
import asyncio
import aiohttp
import aiofiles
import re
from urllib import parse
import os
from moviepy import VideoFileClip, concatenate_videoclips




# def get_page_source(url):
#     resp = requests.get(url)
#     return resp.text
# def get_iframe_src(url):
#     page_source = get_page_source(url)
#     et = etree.HTML(page_source)
#     src = et.xpath("//div[@class='wrapper content']/div[@class='left l']/div[@class='con_c2 ']/div[@class='con_juji_bg ']/div[@class='tab-content']/ul/li/a/@href")[0].strip()
#     src = "https://www.ipehr.com" + src
#     return src
# def get_first_m3u8(url):
#     page_source = get_page_source(url)
#     obj = re.compile(r'"link_pre":"","url":"(?P<m3u8_url>.*?)",',re.S)
#     result = obj.search(page_source)
#     m3u8_url = result.group("m3u8_url")
#     #new_m3u8 = m3u8_url.replace('\/','/')
#     new_m3u8 = "https://v2.tlkqc.com/wjv2/202411/06/gKGmHDfPBJ74/video/index.m3u8"
#
#     print(m3u8_url)
#     print(new_m3u8)
#     return new_m3u8
# def download_m3u8_file(first_m3u8_url):
#     first_m3u8 = get_page_source(first_m3u8_url)
#     second_m3u8_url = first_m3u8.split()[-1]
#     second_m3u8_url = parse.urljoin(first_m3u8_url, second_m3u8_url)
#     second_m3u8=get_page_source(second_m3u8_url)
#     with open("second_m3u8.txt", mode='w', encoding='utf-8') as f:
#         f.write(second_m3u8)
#
# async def download_all_ts():
#     tasks = []
#     with open("second_m3u8.txt", mode='r', encoding='utf-8') as f :
#         for line in f :
#             if line.startswith("#"):
#                 continue
#             task = asyncio.create_task(download_one(line))
#             tasks.append(task)
#     await asyncio.wait(tasks)
#
# async def download_one(url):
#     while 1:
#         try:
#             file_name = url.split("/")[-1]
#             file_name_ = file_name.split(".")[0]
#
#             async with aiohttp.ClientSession() as session:
#                 async with session.get(url) as resp:
#                     content = await resp.content.read()
#                     async with aiofiles.open(f"./film/{file_name_}", mode='wb') as f:
#                         print("ok1")
#                         await f.write(content)
#
#             print(url,"ok2")
#             break
#         except:
#             print("erro")

def merge_ts():

    # with open("second_m3u8.txt", mode='r', encoding='utf-8') as f:
    #     for line in f:
    #         if line.startswith("#"):
    #             continue
    #         line = line.split("/")[-1]
    #         file_name = line.split(".")[0]+".ts"
    #         name_list.append(file_name)
    # now_dir = os.getcwd()
    # os.chdir(r"C:\Users\郑曦\PycharmProjects\pythonProject1\learning\异步\film")
    # temp = []
    # n = 1
    # now_dir_ = os.getcwd()
    # print(now_dir_)
    # name_list = os.listdir(r"C:\Users\郑曦\PycharmProjects\pythonProject1\learning\异步\film")
    # f0 = open(r"C:\Users\郑曦\PycharmProjects\pythonProject1\learning\异步\film"+ 'test1.ts', 'ab')  # 可以在这行代码处通过更改test1的后缀来更改合成后的文件类型
    # index = 0
    # for one in name_list:
    #     # 先检查当前文件是不是ts文件
    #     file_suffix = one.split('.')[1]
    #     if file_suffix != 'ts':  # 如果当前文件不是ts文件，那就跳过
    #         continue
    #     index += 1
    #     print(index, "准备合并第" + str(index) + "个视频")
    #     f1 = open(r"C:\Users\郑曦\PycharmProjects\pythonProject1\learning\异步\film" + one, "rb")
    #     f0.write(f1.read())  # 将当前ts文件写入到test1.ts之中
    #     f1.close()
    # f0.close()
    #

    paths = r'C:\Users\郑曦\PycharmProjects\pythonProject1\learning\异步\film'
    save_path = 'C:\\Users\\Administrator\\Desktop\\'
    out_file_name = '7.mp4'
    file_names = os.listdir(paths)
    print(file_names)

    ts_files = [f for f in os.listdir(paths) if f.endswith('.ts')]
    print(ts_files)
    sorted_files = sorted(ts_files, key=lambda x: int(x.split('.')[0]))
    print(sorted_files)
    with open(paths + 'file_list.txt', 'w', encoding='utf-8') as f:
        for file in sorted_files:
            f.write(f"file '{file}'\n")
    print("生成txt文件成功!")
    ffmpeg_bin_dic = 'C:\\ffmpeg-7.1'
    os.system(
        ffmpeg_bin_dic + 'ffmpeg -f concat -safe 0 -i ' + paths + 'file_list.txt' + ' -c ' + ' copy ' + save_path + out_file_name)
    print("ok9")






def main():
    # url = "https://www.ipehr.com/voddetail/89401.html"
    # src =  get_iframe_src(url)
    # m3u8_first = get_first_m3u8(src)

    #download_m3u8_file(m3u8_first)
    merge_ts()
    # asyncio.run(download_all_ts())

if __name__ == "__main__":
    main()

