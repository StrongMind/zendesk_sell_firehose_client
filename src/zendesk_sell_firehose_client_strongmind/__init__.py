import requests


class ZendeskSellFirehoseClient:
    def __init__(self, bearer_token=None):
        if not bearer_token:
            raise Exception("No API key provided")
        self.bearer_token = bearer_token

    def __getattr__(self, item):
        if item.startswith("get_"):
            resource_type = item.replace("get_", "")
            return lambda position="tail": self.get_resources(resource_type, position)
        raise AttributeError(item)

    def get_resources(self, resource_type, position="tail"):
        items = []
        top = False
        while not top:
            response = requests.get(f"https://api.getbase.com/v3/{resource_type}/stream",
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
