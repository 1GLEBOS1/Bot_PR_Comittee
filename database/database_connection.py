from peewee import *

db = PostgresqlDatabase('bghghwhpirpjqlsphdh0', user="uheu05uastzbbgy71twe", password="956FRuE8x7wt4Ca3hDb9",
                        host="bghghwhpirpjqlsphdh0-postgresql.services.clever-cloud.com", port="5432")


class BaseModel(Model):
    id = AutoField(primary_key=True, unique=True, null=False)

    class Meta:
        database = db
        order_by = id


class PRCommitteeMember(BaseModel):
    telegram_id = IntegerField(null=False, unique=True)
    access_level = IntegerField(null=False)
    name = CharField(max_length=255)
    position = CharField(max_length=255)


class Statistic(BaseModel):
    author_id = ForeignKeyField(PRCommitteeMember, field=PRCommitteeMember.telegram_id, backref='author_id')
    event_id = IntegerField(null=False)
    statistic = TextField(null=False)
