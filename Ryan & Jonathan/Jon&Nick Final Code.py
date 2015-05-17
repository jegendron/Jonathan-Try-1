#We first built a blank data frame, built website urls, ran all urls through 
#and scraped the HTML code for price. The new price was added to the data 
#frame and then graphs were run on the price data to compare them.

#The code was run 4/29/15 at 9am to collect price data
#Any of the save commands are saved to a flashdrive with a specified folder path


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

df = pd.DataFrame({'Game Title': ['Grand Theft Auto V','Bioshock Infinite', \
                        'Dead Space 3', 'Tomb Raider','Hitman Absolution', \
                        'Need for Speed Most Wanted','Resident Evil 6','Skyrim', \
                        'Resident Evil 5','Fallout 3', \
                        'Burnout Paradise','Grand Theft Auto IV','Dead Space',\
                        'Street Fighter IV']})
vendorList = [ \
    'Amazon PS3',\
    'Amazon X360',\
    'Gamestop PS3',\
    'Gamestop X360',\
    'Walmart PS3',\
    'Walmart X360',\
    'Steam']
for vendor in vendorList:
    df[vendor] = pd.Series(['0'], index = df.index)
print (df)
#The data frame is created and filled with zeros to start

b= ' playstation 3'
c= ' xbox 360'
#b & c will be used to create website search urls

##################################################################
#Amazon...
##################################################################
#"root url"
a1url = 'http://www.amazon.com/s?keywords='
aburl=[]
for i in range(len(df['Game Title'])):
    n = a1url+df['Game Title'][i]+b
    n = n.replace(' ','%20')
    aburl[len(aburl):] = [n]
print (aburl)
#The loop adds term to the root url to mimick typing the term in the search bar
#the aburl vector has the search links for playstation 3 on amazon

acurl=[]
for i in range(len(df['Game Title'])):
    n = a1url+df['Game Title'][i]+c
    n = n.replace(' ','%20')
    acurl[len(acurl):] = [n]
print (acurl)
#the acurl vector has the search links for xbox 360 games on amazon

######################################################
#This loop takes the aburl and acurl vectors and opens each individual url
#and scrapes the price from the html source code
for j in range(2):
    for i in range(len(df['Game Title'])):
        print('Game {} out of {}'.format(i, len(df['Game Title'])))
        print('-------------------------------------')
        #try:
        if j == 0:
            html = urlopen(acurl[i]).read()
        else:
            html = urlopen(aburl[i]).read()
        soup = BeautifulSoup(html.decode('utf-8', 'ignore'))
        try:
            r = soup.find("div",{"class":"a-row a-spacing-small"}).find(href=True)#.find("class")
            t = r.attrs.get('href')
            #print (t)
            #Follow link and scrape price from product site
            html = urlopen(t).read()
            soup = BeautifulSoup(html.decode('utf-8', 'ignore'))
            price = soup.find("span",{"id":"actualPriceValue"})
            y=(price.string)
            y = y.replace('$','')
        except:
                y = np.nan
        print('price of game: ', y)
        if j == 0:
            df['Amazon PS3'][i] = y
        else:
            df['Amazon X360'][i] = y
print (df)

#the scraped price values are then stored into the data frame, if the loop 
#did not work, then an empty value is given so the loop doesn't break

df['Amazon PS3'][1]='17.90'
df['Amazon PS3'][2]='15.99'
df['Amazon PS3'][3]='26.99'
df['Amazon PS3'][5]='19.99'
df['Amazon PS3'][7]='17.59'
df['Amazon PS3'][9]='18.00'
df['Amazon PS3'][10]='22.79'
df['Amazon PS3'][13]='12.20'
df['Amazon X360'][1]='9.99'
df['Amazon X360'][2]='17.99'
df['Amazon X360'][3]='19.99'
df['Amazon X360'][7]='17.59'
df['Amazon X360'][8]='13.53'
df['Amazon X360'][9]='10.19'
df['Amazon X360'][10]='23.74'
df['Amazon X360'][13]='10.73'

#Python would many times time out and provide blank values although there was
#the item for sale in question. These were hardcoded to fix that issue

#The first time I ran this and forgot to save the data, I only had to hardcode 
#half of what was here, I tried again after this, but I was blocked 
#out actually 

