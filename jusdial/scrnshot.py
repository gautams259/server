from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from PIL import Image
import pytesseract
import os

class make_screenshot:
    def __init__(self,url):
        #self.driver=webdriver.Firefox()
        self.url=url
    


    def scrnsh(self):#tel ttel
        try:
            options = FirefoxOptions()
            options.add_argument("--headless")
            self.driver = webdriver.Firefox(options=options)
            self.driver.get(self.url)
            img=self.driver.find_element_by_class_name('telnowpr').screenshot_as_png
            with open('mob.png','wb') as f:
                f.write(img)
            self.driver.close()
        except Exception as e:
            print(e)
            self.driver.close()

    def make_txt(self,fl):
        try:
            t=pytesseract.image_to_string('mob.png', config='--psm 7')
            #textract.process('image.jpg', encoding='ascii',method='tesseract')
            return t
        except Exception as e:
            print(e)








#url='https://www.justdial.com/Mumbai/BBAs-Bunts-Institute-For-Higher-Education-(Day-College)-Near-Gaondevi-Chowk-and-Petrol-Pump-Juinagar/022PXX22-XX22-190424145147-E4M3_BZDET?xid=TXVtYmFpIENvbGxlZ2Vz'
url='https://www.justdial.com/Bangalore/Delphi-Automotive-Systems-Brookefield/080PXX80-XX80-170921192858-M7G3_BZDET?xid=QmFuZ2Fsb3JlIFNvZnR3YXJlIENvbXBhbmllcw=='
url='https://www.justdial.com/Bangalore/Ion-Digital-Zone/080PXX80-XX80-181113202608-V3Y7_BZDET?xid=QmFuZ2Fsb3JlIFNvZnR3YXJlIENvbXBhbmllcw=='
#ob=make_screenshot(url)
#ob.scrnsh()
#ob.make_txt('mob.png')
