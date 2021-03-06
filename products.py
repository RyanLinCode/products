import os # operating system

def read_file(filename):
# 讀取檔案
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line: #遇到 '商品,字串'跳過不執行
                continue #繼續
            # strip() 除換行符號 .split(',')用逗點符號做切割
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# 二維清單 2 dimensioning

# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            break
        price = input('請輸入商品價格：')
        # price = int(price)
        # p = [name, price] #小清單
        # p = []
        # p.append(name)
        # p.append(price)
        products.append([name, price])
    print(products)
    return products

# products[0][0] products[0][1] products[1][0] products[1][1]
# 第一個0是大清單的0,第二個0是小清單的0

# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])
        # 小清單的 0 是名字 1 是 價格
# encoding='utf-8' 選擇編碼
# encoding='big5'

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')
            # f.write(p[0] + ',' + str(p[1]) + '\n') #若p1被轉為整數 需要轉回字串才能合併

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # 檢查檔案在不在
        print('year! 找到檔案了!')
        products = read_file(filename)
    else:
        print('找不到檔案')

    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main()
