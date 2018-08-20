# -*- coding: utf-8 -*-
import requests,json, sys
sys.path.insert(0,'C:/hotshits')
from bs4 import BeautifulSoup
import datetime
import time
import logging
for key in logging.Logger.manager.loggerDict:
    print(key)
    logging.getLogger(key).setLevel(logging.CRITICAL)
logging.getLogger('requests').setLevel(logging.CRITICAL)
logging.getLogger('chardet.charsetprober').setLevel(logging.INFO)

states_dic = {'DC': 'District of Columbia', 'AL': 'Alabama', 'AK': 'Alaska', 'AS': 'American Samoa', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FM': 'Federated States Of Micronesia', 'FL': 'Florida', 'GA': 'Georgia', 'GU': 'Guam', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MH': 'Marshall Islands', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'MP': 'Northern Mariana Islands', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PW': 'Palau', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VI': 'Virgin Islands', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'}

"""
pops = requests.get("https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population")
pops = BeautifulSoup(pops.content,'lxml')
len(pops.findAll("tr"))

populousStates = ["District of Columbia"]
for s in pops.findAll("tr")[1:53]:
    name = s.findAll("td")[2].text.strip()
    if not name == "District of Columbia":
        populousStates.append(name)

populousStates =['District of Columbia', 'California', 'Texas', 'Florida', 'New York', 'Illinois', 'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina', 'Michigan', 'New Jersey', 'Virginia', 'Washington', 'Arizona', 'Massachusetts', 'Tennessee', 'Indiana', 'Missouri', 'Maryland', 'Wisconsin', 'Colorado', 'Minnesota', 'South Carolina', 'Alabama', 'Louisiana', 'Kentucky', 'Oregon', 'Oklahoma', 'Connecticut', 'Puerto Rico', 'Iowa', 'Utah', 'Mississippi', 'Arkansas', 'Nevada', 'Kansas', 'New Mexico', 'Nebraska', 'West Virginia', 'Idaho', 'Hawaii', 'New Hampshire', 'Maine', 'Rhode Island', 'Montana', 'Delaware', 'South Dakota', 'North Dakota', 'Alaska', 'Vermont', 'Wyoming']
pops.findAll("tr")[53].findAll("td")[2].text.strip()


sites = requests.get("https://www.craigslist.org/about/sites")
soup = BeautifulSoup(sites.content,'lxml')
soup.find('h1')
states = soup.findAll("h4")


states_and_regions = []
for state in states:
    if not state.text in states_dic.values():
        continue
    cities = state.find_next_sibling().findAll('li')
    for city in cities:
        states_and_regions.append({'state': state.text, 'link': city.find("a")['href'], 'region': city.text.capitalize()})

d = {k:v for v,k in enumerate(populousStates)}
states_and_regions.sort(key= lambda x: d[x['state']])


cities = state.find_next_sibling()
while True:
    state = cities.find_next_sibling()
    state
    cities
    if not state:
        break
    print (state.text)
    cities = state.find_next_sibling()

new_states = []
for i, v in enumerate(states_and_regions):
    new_states.append(v)
print(new_states)
"""

states_and_regions = [{'state': 'California', 'link': 'https://bakersfield.craigslist.org/', 'region': 'Bakersfield'}, {'state': 'California', 'link': 'https://chico.craigslist.org/', 'region': 'Chico'}, {'state': 'California', 'link': 'https://fresno.craigslist.org/', 'region': 'Fresno / madera'}, {'state': 'California', 'link': 'https://goldcountry.craigslist.org/', 'region': 'Gold country'}, {'state': 'California', 'link': 'https://humboldt.craigslist.org/', 'region': 'Humboldt county'}, {'state': 'California', 'link': 'https://inlandempire.craigslist.org/', 'region': 'Inland empire'}, {'state': 'California', 'link': 'https://losangeles.craigslist.org/', 'region': 'Los angeles'}, {'state': 'California', 'link': 'https://merced.craigslist.org/', 'region': 'Merced'}, {'state': 'California', 'link': 'https://monterey.craigslist.org/', 'region': 'Monterey bay'}, {'state': 'California', 'link': 'https://orangecounty.craigslist.org/', 'region': 'Orange county'}, {'state': 'California', 'link': 'https://palmsprings.craigslist.org/', 'region': 'Palm springs'}, {'state': 'California', 'link': 'https://redding.craigslist.org/', 'region': 'Redding'}, {'state': 'California', 'link': 'https://sacramento.craigslist.org/', 'region': 'Sacramento'}, {'state': 'California', 'link': 'https://sandiego.craigslist.org/', 'region': 'San diego'}, {'state': 'California', 'link': 'https://sfbay.craigslist.org/', 'region': 'San francisco bay area'}, {'state': 'California', 'link': 'https://slo.craigslist.org/', 'region': 'San luis obispo'}, {'state': 'California', 'link': 'https://santabarbara.craigslist.org/', 'region': 'Santa barbara'}, {'state': 'California', 'link': 'https://santamaria.craigslist.org/', 'region': 'Santa maria'}, {'state': 'California', 'link': 'https://ventura.craigslist.org/', 'region': 'Ventura county'}, {'state': 'Texas', 'link': 'https://austin.craigslist.org/', 'region': 'Austin'}, {'state': 'Texas', 'link': 'https://collegestation.craigslist.org/', 'region': 'College station'}, {'state': 'Texas', 'link': 'https://dallas.craigslist.org/', 'region': 'Dallas / fort worth'}, {'state': 'Texas', 'link': 'https://houston.craigslist.org/', 'region': 'Houston'}, {'state': 'Texas', 'link': 'https://sanantonio.craigslist.org/', 'region': 'San antonio'}, {'state': 'Florida', 'link': 'https://daytona.craigslist.org/', 'region': 'Daytona beach'}, {'state': 'Florida', 'link': 'https://fortlauderdale.craigslist.org/', 'region': 'Fort lauderdale'}, {'state': 'Florida', 'link': 'https://fortmyers.craigslist.org/', 'region': 'Ft myers / sw florida'}, {'state': 'Florida', 'link': 'https://gainesville.craigslist.org/', 'region': 'Gainesville'}, {'state': 'Florida', 'link': 'https://jacksonville.craigslist.org/', 'region': 'Jacksonville'}, {'state': 'Florida', 'link': 'https://orlando.craigslist.org/', 'region': 'Orlando'}, {'state': 'Florida', 'link': 'https://pensacola.craigslist.org/', 'region': 'Pensacola'}, {'state': 'Florida', 'link': 'https://sarasota.craigslist.org/', 'region': 'Sarasota-bradenton'}, {'state': 'Florida', 'link': 'https://miami.craigslist.org/', 'region': 'South florida'}, {'state': 'Florida', 'link': 'https://spacecoast.craigslist.org/', 'region': 'Space coast'}, {'state': 'Florida', 'link': 'https://tallahassee.craigslist.org/', 'region': 'Tallahassee'}, {'state': 'Florida', 'link': 'https://tampa.craigslist.org/', 'region': 'Tampa bay area'}, {'state': 'Florida', 'link': 'https://treasure.craigslist.org/', 'region': 'Treasure coast'}, {'state': 'New York', 'link': 'https://buffalo.craigslist.org/', 'region': 'Buffalo'}, {'state': 'New York', 'link': 'https://elmira.craigslist.org/', 'region': 'Elmira-corning'}, {'state': 'New York', 'link': 'https://fingerlakes.craigslist.org/', 'region': 'Finger lakes'}, {'state': 'New York', 'link': 'https://glensfalls.craigslist.org/', 'region': 'Glens falls'}, {'state': 'New York', 'link': 'https://hudsonvalley.craigslist.org/', 'region': 'Hudson valley'}, {'state': 'New York', 'link': 'https://ithaca.craigslist.org/', 'region': 'Ithaca'}, {'state': 'New York', 'link': 'https://longisland.craigslist.org/', 'region': 'Long island'}, {'state': 'New York', 'link': 'https://newyork.craigslist.org/', 'region': 'New york city'}, {'state': 'New York', 'link': 'https://rochester.craigslist.org/', 'region': 'Rochester'}, {'state': 'New York', 'link': 'https://syracuse.craigslist.org/', 'region': 'Syracuse'}, {'state': 'Illinois', 'link': 'https://chicago.craigslist.org/', 'region': 'Chicago'}, {'state': 'Illinois', 'link': 'https://rockford.craigslist.org/', 'region': 'Rockford'}, {'state': 'Pennsylvania', 'link': 'https://harrisburg.craigslist.org/', 'region': 'Harrisburg'}, {'state': 'Pennsylvania', 'link': 'https://allentown.craigslist.org/', 'region': 'Lehigh valley'}, {'state': 'Pennsylvania', 'link': 'https://philadelphia.craigslist.org/', 'region': 'Philadelphia'}, {'state': 'Pennsylvania', 'link': 'https://pittsburgh.craigslist.org/', 'region': 'Pittsburgh'}, {'state': 'Pennsylvania', 'link': 'https://scranton.craigslist.org/', 'region': 'Scranton / wilkes-barre'}, {'state': 'Ohio', 'link': 'https://chillicothe.craigslist.org/', 'region': 'Chillicothe'}, {'state': 'Ohio', 'link': 'https://cincinnati.craigslist.org/', 'region': 'Cincinnati'}, {'state': 'Ohio', 'link': 'https://cleveland.craigslist.org/', 'region': 'Cleveland'}, {'state': 'Ohio', 'link': 'https://columbus.craigslist.org/', 'region': 'Columbus'}, {'state': 'Ohio', 'link': 'https://dayton.craigslist.org/', 'region': 'Dayton / springfield'}, {'state': 'Ohio', 'link': 'https://youngstown.craigslist.org/', 'region': 'Youngstown'}, {'state': 'Georgia', 'link': 'https://atlanta.craigslist.org/', 'region': 'Atlanta'}, {'state': 'Georgia', 'link': 'https://macon.craigslist.org/', 'region': 'Macon / warner robins'}, {'state': 'North Carolina', 'link': 'https://asheville.craigslist.org/', 'region': 'Asheville'}, {'state': 'North Carolina', 'link': 'https://charlotte.craigslist.org/', 'region': 'Charlotte'}, {'state': 'North Carolina', 'link': 'https://fayetteville.craigslist.org/', 'region': 'Fayetteville'}, {'state': 'North Carolina', 'link': 'https://greensboro.craigslist.org/', 'region': 'Greensboro'}, {'state': 'North Carolina', 'link': 'https://raleigh.craigslist.org/', 'region': 'Raleigh / durham / ch'}, {'state': 'North Carolina', 'link': 'https://wilmington.craigslist.org/', 'region': 'Wilmington'}, {'state': 'Michigan', 'link': 'https://annarbor.craigslist.org/', 'region': 'Ann arbor'}, {'state': 'Michigan', 'link': 'https://centralmich.craigslist.org/', 'region': 'Central michigan'}, {'state': 'Michigan', 'link': 'https://detroit.craigslist.org/', 'region': 'Detroit metro'}, {'state': 'Michigan', 'link': 'https://grandrapids.craigslist.org/', 'region': 'Grand rapids'}, {'state': 'Michigan', 'link': 'https://nmi.craigslist.org/', 'region': 'Northern michigan'}, {'state': 'Michigan', 'link': 'https://up.craigslist.org/', 'region': 'Upper peninsula'}, {'state': 'New Jersey', 'link': 'https://cnj.craigslist.org/', 'region': 'Central nj'}, {'state': 'New Jersey', 'link': 'https://newjersey.craigslist.org/', 'region': 'North jersey'}, {'state': 'New Jersey', 'link': 'https://southjersey.craigslist.org/', 'region': 'South jersey'}, {'state': 'Virginia', 'link': 'https://fredericksburg.craigslist.org/', 'region': 'Fredericksburg'}, {'state': 'Virginia', 'link': 'https://norfolk.craigslist.org/', 'region': 'Hampton roads'}, {'state': 'Virginia', 'link': 'https://lynchburg.craigslist.org/', 'region': 'Lynchburg'}, {'state': 'Virginia', 'link': 'https://richmond.craigslist.org/', 'region': 'Richmond'}, {'state': 'Washington', 'link': 'https://bellingham.craigslist.org/', 'region': 'Bellingham'}, {'state': 'Washington', 'link': 'https://olympic.craigslist.org/', 'region': 'Olympic peninsula'}, {'state': 'Washington', 'link': 'https://seattle.craigslist.org/', 'region': 'Seattle-tacoma'}, {'state': 'Washington', 'link': 'https://skagit.craigslist.org/', 'region': 'Skagit / island / sji'}, {'state': 'Washington', 'link': 'https://spokane.craigslist.org/', 'region': "Spokane / coeur d'alene"}, {'state': 'Arizona', 'link': 'https://flagstaff.craigslist.org/', 'region': 'Flagstaff / sedona'}, {'state': 'Arizona', 'link': 'https://phoenix.craigslist.org/', 'region': 'Phoenix'}, {'state': 'Arizona', 'link': 'https://prescott.craigslist.org/', 'region': 'Prescott'}, {'state': 'Arizona', 'link': 'https://tucson.craigslist.org/', 'region': 'Tucson'}, {'state': 'Massachusetts', 'link': 'https://boston.craigslist.org/', 'region': 'Boston'}, {'state': 'Massachusetts', 'link': 'https://westernmass.craigslist.org/', 'region': 'Western massachusetts'}, {'state': 'Massachusetts', 'link': 'https://worcester.craigslist.org/', 'region': 'Worcester / central ma'}, {'state': 'Tennessee', 'link': 'https://knoxville.craigslist.org/', 'region': 'Knoxville'}, {'state': 'Tennessee', 'link': 'https://nashville.craigslist.org/', 'region': 'Nashville'}, {'state': 'Indiana', 'link': 'https://indianapolis.craigslist.org/', 'region': 'Indianapolis'}, {'state': 'Missouri', 'link': 'https://kansascity.craigslist.org/', 'region': 'Kansas city'}, {'state': 'Missouri', 'link': 'https://stlouis.craigslist.org/', 'region': 'St louis'}, {'state': 'Maryland', 'link': 'https://baltimore.craigslist.org/', 'region': 'Baltimore'}, {'state': 'Wisconsin', 'link': 'https://eauclaire.craigslist.org/', 'region': 'Eau claire'}, {'state': 'Wisconsin', 'link': 'https://greenbay.craigslist.org/', 'region': 'Green bay'}, {'state': 'Wisconsin', 'link': 'https://racine.craigslist.org/', 'region': 'Kenosha-racine'}, {'state': 'Wisconsin', 'link': 'https://lacrosse.craigslist.org/', 'region': 'La crosse'}, {'state': 'Wisconsin', 'link': 'https://madison.craigslist.org/', 'region': 'Madison'}, {'state': 'Wisconsin', 'link': 'https://milwaukee.craigslist.org/', 'region': 'Milwaukee'}, {'state': 'Colorado', 'link': 'https://boulder.craigslist.org/', 'region': 'Boulder'}, {'state': 'Colorado', 'link': 'https://cosprings.craigslist.org/', 'region': 'Colorado springs'}, {'state': 'Colorado', 'link': 'https://denver.craigslist.org/', 'region': 'Denver'}, {'state': 'Colorado', 'link': 'https://fortcollins.craigslist.org/', 'region': 'Fort collins / north co'}, {'state': 'Colorado', 'link': 'https://rockies.craigslist.org/', 'region': 'High rockies'}, {'state': 'Colorado', 'link': 'https://westslope.craigslist.org/', 'region': 'Western slope'}, {'state': 'Minnesota', 'link': 'https://brainerd.craigslist.org/', 'region': 'Brainerd'}, {'state': 'Minnesota', 'link': 'https://duluth.craigslist.org/', 'region': 'Duluth / superior'}, {'state': 'Minnesota', 'link': 'https://minneapolis.craigslist.org/', 'region': 'Minneapolis / st paul'}, {'state': 'South Carolina', 'link': 'https://charleston.craigslist.org/', 'region': 'Charleston'}, {'state': 'South Carolina', 'link': 'https://columbia.craigslist.org/', 'region': 'Columbia'}, {'state': 'South Carolina', 'link': 'https://greenville.craigslist.org/', 'region': 'Greenville / upstate'}, {'state': 'Alabama', 'link': 'https://bham.craigslist.org/', 'region': 'Birmingham'}, {'state': 'Alabama', 'link': 'https://dothan.craigslist.org/', 'region': 'Dothan'}, {'state': 'Alabama', 'link': 'https://huntsville.craigslist.org/', 'region': 'Huntsville / decatur'}, {'state': 'Alabama', 'link': 'https://montgomery.craigslist.org/', 'region': 'Montgomery'}, {'state': 'Louisiana', 'link': 'https://batonrouge.craigslist.org/', 'region': 'Baton rouge'}, {'state': 'Louisiana', 'link': 'https://neworleans.craigslist.org/', 'region': 'New orleans'}, {'state': 'Kentucky', 'link': 'https://bgky.craigslist.org/', 'region': 'Bowling green'}, {'state': 'Kentucky', 'link': 'https://lexington.craigslist.org/', 'region': 'Lexington'}, {'state': 'Oregon', 'link': 'https://bend.craigslist.org/', 'region': 'Bend'}, {'state': 'Oregon', 'link': 'https://corvallis.craigslist.org/', 'region': 'Corvallis/albany'}, {'state': 'Oregon', 'link': 'https://eastoregon.craigslist.org/', 'region': 'East oregon'}, {'state': 'Oregon', 'link': 'https://eugene.craigslist.org/', 'region': 'Eugene'}, {'state': 'Oregon', 'link': 'https://oregoncoast.craigslist.org/', 'region': 'Oregon coast'}, {'state': 'Oregon', 'link': 'https://portland.craigslist.org/', 'region': 'Portland'}, {'state': 'Oregon', 'link': 'https://salem.craigslist.org/', 'region': 'Salem'}, {'state': 'Oklahoma', 'link': 'https://oklahomacity.craigslist.org/', 'region': 'Oklahoma city'}, {'state': 'Oklahoma', 'link': 'https://stillwater.craigslist.org/', 'region': 'Stillwater'}, {'state': 'Oklahoma', 'link': 'https://tulsa.craigslist.org/', 'region': 'Tulsa'}, {'state': 'Connecticut', 'link': 'https://newlondon.craigslist.org/', 'region': 'Eastern ct'}, {'state': 'Connecticut', 'link': 'https://hartford.craigslist.org/', 'region': 'Hartford'}, {'state': 'Connecticut', 'link': 'https://newhaven.craigslist.org/', 'region': 'New haven'}, {'state': 'Connecticut', 'link': 'https://nwct.craigslist.org/', 'region': 'Northwest ct'}, {'state': 'Puerto Rico', 'link': 'https://puertorico.craigslist.org/', 'region': 'Puerto rico'}, {'state': 'Iowa', 'link': 'https://ames.craigslist.org/', 'region': 'Ames'}, {'state': 'Utah', 'link': 'https://provo.craigslist.org/', 'region': 'Provo / orem'}, {'state': 'Utah', 'link': 'https://saltlakecity.craigslist.org/', 'region': 'Salt lake city'}, {'state': 'Utah', 'link': 'https://stgeorge.craigslist.org/', 'region': 'St george'}, {'state': 'Nevada', 'link': 'https://lasvegas.craigslist.org/', 'region': 'Las vegas'}, {'state': 'Nevada', 'link': 'https://reno.craigslist.org/', 'region': 'Reno / tahoe'}, {'state': 'Kansas', 'link': 'https://lawrence.craigslist.org/', 'region': 'Lawrence'}, {'state': 'Kansas', 'link': 'https://wichita.craigslist.org/', 'region': 'Wichita'}, {'state': 'New Mexico', 'link': 'https://albuquerque.craigslist.org/', 'region': 'Albuquerque'}, {'state': 'New Mexico', 'link': 'https://roswell.craigslist.org/', 'region': 'Roswell / carlsbad'}, {'state': 'Nebraska', 'link': 'https://lincoln.craigslist.org/', 'region': 'Lincoln'}, {'state': 'Nebraska', 'link': 'https://omaha.craigslist.org/', 'region': 'Omaha / council bluffs'}, {'state': 'Idaho', 'link': 'https://boise.craigslist.org/', 'region': 'Boise'}, {'state': 'Hawaii', 'link': 'https://honolulu.craigslist.org/', 'region': 'Hawaii'}, {'state': 'New Hampshire', 'link': 'https://nh.craigslist.org/', 'region': 'New hampshire'}, {'state': 'Maine', 'link': 'https://maine.craigslist.org/', 'region': 'Maine'}, {'state': 'Rhode Island', 'link': 'https://providence.craigslist.org/', 'region': 'Rhode island'}, {'state': 'Montana', 'link': 'https://bozeman.craigslist.org/', 'region': 'Bozeman'}, {'state': 'Montana', 'link': 'https://kalispell.craigslist.org/', 'region': 'Kalispell'}, {'state': 'Montana', 'link': 'https://missoula.craigslist.org/', 'region': 'Missoula'}, {'state': 'Delaware', 'link': 'https://delaware.craigslist.org/', 'region': 'Delaware'}, {'state': 'North Dakota', 'link': 'https://bismarck.craigslist.org/', 'region': 'Bismarck'}, {'state': 'Wyoming', 'link': 'https://wyoming.craigslist.org/', 'region': 'Wyoming'}]



import psycopg2
from tqdm import trange

with open ("F:/apiFiles/dbConfig.json") as kj:
    keys = json.load(kj)

def get_listings(job_type,region,state,d):
    full_link = '{}d/{}'.format(d['link'],job_type)
    print(full_link)
    r = requests.get(full_link)
    r.encoding='utf-8'
    soup=BeautifulSoup(r.content,'lxml')
    full_list = soup.find('ul',{'class':'rows'})
    if not full_list:
        return None
    return full_list.findAll('li',{'class':'result-row'})

# Data saving / retrieval portion and functions, move to other file soon
conn = psycopg2.connect(database=keys['database'],user=keys['user'],password=keys['password'],host=keys['host'])
conn.set_isolation_level(0)
cur = conn.cursor()

def check_id(ID):
    cur.execute("SELECT id FROM checked_ids WHERE ID = '{}'".format(ID))
    previous = [c for c in cur]
    return True if previous else False

import spacy
nlp = spacy.load('en')

def add_id_to_checked_list(ID):
    print("Adding ID: {}".format(ID))
    cur.execute("INSERT INTO checked_ids (id) VALUES (%s)",[ID])

def is_duplicate_job(body,month,day,title,ID):
    doc = nlp(body)
    cur.execute('SELECT body FROM listings WHERE day = (%s) and month = (%s) and title = (%s) and id != (%s)',[day, month,title,str(ID)])
    res = [c for c in cur]
    for o in res:
        if nlp(o[0]).similarity(doc) > 0.95:
            add_id_to_checked_list(ID)
            return True
    return False

def add_job(region,state,link, day, month, location,title,post,ID, timestamp):
    try:
        body = str(post)
        if is_duplicate_job(body,month,day,title,ID):
            return False
        cur.execute("""INSERT INTO listings
        (region, state, link, day, month, location, title, body, id, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (region,state,link, day, month, location,title,body,ID, timestamp ))
        cur.execute("UPDATE listings SET tokens = (setweight(to_tsvector(title), 'A') || setweight(to_tsvector(body), 'B')) WHERE ID = '{}';".format(ID))
        add_id_to_checked_list(ID)
        return True
    except Exception as e:
        print(e)
        return False

def get_job_details(link):
    j = requests.get(link)
    j.encoding='utf-8'
    job = BeautifulSoup(j.content,'lxml')
    post = job.find("section", {"class":"userbody"})
    return post


def get_job(listing,region,state):
    try:
        loc = listing.find('span',{'class': 'result-hood'}).text
    except:
        return None
    try:
        location = loc[loc.index("(")+1:loc.index(")")] if "(" in loc and ")" in loc else loc
        job = listing.find('a',{'class': 'result-title hdrlnk'})
        link, title = job['href'], job.text.lstrip().replace("\n","")
        posting_date = listing.find('time').text
        try:
            date = datetime.datetime.strptime(listing.find('time')['datetime'],'%Y-%m-%d %H:%S')
        except:
            date = datetime.datetime.strptime(posting_date, '%b %d')
        timestamp = int(date.timestamp())
        month = date.month
        day = date.day
        ID = str(int(link.split("/")[-1].replace('.html','')))
        previous = check_id(ID)
        if not previous:
            post = get_job_details(link)
            was_new_job = add_job(region,state,link, day, month, location,title,post,ID, timestamp)
            if was_new_job:
                print("{} ({}-{} #{})".format(title,day,month,ID))
                return "new"
            else:
                return "old"
        else:
            return "old"
    except Exception as e:
        print (e)
        return

import tqdm
def scrape_jobs(job_types,full_page_sleep,job_sleep):
    new = 0
    total = 0
    i = 0
    exclude = []
    for y in tqdm.tqdm(range(len(states_and_regions))):
        for job_type in job_types:
            d = states_and_regions[y]
            region = d['region']
            state = d['state']
            listings = get_listings(job_type,region,state,d)
            if not listings:
                exclude.append(i)
                i += 1
                continue
            t = 0
            for z in range(len(listings)):
                total += 1
                listing = listings[z]
                got_job = get_job(listing,region,state)
                if got_job:
                    t += 1
                    if got_job == "new":
                        new += 1
                        time.sleep(job_sleep)
            i += 1
            time.sleep(full_page_sleep)
            if not t:
                exclude.append(i)
    print("Consider excluding the following: {}".format(exclude))
    print("There were a total of {} new out of {} total listings".format(new,total))

job_types = ['web-html-info-design/search/web','software-qa-dba-etc/search/sof','systems-networking/search/sad']
full_page_sleep = 0.1
job_sleep = 0.05

scrape_jobs(job_types,full_page_sleep,job_sleep)
