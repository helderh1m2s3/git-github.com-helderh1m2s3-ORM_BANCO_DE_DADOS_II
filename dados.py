from esquema import CATEGORIA, CLIENTE, PRODUTOS, HISTORICO_PRECOS, VENDAS

categorias = [
    {'descricao' : "Papelaria"},
    {'descricao' : "Higiene"},
    {'descricao' : "Informatica"},
    {'descricao' : "Padaria"},
    {'descricao' : "Bebidas"}
]

CATEGORIA.insert_many(categorias).execute()

clientes = [
    {'nome' : "Edgler Martins", 'endereco' : "Rua 1, Nº 1, Bairro 1"},
    {'nome' : "Helder Martins", 'endereco' : "Rua 2, Nº 2, Bairro 2"},
    {'nome' : "Maria dos Remedios", 'endereco' : "Rua 3, Nº 3, Bairro 3"},
    {'nome' : "Eveline Martins", 'endereco' : "Rua 4, Nº 4, Bairro 4"},
    {'nome' : "Paulo Martins", 'endereco' : "Rua 5, Nº 5, Bairro 5"}
]

CLIENTE.insert_many(clientes).execute()

produtos = [
    
    {'descricao' :  "Caneta Bic esferográfica azul", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Papelaria"), 'valor' : 1.30},
    {'descricao' :  "Folha A4 - 500 unidades", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Papelaria"), 'valor' : 28},
    {'descricao' :  "Tesoura", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Papelaria"), 'valor' : 5.30},
    {'descricao' :  "Grampeador", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Papelaria"), 'valor' : 25.60},
    {'descricao' :  "Regua 30cm", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Papelaria"), 'valor' : 3},
    {'descricao' :  "Papel Higienico 16 unidade", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Higiene"), 'valor' : 18.80},
    {'descricao' :  "Creme Dental", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Higiene"), 'valor' : 2.50},
    {'descricao' :  "Lamina de Barbear", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Higiene"), 'valor' : 12},
    {'descricao' :  "Pente Fino", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Higiene"), 'valor' : 4},
    {'descricao' :  "Hastes Flexiveis com Ponta de Algodao", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Higiene"), 'valor' : 3.20},
    {'descricao' :  "Teclado", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Informatica"), 'valor' : 30},
    {'descricao' :  "Monitor 24 polegadas", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Informatica"), 'valor' : 1100},
    {'descricao' :  "Caixa de Som", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Informatica"), 'valor' : 35},
    {'descricao' :  "Computador i7", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Informatica"), 'valor' : 3089.50},
    {'descricao' :  "Mouse", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Informatica"), 'valor' : 15.60},
    {'descricao' :  "Pão unidade", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Padaria"), 'valor' : 0.80},
    {'descricao' :  "Bolo", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Padaria"), 'valor' : 15},
    {'descricao' :  "Pastel", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Padaria"), 'valor' : 5.50},
    {'descricao' :  "Torta de Frango", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Padaria"), 'valor' : 80},
    {'descricao' :  "Pudim", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Padaria"), 'valor' : 50},
    {'descricao' :  "Cerveja skol 350 ml", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Bebidas"), 'valor' : 3.80},
    {'descricao' :  "Agua Mineral 500 ml", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Bebidas"), 'valor' : 2},
    {'descricao' :  "Whisky 1000 ml", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Bebidas"), 'valor' : 145},
    {'descricao' :  "Suco de Uva 500 ml", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Bebidas"), 'valor' : 4.50},
    {'descricao' :  "Agua Tonica 350 ml", 'id_categoria' : CATEGORIA.get(CATEGORIA.descricao == "Bebidas"), 'valor' : 6}
]

PRODUTOS.insert_many(produtos).execute()

produto1 = PRODUTOS.select().where(PRODUTOS.descricao == "Caneta Bic esferográfica azul").get()
produto2 = PRODUTOS.select().where(PRODUTOS.descricao == "Folha A4 - 500 unidades").get()
produto3 = PRODUTOS.select().where(PRODUTOS.descricao == "Tesoura").get()
produto4 = PRODUTOS.select().where(PRODUTOS.descricao == "Grampeador").get()
produto5 = PRODUTOS.select().where(PRODUTOS.descricao == "Regua 30cm").get()
produto6 = PRODUTOS.select().where(PRODUTOS.descricao == "Papel Higienico 16 unidade").get()
produto7 = PRODUTOS.select().where(PRODUTOS.descricao == "Creme Dental").get()
produto8 = PRODUTOS.select().where(PRODUTOS.descricao == "Lamina de Barbear").get()
produto9 = PRODUTOS.select().where(PRODUTOS.descricao == "Pente Fino").get()
produto10 = PRODUTOS.select().where(PRODUTOS.descricao == "Hastes Flexiveis com Ponta de Algodao").get()
produto11 = PRODUTOS.select().where(PRODUTOS.descricao == "Teclado").get()
produto12 = PRODUTOS.select().where(PRODUTOS.descricao == "Monitor 24 polegadas").get()
produto13 = PRODUTOS.select().where(PRODUTOS.descricao == "Caixa de Som").get()
produto14 = PRODUTOS.select().where(PRODUTOS.descricao == "Computador i7").get()
produto15 = PRODUTOS.select().where(PRODUTOS.descricao == "Mouse").get()
produto16 = PRODUTOS.select().where(PRODUTOS.descricao == "Pão unidade").get()
produto17 = PRODUTOS.select().where(PRODUTOS.descricao == "Bolo").get()
produto18 = PRODUTOS.select().where(PRODUTOS.descricao == "Pastel").get()
produto19 = PRODUTOS.select().where(PRODUTOS.descricao == "Torta de Frango").get()
produto20 = PRODUTOS.select().where(PRODUTOS.descricao == "Pudim").get()
produto21 = PRODUTOS.select().where(PRODUTOS.descricao == "Cerveja skol 350 ml").get()
produto22 = PRODUTOS.select().where(PRODUTOS.descricao == "Agua Mineral 500 ml").get()
produto23 = PRODUTOS.select().where(PRODUTOS.descricao == "Whisky 1000 ml").get()
produto24 = PRODUTOS.select().where(PRODUTOS.descricao == "Suco de Uva 500 ml").get()
produto25 = PRODUTOS.select().where(PRODUTOS.descricao == "Agua Tonica 350 ml").get()


historico_precos = [
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Caneta Bic esferográfica azul"), 'valor' : produto1.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Folha A4 - 500 unidades"), 'valor' : produto2.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Tesoura"), 'valor' : produto3.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Grampeador"), 'valor' : produto4.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Regua 30cm"), 'valor' : produto5.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Papel Higienico 16 unidade"), 'valor' : produto6.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Creme Dental"), 'valor' : produto7.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Lamina de Barbear"), 'valor' : produto8.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Pente Fino"), 'valor' : produto9.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Hastes Flexiveis com Ponta de Algodao"), 'valor' : produto10.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Teclado"), 'valor' : produto11.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Monitor 24 polegadas"), 'valor' : produto12.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Caixa de Som"), 'valor' : produto13.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Computador i7"), 'valor' : produto14.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Mouse"), 'valor' : produto15.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Pão unidade"), 'valor' : produto16.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Bolo"), 'valor' : produto17.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Pastel"), 'valor' : produto18.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Torta de Frango"), 'valor' : produto19.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Pudim"), 'valor' : produto20.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Cerveja skol 350 ml"), 'valor' : produto21.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Agua Mineral 500 ml"), 'valor' : produto22.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Whisky 1000 ml"), 'valor' : produto23.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Suco de Uva 500 ml"), 'valor' : produto24.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao ==  "Agua Tonica 350 ml"), 'valor' : produto25.valor}
]

HISTORICO_PRECOS.insert_many(historico_precos).execute()


vendas = [
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Caneta Bic esferográfica azul"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 5 , 'valor_unitario' : produto1.valor, 'valor_total' : 5 * produto1.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Folha A4 - 500 unidades"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 6 , 'valor_unitario' : produto2.valor, 'valor_total' : 6 * produto2.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Tesoura"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 3 , 'valor_unitario' : produto3.valor, 'valor_total' : 3 * produto3.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Grampeador"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 8 , 'valor_unitario' : produto4.valor, 'valor_total' : 8 * produto4.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Regua 30cm"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 45 , 'valor_unitario' : produto5.valor, 'valor_total' : 45 * produto5.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Papel Higienico 16 unidade"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 7 , 'valor_unitario' : produto6.valor, 'valor_total' : 7 * produto6.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Creme Dental"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 12 , 'valor_unitario' : produto7.valor, 'valor_total' : 12 * produto7.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Lamina de Barbear"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 76 , 'valor_unitario' : produto8.valor, 'valor_total' : 76 * produto8.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pente Fino"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 234 , 'valor_unitario' : produto9.valor, 'valor_total' : 234 * produto9.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Hastes Flexiveis com Ponta de Algodao"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 87 , 'valor_unitario' : produto10.valor, 'valor_total' : 87 * produto10.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Teclado"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 987 , 'valor_unitario' : produto11.valor, 'valor_total' : 987 * produto11.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Monitor 24 polegadas"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 90 , 'valor_unitario' : produto12.valor, 'valor_total' : 90 * produto12.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Caixa de Som"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 34 , 'valor_unitario' : produto13.valor, 'valor_total' : 34 * produto13.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Computador i7"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 67 , 'valor_unitario' : produto14.valor, 'valor_total' : 67 * produto14.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Mouse"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 1234 , 'valor_unitario' : produto15.valor, 'valor_total' : 1234 * produto15.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pão unidade"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 60 , 'valor_unitario' : produto16.valor, 'valor_total' : 60 * produto16.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Bolo"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 123 , 'valor_unitario' : produto17.valor, 'valor_total' : 123 * produto17.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pastel"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 367 , 'valor_unitario' : produto18.valor, 'valor_total' : 367 * produto18.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Torta de Frango"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 980 , 'valor_unitario' : produto19.valor, 'valor_total' : 980 * produto19.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pudim"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 23 , 'valor_unitario' : produto20.valor, 'valor_total' : 23 * produto20.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Cerveja skol 350 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 43 , 'valor_unitario' : produto21.valor, 'valor_total' : 43 * produto21.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Agua Mineral 500 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 21 , 'valor_unitario' : produto22.valor, 'valor_total' : 21 * produto22.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Whisky 1000 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 12 , 'valor_unitario' : produto23.valor, 'valor_total' : 12 * produto23.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Suco de Uva 500 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 5 , 'valor_unitario' : produto24.valor, 'valor_total' : 5 * produto24.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Agua Tonica 350 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Edgler Martins") , 'quantidade' : 3 , 'valor_unitario' : produto25.valor, 'valor_total' : 3 * produto25.valor},
    
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Caneta Bic esferográfica azul"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 15 , 'valor_unitario' : produto1.valor, 'valor_total' : 15 * produto1.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Folha A4 - 500 unidades"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 56 , 'valor_unitario' : produto2.valor, 'valor_total' : 56 * produto2.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Tesoura"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 53 , 'valor_unitario' : produto3.valor, 'valor_total' : 53 * produto3.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Grampeador"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 18 , 'valor_unitario' : produto4.valor, 'valor_total' : 18 * produto4.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Regua 30cm"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 5 , 'valor_unitario' : produto5.valor, 'valor_total' : 5 * produto5.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Papel Higienico 16 unidade"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 7 , 'valor_unitario' : produto6.valor, 'valor_total' : 7 * produto6.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Creme Dental"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 2 , 'valor_unitario' : produto7.valor, 'valor_total' : 2 * produto7.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Lamina de Barbear"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 6 , 'valor_unitario' : produto8.valor, 'valor_total' : 6 * produto8.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pente Fino"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 24 , 'valor_unitario' : produto9.valor, 'valor_total' : 24 * produto9.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Hastes Flexiveis com Ponta de Algodao"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 7 , 'valor_unitario' : produto10.valor, 'valor_total' : 7 * produto10.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Teclado"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 97 , 'valor_unitario' : produto11.valor, 'valor_total' : 97 * produto11.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Monitor 24 polegadas"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 91 , 'valor_unitario' : produto12.valor, 'valor_total' : 91 * produto12.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Caixa de Som"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 314 , 'valor_unitario' : produto13.valor, 'valor_total' : 314 * produto13.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Computador i7"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 17 , 'valor_unitario' : produto14.valor, 'valor_total' : 17 * produto14.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Mouse"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 124 , 'valor_unitario' : produto15.valor, 'valor_total' : 124 * produto15.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pão unidade"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 610 , 'valor_unitario' : produto16.valor, 'valor_total' : 610 * produto16.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Bolo"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 13 , 'valor_unitario' : produto17.valor, 'valor_total' : 13 * produto17.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pastel"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 37 , 'valor_unitario' : produto18.valor, 'valor_total' : 37 * produto18.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Torta de Frango"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 80 , 'valor_unitario' : produto19.valor, 'valor_total' : 80 * produto19.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pudim"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 213 , 'valor_unitario' : produto20.valor, 'valor_total' : 213 * produto20.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Cerveja skol 350 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 413 , 'valor_unitario' : produto21.valor, 'valor_total' : 413 * produto21.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Agua Mineral 500 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 241 , 'valor_unitario' : produto22.valor, 'valor_total' : 241 * produto22.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Whisky 1000 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 152 , 'valor_unitario' : produto23.valor, 'valor_total' : 152 * produto23.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Suco de Uva 500 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 51 , 'valor_unitario' : produto24.valor, 'valor_total' : 51 * produto24.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Agua Tonica 350 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Helder Martins") , 'quantidade' : 31 , 'valor_unitario' : produto25.valor, 'valor_total' : 31 * produto25.valor},

    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Caneta Bic esferográfica azul"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 115 , 'valor_unitario' : produto1.valor, 'valor_total' : 115 * produto1.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Folha A4 - 500 unidades"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 6 , 'valor_unitario' : produto2.valor, 'valor_total' : 6 * produto2.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Tesoura"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 5 , 'valor_unitario' : produto3.valor, 'valor_total' : 5 * produto3.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Grampeador"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 148 , 'valor_unitario' : produto4.valor, 'valor_total' : 148 * produto4.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Regua 30cm"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 5 , 'valor_unitario' : produto5.valor, 'valor_total' : 5 * produto5.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Papel Higienico 16 unidade"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 74 , 'valor_unitario' : produto6.valor, 'valor_total' : 74 * produto6.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Creme Dental"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 2 , 'valor_unitario' : produto7.valor, 'valor_total' : 2 * produto7.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Lamina de Barbear"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 61 , 'valor_unitario' : produto8.valor, 'valor_total' : 61 * produto8.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pente Fino"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 24 , 'valor_unitario' : produto9.valor, 'valor_total' : 24 * produto9.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Hastes Flexiveis com Ponta de Algodao"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 7 , 'valor_unitario' : produto10.valor, 'valor_total' : 7 * produto10.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Teclado"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 97 , 'valor_unitario' : produto11.valor, 'valor_total' : 97 * produto11.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Monitor 24 polegadas"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 70 , 'valor_unitario' : produto12.valor, 'valor_total' : 70 * produto12.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Caixa de Som"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 314 , 'valor_unitario' : produto13.valor, 'valor_total' : 314 * produto13.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Computador i7"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 61 , 'valor_unitario' : produto14.valor, 'valor_total' : 61 * produto14.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Mouse"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 124 , 'valor_unitario' : produto15.valor, 'valor_total' : 124 * produto15.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pão unidade"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 610 , 'valor_unitario' : produto16.valor, 'valor_total' : 610 * produto16.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Bolo"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 13 , 'valor_unitario' : produto17.valor, 'valor_total' : 13 * produto17.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pastel"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 7 , 'valor_unitario' : produto18.valor, 'valor_total' : 7 * produto18.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Torta de Frango"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 80 , 'valor_unitario' : produto19.valor, 'valor_total' : 80 * produto19.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pudim"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 13 , 'valor_unitario' : produto20.valor, 'valor_total' : 13 * produto20.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Cerveja skol 350 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 43 , 'valor_unitario' : produto21.valor, 'valor_total' : 43 * produto21.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Agua Mineral 500 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 24 , 'valor_unitario' : produto22.valor, 'valor_total' : 24 * produto22.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Whisky 1000 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 12 , 'valor_unitario' : produto23.valor, 'valor_total' : 12 * produto23.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Suco de Uva 500 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 1 , 'valor_unitario' : produto24.valor, 'valor_total' : 1 * produto24.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Agua Tonica 350 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Maria dos Remedios") , 'quantidade' : 341 , 'valor_unitario' : produto25.valor, 'valor_total' : 341 * produto25.valor},

    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Caneta Bic esferográfica azul"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Eveline Martins") , 'quantidade' : 15 , 'valor_unitario' : produto1.valor, 'valor_total' : 15 * produto1.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Folha A4 - 500 unidades"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Eveline Martins") , 'quantidade' : 61 , 'valor_unitario' : produto2.valor, 'valor_total' : 61 * produto2.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Tesoura"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Eveline Martins") , 'quantidade' : 15 , 'valor_unitario' : produto3.valor, 'valor_total' : 15 * produto3.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Grampeador"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Eveline Martins") , 'quantidade' : 18 , 'valor_unitario' : produto4.valor, 'valor_total' : 18 * produto4.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Regua 30cm"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Eveline Martins") , 'quantidade' : 15 , 'valor_unitario' : produto5.valor, 'valor_total' : 15 * produto5.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Papel Higienico 16 unidade"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Eveline Martins") , 'quantidade' : 74 , 'valor_unitario' : produto6.valor, 'valor_total' : 74 * produto6.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Creme Dental"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Eveline Martins") , 'quantidade' : 12 , 'valor_unitario' : produto7.valor, 'valor_total' : 12 * produto7.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Lamina de Barbear"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Eveline Martins") , 'quantidade' : 1 , 'valor_unitario' : produto8.valor, 'valor_total' : 1 * produto8.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pente Fino"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Eveline Martins") , 'quantidade' : 2 , 'valor_unitario' : produto9.valor, 'valor_total' : 2 * produto9.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Hastes Flexiveis com Ponta de Algodao"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Eveline Martins") , 'quantidade' : 7 , 'valor_unitario' : produto10.valor, 'valor_total' : 7 * produto10.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Teclado"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Eveline Martins") , 'quantidade' : 7 , 'valor_unitario' : produto11.valor, 'valor_total' : 7 * produto11.valor},

    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Hastes Flexiveis com Ponta de Algodao"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 17 , 'valor_unitario' : produto10.valor, 'valor_total' : 17 * produto10.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Teclado"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 9 , 'valor_unitario' : produto11.valor, 'valor_total' : 9 * produto11.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Monitor 24 polegadas"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 94 , 'valor_unitario' : produto12.valor, 'valor_total' : 94 * produto12.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Caixa de Som"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 34 , 'valor_unitario' : produto13.valor, 'valor_total' : 34 * produto13.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Computador i7"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 67 , 'valor_unitario' : produto14.valor, 'valor_total' : 67 * produto14.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Mouse"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 124 , 'valor_unitario' : produto15.valor, 'valor_total' : 124 * produto15.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pão unidade"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 610 , 'valor_unitario' : produto16.valor, 'valor_total' : 610 * produto16.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Bolo"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 13 , 'valor_unitario' : produto17.valor, 'valor_total' : 13 * produto17.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pastel"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 71 , 'valor_unitario' : produto18.valor, 'valor_total' : 71 * produto18.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Torta de Frango"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 8 , 'valor_unitario' : produto19.valor, 'valor_total' : 8 * produto19.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Pudim"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 113 , 'valor_unitario' : produto20.valor, 'valor_total' : 113 * produto20.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Cerveja skol 350 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 413 , 'valor_unitario' : produto21.valor, 'valor_total' : 413 * produto21.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Agua Mineral 500 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 214 , 'valor_unitario' : produto22.valor, 'valor_total' : 214 * produto22.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Whisky 1000 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 112 , 'valor_unitario' : produto23.valor, 'valor_total' : 112 * produto23.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Suco de Uva 500 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 11 , 'valor_unitario' : produto24.valor, 'valor_total' : 11 * produto24.valor},
    {'id_produto' : PRODUTOS.get(PRODUTOS.descricao == "Agua Tonica 350 ml"), 'id_cliente' : CLIENTE.get(CLIENTE.nome == "Paulo Martins") , 'quantidade' : 31 , 'valor_unitario' : produto25.valor, 'valor_total' : 31 * produto25.valor}
]

VENDAS.insert_many(vendas).execute()