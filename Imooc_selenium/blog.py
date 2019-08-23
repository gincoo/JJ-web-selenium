#coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.minimize_window()
driver.set_window_size('100','200')
driver.refresh()
driver.back()
driver.forward()

#chrome
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);') # 将页面滚动条滑到底部
# driver.execute_script('arguments[0].scrollIntoView();', element) # 向下滑动滚动条，跳转到目标元素处
# driver.execute_script('arguments[0].scrollIntoView(false);', element) # 向上滑动滚动条，跳转到目标元素处

"""
driver=webdriver.Firefox()
driver.get("http://www.jianshu.com")
#等待页面加载3S time.sleep(3)
'''
0：为顶部；1000000：为底部
#将滚动条移动到页面的顶部 
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
#页面内嵌窗口浏览条滚动
js="var q=document.getElementById('id').scrollTop=1000"
driver.execute_script(js)
time.sleep(3)
''' 
#将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=100000" driver.execute_script(js)
time.sleep(3)


"""