# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:13:46 2022

Hulpklasse om met de Steam store API te werken. De hulpklasse 
bevat al een specifieke methode om app data op te vragen, maar de 
get_request functie kan ook gebruikt worden met andere methoden uit de 
WebAPI methodes.

WebAPI documentatie (met andere methodes):
https://partner.steamgames.com/doc/webapi

Voor sommige methodes van de Steam WebAPI is authenticatie vereist. Hiervoor 
heb je een Steam WebAPI key nodig, zie: https://partner.steamgames.com/doc/webapi_overview/auth

Geeft je call een <Response [400]>? Kijk dan opnieuw naar de documentatie of je 
URL en parameters kloppen.

@author: Lina Blijleven
@extended-by: S. Lukken
"""

#%% IMPORTS
# Importeer de hulpklasse
import apihelper

# Stel hier je API-key in
api_key = 'EC890957993F2D5036E82EFF1DD40882'

#%% CALLS
# Maak een API helper aan
api = apihelper.APIHelper(api_key)

print(api.get_app_data(10))

# Vraag de percentages voor de achievements van een game op.
print(api.get_app_achievements(440))

# Vraag het aantal spelers voor een game op
res = api.get_app_players(440)

# Haal het aantal spelers uit het resultaat
NumberOfPlayers = res['response']['player_count']

# Print het aantal spelers
print("Er zijn op het moment {} spelers.".format(NumberOfPlayers))

#%% CALLS (met authenticatie)

# Heb je een call waar je authenticatie voor nodig hebt?
# Je krijgt dan een error response met een code als 401 of 403. 
# Geef dan een API-key mee in je parameters.
parameters = {
    'key': "EC890957993F2D5036E82EFF1DD40882",
    'appid': 440
}

# Geef de parameters mee aan je call