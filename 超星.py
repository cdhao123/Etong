import requests
from bs4 import BeautifulSoup
url = 'https://mooc1-2.chaoxing.com/ananas/ext/ed_complete.js?v=20141027'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'k8s-ed=a89d681fe006766360085823411137c883fa29b7; jrose=22000E01205F9625261E92246CF14F7D.html-editor-a-2349975098-d5lk2; fanyamoocs=92B8130197B473B09D9B035A95892A87; thirdRegist=0; rt=-2; tl=0; k8s=b764b782d0e2302648e288f667991d08de064042; route=69a208f7ef97c8349a42f0121eef1c12; source=""; jrose=4DB9809DEF84EB8FF265B6D683E211DB.mooc-4197521816-88kd6; uname=2193612793; fid=43575; _uid=103263355; uf=d9387224d3a6095baf6b8eef50d2113df57ef8430992f80a2b7b281d22ed55b3dd3f2c93ce94b3f97f1a219c23ec42b8428b5a98cdb27be888b83130e7eb4704bc28276af6f33cf1fd68be96b6183b1a85ad43d1d7de4b5d6f7ea12f39f7d7e7c5843a470b5c4c45; _d=1574052256905; UID=103263355; vc=7FD6D3203BDE2B42307F594430B2592E; vc2=1B9C3AF96AF1D49EE7DF166D719EDFC2; vc3=cA7SgvS5ktCLoBSmFMNeHZDtZrYxiamFnG1kKsTS4jhJ24KAVJsCh4it82ysSPqe2jMNcRft5IPdVZL3KeFV139w%2FBnvJq5kaDDfC%2FUIchs0pUcV%2FKwhbw7zQkJcAAvPjH92L3HLvIkWYX5GRt6DQDX2Rc4H6%2B%2BGWIc%2BgSmkpfk%3Dde3423ea8b4a36916469a3a3a0b1ab52; DSSTASH_LOG=C_38-UN_63-US_103263355-T_1574052256907; videojs_id=65552',
    'Host': 'mooc1-2.chaoxing.com',
    'Referer': 'https://mooc1-2.chaoxing.com/ananas/modules/innerbook/simple.html?v=2018-0126-1905',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
res = requests.get(url,headers=headers)
print(res.status_code)
