from fastapi import FastAPI  # type: ignore

from store.core.config import settings
from store.routers import api_router


class CreateApp(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH
        )


app = CreateApp()
app.include_router(api_router)
