from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


url = "https://shop.foodsoul.pro" #указываем ссылку
driver = webdriver.Chrome() #запускаем браузер
driver.get(url) #отдаём браузеру ссылку


driver.maximize_window() #включаем полноэкранный режим
time.sleep(1) #останавливаем выполнение на 1сек


delivery_Method = driver.find_element(By.XPATH, "//img[@src='/assets/template_mosaic/pickup_icon.png']")#вкладываем в переменную XPATH элемента
delivery_Method.click()#кликаем на элемент
time.sleep(1.5)


pickup_Point = driver.find_element(By.XPATH, "//li[@class='pickup-item cursor-pointer br-15 position-relative w-100 card ease pickup-list__item']")
pickup_Point.click()
time.sleep(1)


Italian_Food = driver.find_element(By.XPATH, "//a[@href='/kirov/italyanskaya-kuhnya']")
Italian_Food.click()
time.sleep(5)


pizza = driver.find_element(By.XPATH, "//div[@class = 'lazy-load flex-center position-relative overflow-hidden product__image cursor-pointer'][@aria-label='Пицца 4 СЕЗОНА'][1]")
pizza.click()
time.sleep(1)


sauce = driver.find_element(By.XPATH, "//html/body/div[4]/div/div/div/div/div[2]/div[4]/div/div[1]/div[2]/div/div/div/ul/li/div/div[3]/div/div[2]/div/button[2]")
sauce.click()
time.sleep(1)


add_Pizza = driver.find_element(By.XPATH, "//span[@class='price-value total-sum']")
add_Pizza.click()
time.sleep(1)


go_To_Basket = driver.find_element(By.XPATH, "//html/body/div[2]/div[2]/div[2]/div/div/div/button/div[1]")
go_To_Basket.click()
time.sleep(1)


basket = driver.find_element(By.XPATH, "//html/body/div[2]/div[2]/div[2]/div/div/div[2]/div")
basket.screenshot("screenshot.png")#скриншотим элемент
checkout = driver.find_element(By.XPATH, "//html/body/div[2]/div[2]/div[2]/div/div/div[2]/div/button/div")
checkout.click()
time.sleep(5)


driver.quit()#завершаем сеанс
