#获取最新测试报告
import os

def newest_file(test_dir):
    lists=os.listdir(test_dir)
    print(lists)
    lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'))
    print(lists)
    file_path = os.path.join(test_dir,lists[-1])
    return file_path,lists[-1]

if __name__ == '__main__':
     print(newest_file('../report'))
