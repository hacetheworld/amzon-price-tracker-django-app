from django.shortcuts import render, redirect
from .models import Item
from bs4 import BeautifulSoup
import requests
from django.core.mail import send_mail

# Create your views here.


def check_price(URL, excpected_price):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    # print(URL)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="priceblock_dealprice")
    if(price == None):
        price = soup.find(id="priceblock_ourprice")
    if(price == None):
        price = soup.find(id="priceblock_saleprice")
    price = price.get_text()
    converted_price = 0  # float(''.join(price[2:].split(',')))
    if(converted_price < excpected_price):
        subject = 'Price droped on amazon'
        body = f"Check the amazon link {URL}"
        from_email = 'muskanm2019@gmail.com'
        # auth_password = 'xtkehkxfseqkfwbh'
        msg = f"Subject : {subject} \n\n{body}"
        send_mail(
            subject=subject,
            message=msg,
            from_email=from_email,
            recipient_list=['majay1638@gmail.com'],
            fail_silently=False,

        )
    # Content views


def content(response, username):
    products = response.user.productlist.all()
    # for product in products:
    #     # print(product.url)
    check_price(products[0].url, products[0].price)

    if(response.method == "POST"):
        if response.POST.get('name') and response.POST.get('price'):
            url = response.POST.get('name')  # url
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
            source = None
            try:
                source = requests.get(url, headers=headers)
            except:
                return render(response, "content.html", {"msg": "There was some Problem in URL please check product url"})

            soup = BeautifulSoup(source.content, 'html.parser')
            title = " ".join(
                str(soup.find(id="productTitle").get_text()).strip().split(' ')[0:5])
            price = soup.find(id="priceblock_dealprice")
            if(price == None):
                price = soup.find(id="priceblock_ourprice")
            if(price == None):
                price = soup.find(id="priceblock_saleprice")

            if(price == None or title == None):
                return render(response, "content.html", {"msg": "There was some Problem in URL please check product url"})

            price = price.get_text()
            converted_price = float(''.join(price[2:].split(',')))
            item = Item()
            item.user = response.user
            item.name = title
            item.url = url
            item.price = float(response.POST.get("price"))
            item.currentPrice = converted_price
            item.save()
            return render(response, "content.html", {"msg": "Product Saved"})

    if(len(str(response.user)) > 0 and str(response.user) != 'AnonymousUser'):
        return render(response, "content.html", {})
    else:
        return redirect("/")
# def addItem(response):


def delete_view(response, id):
    product = Item.objects.get(id=id)
    # print(response.user)
    product.delete()
    return redirect("/profile/%s" % response.user)
