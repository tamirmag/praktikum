import time
from selenium import webdriver  
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys  

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()  
driver.get("https://ww2.capsim.com/login/")  
driver.find_element_by_name("username").send_keys("<username>")  
driver.find_element_by_name("password").send_keys("<password>")  
driver.find_element_by_name("button").send_keys(Keys.ENTER)  
driver.get("http://ww2.capsim.com/menuApp/studentMain.cfm?simid=G126357_010") 
driver.find_elements_by_xpath("//*[contains(text(), 'Continue to Decisions')]")[0].send_keys(Keys.ENTER)  
driver.find_elements_by_xpath("//a[@onClick = \"showDepartmentPage('Marketing')\"]")[0].send_keys(Keys.ENTER)  

promo = driver.find_element_by_id("Promo_0_0")
awareness = driver.find_element_by_id("Awareness_0_0")
sales = driver.find_element_by_id("Sales_0_0")
accessibility = driver.find_element_by_id("Accessibility_0_0")
regPromo = driver.find_element_by_id("RegPromo_0")
regSales = driver.find_element_by_id("RegSales_0")
recalculate = driver.find_element_by_id("recalculate")
#promo.send_keys("0") 
#sales.send_keys("0") 
#regPromo.send_keys("0") 
#regSales.send_keys("0") 


promo_money = 0
sales_money = 0
regPromo_money = 0
regSales_money = 0

ans = []
promos = []
sale = []
repromos = []
regsel = []
#while int(awareness.text) < 100:
promo.clear()
sales.clear()
regPromo.clear()
regSales.clear()
for x in range(0,4600,100):
    if(x<=3000):
        promo.clear()
        promo_money = x
        promo.send_keys(str(promo_money)) 
    sales.clear()
    sales_money = x
    sales.send_keys(str(sales_money))
    recalculate.send_keys(Keys.ENTER)  
    time.sleep(1) 
    if(x<=3000):
        promos.append([promo_money , awareness.text])
    sale.append([sales_money , accessibility.text])
promo.clear()
sales.clear()
regPromo.clear()
regSales.clear()
for x in range(0,4600,100):
    if(x<=3000):
        regPromo.clear()
        regPromo_money = x
        regPromo.send_keys(str(regPromo_money)) 
    regSales.clear()
    regSales_money = x
    regSales.send_keys(str(regSales_money))
    recalculate.send_keys(Keys.ENTER)  
    time.sleep(1) 
    if(x<=3000):
        repromos.append([regPromo_money , awareness.text])
    regsel.append([regSales_money , accessibility.text])

driver.close()  

import csv  

with open('<path>\\data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    header = ["promo_money" , "awareness"]
    writer.writerow(header)
    writer.writerows(promos)
    writer.writerow('')

    header = ["sales_money" , "accessibility"]
    writer.writerow(header)
    writer.writerows(sale)
    writer.writerow('')

    header = ["reg_promo_money" , "awareness"]
    writer.writerow(header)
    writer.writerows(repromos)
    writer.writerow('')

    header = ["reg_sales_money" , "accessibility"]
    writer.writerow(header)
    writer.writerows(regsel)