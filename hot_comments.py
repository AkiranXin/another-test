import json
import requests

def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open('hot_comments.txt','w',encoding='utf-8') as file:
        for each in hot_comments:
            file.write(each['user']['nickname']+':\n\n')
            file.write(each['content']+'\n')
            file.write("----------------------------------\n")


def get_commands(url):
    name_id = url.split('=')[1]
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
        "referer":"https://music.163.com/"
    }
    params = "x265+BysxyoBsJR80NETdgFR7GNErjCLJRsianwHQ6nd6XqUpo/oH+NJoCy2Sii0wLcsbB6bw8tovRaX8dIl+ouU/cF8Xm4pHxE2prFj2t2z6cP5kWwqALrkyEo8kc1FFi06kEnHSiojlhuEHLdaPvrLRzOw9SGgRg0vayF5ZGy68ozHX8bkVFzXXZf/xRAV"
    encSecKey="d53bb5d53e47ea264990e3951787aee0e83bef31a2fe17d5fe6c63e8c30e83bb9abef47006c802385dfac48e05388a90b5edddd6b9a3d8e3e6e5e9d406903ec2079a3eff3fd2bd076190718ca3f46599a5d5ab0d86caa861d644f3045284fe4388f8a6665b5333b355fe9bda7f8ebde9adcaf478e03a027ed8b05450b589c9fe"
    data = {
        "params":params,
        "encSecKey":encSecKey
    }
    target_url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(name_id)
    res = requests.post(target_url,headers=headers,data=data)
    return res

def main():
    url = input("请输入链接地址:")
    res = get_commands(url)
    get_hot_comments(res)

if __name__ == '__main__':
    main()
