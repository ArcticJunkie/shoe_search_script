from selenium import webdriver
from selenium.webdriver.common.keys import Keys

string_of_shoes = "Nike Roshe LD-1000, Nike Roshe Run, Nike Free RN, adidas ZX Flux, adidas ZX Flux ADV, non-PK adidas NMD, adidas Energy Boost 3,New Balance 574, Saucony Shadow Original, Saucony Jazz, Reebok Classic Leather, New Balance 420, Onitsuka Tiger Mexico 66, Nike Cortez, Greats The Rosen, Nike Pegasus 83, Nike Internationalist, Nike Air Odyssey, Nike Air Max 1, Asics Gel Lyte III, adidas Dragon, adidas ZX700, adidas Los Angeles, Brooks Vanguard, Reebok Royal Glide, New Balance 996, Karhu Albatross,Vans Authentic, Vans Era, Vans Old Skool, Vans 106, Vans LPE, Lakai Daly, Lakai MJ, HUF Cromer, Keds, Nike Dunk Low,adidas Samba, adidas Samba ADV, adidas Campus, German Army Trainer (GAT), PUMA Suede, PUMA Liga,Nike Tennis Classic, adidas Stan Smith, Gola Vantage, CLAE Bradley, Kent Wang sneaker"

list_of_shoes = str.split(string_of_shoes, ',')
links_of_shoes = [shoe.strip() for shoe in list_of_shoes]
final_shoes = [shoe.replace(' ', '%20') for shoe in links_of_shoes]

browser = webdriver.Chrome()
browser.maximize_window()
# browser.execute_script("window.open('https://www.google.com');")
i = 1
for shoe in final_shoes:
    link = 'https://www.sportchek.ca/search.html#q=' + shoe
    browser.execute_script(
        "window.open('');")
    browser.switch_to_window(browser.window_handles[i])
    i = i + 1
    browser.get(link)
    # browser.execute_script("window.open('https://www.google.com');")


exit
