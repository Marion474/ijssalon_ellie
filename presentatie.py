def presenteer(mijn_dict,totaal):
    for item, bedrag in mijn_dict.items():
        print(f"{item} : {bedrag} euro")

    print("=" * 20) 
    print(f"totaal : {totaal} euro")

mijn_dict = {"Vis" : 10, "Vlees" : 25, "Overig" : 15}
totaal = 50

presenteer(mijn_dict, totaal)
