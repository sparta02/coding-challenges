user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class next_level:
    def __init__ (self, id="codetree", level=10):
        self.id=id
        self.level=level

user1=next_level()
print(f"user {user1.id} lv {user1.level}")
user1=next_level("hello", 28)
print(f"user {user1.id} lv {user1.level}")