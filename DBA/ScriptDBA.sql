create table if not exists materia_prima(
id_materiaPrima int auto_increment primary key,
nome varchar(100) not null,
formula varchar(50) not null,
quantidade int not null,
lote varchar(25) not null,
data_validade datetime
);

create table fornecedor(
id_fornecedor int auto_increment primary key,
razao_social varchar(100) not null,
cnpj varchar(15) not null,
contato varchar(15) not null
);

create table fornecedor_materiaPrima(
id_fornecedor int,
id_materiaPrima int,
primary key (id_fornecedor, id_materiaPrima), 
foreign key (id_fornecedor) references fornecedor (id_fornecedor),
foreign key (id_materiaPrima) references material_prima (id_materiaPrima)
);

create table pesquisa(
id_pesquisa int auto_increment primary key,
nome_pesquisa varchar(100) not null,
descricao varchar(250) not null,
data_inicio datetime not null,
data_fim datetime not null,
id_etapaPesquisa int not null,
foreign key (id_etapaPesquisa) references etapaPesquisa (id_etapaPesquisa)
);

create table pesquisa_materiaPrima(
id_pesquisa int not null,
id_materiaPrima int not null,
primary key (id_pesquisa, id_materiaPrima),
foreign key (id_pesquisa) references pesquisa (id_pesquisa),
foreign key (id_materiaPrima) references materia_prima (id_materiaPrima)
);

create table etapaPesquisa(
id_etapaPesquisa int primary key auto_increment,
nome_etapa varchar (100),
descricao_etapa varchar (250)
);

create table statusProducao(
id_statusProducao int primary key auto_increment,
nomeStatus varchar (100),
descricaoStatus varchar (250)
);

create table producao(
id_producao int primary key auto_increment,
nomeMediamento varchar (100) not null,
descricaoMedicamento varchar (250) not null,
data_inicio datetime not null,
data_fim datetime not null,
id_statusProducao int not null,
id_pesquisa int not null,
foreign key (id_pesquisa) references pesquisa (id_pesquisa),
foreign key (id_statusProducao) references statusProducao (id_statusProducao)
);

