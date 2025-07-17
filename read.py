import time


#讀取檔案
def read_file(filename):
    data = []
    count = 0
    with open('reviews.txt', 'r') as f:
    	for line in f:
    		data.append(line)
    		count += 1
    		if count % 1000 == 0:
    		    print(len(data))
    print('檔案讀取完畢,總共有', len(data), '筆資料')
    return data 


#計算每筆留言的長度
def count(data):
    sum_len = 0
    for d in data:
        sum_len += len(d)
    print('平均每筆留言的長度為', sum_len / len(data),'個字')

    #計算小於100字留言的長度
    new = []
    for d in data:
        if len(d) < 100:
            new.append(d)
    # 17-20行 快寫法可寫 
    # new = [d for d in data if len(d) < 100]
    # 解析: 
    # [d(運算) for(迴圈) d(暫時變數) in(在) data(清單) if(判斷式) len(d) < 100 (篩選條件)]
    # "運算"及"判斷式"可根據需求改變, 也可無, 
    # 舉例: 亦可寫 new = [d for d in data] 
    # 就是只把清單內的暫時變數增加到new這個新的清單內

    print('小於100字的留言為', len(new), '筆資料')
    return data

#新增字典，將字串切割後裝入字典內
def word_count(data):
    start_time = time.time()
    wc = {}
    for d in data:
        words = d.split() #如果沒有填入資訊 預設就是以空白鍵做刪除
        for word in words:
            if word in wc:
                wc[word] += 1
            else:
                wc[word] = 1 #新增新的key進wc字典

    #列印出現超過100萬次的字
    for word in wc:
        if wc[word] > 1000000:
            print('出現超過一百萬次以上的字為:', word, wc[word])
    end_time = time.time()
    print('讀取共', end_time - start_time, '秒')
    print('總共有: ', len(wc), '個字存入字典')
    return wc

#查找功能
def user_input(wc):
    while True:
        word = input('請問你想查什麼字(輸入 q 離開): ')
        if word == 'q':
            break
        if word in wc:
            print(word,'出現過的次數為: ', wc[word], '次')
        else:
            print('這個字沒有出現過喔')

    print('感謝使用本查詢功能')

def main():
    filename = 'reviews.txt'
    data = read_file(filename)
    count(data)
    wc = word_count(data)
    user_input(wc)

main()