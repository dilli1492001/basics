total_bill = 0
menu ={
    "idly":30,
    "dosa":40,
    "wada":10,
    "upma":35
}


dish_one_choice=input("enter your first dish : ")
dish_one_quantity=int(input("enter your first dish quantity : "))

dish_two_choice=input("enter your second dish : ")
dish_two_quantity=int(input("enter your second dish quantity :"))

dish_one_bill=(dish_one_quantity*menu.get(dish_one_choice))
dish_two_bill=(dish_two_quantity*menu.get(dish_two_choice))

total_bill = (dish_one_bill+dish_two_bill)


detail_bill=f"""
######welcome to hotel#########
Bill id = {total_bill*356}
{dish_one_choice} X {menu.get(dish_one_choice)} = {dish_one_bill}
{dish_two_choice} X {menu.get(dish_two_choice)} = {dish_two_bill}
-------------------------------------------------------------------
GST: 0%
TAXES: 0%
------------------------------------TOTAL BILL: Rs.{total_bill}/----

THANKS FOR VISITING US

"""

print(detail_bill)




