import pytest
from faker import Faker

from pydantic_factories import ConfigurationError, ModelFactory
from tests.models import Pet


def test_allows_user_to_define_faker_instance():
    my_faker = Faker()
    setattr(my_faker, "__test__attr__", None)

    class MyFactory(ModelFactory):
        __model__ = Pet
        __faker__ = my_faker

    assert hasattr(MyFactory.get_faker(), "__test__attr__")


def test_validates_model_is_set_in_build():
    with pytest.raises(ConfigurationError):

        class MyFactory(ModelFactory):
            pass

        MyFactory.build()


def test_validates_model_is_set_in_batch():
    with pytest.raises(ConfigurationError):

        class MyFactory(ModelFactory):
            pass

        MyFactory.batch(2)


def test_validates_connection_in_create_sync():
    with pytest.raises(ConfigurationError):

        class MyFactory(ModelFactory):
            pass

        MyFactory.create_sync()


def test_validates_connection_in_create_batch_sync():
    with pytest.raises(ConfigurationError):

        class MyFactory(ModelFactory):
            pass

        MyFactory.create_batch_sync(2)


@pytest.mark.asyncio
async def test_validates_connection_in_create_async():
    with pytest.raises(ConfigurationError):

        class MyFactory(ModelFactory):
            pass

        await MyFactory.create_async()


@pytest.mark.asyncio
async def test_validates_connection_in_create_batch_async():
    with pytest.raises(ConfigurationError):

        class MyFactory(ModelFactory):
            pass

        await MyFactory.create_batch_async(2)