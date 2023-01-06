# Zendesk Sell Firehose Client

Client for ZenDesk Sell Firehose API

## Installation

```bash
pip install zendesk_sell_firehose_client
```


## Usage

```python
from zendesk_sell_firehose_client import ZendeskSellFirehoseClient

client = ZendeskSellFirehoseClient(bearer_token="{BEARER_TOKEN_HERE}")

# Get all leads
leads = client.get_leads()
```


## Development

### Setup

```bash
pip install -r requirements.txt
```

### Testing

```bash
pytest
```
