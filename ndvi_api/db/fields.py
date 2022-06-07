import sqlalchemy
from db.base import metadata

fields = sqlalchemy.Table(
    "fields",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("geojson", sqlalchemy.JSON)
    )

# ndvis = sqlalchemy.Table(
#     "ndvis",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
# )

maps = sqlalchemy.Table(
    "maps",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("field_id", sqlalchemy.ForeignKey("fields.id")),
    sqlalchemy.Column("html", sqlalchemy.Text())
)