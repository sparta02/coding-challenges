discount_list=[]
answer = [0, 0]

def calc_emot(users, emoticons, discount_list):
    reg_people, sale_amount = 0, 0
    
    #print(f"현재 적용하는 할인률: {discount_list}")
    
    # i번째 사람에 대해 테스트
    for i in range(len(users)):
        temp_price=0
        # j번째 이모티콘
        for j in range(len(emoticons)):
            # 유저가 원하는 할인률 이상이라면
            if discount_list[j]>=users[i][0]:
                #print(f"{i+1}번째 사람이 {j+1}번째 이모티콘 구매, 금액: {int(emoticons[j]*(100-discount_list[j])/100)}")
                temp_price+=int(emoticons[j]*(100-discount_list[j])/100)
        # 유저가 설정한 금액 이상이라면 이모티콘 플러스 가입
        if users[i][1]<=temp_price:
            reg_people+=1
        else:
            sale_amount+=temp_price
    #print(f"이모티콘 가입자 수: {reg_people}, 판매액: {sale_amount}")
    return reg_people, sale_amount
            
                     

def make_discount_per(users, emoticons):
    global answer
    # n개의 할인률이 다 정해지면
    if len(discount_list)==len(emoticons):
        # 함수 호출하여 할인률에 따른 이모티콘 플러스 가입자수, 이모티콘 판매액 계산
        reg_people, sale_amount =calc_emot(users, emoticons, discount_list)
        if reg_people >answer[0]:
            answer=[reg_people, sale_amount]
        elif reg_people==answer[0] and sale_amount>answer[1]:
            answer=[reg_people, sale_amount]
        return
    else:
        for i in range(1, 5):
            discount_list.append(i*10)
            make_discount_per(users, emoticons)
            discount_list.pop()
    
def solution(users, emoticons):
    make_discount_per(users, emoticons)
        
        
    return answer