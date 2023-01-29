import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib

keyword = input('Enter your product :')

urlA = 'https://www.amazon.in/s?k='+keyword+''
urlF = 'https://www.flipkart.com/search?q='+keyword+''

urlt = 'https://www.trustbasket.com/search?type=product&q='+keyword+''

urlu = 'https://www.ugaoo.com/search?q='+keyword+''
prices = {}
def scrape(url):
    if url == urlF:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemF = soup.find('div', class_='s1Q9rs')
            costF = soup.find('div', class_='_30jeq3')
            #print(itemF[0].text + " " + costF[0].text)
            #costF = costF[0].text[1:]
            prices["Flipkart"] = costF
            print('Data is Retrieved Successfully!!')
            print('========================================================')
        except Exception as e:
            print('data from Flipkart is not found')

   # if url == urlA:
    #    try:
     #       res = requests.get(url).content
    #        soup = BeautifulSoup(res, 'html.parser')
       #     print (soup)
      #      costA = soup.find('div',class_='a-row a-size-base a-color-base')
            #.find('a', class_='a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal').find('span',class_='a-price')
        #    print (costA)
         #   itemA= soup.find_all('span', class_="a-price-whole")
         #   #print(itemA[0].text + " " + costA[0].text)
         #   costA = costA[0].text[0:]
        #    prices["Amazon"] = costA
        #    print('Data is Retrieved Successfully!!')
         #   print('========================================================')
       # except Exception as e:
       #     print('data from amazon is not found',e)

   
    elif url == urlt:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            

            itemB = soup.find('div',class_='block-row').find('div',class_='product-bottom').find('a',class_='product-title').text
            costB = soup.find('div',class_='block-row').find('div',class_='product-bottom').find('div',class_='price-box').find('p',class_='sale').find('span',class_='special-price').text
           # print (itemB)
            #print(costB)
            
            #print(itemB[0].text+ " " + costB[0].text)
            
            prices["truebasket"] = costB
            print('Data is Retrieved Successfully!!')
            print('========================================================')
        except Exception as e:
            print('data from Trust basket is not found')

    elif url == urlu:
        try:
            
            
            r = urllib.request.urlopen(url)
           
            source_code = r.read()
            #res = requests.get(url).content
            soup = BeautifulSoup(source_code, 'html.parser')
            
            print(soup.find('div',class_='st-row').text)
            
            
            itemB = soup.find('div',class_='st-row').find('div',id="right",class_='st-col-xs-12 st-col-sm-12 st-col-md-9').find('div',id='products-listing',class_='st-row').find('div',class_='st-product st-col-xs-6 st-col-sm-4 st-col-md-4').find('div',class_='product-inner product_6940995485828').find('div',class_='product-bottom').find('a').find('div',class_='product-bottom-inner').find('div',class_='product-title').text
            print(itemB)
            
            
            
            #costB = soup.find_all('span', class_='discounted_price money')
            
            #print(itemB[0].text+ " " + costB[0].text)
            
            prices["ugaoo"] = itemB
            print('Data is Retrieved Successfully!!')
            print('========================================================')
        except Exception as e:
            print('data from Ugaoo is not found',e)
def priceComparision():
    print('Showing results for : {keyword} in different sites')
    for item in prices.items():
        print(item[0],":",item[1])
        print(prices)
        
if __name__ == '__main__':
    print('connecting to Flipkart.com')
    scrape(urlF)
   # print('connecting to Amazon.in')
    #scrape(urlA)
    print('connecting to Trust basket')
    scrape(urlt)
    #print('connecting to Ugaoo')
    #scrape(urlu)
    priceComparision()