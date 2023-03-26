from app import db

class User(db.Model):
    __tablename__ = "tb_user"
    __table_args__={'mysql_collate':'utf8mb4_general_ci'}

    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(200))
    password = db.Column(db.String(200))

    updated_by = db.Column(db.String(200))
    created_by  = db.Column(db.String(200))
    updated_at = db.Column(db.DateTime)
    created_at  = db.Column(db.DateTime, server_default=db.func.now())

    user_detail = db.relationship('UserDetail', backref='tb_user', lazy=True)

    def __repr__(self):
        return 'id = %s, account = %s, password=%s, updated_by = %s, created_by = %s, updated_at = %s, created_at = %s' % (
            self.id, self.account, self.password, self.updated_by,  self.created_by, self.updated_at, self.created_at,)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'account': self.account,
            'password': self.password,
        }