from database.dba import db


class StatusProducao(db.Model):
    __tablename__ = 'statusProducao'
    
    id_statusProducao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomeStatus = db.Column(db.String(100), nullable=True)
    descricaoStatus = db.Column(db.String(250), nullable=True)
    
    def __init__(self, nomeStatus, descricaoStatus):
        self.nomeStatus = nomeStatus
        self.descricaoStatus = descricaoStatus
    
    def to_disc(self):
        return {
            'id': self.id_statusProducao,
            'nomeStatus': self.nomeStatus,
            'descricaoStatus': self.descricaoStatus
        }
