import os.path,sys


def gettext():
    text=[]
    with open('text.txt','r',encoding='utf-8') as f:
	    for line in f:
		    text.extend(list(line.strip('\n').split(',')))
    return text

def file_extension(path):
    return os.path.splitext(path)[1]

def text_suffering(text):
    list = []
    for i in range(len(text)):
        l = text[i].split('/')
        if ((l[3] == '._.DS_Store') or (l[3] == '.DS_Store')):
            continue
        list.append(text[i])
    return list


if __name__ == '__main__':
    a = gettext()
    list = text_suffering(a)
    #for value in list:
        #print(value)
    #cc = opencc.OpenCC('t2s')

    aa = cc.convert(u'Open Chinese Convert（OpenCC）「開放中文轉換」，是一個致力於中文簡繁轉換的項');
    print(aa)




