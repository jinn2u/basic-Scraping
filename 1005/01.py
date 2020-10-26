from selenium import webdriver

# Chrome 드라이버 추출하기
driver = webdriver.Chrome(r'D:\exe\chromedriver.exe')


# 3초 대기하기 : 기본적으로 웹 자원들이 모두 로드될때까지 기다려주지만, 암묵적으로 모든 자원이 로드될때 까지 기다리게 하는 시간을 직접 implicitly_wait을 통해 지정할 수 있다.
driver.implicitly_wait(3)

# URL 읽어 들이기
driver.get('https://google.com')

# 화면을 캡처해서 저장하기
driver.save_screenshot("google.png")

# 브라우저 종료하기
driver.quit()