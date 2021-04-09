# 二維清單 2 dimensioning
# 大清單
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	# price = int(price)
	p = [name, price] #小清單
	# p = []
	# p.append(name)
	# p.append(price)
	products.append(p) # products.append([name, price])
print(products)

# products[0][0] products[0][1] products[1][0] products[1][1]
# 第一個0是大清單的0,第二個0是小清單的0


for p in products:
	print(p[0], '的價格是', p[1])
	# 小清單的 0 是名字 1 是 價格
# encoding='utf-8' 選擇編碼
# encoding='big5'
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
		# f.write(p[0] + ',' + str(p[1]) + '\n') #若p1被轉為整數 需要轉回字串才能合併