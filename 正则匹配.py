import re
def list_in_string(string):
    if re.search(r'(发行|变动|转让|交易|减持|增持|托管|拍卖).{0,10}(前|后)', string) != None:
        return True
    else:
        return False

if __name__ =='__main__':
    flag = list_in_string("发行120万老干妈前")
    print(flag)