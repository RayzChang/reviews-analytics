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
#17-20行 快寫法可寫 
#new = [d for d in data if len(d) < 100]
#解析: 
#[d(運算) for(迴圈) d(暫時變數) in(在) data(清單) if(判斷式) len(d) < 100 (篩選條件)]
#"運算"及"判斷式"可根據需求改變, 也可無, 
#舉例: 亦可寫 new = [d for d in data] 
#就是只把清單內的暫時變數增加到new這個新的清單內

print('小於100字的留言為', len(new), '筆資料')