########################################################
#Gamestop
########################################################
#"root url"
g1url = 'http://www.gamestop.com/browse?nav=16k-'
u = 'http://www.gamestop.com'

gburl=[]
for i in range(len(df['Game Title'])):
    n = g1url + df['Game Title'][i] + b
    n = n.replace(' ','%20')
    gburl[len(gburl):] = [n]
#print (gburl)

#The loop adds term to the root url to mimick typing the term in the search bar
#the gburl vector has the search links for playstation 3 on gamestop

gcurl=[]
for i in range(len(df['Game Title'])):
    n = g1url + df['Game Title'][i] + c
    n = n.replace(' ','%20')
    gcurl[len(gcurl):] = [n]
#print (gcurl)   
#the gcurl vector has the search links for playstation 3 on gamestop
    
###############################################################
#This loop scrapes the website and grabs the price values in a similar for loop
#that amazon did (lines 61-88)
for j in range(2):
    for i in range(len(df['Game Title'])):
        print('Game {} out of {}'.format(i, len(df['Game Title'])))
        print('-------------------------------------')
        try:
            if j == 0:
                html = urlopen(gcurl[i]).read()
            else:
                html = urlopen(gburl[i]).read()
                
            soup = BeautifulSoup(html.decode('utf-8', 'ignore'))
            try:
                # [A] Regular site with multiple listings, picks the first link
                r = soup.find("div",{"class":"product_info grid_12"}).find(href=True) #.find("class")
                t = r.attrs.get('href')
                print('link to game: ', t)
                #shows the link to the game so we can check for accuracy
                q = u + t
                # Follow link and scrape price from product site
                html = urlopen(q).read()
                soup = BeautifulSoup(html.decode('utf-8', 'ignore'))
                price = soup.find("div",{"class":"buy1"}).find("h3").find("span")
                r = price.string
                r = r.replace('$','')
                #removes the dollar sign notation
            except:
                # If search results in one match, it directly jumps to product page
                # We then need to scrape the price differently.....
                a = str(soup.find_all('script', attrs={'language': 'JavaScript'}))
                r = float(re.findall(r'\d+\.\d+', a)[0])
        except:
            r = np.nan
            #stops python from automatically timing out
        print('price of game: ', r)
        if j == 0:
            df['Gamestop PS3'][i] = r
        else:
            df['Gamestop X360'][i] = r

df['Gamestop PS3'][1]='19.99'
df['Gamestop PS3'][3]='29.99'
df['Gamestop PS3'][5]='19.99'
df['Gamestop PS3'][6]='19.99'
df['Gamestop PS3'][8]='19.99'
df['Gamestop X360'][0]='29.99'
df['Gamestop X360'][1]='19.99'
df['Gamestop X360'][3]='29.99'
df['Gamestop X360'][5]='19.99'
df['Gamestop X360'][8]='17.99'

#I had to hardcode for these errors

##################################################################
#Steam
##################################################################
#"root url"
s1url = 'http://store.steampowered.com/search/?snr=1_4_4__12&term='
u = 'http://store.steampowered.com'
surl=[]
for i in range(len(df['Game Title'])):
    n = s1url+df['Game Title'][i]
    n = n.replace(' ','%20')
    surl[len(surl):] = [n]
#print (ssurl)

#here only run one loop because steam is a seperate platform that is not xbox 
#or playstation, so search for the game title by itself without b or c

###################################################################
#a simpler loop is used since it does not need to run again for a second vendor
#since steam is it's own platform
for i in range(len(df['Game Title'])):
    print('Game {} out of {}'.format(i, len(df['Game Title'])))
    print('-------------------------------------')
    try:
        html = urlopen(surl[i]).read()
        soup = BeautifulSoup(html.decode('utf-8', 'ignore'))
        try:
            price = soup.find("div",{"class":"col search_price "})
            r=(price.string)
            #print (r)
            r = r.replace('$','')
            q= re.findall(r'\d+', r)
            t= (q[0]+'.'+q[1])
        except:
            pass
            #so python doesn't time out
    except:
        t = np.nan
        #so python doesn't time out
    print('price of game: ', t)
    df['Steam'][i] = t

