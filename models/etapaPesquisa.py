from database.dba import db


class EtapaPesquisa(db.Model):
    __tablename__ = 'etapaPesquisa'
    
    id_etapaPesquisa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_etapa = db.Column(db.String(100), nullable=True)
    descricao_etapa = db.Column(db.String(250), nullable=True)
    
    def __init__(self, nome_etapa, descricao_etapa):
        self.nome_etapa = nome_etapa
        self.descricao_etapa = descricao_etapa
    
    def to_disc(self):
        return {
            'id': self.id_etapaPesquisa,
            'nomeEtapa': self.nome_etapa,
            'descricaoEtapa': self.descricao_etapa
        }
