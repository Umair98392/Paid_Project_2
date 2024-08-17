import csv, sqlite3

con = sqlite3.connect('home_database') # change to 'sqlite:///your_filename.db'
cur = con.cursor()
#cur.execute("CREATE TABLE apis_localitydescription (Id, MSSubClass, MSZoning, LotFrontage, #LotArea, Street, Alley, LotShape, LandContour, Utilities, LotConfig, LandSlope, #Neighborhood);") # use your column names here

with open('locality_data.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['Id'], i['MSSubClass'], i['MSZoning'], i['LotFrontage'], i['LotArea'], i['Street'], i['Alley'], i['LotShape'], i['LandContour'], i['Utilities'], i['LotConfig'], i['LandSlope'], i['Neighborhood']) for i in dr]

cur.executemany("INSERT OR IGNORE INTO apis_localitydescription (Id, MSSubClass, MSZoning, LotFrontage, LotArea, Street, Alley, LotShape, LandContour, Utilities, LotConfig, LandSlope, Neighborhood)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? );", to_db)
con.commit()
con.close()