df['Steam'][13] = '19.99'
#There was one error which we had to hardcoded for

##################################################################
#Walmart
##################################################################
#"root url"
w1url = 'http://www.walmart.com/search/?query='
u = 'http://www.walmart.com'
wburl=[]
for i in range(len(df['Game Title'])):
    n = w1url+df['Game Title'][i]+b
    n = n.replace(' ','%20')
    wburl[len(wburl):] = [n]
#print (wburl)

#The loop adds term to the root url to mimick typing the term in the search bar
#the Wburl vector has the search links for playstation 3 on walmart

wcurl=[]
for i in range(len(df['Game Title'])):
    n = w1url+df['Game Title'][i]+c
    n = n.replace(' ','%20')
    wcurl[len(wcurl):] = [n]
#print (wcurl)
#the Wcurl vector has the search links for playstation 3 on walmart

##################################################################
#scrape the site for the price just like the amazon and gamestop example and
#add it into the data frame
for j in range(2):
    for i in range(len(df['Game Title'])):
        print('Game {} out of {}'.format(i, len(df['Game Title'])))
        print('-------------------------------------')
        try:
            if j == 0:
                html = urlopen(wcurl[i]).read()
            else:
                html = urlopen(wburl[i]).read()
                
            soup = BeautifulSoup(html.decode('utf-8', 'ignore'))
            try:
                r = soup.find("a",{"class":"js-product-image"})
                t = r.attrs.get('href')
                #print (t)
                q=u+t
                html = urlopen(q).read()
                soup = BeautifulSoup(html.decode('utf-8', 'ignore'))
                x = soup.find("div",{"class": "js-price-display price price-display"})
                r= (x.get_text())
                r = r.replace('$','')
                print (r)
            except:
                pass
        except:
            r = np.nan    
        print('price of game: ', r)
        if j == 0:
            df['Walmart PS3'][i] = r
        else:
            df['Walmart X360'][i] = r
print (df)            

df['Walmart PS3'][3] = np.nan
df['Walmart PS3'][11] = '19.96'
df['Walmart PS3'][12] = np.nan
df['Walmart X360'][3] = '17.05'
df['Walmart X360'][7] = '18.99'
df['Walmart X360'][11] = '15.99'
df['Walmart X360'][12] = np.nan

#The following needed to be hard coded

########################################################
########################################################
#The data frame values are filled, so convert the strings and other types into
#usable numbers
            
df['Amazon PS3'] = df['Amazon PS3'].astype(float)
df['Amazon X360'] = df['Amazon X360'].astype(float)

df['Gamestop PS3'] = df['Gamestop PS3'].astype(float)
df['Gamestop X360'] = df['Gamestop X360'].astype(float)

df['Walmart PS3'] = df['Walmart PS3'].astype(float)
df['Walmart X360'] = df['Walmart X360'].astype(float)

df['Steam'] = df['Steam'].astype(float)

#after the data frame is converted from strings to numbers we then save it
#df.save('G:/Files/College_Folders/ECON_470/Group_Project/Dataframe.pkl') 
df = pd.load('G:/Files/College_Folders/ECON_470/Group_Project/Dataframe.pkl')

#replace the spaces with underscores for the title so we can run the 
#future correlation commands
df = df.rename(columns={'Amazon PS3': 'Amazon_PS3', 'Amazon X360': 
'Amazon_X360', 'Gamestop PS3': 'Gamestop_PS3', 'Gamestop X360': 'Gamestop_X360',
'Walmart PS3' : 'Walmart_PS3','Walmart X360' : 'Walmart_X360'})

#to make a dataframe that shows the release dates and publishers
#put the game titles into a new data frame, then just fill values
df9 = pd.DataFrame(df['Game Title'])

df9['Release Date'] = pd.Series(['-'], index = df9.index)
df9['Publisher'] = pd.Series(['-'], index = df9.index)

df9['Release Date'][0] = '2013'
df9['Release Date'][1] = '2013'
df9['Release Date'][2] = '2013'
df9['Release Date'][3] = '2013'
df9['Release Date'][4] = '2012'
df9['Release Date'][5] = '2012'
df9['Release Date'][6] = '2012'
df9['Release Date'][7] = '2011'
df9['Release Date'][8] = '2009'
df9['Release Date'][9] = '2008'
df9['Release Date'][10] = '2008'
df9['Release Date'][11] = '2008'
df9['Release Date'][12] = '2008'
df9['Release Date'][13] = '2008'

