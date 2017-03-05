import pandas as pd

if __name__=="__main__":
    d = pd.read_csv('gtd98_now.csv')

    polity = pd.read_csv('p4v2015.csv')
    polity['country_code'] = polity['scode']
    polity['iyear'] = polity['year']
    pol_merged = d.merge(polity[['country_code', 'iyear', "polity"]])
    print "done pol"

    conflict = pd.read_csv('recent-conflict.csv')
    conflict["country_code"] = conflict["Location ISO"]
    conflict["iyear"] = conflict["Year"]
    conflict_merged = pol_merged.merge(conflict[["country_code", "iyear", "Recent Conflict"]])
    print "done conflict"

    gdp = pd.read_excel('pwt90.xlsx', sheetname="Data")

    gdp["country_name"] = gdp["country"] 
    del gdp["country"] 
    final_merged = conflict_merged.merge(gdp,left_on=['iyear','country_code'], right_on=['year','countrycode'])
    print "done gdp"


    final_merged["country_code_origin"] = final_merged["country_code"]
    # drop repetitive table
    del final_merged["countrycode"]
    del final_merged["country_name"]
    del final_merged["year"]
    final_merged.to_csv("gtd98_now_polity_gdp_violence.csv", encoding="UTF-8")

