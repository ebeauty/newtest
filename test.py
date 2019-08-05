import os.path

def file_extension(path):
    return os.path.splitext(path)[1]

if __name__ == '__main__':
    #a = gettext()
    a = [
        'handian2 /『史部』 / 编年 / 中华民国史事日志',
        'handian2 /『史部』 / 传记 / 廿二史劄记',
        ' handian2 /『子部』 / 释家 /._.DS_Store',
        'handian2 /『子部』 / 释家 /.DS_Store',
        'handian2 /『子部』 / 医家 / 血證論',
        'handian2 /『子部』 / 医家 / 醫學三字經',
    ]
    a = a.split('/')
    print(a[3])

