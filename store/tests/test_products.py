from math import prod
import pytest
from model_bakery import baker
from store.models import Collection, Product
from rest_framework import status


@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/', product)
    return do_create_product


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_returns_401(self, create_product):
        product = baker.make(Product, description='a')
        response = create_product(product.__dict__)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_anonymous_returns_403(self, create_product, authenticate):
        authenticate()

        response = create_product(
            (baker.make(Product, description='a')).__dict__)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, create_product, authenticate):
        authenticate(is_staff=True)

        response = create_product(
            (baker.make(Product, title='', description='a')).__dict__)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, create_product, authenticate):
        authenticate(is_staff=True)
        collection = Collection.objects.create(title='a')

        response = create_product({'title': 'a', 'slug': '-', 'inventory': 1,
                                  'collection': collection.id, 'description': 'a', 'unit_price': 10})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0
