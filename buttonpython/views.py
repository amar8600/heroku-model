from django.shortcuts import render, redirect


def button(request):
    return render(request, 'home1.html')
def new1(request):
  return render(request, 'new.html')


def aboutus(request):
    return render(request, 'aboutus.html')

def auth_social(request):
  return render(request, 'auth_social.html')


def external(request):
  search = request.POST['search']
  from oauth2client.tools import argparser
  from urllib.request import Request, urlopen
  from urllib.parse import quote
  from urllib.parse import quote_plus
  from urllib.error import HTTPError
  from bs4 import BeautifulSoup
  import time
  import numpy as np
  import random

  class Test:

    def med_links(self, x):
      self.x = x
      links = []
      for data in x:
        for a in data.find_all('a'):
            links.append(a.get('href'))
      return (links)

    def clapcount(self, z):
      clapcount = []
      self.z = z
      for node in z:
          clapcount.append(''.join(node.findAll(text=True)))
      return (clapcount)

    def med_titles(self, k):
      self.k = k
      titles = []
      for node in k:
          titles.append(''.join(node.findAll(text=True)))
      return (titles)

    def videotitle(self, vids):                         # youtube
      self.vids = vids
      videotitle = []
      for v in vids:
          tmp = v['title']
          videotitle.append(tmp)
          videotitle1 = videotitle[1:18]
      return videotitle1

    def videourl(self, vids):
      self.vids = vids
      videourl = []
      for v in vids:
          tmp = 'https://www.youtube.com' + v['href']
          videourl.append(tmp)
          videourl1 = videourl[1:18]
      return videourl1

    # Code with Papers functions

    def cop_desc(self, a):
      self.a = a
      desc = []
      for i in a:
        desc.append(i.find('p', attrs={'class': 'item-strip-abstract'}).text)
      return desc

    def cop_codelinks(self, b):
      code = []
      github_code = []
      self.b = b

      for i in b:
        try:
          code.append(i.find('a', attrs={'class': 'badge badge-dark'})['href'])
        except TypeError:
          pass

      for i in range(len(code)):
        github_code.append('https://paperswithcode.com{}'.format(code[i]))
      return github_code

    def cop_titles(self, c):
      titles = []
      self.c = c
      for node in c:
          titles.append(''.join(node.findAll(text=True)))
      # Because of the first content is coming as a str "Search Result"
      titles1 = titles[1:]
      return titles1

    def git_titles(self,x):
      self.x = x
      titles = []
      for node in x:
            titles.append(' '.join(node.findAll(text=True)))
      return titles
    
    def git_links(self,x):
        self.x = x
        links = []
        for a in x :
            links.append('https://github.com{}'.format(a['href']))
        return links
    
    def git_stars(self,x):
        self.x = x
        stars = []
        for node in x:
            stars.append(''.join(node.findAll(text=True)))
        stars1 = [x.strip('  \n') for x in stars]
        return stars1

    def rel_words(self,x):
      self.x = x
      titles = []
      for node in x:
            titles.append(','.join(node.findAll(text=True)))
      
      titles1 = str(titles)
      titles2 = titles1.split(',')
      titles3 = titles2[1:6]

      return titles3



  class Sol:
    ob=Test()
    
    # user = str(input("Enter the Keyword:"))

    qstr = quote('%s'%(search))# %20
    
    req = Request('https://medium.com/search?q={}'.format(qstr), headers={'User-Agent': 'Mozilla/5.0',"Accept-Language": "en-US,en;q=0.5"})
    req.add_header('Accept-Encoding','utf-8')
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage.decode('utf-8','ignore'),features="lxml")

    # for code with papers
    qstr1  = quote_plus('%s'%(search))#+
    req1 = Request('https://paperswithcode.com/search?q={}'.format(qstr1), headers={'User-Agent': 'Mozilla/5.0'})
    req1.add_header('Accept-Encoding','utf-8')
    webpage1 = urlopen(req1).read()
    soup1 = BeautifulSoup(webpage1.decode('utf-8','ignore'),features="lxml")

    # for Youtube
    req2 = Request("https://m.youtube.com/results?search_query={}".format(qstr1), headers={'User-Agent': 'Mozilla/5.0'})
    req2.add_header('Accept-Encoding','utf-8')
    webpage2 = urlopen(req2).read()
    soup2 = BeautifulSoup(webpage2.decode('utf-8','ignore'),features="lxml")


    # Github 
    qstr3 = quote_plus('%s'%(search))
    req3 = Request('https://github.com/search?q={0}'.format(qstr3), headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 111; SF1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36'})
    req3.add_header('Accept-Encoding','utf-8')
    try:
      webpage3 = urlopen(req3).read()
      soup3 = BeautifulSoup(webpage3.decode('utf-8','ignore'),features="lxml")
      x3 = soup3.find_all('a',attrs= {'class':'v-align-middle'})
      y3 = soup3.find_all('a',attrs= {'class':'v-align-middle'},href = True)
      z3 = soup3.findAll('div',attrs= {'class':'pl-2 pl-md-0 text-right flex-auto min-width-0'})
      git_titles = ob.git_titles(x3)
      git_links = ob.git_links(y3)
      git_stars = ob.git_stars(z3)
      repos_len = 'Found '  +str(len(x3))+ ' contents'

    except HTTPError:
        time.sleep(5)
        try:
            print('second try')
            webpage3 = urlopen(req3).read()
            soup3 = BeautifulSoup(webpage3.decode('utf-8','ignore'),features="lxml")
            x3 = soup3.find_all('a',attrs= {'class':'v-align-middle'})
            y3 = soup3.find_all('a',attrs= {'class':'v-align-middle'},href = True)
            z3 = soup3.findAll('div',attrs= {'class':'pl-2 pl-md-0 text-right flex-auto min-width-0'})
            git_titles = ob.git_titles(x3)
            git_links = ob.git_links(y3)
            git_stars = ob.git_stars(z3)
            repos_len = 'Found '  +str(len(x3))+ ' contents'

        except HTTPError:
            print("Failed twice :S")
    


    # For related words
    
    y1 = soup.find_all('ul',attrs= {'class':'u-clearfix u-marginTop10 u-marginBottom50'})
    

    # x3 = soup3.find_all('a',attrs= {'class':'v-align-middle'})
    # y3 = soup3.find_all('a',attrs= {'class':'v-align-middle'},href = True)
    # z3 = soup3.findAll('div',attrs= {'class':'pl-2 pl-md-0 text-right flex-auto min-width-0'})


    y=soup.find_all('div',attrs= {'class':'postArticle-content'})
    x1=soup.findAll('span',attrs={'class':'u-relative u-background js-actionMultirecommendCount u-marginLeft5'})
    x2=soup.findAll('div',attrs={'class':'section-inner sectionLayout--insetColumn'})

    
    vids = soup2.findAll('a',attrs={'class':'yt-uix-tile-link'})

    res=ob.med_links(y)
    res1=ob.clapcount(x1)
    res2=ob.med_titles(x2)

    you1 = ob.videotitle(vids)
    you2 = ob.videourl(vids)
   

    cop_desc = soup1.findAll('div',attrs={'class':'col-lg-9 item-content'})
    cop_codelinks =soup1.findAll('div',attrs={'class':'entity'})
    cop_titles = soup1.findAll('h1')

    cop1 = ob.cop_desc(cop_desc)
    cop2 = ob.cop_codelinks(cop_codelinks)
    cop3 = ob.cop_titles(cop_titles)

    
    # git_titles = ob.git_titles(x3)
    # git_links = ob.git_links(y3)
    # git_stars = ob.git_stars(z3)

    rel_words = ob.rel_words(y1)

  

    med_len = 'Found '  +str(len(res2))+ ' contents'
    you_len = 'Found '  +str(len(you1))+ ' contents'
    cop_len = 'Found '  +str(len(cop3))+ ' contents'
    # repos_len = 'Found '  +str(len(x3))+ ' contents'
  ob1 = Sol()
  

  return render(request, 'home1.html', {'med1':'Medium_Website_content','med_len':ob1.med_len,'zip_data':zip( ob1.res2,ob1.res,ob1.res1),'med3':'Clapcounts','data3':ob1.res1,
  'you1':'Youtube_Website_Contents','you_len':ob1.you_len,'you2':'Youtube_links','zip_data1':zip( ob1.you1,ob1.you2),
  'cop3':'Code_With_Papers','cop_len':ob1.cop_len,'cop2':'Cop_links','cop1':'Cop_desc','zip_data2':zip( ob1.cop3,ob1.cop1,ob1.cop2),
  'git0':'Github_Website_Contents','repos_len':ob1.repos_len,'git1':'Repos_links','git2':'Repos_stars','zip_data3':zip(ob1.git_titles,ob1.git_links,ob1.git_stars),
  'search':search,'rel_words':ob1.rel_words })

