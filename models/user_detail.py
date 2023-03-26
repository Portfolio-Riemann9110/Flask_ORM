from app import db


class UserDetail(db.Model):
    __tablename__ = 'tb_user_detail'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)  
    user_id = db.Column(db.Integer, db.ForeignKey('tb_user.id'), nullable=False)
    updated_by = db.Column(db.String(200))
    created_by  = db.Column(db.String(200))
    updated_at = db.Column(db.DateTime)
    created_at  = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return 'id = %s, level = %s' % (
            self.id, self.level)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }
