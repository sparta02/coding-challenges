unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class 클래스:
    def __init__ (self, unlock_code, wire_color, seconds):
        self.u=unlock_code
        self.w=wire_color
        self.s=seconds

번 = 클래스(unlock_code, wire_color, seconds)
print(f"code : {번.u}")
print(f"color : {번.w}")
print(f"second : {번.s}")