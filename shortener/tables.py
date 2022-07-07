from sqlalchemy import MetaData, Column, String
from sqlalchemy.sql.schema import Table
from sqlalchemy.sql.sqltypes import DateTime, Integer

metadata = MetaData()

urls = Table(
    "urls",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("url", String(255), nullable=False),
    Column("url_hash", String(10), nullable=False),
    Column("created_at", DateTime, nullable=False)
)
