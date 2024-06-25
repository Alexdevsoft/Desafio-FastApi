from pydantic import ValidationError

import pytest
from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_success():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "Iphone 14 Pro Max"


def test_schemas_return_raise():
    data = {"name": "Iphone 14 Pro Max", "quantity": 10, "price": 8.500}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Iphone 14 Pro Max", "quantity": 10, "price": 8.5},
        "url": "https://errors.pydantic.dev/2.5/v/missing",
    }


@pytest.fixture
async def product_inserted(product_in: ProductIn):
    """Insert a product into the database and return it."""
    return await product_usecase.create(body=product_in)


@pytest.fixture
def products_in() -> list[ProductIn]:
    """Create a list of ProductIn instances with predefined data."""
    return [ProductIn(**product) for product in products_data()]


@pytest.fixture
async def products_inserted(products_in: list[ProductIn]):
    """Insert multiple products into the database and return them."""
    return [await product_usecase.create(body=product) for product in products_in]
