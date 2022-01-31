import requests

class SnackboxRPCHelper:
    def __init__(self, snackboxApiURL: str):
        self.SnackboxApiURL = snackboxApiURL

    def SendPostRequest(self, url, parameters=None):
        try:
            response = requests.post(url=url, params=parameters)
        except:
            return None

        if response:
            return response.json()

        return None

    def SendUnlockRequest(self, unlockTimeMS: int):
        return self.SendPostRequest(f"{self.SnackboxApiURL}/v1/Unlock", {
            "UnlockTimeMS": unlockTimeMS
        })
