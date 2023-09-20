from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium import webdriver

class OTB:
    def __init__(self):
        self.options = Options()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
        self.options.add_experimental_option("prefs", {"safebrowsing.enabled": True})
        self.options.add_experimental_option("detach", True)
        self.options.add_argument("--start-maximized")
        self.options.add_argument('user-agent=' + user_agent)
        self.driver = webdriver.Chrome('chromedriver', options=self.options)
        self.wait = WebDriverWait(self.driver, 10)

    def convert_octal_to_binary(self, search_keyword):
        list_void = search_keyword.split()
        concat = ''
        print(list_void)
        for octa in list_void :
            for i in range(0,3):
                if octa[i] == '0' :
                    concat = concat+'000'
                elif octa[i] == '1' :
                    concat = concat+'001'
                elif octa[i] == '2' :
                    concat = concat+'010'
                elif octa[i] == '3' :
                    concat = concat+'011'
                elif octa[i] == '4' :
                    concat = concat+'100'
                elif octa[i] == '5' :
                    concat = concat+'101'
                elif octa[i] == '6' :
                    concat = concat+'110'
                elif octa[i] == '7' :
                    concat = concat+'111'
                else :
                    print('8진수가 아닙니다')
                #concat = concat+' '

        result = ''
        for i in range(0, len(concat), 9):
            result += concat[i:i+9] + ' '
        print(result.strip())
        self.driver.get('https://www.rapidtables.com/convert/number/binary-to-ascii.html')
        self.driver.find_element(By.ID, 'bin').send_keys(result)
        select = Select(self.driver.find_element(By.ID, 'charsel'))
        select.select_by_value('euc-kr')
        self.driver.find_element(By.XPATH,'//*[@id="doc"]/form/div[5]/button[1]').click()

octalbinary = OTB()
search_keyword = input('변환값 : ')
octalbinary.convert_octal_to_binary(search_keyword)