df9['Publisher'][0] = 'Rockstar Games'
df9['Publisher'][1] = '2K'
df9['Publisher'][2] = 'EA'
df9['Publisher'][3] = 'Square Enix'
df9['Publisher'][4] = 'Square Enix'
df9['Publisher'][5] = 'EA'
df9['Publisher'][6] = 'Capcom'
df9['Publisher'][7] = 'Bethesda'
df9['Publisher'][8] = 'Capcom'
df9['Publisher'][9] = 'Bethesda'
df9['Publisher'][10] = 'EA'
df9['Publisher'][11] = 'Rockstar Games'
df9['Publisher'][12] = 'EA'
df9['Publisher'][13] = 'Capcom'

#df9.save('G:/Files/College_Folders/ECON_470/Group_Project/PublisherList.pkl') 
df9 = pd.load('G:/Files/College_Folders/ECON_470/Group_Project/PublisherList.pkl')

#provides full summary statistics and puts it into a new data frame
#lines 380-383 were used to make the df2 loaded from 383 & 384

#df2= df.describe()
#df2.index.names = ['Summary Stats']

#df2.save('G:/Files/College_Folders/ECON_470/Group_Project/AggregateSumStats.pkl')
df2 = pd.load('G:/Files/College_Folders/ECON_470/Group_Project/AggregateSumStats.pkl')

#these are the basic summary statistics without the count, 25% & 75% made into
#a new data frame.....
#df3 = df2.drop(df2.index[[0,4,6]])

#df3.save('G:/Files/College_Folders/ECON_470/Group_Project/SumStats.pkl')
df3 = pd.load('G:/Files/College_Folders/ECON_470/Group_Project/SumStats.pkl')

#This new data frame does summary statistics without the following outliers

#df['Walmart_X360'][0]='NaN'
#df['Walmart_PS3'][0]='NaN'
#df['Walmart_X360'][4]='NaN'
#df['Walmart_PS3'][4]='NaN'
#df['Steam'][0]='NaN'
#df['Steam'][6]='NaN'
#df4= df.describe()

#df4.save('G:/Files/College_Folders/ECON_470/Group_Project/SumStatsFixed.pkl')
df4 = pd.load('G:/Files/College_Folders/ECON_470/Group_Project/SumStatsFixed.pkl')

#this data frame are basic sum stats without the count, 25% & 75% rows
#df5 = df4.drop(df2.index[[0,4,6]])
#df5.index.names = ['Summary Stats']

#df5.save('G:/Files/College_Folders/ECON_470/Group_Project/CondenseSumStatsFixed.pkl')
df5 = pd.load('G:/Files/College_Folders/ECON_470/Group_Project/CondenseSumStatsFixed.pkl')
#####################################################################
#The following is a data frame that shows all of the correlations we ran

df6 = pd.DataFrame({'Correlations': ['Amazon PS3', 'Amazon X360', 'Gamestop PS3',\
    'Gamestop X360', 'Walmart PS3', 'Walmart X360', 'Steam']})

#We didn't run correlations on these so they are filled with blank values

#df6['Amazon PS3'] = pd.Series(['-'], index = df6.index)
#df6['Amazon X360'] = pd.Series(['-'], index = df6.index)
#df6['Gamestop PS3'] = pd.Series(['-'], index = df6.index)
#df6['Gamestop X360'] = pd.Series(['-'], index = df6.index)
#df6['Walmart PS3'] = pd.Series(['-'], index = df6.index)
#df6['Walmart X360'] = pd.Series(['-'], index = df6.index)
#df6['Steam'] = pd.Series(['-'], index = df6.index)

#These are the same variable against itself, so it will automatically be 1
#df6['Amazon PS3'][0] = 1
#df6['Amazon X360'][1] = 1
#df6['Gamestop PS3'][2] = 1
#df6['Gamestop X360'][3] = 1
#df6['Walmart PS3'][4] = 1
#df6['Walmart X360'][5] = 1
#df6['Steam'][6] = 1

