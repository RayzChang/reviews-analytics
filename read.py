data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
		    print(len(data))

print('檔案讀取完畢,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
print('平均每筆留言的長度為', sum_len / len(data),'個字')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('小於100字的留言為', len(new), '筆資料')