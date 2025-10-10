from database.dba import db

fornecedor_materiaPrima = db.Table('fornecedor_materiaPrima',
    db.Column('id_fornecedor', db.Integer, db.ForeignKey('fornecedor.id_fornecedor'), primary_key=True),
    db.Column('id_materiaPrima', db.Integer, db.ForeignKey('materia_prima.id_materiaPrima'), primary_key=True)
)

class fornecedor(db.Model):
    __tablename__ = 'fornecedor'
    
    id_fornecedor = db.Column(db.Integer, primary_key=True)
    razao_social = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(15), nullable=False)
    contato = db.Column(db.String(15), nullable=False)
    
    materiais = db.relationship('materia_prima', secondary=fornecedor_materiaPrima, backref='fornecedores')
    
    def __init__(self, razao_social, cnpj, contato):
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.contato = contato
    
    
    def to_disc(self, incluir_materiais=False):
        data = {
            'id': self.id_fornecedor,
            "razao_social": self.razao_social,
            'cnpj': self.cnpj,
            'contato': self.contato
        }
        if incluir_materiais:
            data['materiais'] = [m.to_disc() for m in self.materiais]
        return data
