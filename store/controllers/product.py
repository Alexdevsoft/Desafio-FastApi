from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from pydantic import UUID4
from store.core.exceptions import NotFoundException
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from store.usecases.product import ProductUsecase

router = APIRouter(tags=["products"])


@router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
async def create_product(
    body: ProductIn = Body(...), usecase: ProductUsecase = Depends()
) -> ProductOut:
    return await usecase.create(body=body)


@router.get("/{id}", response_model=ProductOut, status_code=status.HTTP_200_OK)
async def get_product(
    id: UUID4 = Path(...), usecase: ProductUsecase = Depends()
) -> ProductOut:
    try:
        return await usecase.get(id=id)
    except NotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.get("/", response_model=List[ProductOut], status_code=status.HTTP_200_OK)
async def list_products(usecase: ProductUsecase = Depends()) -> List[ProductOut]:
    return await usecase.query()


@router.patch("/{id}", response_model=ProductUpdateOut, status_code=status.HTTP_200_OK)
async def update_product(
    id: UUID4 = Path(...),
    body: ProductUpdate = Body(...),
    usecase: ProductUsecase = Depends(),
) -> ProductUpdateOut:
    return await usecase.update(id=id, body=body)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    id: UUID4 = Path(...), usecase: ProductUsecase = Depends()
) -> None:
    try:
        await usecase.delete(id=id)
    except NotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
