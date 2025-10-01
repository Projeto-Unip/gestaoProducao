from database.dba import db


class materia_prima(db.Model):
    __tablename__ = 'materia_prima'
    
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(100), nullable=False)
    formula = db.Column(db.String(50), nullable=False)
    dataValidade = db.Column(db.String(20), nullable=False)
    
    def to_disc(self):
        return {
            'nome': self.nome,
            'formula': self.formula,
            'dataValidade': self.dataValidade
        }


