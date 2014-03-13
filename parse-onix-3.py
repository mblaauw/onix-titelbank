from bs4 import BeautifulSoup
from lxml import etree



soup = BeautifulSoup(open('titelbank/TB30_totaal_2014-03_073van073.onx/TB30_totaal_2014-03_073van073.onx', 'r'), features='xml')
productBlock = soup.find_all('Product')

print 'books to process: ' + str(len(productBlock))

for eachProductBlock in productBlock:



    tree = etree.fromstring(str(eachProductBlock))

    contributors = tree.xpath('//Contributor')
    for eachContributor in contributors:
        print eachProductBlock














print tree.xpath("/ONIXMessage/Product")
