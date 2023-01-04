import pytest

from zendesk_sell_firehose_client_strongmind import ZendeskSellFirehoseClient


def describe_a_zendesk_sell_firehose_client():
    @pytest.fixture
    def api_key():
        return "1234567890"

    @pytest.fixture
    def client(api_key):
        return ZendeskSellFirehoseClient(api_key=api_key)

    def it_exists(client):
        assert client

    def describe_when_initializing():
        def it_raises_an_exception_when_no_api_key_is_provided():
            with pytest.raises(Exception) as e:
                ZendeskSellFirehoseClient()
            assert str(e.value) == "No API key provided"
