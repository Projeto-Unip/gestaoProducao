from database.dba import db


class materia_prima(db.Model):
    __tablename__ = 'materia_prima'
    
    id_materiaPrima = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(100), nullable=True)
    formula = db.Column(db.String(50), nullable=True)
    quantidade = db.Column(db.Integer, nullable=True)
    lote = db.Column(db.String(25), nullable=True)
    data_validade = db.Column(db.String(20), nullable=False)
    
    def __init__(self, nome, formula, qtd, lote, data_validade):
        self.nome = nome
        self.formula = formula
        self.quantidade = qtd
        self.lote = lote
        self.data_validade = data_validade
    
    def to_disc(self):
        return {
            'nome': self.nome,
            'formula': self.formula,
            'quatidade': self.quantidade,
            'lote': self.lote,
            'dataValidade': self.data_validade
        }
    
        
        


