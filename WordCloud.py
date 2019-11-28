from wordcloud import WordCloud
import PIL .Image as image
import numpy as np
import jieba
clear_list = ['两个','只是','问题','主要','知道','看见','这儿','哪儿','现在','以后','突然','因为','所以','不是','如果','为了','他们','时候','那么','但是','它们','自己','然而','什么','由于','已经','可是','例如','或者','可以','很多','这些','往往','就是','没有','一个','一种','甚至','不过','这里','那里','一些','这个','那个','不仅','而且','不会','不能','这是','还是','这种','那种','尽管','无论','还是']

def trans_CN(text):
    word_list = jieba.cut(text)
    object_list = []
    for word in word_list:
        if word not in clear_list:
            object_list.append(word)
    result = " ".join(object_list)
    return result

file_name = '中国崛起.txt' #把像生成词云的文档复制到记事本上面，并放在代码同目录下
File = open(file_name ,'r',encoding='UTF-8')
content = File.read()
content = trans_CN(content)
File.close()
picture = "中国地图.png"   #随便找一张白底的图片（不要空心的）,放在和代码相同目录下面
mask = np.array(image.open(picture))
wordcloud = WordCloud(scale=16,background_color='white',mask = mask,font_path='C:\Windows\Fonts\simhei.ttf').generate(content)
image_produce = wordcloud.to_image()
image_produce.show()
wordcloud.to_file('中国崛起词云图.png')


