from api import db, ma

class Advertisement(db.Model):
    id = db.Column(db.Integer, index=True, autoincrement=True,
        primary_key=True, unique=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(128), nullable=False)
    image = db.Column(db.String(128))

    def __repr__(self):
        return '<Advertisement {}>'.format(self.id)

class AdvertisementSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'image')
