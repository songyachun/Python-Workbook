import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            # print('childpath=', childpath)
            total += disk_usage(childpath)
    print('{0:7}'.format(total), path)
    return total


if __name__ == "__main__":
    patha = r'D:\Desktop\Python-Workbook'
    disk_usage(patha)
