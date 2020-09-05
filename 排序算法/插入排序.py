def insert_sort(alist):
    for i in range(1, len(alist)):
        value = alist[i]
        j = i - 1
        while j >= 0:
            # 如果第二个比第一个小 交换
            if alist[j] > value:
                alist[j + 1] = alist[j]
            else:
                break
            j -= 1

            alist[j + 1] = value
            print(alist)
    return alist


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(alist)

    print("最后一次")
    print(alist)
