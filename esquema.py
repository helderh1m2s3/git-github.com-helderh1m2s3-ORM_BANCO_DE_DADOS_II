from datetime import datetime
from peewee import PostgresqlDatabase, Model, TextField, FloatField, IntegerField, ForeignKeyField, DateTimeField, PrimaryKeyField

db = PostgresqlDatabase('peewee_bd2',port=5432,user='postgres',password='Helder@1992')

class BaseModel(Model):
    class Meta():
        database = db

class CATEGORIA(BaseModel):
    id = PrimaryKeyField()
    descricao = TextField(unique =True)
    
class CLIENTE(BaseModel):
    id = PrimaryKeyField()
    nome = TextField()
    endereco = TextField()
    data_registro = DateTimeField(default = datetime.now)

class PRODUTOS(BaseModel):
    id = PrimaryKeyField()
    descricao = TextField()
    id_categoria = ForeignKeyField(CATEGORIA, backref='produtos')
    valor = FloatField()
    
class HISTORICO_PRECOS(BaseModel):
    id = PrimaryKeyField()
    id_produto = ForeignKeyField(PRODUTOS, backref='historicoprecoprodutos')
    valor = FloatField()
    data = DateTimeField(default = datetime.now)
    
class VENDAS(BaseModel):
    id = PrimaryKeyField()
    id_produto = ForeignKeyField(PRODUTOS, backref='vendasprodutos')
    id_cliente = ForeignKeyField(CLIENTE, backref='vendascliente')
    data = DateTimeField(default = datetime.now)
    quantidade = IntegerField()
    valor_unitario = FloatField()
    valor_total = FloatField()

db.connect()
db.create_tables([CATEGORIA, CLIENTE, PRODUTOS, HISTORICO_PRECOS, VENDAS])


# CREATE OR REPLACE FUNCTION GRAVA_HISTORICO_PRECO() RETURNS TRIGGER AS 
# $$
# BEGIN
# 	IF NEW.id != (SELECT id FROM public.produtos) THEN
# 		INSERT INTO historico_precos (id_produto, valor) 
# 		VALUES (NEW.id, NEW.valor);
# 	ELSE 
# 		IF NEW.valor != OLD.valor THEN
# 			INSERT INTO historico_precos (id_produto, valor) 
# 			VALUES (NEW.id, NEW.valor);
# 		ELSE
# 			RAISE EXCEPTION 'Valor Igual ao Existente';
# 		END IF;
# 	END IF;
	
# END;
# $$ LANGUAGE plpgsql;

# CREATE OR REPLACE TRIGGER trigger_grava_historico_preco
#     BEFORE INSERT OR UPDATE 
#     ON public.produtos
#     FOR EACH ROW
#     EXECUTE FUNCTION public.grava_historico_preco();