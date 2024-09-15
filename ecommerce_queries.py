import sqlite3
import sqlite_lib
sqlite_lib.connect("comm.db")
my_total:list[tuple] = sqlite_lib.run_query_select("select count(*) from ecommerce")
print(f" my_total {my_total}")
############################################################

my_average:list[tuple] = sqlite_lib.run_query_select("select avg(age) from ecommerce")
print(f" my_average {my_average[0][0]:.2f}")
##############################################################

men_count:list[tuple] = sqlite_lib.run_query_select("""select count(*) from ecommerce
                                                    where gender = 'Male'""")
women_count:list[tuple] = sqlite_lib.run_query_select("""select count(*) from ecommerce
                                                    where gender = 'Female'""")
print(f" men_count {men_count[0][0]}")
print(f" women_count {women_count[0][0]}")
##########################################################

men_avg_item:list[tuple] = sqlite_lib.run_query_select("""select avg("Items Purchased") from ecommerce
where gender = "Male"; """)
women_avg_item:list[tuple] = sqlite_lib.run_query_select("""SELECT AVG("Items Purchased") 
FROM ecommerce 
WHERE gender = "Female";""")
print(men_avg_item)
print(f" men_avg_item {men_avg_item[0][0]:.2f}")
print(f" women_avg_item {women_avg_item[0][0]:.2f}")
#######################################################
membership_count:list[tuple] = sqlite_lib.run_query_select("""SELECT count(Distinct "Membership Type") 
FROM ecommerce;""")
print(f" membership_count {membership_count[0][0]}")
#############################################################
membership_group_count:list[tuple] = sqlite_lib.run_query_select("""SELECT count(*) 
FROM ecommerce 
group by "Membership Type" """)
for i in range(len(membership_group_count)):
    print(f"membership_group_count {membership_group_count[i][0]} for i {i}")
#########################################################################
new_yorkers:list[tuple] = sqlite_lib.run_query_select("""SELECT count(*) 
FROM ecommerce 
where city like "New York" """)
print(f"new_yorkers {new_yorkers[0][0]}")
##########################################################################
city_count:list[tuple] = sqlite_lib.run_query_select(("""SELECT count(*) as c, city 
FROM ecommerce 
group by City 
order by c desc"""))
for i in range(len(city_count)):
    print(f"{city_count[i][1]} {city_count[i][0]}")
######################################################################
total_sum_men:list[tuple] = sqlite_lib.run_query_select("""select sum("Total spend") from ecommerce e 
 where gender like "Male" """)
print(f"total sum men {total_sum_men[0][0]}")

total_sum_women:list[tuple] = sqlite_lib.run_query_select("""select sum("Total spend") from ecommerce e 
 where gender like "Female" """)
print(f"total sum women {total_sum_women[0][0]}")
###################################################################
max_items_purchased:list[tuple] = sqlite_lib.run_query_select(""" select "Customer ID" , City , age, "Items Purchased" from ecommerce e 
 where "Items Purchased" = (select max("Items Purchased") from ecommerce)""")
print("max items purchased:")
for i in range(len(max_items_purchased)):
    print("*"*40)
    print(f"customer id: {max_items_purchased[i][0] } ")
    print(f"city: {max_items_purchased[i][1] } ")
    print(f"age: {max_items_purchased[i][2] } ")
    print(f"items purchased: {max_items_purchased[i][3] } ")
#################################################################
print("*"*40)
min_items_purchased:list[tuple] = sqlite_lib.run_query_select(""" select "Customer ID" , City , age, "Items Purchased" from ecommerce e 
 where "Items Purchased" = (select min("Items Purchased") from ecommerce)""")
print("min items purchased:")
for i in range(len(min_items_purchased)):
    print("*"*40)
    print(f"customer id: {min_items_purchased[i][0] } ")
    print(f"city: {min_items_purchased[i][1] } ")
    print(f"age: {min_items_purchased[i][2] } ")
    print(f"items purchased: {min_items_purchased[i][3] } ")













sqlite_lib.close()

# def run_query_select(query: str) -> list[tuple]:
# def run_query_update(query: str) -> None:
# select count(DISTINCT e."Membership Type") from ecomm e;