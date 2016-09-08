import mechanize
from bs4 import BeautifulSoup

def select_form(form):
    ''' form slection by submit button id '''
    return form.attrs.get('id', None) == 'new_user'
#using mechanize for authentication
br = mechanize.Browser()
br.open('https://code.gramener.com/users/sign_in?redirect_to_referer=yes')
# form selection by predicate function
br.select_form(predicate=select_form)
file = open('login.txt', 'r')
details=file.read().split(",")
# user authentication details
br.form['user[login]'] = details[0]
br.form['user[password]'] = details[1]
res = br.submit()
final = res.geturl()
if final=="https://code.gramener.com/users/sign_in":
    print "wrong credentials"
else:
    print "success"