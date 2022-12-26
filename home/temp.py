
from py_edamam import Edamam
import requests
import json

#e = Edamam(nutrition_appid='c8281fe8',
           #nutrition_appkey='88d598022998c3f7b0ae17fc1771f7a2')


def extract(ingredient):
    api = ''
    api_url = 'https://api.edamam.com/api/nutrition-data?app_id=c8281fe8&app_key=88d598022998c3f7b0ae17fc1771f7a2&nutrition-type=cooking&ingr='
    query = ingredient
    response = requests.get(api_url + query)
    if response.status_code == requests.codes.ok:
        api = json.loads(response.content)
    nutrient_data = api
    data = nutrient_data['totalNutrients']
    

    label_to_extract = ['CHOCDF.net','FAT','FIBTG','SUGAR','PROCNT','CHOLE','VITC','VITB12','TOCPHA']
    #map = ['Carbohydrates', 'Total lipid (fat)', 'Fiber, total dietary', 'Sugars, total', 'Protein', 'Cholesterol', 'Vitamin C, total ascorbic acid', 'Vitamin B-12', 'Vitamin E (alpha-tocopherol)']
    #res = {label_to_extract[i]: map[i] for i in range(len(map))}
    mapDict = {'CHOCDF.net':'Carbohydrates','FAT':'Total lipid (fat)','FIBTG':'Fiber, total dietary','SUGAR':'Sugars, total','PROCNT':'Protein','CHOLE':'Cholesterol','VITC':'Vitamin C, total ascorbic acid','VITB12':'Vitamin B-12','TOCPHA':'Vitamin E (alpha-tocopherol)'}
    #finalList = []
    #finalList.append(str(calories)+" Calories ")
    tempDict = {}
    calories = nutrient_data['calories']
    tempDict['Calories'] = calories
    for curLabel in label_to_extract:
        try:
            curVal = data[curLabel]
            label = str(curVal['label'])
            temp_quantity = float(curVal['quantity'])
            format_float = "{:.2f}".format(temp_quantity)
            quantity = str(format_float)
            unit = str(curVal['unit'])
            tempDict1 = {label:quantity+" "+unit}
            tempDict.update(tempDict1)
            #resultStr = label+" "+quantity+" "+unit
            #finalList.append(tempDict)
        except:
            label = mapDict[curLabel]
            tempDict1={label:0}
            tempDict.update(tempDict1)
            print("Don't Mind Me, You Enjoy !!!!!")
    
    return tempDict





