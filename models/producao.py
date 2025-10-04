from database.dba import db


class Producao(db.Model):
    __tablename__ = 'producao'
    
    id_producao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomeMediamento = db.Column(db.String(100), nullable=False)
    descricaoMedicamento = db.Column(db.String(250), nullable=False)
    data_inicio = db.Column(db.DateTime, nullable=False)
    data_fim = db.Column(db.DateTime, nullable=False)
    id_statusProducao = db.Column(db.Integer, db.ForeignKey('statusProducao.id_statusProducao'), nullable=False)
    id_pesquisa = db.Column(db.Integer, db.ForeignKey('pesquisa.id_pesquisa'), nullable=False)
    
    status = db.relationship('StatusProducao', backref='producoes')
    pesquisa = db.relationship('Pesquisa', backref='producoes')
    
    def __init__(self, nomeMediamento, descricaoMedicamento, data_inicio, data_fim, id_statusProducao, id_pesquisa):
        self.nomeMediamento = nomeMediamento
        self.descricaoMedicamento = descricaoMedicamento
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.id_statusProducao = id_statusProducao
        self.id_pesquisa = id_pesquisa
    
    def to_disc(self, incluir_status=False, incluir_pesquisa=False):
        data = {
            'id': self.id_producao,
            'nomeMedicamento': self.nomeMediamento,
            'descricaoMedicamento': self.descricaoMedicamento,
            'dataInicio': self.data_inicio.isoformat() if self.data_inicio else None,
            'dataFim': self.data_fim.isoformat() if self.data_fim else None,
            'idStatusProducao': self.id_statusProducao,
            'idPesquisa': self.id_pesquisa
        }
        if incluir_status and self.status:
            data['status'] = self.status.to_disc()
        if incluir_pesquisa and self.pesquisa:
            data['pesquisa'] = self.pesquisa.to_disc()
        return data
