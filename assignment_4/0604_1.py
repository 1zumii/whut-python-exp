"""
检查word文档的连续重复字。
在word文档中，经常会由于键盘操作不小心而使得文档中出现连续的重复字，
例如“用户的的资料”或“需要需要用户输入”之类的情况。
使用扩展库python-docx对word文档(QT学习之路2.doc)进行检查并提示类似的重复汉字.
"""
from docx import Document
import re

# https://cloud.tencent.com/developer/article/1107616
qtDoc = Document('qt2.docx')
text = ''.join((p.text for p in qtDoc.paragraphs))
result = re.findall(r'(([\u4e00-\u9fa5、！：；，]).?\2)', text)
for word in result:
	print(word[0])
