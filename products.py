# 二維清單 2 dimensioning
# 大清單
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	p = [name, price] #小清單
	# p = []
	# p.append(name)
	# p.append(price)
	products.append(p) # products.append([name, price])
print(products)

# products[0][0] products[0][1] products[1][0] products[1][1]
# 第一個0是大清單的0,第二個0是小清單的0