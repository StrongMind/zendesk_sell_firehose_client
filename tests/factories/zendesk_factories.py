import factory
from factory import DictFactory, ListFactory



class ZendeskLeadFactory(DictFactory):
    data = {
        "id": 4255984,
        "creator_id": 190756,
        "owner_id": 190756,
        "first_name": "ABC",
        "last_name": "XYZ",
        "organization_name": None,
        "status": "New",
        "source_id": 134455,
        "title": "CEO",
        "description": None,
        "industry": None,
        "website": None,
        "email": None,
        "phone": "1234-5677",
        "mobile": None,
        "fax": None,
        "twitter": None,
        "facebook": None,
        "linkedin": None,
        "skype": None,
        "address": {
            "country": "Poland",
            "city": "KRK",
            "state": "",
            "postal_code": "",
            "line1": "street 123"
        },
        "tags": [
            {
                "data": {
                    "name": "ABC",
                    "resource_type": "lead",
                    "id": 512665
                },
                "meta": {
                    "type": "tag"
                }
            }
        ],
        "custom_field_values": [
            {
                "value": False,
                "custom_field": {
                    "data": {
                        "name": "myField",
                        "resource_type": "lead",
                        "id": 29609,
                        "type": "bool"
                    },
                    "meta": {
                        "type": "custom_field"
                    }
                }
            }
        ],
        "created_at": "2016-03-15T09:13:06Z"
    }
    meta = {
        "event_id": "XqEROfOwTCucD-qjE1cO6w",
        "event_cause": "interaction",
        "sequence": 1,
        "event_type": "updated",
        "previous": {
            "title": "123"
        },
        "type": "lead",
        "event_time": "2016-08-18T07:29:42Z"
    }

class ZendeskSellResponseFactory(DictFactory):
    class Params:
        position = factory.Faker('uuid4')
        top = False

    meta = factory.SubFactory(
        DictFactory,
        links=factory.SubFactory(
            DictFactory,
            next=factory.LazyAttribute(
                lambda
                    links: f"https://api.getbase.com/v3/leads/stream?position={links.factory_parent.position}"
            )
        ),
        position=factory.SelfAttribute('..position'),
        top=factory.SelfAttribute('..top'),
    )
    items = factory.List([
    ])
