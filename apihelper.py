# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:27:24 2022

Helperklasse voor de Steam API. A.u.b. niet de functie get_request aanpassen.

@author: Lina Blijleven
@extended-by: S. Lukken
"""

#%% IMPORTS
# Hieronder vind je de benodigde libraries.
# Nog niet geinstalleerd? Gebruik 'pip install <naam>' in je 
# terminal of zoek specifieke instructies voor het installeren 
# van de library.

# Werken met API verzoeken
import requests

#%% API Class
class APIHelper:
    def __init__(self, apiKey: str):
        self.APIKey = apiKey
    
    """
    Geef de response in JSON terug voor een GET-verzoek, met optionele parameters.
    Deze functie helpt je met het opvragen van Steam data
        
    Parameters
    ----------
    url : string
    parameters : {'parameter': 'value'}
        parameters die nodig zijn voor het verzoek
        
    Returns
    -------
    json_data
        json-formatted output (lijkt wat op een dictionary)
    """
    def get_request(self, url, parameters=None):
        
        # Probeer het verzoek uit te voeren met de requests library
        try:
            response = requests.get(url=url, params=parameters)
        # Niet gelukt :'(
        except:
            print('Verzoek kon niet verstuurd worden. Probeer het later opnieuw.')
            return None
        
        # Is er een resultaat?
        if response:
            # Vraag de JSON uit het antwoord op
            return response.json()
        else:
            # Wacht even en probeer het opnieuw, misschien is de server druk.
            print('We konden geen JSON uit de response halen, check alsjeblieft je URL en verplichte parameters.')
            return response
       
    """
    Hulpfunctie om data voor een game op te vragen.
    
    Returns : json geformatteerde data
    """
    def get_app_data(self, appId: int):
    
        # Voer een HTTP GET-verzoek uit
        return self.get_request("http://store.steampowered.com/api/appdetails/", {
            "appid": appId
        })
    
    """
    Hulpfunctie om de achievement rates van een game op te vragen.
    
    Returns: json geformatteerde data
    """
    def get_app_achievements(self, gameId: int):
        
        # Voer een HTTP GET-verzoek uit
        return self.get_request("https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v2/", {
            "gameid": gameId
        })

    """
    Hulpfunctie om het aantal spelers van een game op te vragen.
    """
    def get_app_players(self, appId: int):
        
        # Voer een HTTP GET-verzoek uit
        return self.get_request("https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1", {
            "appid": appId
        })

    """
    Helper functie voor het ophalen van de achievement-stats van een steamgebruiker voor een bepaalde SteamApp.
    """
    def GetPlayerAchievements(self, appId: int, steamId: int):
        return self.get_request(f"http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001", {
            "appid": appId,
            "key": self.APIKey,
            "steamid": steamId
        })
