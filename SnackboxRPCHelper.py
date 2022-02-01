import requests


class SnackboxRPCHelper:
    def __init__(self, snackboxApiURL: str):
        self.SnackboxApiURL = snackboxApiURL

    def SendPostRequest(self, url, parameters=None):
        try:
            response = requests.post(url=url, json=parameters)
        except:
            return None

        if response:
            try:
                return response.json()
            except:
                return None

        return None

    def DoRPC(self, rpcMethod: str, *args):
        return self.SendPostRequest(f"{self.SnackboxApiURL}/rpc", {
            "jsonrpc": "2.0",
            "method": rpcMethod,
            "params": [*args]
        })

    def SendUnlockRequest(self, unlockTimeMS: int):
        return self.DoRPC("Unlock", unlockTimeMS)

    def SendLockRequest(self):
        return self.DoRPC("Lock")
