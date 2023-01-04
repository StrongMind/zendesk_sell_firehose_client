import pytest
from faker import Faker
from pytest_describe import behaves_like

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
        def describe_when_at_top():
            def describe_with_no_data():
                pass


def a_resource():
    def it_exists(resource):
        assert resource


@behaves_like(a_resource)
def describe_an_appointment():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Appointment
        return Appointment()


@behaves_like(a_resource)
def describe_an_associated_contact():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import AssociatedContact
        return AssociatedContact()


@behaves_like(a_resource)
def describe_a_call():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Call
        return Call()


@behaves_like(a_resource)
def describe_a_collaboration():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Collaboration
        return Collaboration()


@behaves_like(a_resource)
def describe_a_collaboration_request():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import CollaborationRequest
        return CollaborationRequest()


@behaves_like(a_resource)
def describe_a_contact():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Contact
        return Contact()


@behaves_like(a_resource)
def describe_a_custom_field():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import CustomField
        return CustomField()


@behaves_like(a_resource)
def describe_a_deal():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Deal
        return Deal()


@behaves_like(a_resource)
def describe_a_document():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Document
        return Document()


@behaves_like(a_resource)
def describe_a_lead():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Lead
        return Lead()


@behaves_like(a_resource)
def describe_a_line_item():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import LineItem
        return LineItem()


@behaves_like(a_resource)
def describe_a_loss_reason():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import LossReason
        return LossReason()


@behaves_like(a_resource)
def describe_a_note():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Note
        return Note()


@behaves_like(a_resource)
def describe_an_order():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Order
        return Order()


@behaves_like(a_resource)
def describe_a_product():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Product
        return Product()


@behaves_like(a_resource)
def describe_a_source():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Source
        return Source()


@behaves_like(a_resource)
def describe_a_stage():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Stage
        return Stage()


@behaves_like(a_resource)
def describe_a_tag():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Tag
        return Tag()


@behaves_like(a_resource)
def describe_a_task():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Task
        return Task()


@behaves_like(a_resource)
def describe_an_unqualified_reason():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import UnqualifiedReason
        return UnqualifiedReason()


@behaves_like(a_resource)
def describe_a_user():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import User
        return User()


@behaves_like(a_resource)
def describe_a_visit():
    @pytest.fixture
    def resource():
        from zendesk_sell_firehose_client_strongmind.resources import Visit
        return Visit()
