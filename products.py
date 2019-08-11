import os # operating system

#讀取檔案
products = [] #產生空清單 叫做 products

if os.path.isfile('products.csv'):  #檢查檔案  #os=作業系統 path路徑 os.path.isfile 檢查檔案在嘛
	print('yeah! 找到檔案了!')   
	with open('products.csv', 'r', encoding='utf-8') as f: #encoding='utf-8' 寫入讀取都要用一樣的編碼
		for line in f:
			if '商品,價格' in line:
				continue #跳過 跳到下一迴圈
			name, price = line.strip().split(',') #spilt=切割 遇到逗點做分割
			#.strip=去掉換行符號(\n) 
			products.append([name, price])
	print(products)
else:
	print('找不到檔案.....')

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

 

#寫入檔案
                       #r=讀取 w=寫入   as f = 當作f = products.txt = f 只是簡稱
with open('products.csv', 'w', encoding='utf-8') as f:   
	f.write('商品,價格\n')   #寫入前 先寫欄位
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
		#f.write 才是真的寫入

		#encoding(編碼),utf-8 最廣泛使用的編碼