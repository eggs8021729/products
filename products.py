products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

                       #r=讀取 w=寫入   as f = 當作f = products.txt = f 只是簡稱
with open('products.csv', 'w', encoding='utf-8') as f:   
	f.write('商品,價格\n')   #寫入前 先寫欄位
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
		#f.write 才是真的寫入

		#encoding(編碼),utf-8 最廣泛使用的編碼