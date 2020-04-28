from bs4 import BeautifulSoup as soup
from urllib.request import urlopen 
import csv
import re
import time


def getDep_links(contaiter):
    links = []
    titles = []

    links_ = contaiter.findAll("a")
    for link in links_:
        titles.append(link.text)
        links.append(link.get("href"))
        
    return titles, links



def getTeacherInfo(tlink):
    # print(tlink)
    depClient = urlopen(tlink)
    dept_page = depClient.read()
    depClient.close()
    member_soup = soup(dept_page, "html.parser")

    info_title = member_soup.findAll("div",{"class":"profile-row-left"})
    info =member_soup.findAll("div",{"class":"profile-row-right"})

    headers = ["Name", "Employee ID", "Designation", "Department", "Faculty", "Personal Webpage","E-mail", "Phone","Cell-Phone"]
    valuse = []

    for t in info:
        valuse.append((t.text).replace("-",' '))
    

    print("saving info >>> ",valuse[0] )

    myDict  = dict(zip(headers, valuse))
    with open(file= "teacherS.csv", mode= 'a',encoding='cp850', errors='replace', newline='\n') as f:
        wirtter = csv.DictWriter(f,headers)
        wirtter.writerow(myDict)





def faculty_member_NextPages( dept_url, page_poss):

    time.sleep(0.05)

    print("Page scanning section>>> ", page_poss)
    link = (dept_url[:(len(dept_url)-5)]) + "/" + str(page_poss+20)
    print(link)
    s = len(TeacherProfileLinks)

    goToDep(link)
    if s == len(TeacherProfileLinks):
        return

    poss = page_poss+ 20
    print("Total Collected teachers: " , len(TeacherProfileLinks))

    faculty_member_NextPages(dept_url,poss)

    
            
        
    

# faculty teacher's profile Links
TeacherProfileLinks = []


def goToDep(dept_url ):

    depClient = urlopen(dept_url)
    dept_page = depClient.read()
    depClient.close()
    dept_soup = soup(dept_page, "html.parser")
    teachers_con = dept_soup.findAll("li", {"class":"item item-designer"})

    if len(teachers_con) ==0:
        print("Golla here")
        return

    for teacher in teachers_con:
        TeacherProfileLinks.append(teacher.find("a").get("href"))
        # print(teacher.find("a").get("href"))
    print("teachers ",len(TeacherProfileLinks))





faculty_url = "https://faculty.daffodilvarsity.edu.bd/"
uClient = urlopen(faculty_url)
page_faculty = uClient.read()
uClient.close()

faculty_soup = soup(page_faculty, "html.parser")

facultys_container = faculty_soup.findAll("div",{"class":"columns-col columns-col-6"})

# container0 = facultys_container[1]
# container0_titles = facultys_container[0].text
# print(container0_titles)

for container0 in facultys_container:

    titles , links = getDep_links(container0)

    for link in links:
        goToDep(link)
        faculty_member_NextPages(link, page_poss= 0)
        

print(len(TeacherProfileLinks))

headers = ["Name", "Employee ID", "Designation", "Department", "Faculty", "Personal Webpage","E-mail", "Phone","Cell-Phone"]
   
with open(file= "teacherS.csv", mode= 'w',encoding='cp850', errors='replace', newline='\n') as f:
        wirtter = csv.DictWriter(f,headers)
        wirtter.writeheader()

for teacher in TeacherProfileLinks:
    getTeacherInfo(tlink= teacher)
    
    
    
    
    
    
    
    
    
    
 
