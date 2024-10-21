# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止

answer = 58
# 1.告訴使用者需要輸入的數字範圍 input()
while True:
    data =int(input ("輸入1-100數字: ")) #要放迴圈,不然輸入錯誤不會再能輸入

# 2.使用者猜對要回傳「恭喜中獎」，並結束迴圈的執行
    if data == answer:
        print("恭喜中獎!!")
        break
# 3.超出範圍要顯示「超出範圍請重新輸入」
    elif data < 0 or data >100:
        print("超出範圍請重新輸入!")

# 4.數字太大 要提示「請輸入更小的數字」
    elif  data >answer:
        print("請輸入更小的數字!!")


# 5.數字太小 要提示「請輸入更大的數字」
    elif  data < answer:
        print("請輸入更大的數字!!")

55