from selenium import webdriver
from gdev_api import unit_count_from_profile

options = webdriver.EdgeOptions()
options.headless = True
driver = webdriver.Edge(options=options)

total_unit_count = 0
with open("usernames.txt", "r") as file:
    for line in file:
        user_unit_count = unit_count_from_profile(driver, line.strip())
        if user_unit_count >= 2:
            total_unit_count = total_unit_count + user_unit_count

print(f"Total unit count: {total_unit_count}")
successful_user_count = total_unit_count // 4
print(f"Successful user count: {successful_user_count}")
if 25 < successful_user_count < 50:
    print("SWAG Kit 1")
elif successful_user_count > 50:
    print("SWAG Kit 2")
else:
    print("Nothing :(")

driver.close()
