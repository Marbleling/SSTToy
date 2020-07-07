from selenium import webdriver
from selenium.webdriver.firefox.options import Options

default_site = "https://gongu.copyright.or.kr/gongu/wrt/wrtCl/listWrtText.do?menuNo=200019&pageUnit=30"

options = Options()
options.headless = True

browser = webdriver.Firefox(options=options)
result_links = []

for idx in range(1010, 36681):
    target_site = default_site + '&pageIndex=' + str(idx)
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