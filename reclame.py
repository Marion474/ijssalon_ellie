from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = (f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro.")
    return uitvoer  
print(aanbieding_1("aardbei", 4, 0.1))


def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    totaal_met_btw = totaal + btw_bedrag
    return totaal, btw_bedrag
dagelijkse_inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09
totaal, btw_bedrag = inkomsten_totaal(dagelijkse_inkomsten, btw_percentage)
print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden.")


def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return laagste, hoogste

dagelijkse_inkomsten = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(dagelijkse_inkomsten)
print(resultaat)


def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde = totaal / aantal
    return gemiddelde

dagelijkse_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(f"De gemiddelde inkomsten deze week zijn {gemiddelde(dagelijkse_inkomsten)} euro.")


def meervoudig(invoer_lijst):
    resultaat = laag_en_hoog(invoer_lijst)
    return resultaat

voorbeeld = [10, 5, 3, 2, 1, 2, 9]
print(meervoudig(voorbeeld))


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer