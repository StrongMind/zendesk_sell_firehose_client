import pytest
import requests
from faker import Faker
from mockito import mock

from factories.zendesk_factories import ZendeskSellResponseFactory, ZendeskLeadFactory
from zendesk_sell_firehose_client_strongmind import ZendeskSellFirehoseClient

fake = Faker()


def describe_a_zendesk_sell_firehose_client():
    @pytest.fixture
    def bearer_token():
        return fake.word()

    @pytest.fixture
    def client(bearer_token):
        return ZendeskSellFirehoseClient(bearer_token=bearer_token)

    def it_exists(client):
        assert client

    def describe_when_initializing():
        def it_raises_an_exception_when_no_api_key_is_provided():
            with pytest.raises(Exception) as e:
                ZendeskSellFirehoseClient()
            assert str(e.value) == "No API key provided"

        def it_holds_api_key(client, bearer_token):
            assert client.bearer_token == bearer_token

    def describe_getting_leads():
        @pytest.fixture()
        def leads():
            return []

        @pytest.fixture()
        def zendesk_sell_response():
            return ZendeskSellResponseFactory(top=True)

        @pytest.fixture()
        def zendesk_sell_response_http_response(zendesk_sell_response):
            return mock({
                'status_code': 200,
                'json': lambda *args, **kwargs: zendesk_sell_response,
                'raise_for_status': lambda: None
            })

        @pytest.fixture()
        def zendesk_sell_response_request_mock(when, bearer_token, zendesk_sell_response_http_response):
            when(requests).get("https://api.getbase.com/v3/leads/stream",
                               params={"position": "tail"},
                               headers={'Authorization': f'Bearer {bearer_token}'}).thenReturn(
                zendesk_sell_response_http_response)

        @pytest.fixture()
        def result(zendesk_sell_response_request_mock, client):
            return client.get_leads()

        def describe_when_error_response_is_returned():
            @pytest.fixture()
            def zendesk_sell_response_http_response():
                def raise_for_status():
                    raise requests.HTTPError()

                return mock({'status_code': 400, 'raise_for_status': raise_for_status})

            def it_raises_exception(zendesk_sell_response_request_mock, client):
                with pytest.raises(requests.HTTPError):
                    client.get_leads()

        def describe_when_at_top():
            def describe_with_no_data():
                def it_returns_an_empty_item_set(result):
                    assert result['items'] == []

                def it_returns_a_position(result, zendesk_sell_response_request_mock, zendesk_sell_response):
                    assert result['position'] == zendesk_sell_response["meta"]["position"]

            def describe_with_leads():
                @pytest.fixture()
                def leads():
                    return ZendeskLeadFactory.build_batch(4)

                @pytest.fixture()
                def zendesk_sell_response(leads):
                    return ZendeskSellResponseFactory(items=leads)

                def it_returns_leads_as_items(result, zendesk_sell_response_request_mock, leads):
                    assert result['items'] == leads


