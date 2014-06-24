#!/usr/bin/python
# -*- coding: utf-8 -*- 

####################### DARDAR SAAD V 1############################
############### voir plus sur http://goo.gl/hGsZH6 ################

import mechanize
import cookielib
import cgi 
import sys, string
from BeautifulSoup import BeautifulSoup

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>MCNOPS CGI Program - DARDAR SAAD</title>"
print "</head>"
print "<body>"

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

#the variables entered by the user
imm = form.getvalue('immatriculation')
st = imm[0:2]
im = imm[3:9]
af = form.getvalue('passwd')

# The site we will navigate into, handling it's session
br.open('http://196.12.238.169/external-services/www/index.php?module=assure&action=famille:validateadh&statut=' + st +'&sbm=Valider&imm='+ im + '&aff='+ af)


#Read information
response1 = br.follow_link(nr=4)
html = response1.read()
soup = BeautifulSoup(html)

table = soup.find("table")
print """<table align="center" border="1" cellpadding="1" cellspacing="0" >
   <tr bgcolor="#EBD096">
       <th>Nb.Dos</th>
       <th>Etat</th>
       <th>Date Paiement</th>
	   <th>Frais engages</th>
	   <th>Total</th>
   </tr>
 
   <tr>"""
   
for row in table.findAll('tr')[1:]:
    col = row.findAll('td')
    a = col[0].string
    b = col[1].string 
    c = col[2].string 
    d = col[3].string 
    e = col[4].string 
    f = col[5].string 
    g = col[6].string 
    h = col[7].string 
    i = col[8].string 
    j = col[9].string 
	
    print "<td> %s </td> <td> %s </td> <td> %s </td> <td> %s </td> <td> %s </td>    " % (str(b), str(c) , str(d) , str(g) , str(j))
    print """
          </tr> """

print """ </table> """
print """ <p> <pre>
 _______ __    _ _______ _______ _______ 
|       |  |  | |       |       |       |
|       |   |_| |   _   |    _  |  _____|
|       |       |  | |  |   |_| | |_____ 
|      _|  _    |  |_|  |    ___|_____  |
|     |_| | |   |       |   |    _____| |
|_______|_|  |__|_______|___|   |_______|

         #### V1.0 - Alpha - ####
</pre></p> """
print "</body>"
print "</html>"

br.close()
sys.exit()
