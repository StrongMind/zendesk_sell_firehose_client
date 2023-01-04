class ZendeskSellFirehoseClient:
    def __init__(self, bearer_token=None):
        if not bearer_token:
            raise Exception("No API key provided")
        self.bearer_token = bearer_token
