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
page = 1
boo = True
if details[0].index("@")>0:
    details[0]=details[0].split("@")[0]
    print details[0]
    pass
print "opening file..."
file=open('projects.txt','w')
while boo:
    '''traversing through all the projects in multiple pages'''
    p = str(page)
    print "writing page "+p+" into file.."
    ''' getting the next page url by changing its page number to url available'''
    stri = "/explore/projects?page="+p
    x = br.open(final+stri)
    soup = BeautifulSoup(br.response().read(), 'lxml')
    for record in soup.findAll("a", attrs={"class": "project"}):
        '''traversing project names in one page'''
        file.write("https://"+details[0]+":"+details[1]+"@code.gramener.com"+record.get('href')+".git")
        file.write("\n")
    for record in soup.findAll("div", attrs={"class": "gl-pagination"}):
        ''' finding the availability of next page'''
        for rec in record.findAll("ul", attrs={"class": "pagination clearfix"}):
            for r in rec.findAll("li", attrs={"class": "next disabled"}):
                '''next button in page is disabled means end of project pages'''
                boo = False
    page += 1
    pass

file.close()
print "file closed successfully.."
