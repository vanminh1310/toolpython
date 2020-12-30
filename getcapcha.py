import base64
from selenium import webdriver
import os
from time import sleep
browser = webdriver.Chrome(executable_path="./chromedriver")
browser.get("http://dangkyhoc.utc2.edu.vn/taikhoan#")

for i in range (591,600):
    els_capcha = browser.find_element_by_xpath("//*[@id='imgUserCaptcha']/img")

    try:
        img_captcha_base64 = browser.execute_async_script("""
        			var ele = arguments[0], callback = arguments[1];
        			ele.addEventListener('load', function fn(){
        			ele.removeEventListener('load', fn, false);
        			var cnv = document.createElement('canvas');
        			cnv.width = this.width; cnv.height = this.height;
        			cnv.getContext('2d').drawImage(this, 0, 0);
        			callback(cnv.toDataURL('image/png').substring(22));
        			}, false);
        			ele.dispatchEvent(new Event('load'));
        			""", els_capcha)
        path= '/home/vanminh/Documents/toolpython/img/'+str(i)+'.png'
        with open(path, 'wb') as f:
            f.write(base64.b64decode(img_captcha_base64))
            print(path)
            browser.refresh()
    except Exception as e:
        print(e)
        browser.refresh()
        
        
    


