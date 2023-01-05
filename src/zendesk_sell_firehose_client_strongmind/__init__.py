import requests


class ZendeskSellFirehoseClient:
    def __init__(self, bearer_token=None):
        if not bearer_token:
            raise Exception("No API key provided")
        self.bearer_token = bearer_token

    def get_leads(self):
        items = []
        position = "tail"
        top = False
        while not top:
            response = requests.get("https://api.getbase.com/v3/leads/stream",
                                    headers={'Authorization': f'Bearer {self.bearer_token}'},
                                    params={"position": position})
            response.raise_for_status()

            result = response.json()
            position = result['meta']['position']
            top = result['meta']['top']
            items.extend(result['items'])
        return {
            "position": result['meta']['position'],
            "items": items
        }