#df6.save('G:/Files/College_Folders/ECON_470/Group_Project/Correlationtable.pkl')
df6 = pd.load('G:/Files/College_Folders/ECON_470/Group_Project/Correlationtable.pkl')

############################################################################
#All the following run correlations between columns
#to do this, df and df2 must be already loaded

#Company A Xbox 360 correlated to Company A PS3 games
df6['Amazon PS3'][1] = df.Amazon_X360.corr(df.Amazon_PS3)
df6['Amazon X360'][0] = df.Amazon_X360.corr(df.Amazon_PS3)
#Amazon Xbox 360 versus PS3 correlation

df6['Gamestop PS3'][3] = df.Gamestop_X360.corr(df.Gamestop_PS3)
df6['Gamestop X360'][2] = df.Gamestop_X360.corr(df.Gamestop_PS3)
#Gamestop Xbox 360 versus PS3 correlation

df6['Walmart PS3'][5] = df.Walmart_X360.corr(df.Walmart_PS3)
df6['Walmart X360'][4] = df.Walmart_X360.corr(df.Walmart_PS3)
#Walmart Xbox 360 versus PS3 correlation

############################################################################
#All companies Xbox 360 correlated to each other in various pairs
df6['Amazon X360'][3] = df.Amazon_X360.corr(df.Gamestop_X360)
df6['Gamestop X360'][1] = df6['Amazon X360'][3]
#Amazon versus Gamestop for Xbox 360 correlation

df6['Amazon X360'][5] = df.Amazon_X360.corr(df.Walmart_X360)
df6['Walmart X360'][1] = df6['Amazon X360'][5]
#Amazon versus Walmart for Xbox 360 correlation

df6['Gamestop X360'][5] = df.Gamestop_X360.corr(df.Walmart_X360)
df6['Walmart X360'][3] = df6['Gamestop X360'][5]
#Gamestop versus Walmart for Xbox 360 correlation

############################################################################
#All companies PS3 correlated to each other in various pairs
df6['Amazon PS3'][2] = df.Amazon_PS3.corr(df.Gamestop_PS3)
df6['Gamestop PS3'][0] = df6['Amazon PS3'][2]
#Amazon versus Gamestop for PS3 correlation

df6['Amazon PS3'][4] = df.Amazon_PS3.corr(df.Walmart_PS3)
df6['Walmart PS3'][0] = df6['Amazon PS3'][4]
#Amazon versus Walmart for PS3 correlation

df6['Gamestop PS3'][4] = df.Gamestop_PS3.corr(df.Walmart_PS3)
df6['Walmart PS3'][2] = df6['Gamestop PS3'][4]
#Gamestop versus Walmart for PS3 correlation

############################################################################
#All companies Xbox 360 correlated to Steam
df6['Amazon X360'][6] = df.Amazon_X360.corr(df.Steam)
df6['Steam'][1] = df6['Amazon X360'][6]
#Amazon's Xbox 360 versus Steam correlation

df6['Gamestop X360'][6] = df.Gamestop_X360.corr(df.Steam)
df6['Steam'][3] = df6['Gamestop X360'][6]
#Gamestop Xbox 360 versus Steam correlation

df6['Walmart X360'][6] = df.Walmart_X360.corr(df.Steam)
df6['Steam'][5] = df6['Walmart X360'][6]
#Walmart Xbox 360 versus Steam correlation

############################################################################
#All companies PS3 correlated to Steam
df6['Amazon PS3'][6] = df.Steam.corr(df.Amazon_PS3)
df6['Steam'][0] = df6['Amazon PS3'][6]
#Amazon PS3 versus Steam correlation

df6['Gamestop PS3'][6] = df.Steam.corr(df.Gamestop_PS3)
df6['Steam'][2] = df6['Gamestop PS3'][6]
#Gamestop PS3 versus Steam correlation

df6['Walmart PS3'][6] = df.Steam.corr(df.Walmart_PS3)
df6['Steam'][4] = df6['Walmart PS3'][6]
#Walmart PS3 vs Steam correlation

