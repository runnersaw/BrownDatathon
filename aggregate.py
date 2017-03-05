import pandas as pd
from database import data

if __name__=="__main__":
    polity = pd.read_csv('./files/p4v2015.csv')
    polity['country_code'] = polity['scode']
    polity['iyear'] = polity['year']
    pol_merged = data.merge(polity[['country_code', 'iyear', "polity"]], how='left')
    print "done pol"

    conflict = pd.read_csv('./files/recent-conflict.csv')
    conflict["country_code"] = conflict["Location ISO"]
    conflict["iyear"] = conflict["Year"]
    conflict_merged = pol_merged.merge(conflict[["country_code", "iyear", "Recent Conflict"]], how='left')
    print "done conflict"

    gdp = pd.read_excel('./files/pwt90.xlsx', sheetname="Data")

    gdp["country_name"] = gdp["country"]
    del gdp["country"]
    final_merged = conflict_merged.merge(gdp,left_on=['iyear','country_code'], right_on=['year','countrycode'], how='left')
    print "done gdp"


    final_merged["country_code_origin"] = final_merged["country_code"]
    # drop repetitive table
    del final_merged["countrycode"]
    del final_merged["country_name"]
    del final_merged["year"]
    final_merged.to_excel("./files/gtd_94to15_aggregated.xlsx", encoding="UTF-8")

