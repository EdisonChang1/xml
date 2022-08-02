"""
### 1.  自己找 XML, ，把資料取得，並列印出來


### 2.   上面2題，把取得的XML 資料，存在檔案 xml 中


### 3.  上面 顯示圖表


### 4.  做一些數學 統計  計算, 總和，平均

### 5. Github  ###
新增一個專案
"""
from xml.etree import ElementTree
import sys
import xml.etree.ElementTree as ET
import urllib.request as httplib
import mylibs
#  SSL  處理，  https    SSSSSS 就需要加上以下2行
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

######### 由網路下載 JSON 的 字串
# https://data.gov.tw/dataset/156012
# 本府通過英檢人數統計
url="https://opendataap2.penghu.gov.tw/./resource/files/2022-07-28/589ec608e0622db6c05fb74e51a3d93f.xml"
contents= mylibs.url_Get(url)
mylibs.file_write('本府通過英檢人數統計.xml',contents)

# 加载XML文件
root = ElementTree.fromstring(contents)
row= root.findall("row_item/機關")
# 取得Tags
elemList = []
for elem in root.iter():
    elemList.append(elem.tag)

elemList = list(set(elemList))
print(elemList)

# 取得所有資料
organList=[]
percentagelList=[]

# XML 解析
organ=root.findall("row_item/機關")
agencybudgetPosts=root.findall("row_item/機關預算員額數")
passedPeople=root.findall("row_item/通過英檢人數")
percentage=root.findall("row_item/通過英檢人數佔機關總人數百分比")

n=0
while n<len(row):
           str1 = " 機關:"+organ[n].text + \
           " ,機關預算員額數："+agencybudgetPosts[n].text + \
           " ,通過英檢人數："+passedPeople[n].text + \
           " ,通過英檢人數佔機關總人數百分比："+percentage[n].text

           organList.append(organ[n].text)
           # percentagelList.append(float(percentage[n].text))  # 字串轉浮點數
           print(str1)
           n = n + 1

# ListLabel=["本府通過英檢人數統計","本府通過英檢人數統計"]
# mylibs.matplotlib_draw6Charts(organList,percentagelList,ListLabel)


import matplotlib.pyplot as plt # 匯入matplotlib 的pyplot 類別，並設定為plt
from matplotlib.font_manager import FontProperties # 中文字體

# 換成中文的字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

plt.plot(organList,percentagelList, "g--",label='通過英檢人數統計')
plt.legend()         # 自動改變顯示的位置

plt.title("本府通過英檢人數統計")
plt.ylabel('人數') # 顯示Y 座標的文字
plt.xlabel('類別') # 顯示Y 座標的文字

plt.show() # 繪製


