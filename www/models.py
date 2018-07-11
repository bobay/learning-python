import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primaryKey = True, default = next_id(), ddl = 'varchar(50)')
    email = StringField(ddl = 'varchar(50)')
    passwd = StringField(ddl = 'varchar(50)')
    admin = BooleanField()
    name = StringField('varchar(50)')
    image = StringField('varchar(500)')
    crated_at = FloatField(default = time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primaryKey = True, default = next_id(), ddl = 'varchar(50)')
    user_id = StringField(ddl = 'varchar(50)')
    user_name = StringField(ddl = 'varchar(50)')
    user_image = StringField('varchar(500)')
    name = StringField('varchar(50)')
    summary = StringField('varchar(200)')
    content = TextField()
    crated_at = FloatField(default = time.time)

class Comment(Model)
    __table__ = 'comments'

    id = StringField(primaryKey = True, default = next_id(), ddl = 'varchar(50)')
    blog_id = StringField(ddl = 'varchar(50)')
    user_id = StringField(ddl = 'varchar(50)')
    user_name = StringField(ddl = 'varchar(50)')
    user_image = StringField('varchar(500)')
    content = TextField()
    crated_at = FloatField(default = time.time)