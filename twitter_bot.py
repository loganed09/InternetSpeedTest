from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InternetSpeedTwitterBot():
    def __init__(self, down, up):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        
        self.driver = webdriver.Chrome(options=self.chrome_options)

        self.wait = WebDriverWait(self.driver, 60)
        self.down = down
        self.up = up


    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')

        start_button = self.driver.find_element(By.CLASS_NAME, 'js-start-test')
        start_button.click()
        
        next_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')))
        next_button.click()

        
        down_speed = self.driver.find_element(By.CLASS_NAME, 'download-speed').text
        up_speed = self.driver.find_element(By.CLASS_NAME, 'upload-speed').text
        return (down_speed, up_speed)

    def tweet_at_provider(self,email, username, password):
        internet_speeds = self.get_internet_speed()

        if float(internet_speeds[0]) < self.down or float(internet_speeds[1]) < self.up:
            self.driver.get('https://twitter.com/?lang=en')

            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')))
            sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
            sign_in.click()

            self.wait.until(EC.url_matches('https://twitter.com/i/flow/login'))
            self.wait.until(EC.element_to_be_clickable(((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'))))
            email_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            email_input.send_keys(email)
            next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
            next_button.click()

            if self.wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div'), 'unusual login')):
                username_input_verification = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
                username_input_verification.send_keys(username)
                log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
                log_in_button.click()
                #self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
                
        
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
            password_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password_input.send_keys(password)
            log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
            log_in_button.click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
            tweet_box = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            tweet_box.send_keys(f'Internet Provider, whats the deal with my internet? Download is {internet_speeds[0]} and Upload is {internet_speeds[1]}')        

            post_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')
            self.wait.until(EC.element_to_be_clickable(post_btn))
            post_btn.click()