import factory


class ZenDeskResponseMetaFactory(factory.DictFactory):
    links = factory.SubFactory(factory.DictFactory, next="")
    position = ""
    top = False


class ZenDeskResponseFactory(factory.DictFactory):
    meta = factory.SubFactory(factory.ZenDeskResponseMetaFactory)

    items = []
