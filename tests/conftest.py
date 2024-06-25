import asyncio
from uuid import UUID

import pytest
from httpx import AsyncClient

from store.db.mongo import db_client
from store.schemas.product import ProductIn, ProductUpdate
from store.usecases.product import product_usecase
from tests.factories import product_data, products_data


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the event loop for the session scope."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    """Provide a MongoDB client."""
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    """Clear collections in the MongoDB database before each test."""
    yield
    db = mongo_client.get_database()
    collection_names = await db.list_collection_names()
    for collection_name in collection_names:
        if not collection_name.startswith("system"):
            await db[collection_name].delete_many({})


@pytest.fixture
async def client() -> AsyncClient:
    """Provide an HTTP client for making requests to the FastAPI app."""
    from store.main import app

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def products_url() -> str:
    """Return the URL for the products endpoint."""
    return "/products/"


@pytest.fixture
def product_id() -> UUID:
    """Provide a UUID for testing purposes."""
    return UUID("fce6cc37-10b9-4a8e-a8b2-977df327001a")


@pytest.fixture
def product_in(product_id: UUID) -> ProductIn:
    """Create a ProductIn instance with predefined data and a specific ID."""
    return ProductIn(**product_data(), id=product_id)


@pytest.fixture
def product_update(product_id: UUID) -> ProductUpdate:
    """Create a ProductUpdate instance with predefined data and a specific ID."""
    return ProductUpdate(**product_data(), id=product_id)


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