##############################################################################
#To relabel the games into a shorter title that fits in the upcoming graphs
df['Game Title'] = ['Grand Theft Auto V','Bioshock Infinite', \
                        'Dead Space 3', 'Tomb Raider','Hitman Absolution', \
                        'NFS Most Wanted','Resident Evil 6','Skyrim', \
                        'Resident Evil 5','Fallout 3', \
                        'Burnout Paradise','Grand Theft Auto IV','Dead Space',\
                        'Street Fighter IV']
##############################################################################
#Graphs!!!
##############################################################################
#This graphs all of the games sold on Amazon
tv = df['Amazon_X360'].values
xv = df['Amazon_PS3'].values
#pulls values from the 1st data frame

#Parameters created for the bar graph
N=len(tv)
ind = np.arange(N)
width = 0.3

#lines 536-538 change the dimensions of the graph so you can save it, if you
#don't do this, it will cut off part of the graph
fig = plt.figure()
fig.subplots_adjust(bottom=0.35)
ax = fig.add_subplot(111)

#rects1&2 are used to show 2 variables compared on the same bar graph
rects1 = ax.bar(ind, tv, width, color='green')
rects2 = ax.bar(ind+width, xv, width, color='blue')                        
                        
ax.set_xticks(.2 + np.arange(len(xv)))
ax.set_ylabel('Price')
ax.set_xlabel('Game Title')
ax.set_title('Amazon')
xTickMarks = [str(df['Game Title'][i]) for i in range(len(df['Game Title']))]
#This allows the x values to be the categorical variable of 'Game Title'
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=75, fontsize=7.5)
#This allows you to format how large and at what angle the label goes
ax.legend((rects1[0], rects2[0]), ('X360','PS3'),loc='best')
#plots a key    
plt.show()
fig.savefig('G:/Files/College_Folders/ECON_470/Group_Project/Graphs/GraphAmazon.png')
#saves the graph

###############################################################################
#This graphs all of the games sold on Gamestop
tv = df['Gamestop_X360'].values
xv = df['Gamestop_PS3'].values
#pulls values from the 1st data frame

#Parameters created for the bar graph
N=len(tv)
ind = np.arange(N)
#width already coded

#formats the graph so it can save
fig = plt.figure()
fig.subplots_adjust(bottom=0.35)
ax = fig.add_subplot(111)

#rects1&2 are used to show 2 variables compared on the same bar graph
rects1 = ax.bar(ind, tv, width, color='green')
rects2 = ax.bar(ind+width, xv, width, color='blue')
                        
                        
ax.set_xticks(.2 + np.arange(len(xv)))
ax.set_ylabel('Price')
ax.set_xlabel('Game Title')
ax.set_title('Gamestop')
xTickMarks = [str(df['Game Title'][i]) for i in range(len(df['Game Title']))]
#This allows the x values to be the categorical variable of 'Game Title'
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=75, fontsize=7.5)
#This allows you to format how large and at what angle the label goes
ax.legend((rects1[0], rects2[0]), ('X360','PS3'),loc='best')    
#plots a key    
plt.show()
fig.savefig('G:/Files/College_Folders/ECON_470/Group_Project/Graphs/GraphGamestop.png')
#saves the graph

###############################################################################
#This graphs all of the games sold on just Walmart
tv = df['Walmart_X360'].values
xv = df['Walmart_PS3'].values
#pulls values from the 1st data frame

N=len(tv)
ind = np.arange(N)
#width already coded

#formats the graph so it can save
fig = plt.figure()
fig.subplots_adjust(bottom=0.35)
ax = fig.add_subplot(111)

#rects1&2 are used to show 2 variables compared on the same bar graph
rects1 = ax.bar(ind, tv, width, color='green')
rects2 = ax.bar(ind+width, xv, width, color='blue')
                        
                        
ax.set_xticks(.2 + np.arange(len(xv)))
ax.set_ylabel('Price')
ax.set_xlabel('Game Title')
ax.set_title('Walmart')
xTickMarks = [str(df['Game Title'][i]) for i in range(len(df['Game Title']))]
#This allows the x values to be the categorical variable of 'Game Title'
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=75, fontsize=7.5)
#This allows you to format how large and at what angle the label goes
ax.legend((rects1[0], rects2[0]), ('X360','PS3'),loc='best')    
#plots a key    
plt.show()
fig.savefig('G:/Files/College_Folders/ECON_470/Group_Project/Graphs/GraphWalmart.png')
#saves graph

