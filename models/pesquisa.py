from database.dba import db

pesquisa_materiaPrima = db.Table('pesquisa_materiaPrima',
    db.Column('id_pesquisa', db.Integer, db.ForeignKey('pesquisa.id_pesquisa'), primary_key=True),
    db.Column('id_materiaPrima', db.Integer, db.ForeignKey('materia_prima.id_materiaPrima'), primary_key=True)
)


class Pesquisa(db.Model):
    __tablename__ = 'pesquisa'
    
    id_pesquisa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_pesquisa = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(250), nullable=False)
    data_inicio = db.Column(db.DateTime, nullable=False)
    data_fim = db.Column(db.DateTime, nullable=False)
    id_etapaPesquisa = db.Column(db.Integer, db.ForeignKey('etapaPesquisa.id_etapaPesquisa'), nullable=False)
    
    etapa = db.relationship('EtapaPesquisa', backref='pesquisas')
    materiais = db.relationship('materia_prima', secondary=pesquisa_materiaPrima, backref='pesquisas')
    
    def __init__(self, nome_pesquisa, descricao, data_inicio, data_fim, id_etapaPesquisa):
        self.nome_pesquisa = nome_pesquisa
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.id_etapaPesquisa = id_etapaPesquisa
    
    def to_disc(self, incluir_etapa=False, incluir_materiais=False):
        data = {
            'id': self.id_pesquisa,
            'nomePesquisa': self.nome_pesquisa,
            'descricao': self.descricao,
            'dataInicio': self.data_inicio.isoformat() if self.data_inicio else None,
            'dataFim': self.data_fim.isoformat() if self.data_fim else None,
            'idEtapaPesquisa': self.id_etapaPesquisa
        }
        if incluir_etapa and self.etapa:
            data['etapa'] = self.etapa.to_disc()
        if incluir_materiais:
            data['materiais'] = [m.to_disc() for m in self.materiais]
        return data
