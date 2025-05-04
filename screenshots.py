from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




class Screenshot:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        # Initialize the Chrome WebDriver
        # self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)


        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
    def take_screenshots(self, domains):
        for domain in domains:
            try:
                 # Wait for the page to fully load (e.g., wait for the body element to be present)
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
                self.driver.get(f'https://{domain}')
            except Exception as e:
                print(f"Error accessing {domain}")
                continue
            
            self.driver.save_screenshot(f'screenshots/{domain}.png')
        self.driver.quit()