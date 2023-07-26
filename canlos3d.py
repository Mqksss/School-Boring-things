#Ice filaments : 0,75kg (750g) --> Price : 16,94 eur (amazon)
#0,1250 kWh --> average consumption of ender 3
#0,1558 eur/kWh --> price of a kWh (Paris 15e, ENGIE)
#0,80 eur/h --> average price of an hour of usage

fprice = 17 #filament price in euros
weight = 750 #in grams (of the whole spool)

eprice = 0.80 #electricity price in euros

printcons = int(input("Enter the consumption of filament in grams of the print :"))
time = int(input("Enter the time of the print :"))

def brut(price,weight,printcons):
    cost = price * printcons / weight
    return cost
print("The raw price of the print will be around :",brut(fprice,weight,printcons))

def timing(time):
    tmp = 0
    res = 0
    cost = brut(fprice,weight,printcons)
    if time < 3:
        tmp = (25 * cost)
        res = (tmp / 100) + cost
        final = res + (eprice * time)
        return final
    elif time == 3:
        tmp = (50 * cost)
        res = (tmp / 100) + cost
        final = res + (eprice * time)
        return final
    elif time > 3:
        tmp = (75 * cost)
        res = (tmp / 100) + brut(fprice,weight,printcons)
        final = res + (eprice * time)
        return final
    return False
print("The price with the print time will be around :",timing(time))




