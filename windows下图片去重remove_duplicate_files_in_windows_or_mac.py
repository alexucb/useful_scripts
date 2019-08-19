import os
import hashlib
import glob

allfile = glob.glob("D:\\美国之行1001\\*\\*")

def getmd5(filename):
    file_txt = open(filename, 'rb').read()
    m = hashlib.md5(file_txt)
    return m.hexdigest()
def main():
        de = 0
        all_size = {}
        for i, v in enumerate(allfile):
            try:
                key  = getmd5(v)
                if key in all_size:
                    os.remove(v)
                    de += 1
                    print('删除', v)
                else:
                    all_size[getmd5(v)]=v
            except:
                pass
        print('总共文件数:', len(allfile))
        print('共删文件数:', de)
if __name__ == '__main__':
    main()