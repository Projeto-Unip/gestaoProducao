from database.dba import db


class Fornecedor():
    
    id_fornecedor = db.Column(db.Integer, primary_key=True)
    razaoSocial = db.Column(db.String(100), nullable=True)
    cnpj = db.Column(db.String(15), nullable=True)
    contato = db.Column(db.String(15), nullable=True)
    
    def __init__(self, razaoSocial, cnpj, contato):
        self.razaoSocial = razaoSocial
        self.cnpj = cnpj
        self.contato = contato
    
    
    def to_disc(self):
        return {
            "Razao-social": self.razaoSocial,
            'CNPJ': self.cnpj,
            'Contato': self.contato
        }
