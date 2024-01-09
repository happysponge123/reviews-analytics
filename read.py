data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data)/10000, '%')

print('檔案讀取完了，總共有', len(data), '筆資料')

rlen = []
sum_len = 0
for d in data:
	sum_len += len(d)

print('每筆留言的平均長度: ', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '留言長度小於100')
print(new[0])

