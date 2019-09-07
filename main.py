# 爬取网页数据
from bs4 import BeautifulSoup
import re
import csv
from log import DuxiuLog
import pandas as pd
import requests
import time

'''
解析目标数据
书名 作者 出版社 图书简介 主题词 分类号
'''
class DuxiuDetail:

    def __init__(self, soup):
        self.soup = soup
    
    '''
    解析书名
    '''
    def get_bookname(self):
        pass

    '''
    解析作者
    '''
    def get_author(self):
        pass

    '''
    解析出版社
    '''
    def get_chubanshe(self):
        pass

    '''
    解析简介
    '''
    def get_intro(self):
        pass

    '''
    解析主题词
    '''
    def get_topic_words(self):
        pass

    '''
    解析分类号
    '''
    def get_fenleihao(self):
        pass

'''
爬取数据
'''

'''
解析数据
'''

def reg_parse(str):
    # print(str)
    book = {}
    # str = '''    <dl>
	# 							<dt>
									
	# 									<a href="bookDetail.jsp?dxNumber=000016523164&amp;d=2698808B67B6D6CF50D07D0AF4703FE8&amp;fenlei=01080201" target="_blank">《马克思主义经典著作研究读本  列宁《共产主义运动中的“左派”幼稚病》》</a>
	# 								&nbsp;&nbsp;<a href="/goreadbookgc.jsp?dxid=000016523164&amp;unitid=1247&amp;d=DC9BCB34D40B7125A50BD2E615F5E117&amp;timestr=1567738446276" target="_blank"><img src="/images/libbook.gif" border="0"></a>
												

	# 													&nbsp;&nbsp;<a href="/goreadbaoku.jsp?dxid=000016523164&amp;ssnum=14220905&amp;d=FEEAA7E19DDC60E2BD1DF88AAD15B8BB&amp;fenlei=01080201" target="_blank">
	# 													<img src="/images/readAll_bk.jpg" border="0"></a>
													
	# 							</dt>
	# 							<dd>作者:吴克明编著&nbsp;&nbsp;</dd><dd>页数:272&nbsp;&nbsp;</dd><dd>出版社:北京：中央编译出版社&nbsp;&nbsp;</dd><dd>出版日期:2017.03&nbsp;&nbsp;</dd><dd>简介:本书围绕《共产主义运动中的“左派”幼稚病》这一经典文献展开研究，主要由历史考证（包括写作背景、国内外主要版本和传播情况）、研究状况（含国内外的研究状况）、当代解读（包括文本的基本结构和主要内容、重要理论观点及其当代意义）、经典著作选编和附录等部分构成。全书充分结合历史和现实背景，全面解读列宁《共产主义运动中的“左派”幼稚病》，点评和启示简明透彻，能对马克思主义理论及其中国化发展史与传播史、科学社会主义和国际共产主义运动等学科领域研究起到较重要的参考价值。&nbsp;&nbsp;</dd><dd>主题词:《共产主义运动中的“左派”幼稚病-》--列宁著作研究&nbsp;&nbsp;</dd>
	# 							<dd>&nbsp;<b>分类</b>:&nbsp;<span id="m_fl"><a href="advsearch?channel=advsearch&amp;rn=50&amp;ecode=utf-8&amp;Field=&amp;btype=&amp;&amp;fenleiID=01">马克思主义、列宁主义、毛泽东思想、邓小平理论</a>-&gt;<a href="advsearch?channel=advsearch&amp;rn=50&amp;ecode=utf-8&amp;Field=&amp;btype=&amp;&amp;fenleiID=0108">马克思主义、列宁主义、毛泽东思想、邓小平理论的学习和研究</a>-&gt;<a href="advsearch?channel=advsearch&amp;rn=50&amp;ecode=utf-8&amp;Field=&amp;btype=&amp;&amp;fenleiID=010802">列宁主义的学习和研究</a>-&gt;<a href="advsearch?channel=advsearch&amp;rn=50&amp;ecode=utf-8&amp;Field=&amp;btype=&amp;&amp;fenleiID=01080201">列宁著作的学习和研究</a></span></dd>

	# 						</dl>'''
    # 找到作者
    author_pattern = '<dd>作者:(.*?)</dd>'
    author = re.compile(author_pattern).search(str)
    if author :
        author = author.group(1).replace('&nbsp;', '') # group为0返回全部字符串，包括了<dd>这些 group为1则代表着只是选择目标字符串
        book['author'] = author
    else :
        book['author'] = 'NULL'
    
    # 找到出版社 
    chubanshe_pattern = '<dd>出版社:(.*?)</dd>'
    chubanshe = re.compile(chubanshe_pattern).search(str)
    if chubanshe:
        chubanshe = chubanshe.group(1).replace('&nbsp;', '')
        book['chubanshe'] = chubanshe
    else:
        book['chubanshe'] = 'NULL'

    # 图书简介 
    jianjie_pattern = '<dd>简介:(.*?)</dd>'
    jianjie = re.compile(jianjie_pattern).search(str)
    if jianjie:
        jianjie = jianjie.group(1).replace('&nbsp;', '')
        book['jianjie'] = jianjie
    else:
        book['jianjie'] = 'NULL'

    # 主题词 
    zhutici_pattern = '<dd>主题词:(.*?)</dd>'
    zhutici = re.compile(zhutici_pattern).search(str)
    if zhutici:
        zhutici = zhutici.group(1).replace('&nbsp;', '')
        book['zhutici'] = zhutici
    else:
        book['zhutici'] = 'NULL'
    return book
'''
工作启动
page 起始页 比如1
final_page 最后一页 比如40
fenlei_id 分类的ID 比如
'''
def work(page, final_page, fenlei_id):

    for page in range(final_page):

        page = page + 1
        url = '''http://book.duxiu.com/advsearch?Pages={page}&rn=50&ecode=utf-8&fenleiID={fenlei_id}&Sort=3&channel=search#searchinfo'''.format(page = page, fenlei_id = fenlei_id) # 按照时间排序
        excel_name = fenlei_id + '_' + str(page)
        print(str(fenlei_id) + '--' + str(page))

        time.sleep(10)

        html = requests.get(url)
        html = html.text
        soup = BeautifulSoup(html, 'html.parser') # 加载文档
        lis = soup.select('div.books ul li')

        data = []

        for li in lis:
            book = {}

            dl = li.select_one('dl')
            
            book = reg_parse(dl.prettify().replace('\n', '').replace(' ', '')) 
            # dl.get_text() 只是保留文本
            # dl.prettify() 保留了换行符合空格符

            book_name = dl.select_one('dt a').get_text() # 书名
            book['book_name'] = book_name

            fenlei = ''
            fenlei_as = dl.select('#m_fl a')
            for fenlei_a in fenlei_as:
                fenlei += fenlei_a.get_text() + ''
            book['fenlei'] = fenlei.rstrip()
            data.append(book)

        
        data = pd.DataFrame(data)
        data.to_excel('./dataset/' + excel_name +'.xlsx')


if __name__ == "__main__":
   
    # 输入参数
    page = 1
    final_page = 40
    fenlei_id = '02'

    work(page, final_page, fenlei_id)

    # 分类ID最大值为22

    
    


