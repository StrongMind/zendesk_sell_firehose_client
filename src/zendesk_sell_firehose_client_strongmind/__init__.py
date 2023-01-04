import requests
class ZendeskSellFirehoseClient:
    def __init__(self, bearer_token=None):
        if not bearer_token:
            raise Exception("No API key provided")
        self.bearer_token = bearer_token

    def get_leads(self):
        response = requests.get("https://api.getbase.com/v3/leads/stream",
                                headers={'Authorization': f'Bearer {self.bearer_token}'},
                                params={"position": "tail"})
        response.raise_for_status()
        return {
            "position": response.json()['meta']['position'],
            "items": []
        }
