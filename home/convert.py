from unitconvert import volumeunits


def tsp_to_oz(value):
    ans = volumeunits.VolumeUnit(value, 'tsp', 'floz').doconvert()
    return ans

def tbsp_to_oz(value):
    ans = volumeunits.VolumeUnit(value, 'tbsp', 'floz').doconvert()
    return ans

def cup_to_oz(value):
    ans = volumeunits.VolumeUnit(value, 'cup', 'floz').doconvert()
    return ans



#Volume [VolumeUnit]: - Metric: Milliliter (ml), Liter (l) - US customary: Teaspoon (tsp), Tablespoon (tbsp), fluid Ounces (floz), Cup (cup), Pint (pt), Quart (qt), Gallon (gal)

#Mass [MassUnit]: Milligram (mg), Gram (g), Ounce (oz), Pound (lb), Kilogram (kg)