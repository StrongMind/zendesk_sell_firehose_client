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

        def describe_when_all_data_is_in_one_response():
            # when tail and top are the same page.
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
                    return ZendeskSellResponseFactory(items=leads, top=True)

                def it_returns_leads_as_items(result, zendesk_sell_response_request_mock, leads):
                    assert result['items'] == leads

        def describe_when_data_is_in_multiple_responses():
            # when tail and top are not the same page.
            @pytest.fixture()
            def zendesk_sell_responses():
                responses = ZendeskSellResponseFactory.build_batch(fake.random_int(min=3, max=5))
                responses.append(ZendeskSellResponseFactory(top=True))
                return responses

            @pytest.fixture()
            def zendesk_sell_response_http_responses(zendesk_sell_responses):
                mocks = []

                class RequestMock:
                    def __init__(self, mock_response):
                        self.response = mock_response

                    status = 200

                    def json(self):
                        return self.response

                    def raise_for_status(self):
                        pass

                for response in zendesk_sell_responses:
                    mocks.append(RequestMock(response))
                return mocks

            @pytest.fixture()
            def zendesk_sell_response_request_mock(when, bearer_token, zendesk_sell_response_http_responses):
                previous_position = "tail"
                for response in zendesk_sell_response_http_responses:
                    when(requests).get("https://api.getbase.com/v3/leads/stream",
                                       params={"position": previous_position},
                                       headers={'Authorization': f'Bearer {bearer_token}'}).thenReturn(
                        response)
                    previous_position = response.json()['meta']['position']

            def it_returns_the_last_position(result, zendesk_sell_response_request_mock, zendesk_sell_responses):
                assert result['position'] == zendesk_sell_responses[-1]["meta"]["position"]

            def it_returns_no_items(result, zendesk_sell_response_request_mock, zendesk_sell_responses):
                assert result['items'] == []

            def describe_with_leads():
                @pytest.fixture()
                def leads():
                    return ZendeskLeadFactory.build_batch(fake.random_int(min=5, max=15))

                @pytest.fixture()
                def zendesk_sell_responses(leads):
                    responses = []
                    # spread the leads across the pages randomly
                    while len(leads) > 0:
                        # make half of pages blank, as this is a regular case for the firehose API
                        responses.append(ZendeskSellResponseFactory(items=[], top=False))
                        top = False
                        random_slice = fake.random_int(min=1, max=len(leads))
                        # if we're on the last page, make sure that top is true
                        if len(leads) == random_slice:
                            top = True
                        responses.append(ZendeskSellResponseFactory(items=leads[:random_slice],
                                                                    top=top))
                        leads = leads[random_slice:]
                    return responses

                def it_returns_leads_as_items(result, zendesk_sell_response_request_mock, leads):
                    assert result['items'] == leads

                def describe_when_data_is_in_multiple_responses_and_random_position_is_provided():
                    @pytest.fixture()
                    def random_position():
                        return fake.word()

                    @pytest.fixture()
                    def zendesk_sell_response_request_mock(when, bearer_token, zendesk_sell_response_http_responses,
                                                           random_position):
                        previous_position = random_position
                        for response in zendesk_sell_response_http_responses:
                            when(requests).get("https://api.getbase.com/v3/leads/stream",
                                               params={"position": previous_position},
                                               headers={'Authorization': f'Bearer {bearer_token}'}).thenReturn(
                                response)
                            previous_position = response.json()['meta']['position']

                    @pytest.fixture()
                    def result(zendesk_sell_response_request_mock, client, zendesk_sell_responses, random_position):
                        return client.get_leads(random_position)

                    def it_returns_the_last_position(result,
                                                     zendesk_sell_responses):
                        assert result['position'] == zendesk_sell_responses[-1]['meta']['position']

                    def it_returns_leads_on_pages_beyond_provided_position(result,
                                                                           leads):
                        assert result['items'] == leads
