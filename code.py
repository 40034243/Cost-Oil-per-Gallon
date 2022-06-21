import requests

for i in range(1):
    arr = []
    
    #distribution and marketing costs
    api = requests.get('https://api.eia.gov/series/?api_key=k0t5vUx5FxlQfOsdiaNDuIGNTT1UmVwK5sK2EwB5&series_id=PET.EMA_EPMR_PTG_NUS_DPG.M').json()
    disMarkCosts = (((api.get("series")[0]).get("data")[i])[1])
    arr.append(disMarkCosts)
    
    #refining costs
    api = requests.get('https://api.eia.gov/series/?api_key=k0t5vUx5FxlQfOsdiaNDuIGNTT1UmVwK5sK2EwB5&series_id=PET.EMA_EPM0_PDR_NUS_DPG.M').json()
    refCosts = (((api.get("series")[0]).get("data")[i])[1])
    arr.append(refCosts)
    
    #cost of crude oil per gallon 
    api = requests.get('https://api.eia.gov/series/?api_key=k0t5vUx5FxlQfOsdiaNDuIGNTT1UmVwK5sK2EwB5&series_id=PET.RWTC.M').json()
    crudeOil = (((api.get("series")[0]).get("data")[i])[1]) / 42
    arr.append(crudeOil)
    
    #taxes - EIA only provides an Excel sheet
    #This number is the federal + state tax per gallon for Florida
    fedStateTaxesFL = 0.539
    arr.append(fedStateTaxesFL)
    
    #weight of importance to oil price - as depicted in graph in readme
    weighted = [0.11, 0.18, 0.59, 0.12]
    res_list = []
    
    #finds the weighted sum - petrol per gallon
    finalSum = 0
    for i in range(0, len(arr)):
        res_list.append(arr[i] * weighted[i])
        finalSum = finalSum + res_list[i]
        
    print("Wholesale Avg. Gas Prices: ")
    print(finalSum)
