class ZendeskSellFirehoseClient:
    def __init__(self, api_key=None):
        if not api_key:
            raise Exception("No API key provided")
