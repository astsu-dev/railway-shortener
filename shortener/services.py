import uuid
import datetime
import base64

from sqlalchemy.sql.expression import insert, select

from shortener.db import database
from shortener import tables
from shortener.exceptions import URLHashNotFoundError


class URLShortenerService:
    @classmethod
    def generate_url_hash(cls) -> str:
        """Generates uuid4 string encoded by base64 urlsafe algorithm."""

        return base64.urlsafe_b64encode(uuid.uuid4().bytes).decode("utf-8")[:7]

    async def short_url(self, url: str) -> str:
        """Creates uuid4 encoded by base64 algorithm, writes the result to db with the original url.

        Args:
            url (str): url to short.

        Returns:
            str: shortened url.
        """

        url_hash = self.generate_url_hash()
        async with database.connection() as connection:
            query = insert(tables.urls).values(url=url, url_hash=url_hash, created_at=datetime.datetime.now())
            await connection.execute(query)
        return url_hash

    async def get_url_by_hash(self, url_hash: str) -> str:
        """Returns url by `url_hash` from database.

        Args:
            url_hash (str): url hash.

        Raises:
            URLHashNotFoundError: will be raised if url hash does not exist in database.
        
        Returns:
            str: full url.
        """

        async with database.connection() as connection:
            query = select(tables.urls).where(tables.urls.c.url_hash == url_hash)
            db_model = await connection.fetch_one(query)
            if db_model is not None:
                return db_model["url"]
            raise URLHashNotFoundError
