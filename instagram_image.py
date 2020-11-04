from urllib.request import urlopen
from urllib.parse import quote_plus  # 아스키 코드로 변환시켜준다.
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# 변수 url 에 저장될 url 형식은 아래와 같다.
# https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%9C%A0/

baseUrl = 'https://www.instagram.com/explore/tags/'
plusUrl = input('검색할 태그를 입력하세요 : ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome("./chromedriver.exe")
driver.get(url)
time.sleep(3)

real_link = []

SCROLL_PAUSE_TIME = 0.8
for steps in range(100):  # 반복문 시작
    pageString = driver.page_source
    bs = BeautifulSoup(pageString, "lxml")

    # 게시물 정보
    for link1 in bs.find_all(name="div", attrs={"class": "Nnq7C weEfm"}):
        title = link1.select('a')[0]
        real = title.attrs['href']
        real_link.append(real)

    # 페이지 스크롤
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break

        else:
            last_height = new_height
            continue

length = len(real_link)
print("total  " + str(len(real_link)) + "  data")
# print(real_link)

# try:
#     for i in range(0, length):
#         req = 'https://www.instagram.com/p' + real_link[i]
#         driver.get(req)
#         webpage = driver.page_source
#         soup = BeautifulSoup(webpage, "html.parser")
#         soup1 = str(soup.find_all(attrs={'class': 'ele1d'}))
#

# html = driver.page_source
# soup = BeautifulSoup(html, "lxml")
#
# # select는 페이지에 있는 정보를 다 가져 온다.
# # 클래스가 여러 개면 기존 클래스의 공백을 없애고 .으로 연결시켜 주어야 한다.
# insta = soup.select('.v1Nh3.kIKUG._bz0w')
#
# n = 1
#
# print("intsa complete and waiting")
# time.sleep(10)
#
#
# # 이미지 하나만 가져올 게 아니라 여러 개를 가져올 것이므로 반복문을 쓴다.
# for i in insta:
#     # 인스타 주소에 i번 째의 a태그의 href 속성을 더하여 출력한다.
#     print('https://www.instagram.com' + i.a['href'])
#     # 인스타 페이지 소스에서 이미지에 해당하는 클래스의 이미지 태그의 src 속성을 imgUrl에 저장한다.
#     imgUrl = i.select_one('.KL4Bh').img['src']
#     with urlopen(imgUrl) as f:
#         # img라는 폴더 안에 programmer(n).jpg 파일을 저장한다.
#         # 텍스트 파일이 아니기 때문에 w(write)만 쓰면 안되고 binary 모드를 추가시켜야 한다.
#         with open('./img/' + plusUrl + str(n) + '.jpg', "wb") as h:
#             # f를 읽고 img에 저장한다.
#             img = f.read()
#             # h에 위 내용을 쓴다.
#             h.write(img)
#     # 계속 programmer 1에 덮어쓰지 않도록 1을 증가시켜 준다
#     n += 1
#     print(imgUrl)
#     # 출력한 걸 보았을 때 구분하기 좋도록 빈 줄을 추가시킨다.
#     print()
# # 마지막에 driver를 닫아준다. (열린 창을 닫는다.)
# driver.close()
#
# # 우리가 인스타 페이지에 들어가서 스크롤 하기 전까지 보여진 사진 개수가 img 폴더에 저장된다.
