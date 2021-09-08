from selenium import webdriver
import time
import requests
import os
import argparse


print(argparse())

class InstaBot:
    links=[]
    profile_to_search= ' ' # the profile user to download IGTV from
    def __init__(self):
        self.login('username','pw') # insert Username & password
        self.links = self.get_video_link()
        self.download_video()
        

    def login(self, username: str, password: str):
        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com/')
        time.sleep(2)
        
        try:
            cookies= self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
            if cookies:
                cookies.click()
        except:
            pass
        time.sleep(2.5)
        user_name= self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_name.send_keys(username)
        pass_input= self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_input.send_keys(password)
        time.sleep(3)
        accept_btn= self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(2)
        try:
            notification= self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            if notification:
                notification.click()
        except:
            pass
        
        time.sleep(1.4)
        
        #IGTV videos
    def get_video_link(self):
        self.driver.get('https://www.instagram.com/{self.profile_to_search}/channel/') 
        time.sleep(3)
        anchs = self.driver.find_elements_by_xpath('//div[@class="Gx7Kn"]//a')
        links= [item.get_attribute('href') for item in anchs]
        return links
    

    def download_video(self):
        curr_wkdir= os.getcwd()
        vid_path= os.path.join(curr_wkdir,'vid_file')
        os.makedirs(vid_path, exist_ok = True)
        downd_vid= [x for x in os.listdir(vid_path) if x.endswith('.mp4')]
        links = self.links
        if links:
            try:    
                for num, link in enumerate(links):
                    time.sleep(1.3)
                    self.driver.get(link)
                    if num <= 3 :
                        vid_link= self.driver.find_element_by_xpath('//video[@src]')
                        vid_url= vid_link.get_attribute('src')
                        re = requests.get(vid_url)
                        name= ' '  #customise 
                        vid_name= f'{name}{num}.mp4'
                        if downd_vid:
                            if vid_name in downd_vid:
                                print('class already exists')
                            else:
                                with open(vid_name, 'wb') as f:
                                    f.write(re.content)
                    else:  
                        break
            
            except:
                raise Exception('Unable to download the video')

def main():
    my_bot = InstaBot()
   


if __name__ == '__main__':
    main()