###############################################################################
#This graphs all of the games sold on just Steam
tv = df['Steam'].values
N=len(tv)
ind = np.arange(N)
#width already coded

#formats the graph so it can save
fig = plt.figure()
fig.subplots_adjust(bottom=0.35)
ax = fig.add_subplot(111)

#The code is simpler since there are not 2 values being plotted, but just one.
ax.bar(1 + np.arange(len(tv)), tv, align='center', color='red')
                                           
ax.set_xticks(1.1 + np.arange(len(tv)))
ax.set_ylabel('Price')
ax.set_xlabel('Game Title') 
ax.set_title('Steam')
xTickMarks = [str(df['Game Title'][i]) for i in range(len(df['Game Title']))]
#This allows the x values to be the categorical variable of 'Game Title'
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=75, fontsize=7.5)
#This allows you to format how large and at what angle the label goes
plt.show()
fig.savefig('G:/Files/College_Folders/ECON_470/Group_Project/Graphs/GraphSteam.png')
#saves the graph

#######################################################################
#One graph per each individual game, with all sites included
#######################################################################

#tv vector is filled with 5 zeros, so when the graphs plot, it fills value only
#for steam and not for any other vendor, hard-coded essentially
qv=['Amazon','Gamestop','Walmart','Steam']
yv=[]
uv=[]
iv=[]
tv=[0,0,0]

#Parameters created for the bar graph
N=4
width = 0.35  

for i in range(len(df['Game Title'])):    
    plt.close('all')
    
    #The loop pulls the same index from all websites at the same time, so 
    #an individual game title is compared between all websites in all versions

    #This entire loop pulls values from the 1st data frame
    #yv is the x360 vector, iv is the ps3 vector and tv is the steam vector  
    xv = df['Amazon_X360'].values
    zv = xv[i] 
    yv[len(yv):] = [zv]
    xv = df['Gamestop_X360'].values
    zv = xv[i]
    yv[len(yv):] = [zv]
    xv = df['Walmart_X360'].values
    zv = xv[i]
    yv[len(yv):] = [zv]
    yv[len(yv):] = [0]   
    xv = df['Amazon_PS3'].values
    zv = xv[i] 
    iv[len(iv):] = [zv]
    xv = df['Gamestop_PS3'].values
    zv = xv[i]
    iv[len(iv):] = [zv]
    xv = df['Walmart_PS3'].values
    zv = xv[i]
    iv[len(iv):] = [zv]
    iv[len(iv):] = [0]
    
    xv = df['Steam'].values
    zv = xv[i]
    tv[len(tv):] = [zv]

   
    ind = np.arange(len(iv))
    fig, ax = plt.subplots()
    
    #these graph ps3 values with xbox 360 values
    rects1 = ax.bar(ind, yv, width, color='green')
    rects2 = ax.bar(ind+width, iv, width, color='blue')

    rects3 = ax.bar(ind+(width/2), tv, width, color='red')
    #this new rects3 is the value for the website steam
    #it is never graphed with xbox or ps3, but for it to be different it must
    #be coded as a 3rd value    
    ax.set_ylabel('Price')
    ax.set_xlabel('Merchant')
    ax.set_title('{}'.format(df['Game Title'][i]))
    #title will change for each iteration so the graphs are seperate
    xTickMarks = [str(qv[i]) for i in range(4)]
    #this allows x to be the categorical title for each individual merchant
    ax.set_xticks(.3+np.arange(len(yv)))
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=25, fontsize=10)
    #This allows you to format how large and at what angle the label goes
    ax.legend((rects1[0], rects2[0], rects3[0]), ('X360','PS3','Steam'),loc='best')    
    #makes a key
    plt.show()
    fig.savefig('G:/Files/College_Folders/ECON_470/Group_Project/Graphs/{} Graph.png'.format(df['Game Title'][i]))    
    #saves each graph as the game title, this allows all the graphs to save at
    #once and not over write each other    
    yv=[]
    iv=[]
    tv=[0,0,0]
    
    #it is important to continually empty the vectors at the end of each iteration,
    #so df values do not overlap in the graphs
    
"""Thank you for looking at our source code!"""