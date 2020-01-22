from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://stackoverflow.com")
search = driver.find_element_by_name("q")

#enter scraping criteria:
search.send_keys("pointer")
search.send_keys(Keys.ENTER)

file1 = open("myfile.txt","w") 
for vari in range(1,5):
    title = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div[4]/div/div["+str(vari)+"]/div[2]/div[1]/h3")
    file1.write(title.text) 
    file1.write("\n")
    print(title.text)

file1.close() 