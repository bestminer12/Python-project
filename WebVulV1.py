import requests
import os
import pandas as pd


urls=[]
result={'payload'}

def get_payload():
    filename="urls.txt"
    f=open(filename, "r")
    lines=f.readlines()
    for each_line in lines:
        if not each_line.startswith("http"):
            url="http://"+each_line
        urls.append(url.rstrip())
    f.close()
    print(urls)

def web_req():
    for each_url in urls:
        res=requests.get(each_url)
        content_length_bytes = len(res.content)
        print("Connecting to "+each_url)
        print("Status code: "+str(res.status_code))
        print("Length: "+str(content_length_bytes))
        print("===============Response===============")
        print(res.text[:500])


def save_data_to_csv():
    pass

if __name__ == '__main__':
    get_payload() ## url 리스트 읽어오기
    web_req() ## 웹 테스트
    save_data_to_csv() ## 결과값 csv 파일로 저장

    