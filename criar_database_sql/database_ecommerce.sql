CREATE DATABASE DATABASE ecommerce;

USE ecommerce;

-- criar tabela cliente

CREATE TABLE Clients(
	idClient INT auto_increment PRIMARY KEY,
	  Fname VARCHAR(10),
    Minit CHAR(3),
	  Lname VARCHAR(20),
    CPF CHAR (11) NOT NULL,
    Address VARCHAR(30),
    CONSTRAINT unique_cpf_cliente UNIQUE (CPF)
);

CREATE TABLE clients auto_incremente=1;

--desc clients;
-- criar tabela produto
-- size = dimensão do produto
CREATE TABLE product(
	idProduct INT auto_increment PRIMARY KEY,
	  Pname VARCHAR(10),
    classification_kids bool,
	  category enum('Eletrônico', 'Vestimenta', 'Brinquedos', 'Alimentos', 'Móveis') NOT NULL,
    avaliação FLOAT DEFAULT 0, # se não colocar nada o valor vai ser NULL
    size VARCHAR(10)
);

-- Desafio - terminar de implementar a tabela e criar conexão com as tabelas relacionadas
-- Refletir sobre as modificações relacionadas no diagrama
-- Criar CONSTRAINT relacionar ao pagamento
CREATE TABLE payments(
	idclient INT,
    idPayment INT,
    typePayment enum('Boleto', 'Cartão', 'Dinheiro', 'PIX'),
    limitAvailable FLOAT,
    PRIMARY KEY (idCliente, id_playment)
);

-- criar tabela pedido
CREATE TABLE orders(
	idOrder INT auto_increment PRIMARY KEY,
    idOrderCliente INT,
    orderStatus enum('Cancelado', 'Confirmado', 'Em Processamento') DEFAULT 'Em processamento',
    orderDescription VARCHAR(225),
    sendValue FLOAT DEFAULT 10,
    paymentCash BOOLEAN DEFAULT false,
    CONSTRAINT fk_orders_client FOREIGN KEY (idOrderCliente) REFERENCES clients(idClient) ON UPDATE cascade
);

-- DESC orders;

-- criar tabela estoque
CREATE TABLE productStorage(
	idProdStorage INT auto_increment PRIMARY KEY,
    storageLocation VARCHAR(225),
    quantity INT DEFAULT 0
);

-- criar tabela fornecedor
CREATE TABLE supplier(
	idSupllier INT auto_increment PRIMARY KEY,
    SocialName VARCHAR(225) NOT NULL,
    CNPJ CHAR(15) NOT NULL,
    contact VARCHAR(11) NOT NULL,
    CONSTRAINT unique_supplier UNIQUE (CNPJ)
);

CREATE TABLE seller(
	idSeller INT auto_increment PRIMARY KEY,
    SocialName VARCHAR(225) NOT NULL,
    abstName VARCHAR(225),
    CNPJ CHAR(15),
    CPF CHAR(9),
    location VARCHAR(255),
    contact VARCHAR(11) NOT NULL,
    CONSTRAINT unique_cnpj_supplier UNIQUE (CNPJ),
    CONSTRAINT unique_cpf_supplier UNIQUE (CPF)
);

CREATE TABLE productSeller(
	idPseller INT, #vai herdar valores de uma FK
    idProduct INT,
    prodQuantity INT DEFAULT 1,
    PRIMARY KEY (idPseller, IdProduct),
    CONSTRAINT fk_product_seller FOREIGN KEY (idPseller) REFERENCES seller (idSeller),
    CONSTRAINT fk_product_product FOREIGN KEY (idProduct) REFERENCES product (idProduct) #Tabela product
);

-- DESC productSeller;

CREATE TABLE productOrder(
	idPOproduct INT, #vai herdar valores de uma FK
    idPOorder INT,
    poQuantity INT DEFAULT 1,
    poStatus enum('Disponível', 'Sem estoque') DEFAULT 'Disponível',
    PRIMARY KEY (idPOproduct, idPOorder),
    CONSTRAINT fk_productorder_seller FOREIGN KEY (idPOproduct) REFERENCES product(idProduct),
    CONSTRAINT fk_productorder_product FOREIGN KEY (idPOorder) REFERENCES orders(idOrder)
);

create table storageLocation(
	idLproduct INT, #vai herdar valores de uma FK
    idLsotrage INT,
    location VARCHAR(255) NOT NULL,
    PRIMARY KEY (idLproduct, idLsotrage),
    CONSTRAINT fk_storage_location_product FOREIGN KEY (idLproduct) REFERENCES product(idProduct),
    CONSTRAINT fk_product_product_storage FOREIGN KEY (idLsotrage) REFERENCES productStorage(idProdStorage)
);

create table productSupplier(
		idPsSupplier INT,
		idPsProduct INT
		quantity INT NOT NULL,
		PRIMARY KEY (idPsSupplier, idPsProduct),
		CONSTRAINT fk_product_supplier_product FOREIGN KEY (idPsSupplier) REFERENCES supplier (idSupplier),
		CONSTRAINT fk_product_supplier_product FOREIGN KEY (idPsProduct) REFERENCES product(idProduct)
);
