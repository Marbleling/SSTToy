from selenium import webdriver
from selenium.webdriver.firefox.options import Options

default_site = {"https://gongu.copyright.or.kr/gongu/wrt/wrtCl/listWrtText.do?menuNo=200019&sortSe=&licenseCd=97&searchWrd=&pageUnit=24": 2089,
                "https://gongu.copyright.or.kr/gongu/wrt/wrtCl/listWrtText.do?menuNo=200019&sortSe=&licenseCd=20_21_22_23_24_25_26_27&searchWrd=&pageUnit=24": 10}

options = Options()
options.headless = True

browser = webdriver.Firefox(options=options)
result_links = []

for site in default_site:
    for idx in range(1, default_site[site]+1):
        target_site = site + '&pageIndex=' + str(idx)
        browser.get(target_site)

        print('IDX : ' + str(idx))

        elements = browser.find_elements_by_class_name('licsCon')

        for el in elements:
            try:
                link = el.find_element_by_tag_name('a').get_attribute('href')
                print(link)
                result_links.append(link)
            except:
                pass

        if len(result_links) > 1000:
            f = open('text_sites.txt', 'a')
            for link in result_links:
                f.write(link + '\n')

            f.close()

            result_links = []

            browser.quit()
            browser = webdriver.Firefox(options=options)

            print('WRITE')

f = open('text_sites.txt', 'a')
for link in result_links:
    f.write(link + '\n')

f.close()

result_links = []

browser.quit()
browser = webdriver.Firefox(options=options)

print('WRITE')