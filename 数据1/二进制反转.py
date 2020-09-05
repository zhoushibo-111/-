

def reverseBits(n):
        str1 = bin(n)  # 转换为二进制字符串
        str2 = str1[2:].zfill(32)  # 去掉前'0b'后填充为32位
        str3 = str2[::-1]  # 字符串反转
        # return int(str3, 2)  # 转为10进制
        return str3  # 转为10进制


if __name__ == '__main__':
    a = reverseBits(10)
    print(a)
