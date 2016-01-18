"""
Shop list - A script to remind me what to buy.
"""


shop_list = []
user_input = ""

while user_input != "done":
    print "What do you need to buy? (Write done to finish)"
    user_input = raw_input()
    if user_input != "done":
        shop_list.append(user_input)

for item in shop_list:
    print "You need to buy %s" % item


