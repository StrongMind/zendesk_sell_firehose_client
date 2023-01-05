import pytest
from pytest_describe import behaves_like


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
