import jieba
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud

text = open(r'./文本可视化/英文.txt').read()
# print(text)

cut_text = jieba.cut(text)
result = " ".join(cut_text)
# print(result)

wc = WordCloud(font_path=r'./simhei.ttf',
               background_color='white',
               mask=np.array(Image.open('./文本可视化/test1.jpeg')),
               width=500,
               height=350,
               max_font_size=50,
               min_font_size=10)
wc.generate(result)
wc.to_file(r'wordcloud.png')
plt.figure('jay')
plt.imshow(wc)
plt.axis('off')
plt.show()
