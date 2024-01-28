from bs4 import BeautifulSoup
import requests
# from PIL import Image
try:
    response = requests.get("https://www.moparpartsgiant.com/parts/mopar-belt-serpentine~68232297aa.html")
    soup = BeautifulSoup(response.text,'html.parser')

    header_tags = soup.find_all(['h1'])
    for header_tag in header_tags:
        print(header_tag.text.strip())

    para = soup.find('p' , class_="pn-detail-sub-desc")
    print(para.text.strip())

    # image_path ='E:\image\parts1.jpg'
    # img = Image.open(image_path)
    # img.show()


    price = soup.find('span', class_="price-section-price")
    print(price.text.strip())

    price_save = soup.find('span', class_="price-section-retail")
    price_bar = "\u0336".join(price_save.text.strip())
    print(price_bar)

    price_you = soup.find('div', class_="price-section-save")
    print(price_you.text.strip())

    table_head = soup.find('h2',class_='pn-tab-h2')
    print(table_head.text.strip())

    table = soup.find('table',class_="pn-spec-list")
    if table:
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if columns:
                row_data = [column.text.strip() for column in columns]
                print(row_data)
    else:
        print("failed")

    table_head2 = soup.find('div', class_="pn-tab-title")
    print(table_head2.text.strip())

    vehicle_fitment = soup.find('table', class_="fit-vehicle-list-table")
    if vehicle_fitment:
        for row2 in vehicle_fitment.find_all('th'):
            columns1 = row2.find_all('th')
            print(row2.text.strip())
        for row1 in vehicle_fitment.find_all('tr'):
            columns1 = row1.find_all('td')
            if columns1:
                row_data1 = [column1.text.strip() for column1 in columns1]
                print(row_data1)
    else:
        print("failed")


except Exception as e:
        print ("failed to reach this website https://www.moparpartsgiant.com/parts/mopar-belt-serpentine~68232297aa.html")

