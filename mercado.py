def supermercado():
    preco_arroz = 25.50
    preco_feijao = 8.90
    preco_oleo = 7.00
    preco_cafe = 50.00
    preco_leite = 4.50

    qtd_arroz = 0
    qtd_feijao = 0
    qtd_oleo = 0
    qtd_cafe = 0
    qtd_leite = 0

    subtotal_arroz = 0
    subtotal_feijao = 0
    subtotal_oleo = 0
    subtotal_cafe = 0
    subtotal_leite = 0

    sair = False
    while sair == False:
        print("\n**** Supermercado Python ****")
        print("1. Adicionar item ao carrinho")
        print("2. Ver total da compra")
        print("3. Finalizar compra")

        opcao = 0
        while opcao < 1 or opcao > 3:
            entrada = input("Escolha uma opcao (1-3): ")
            if entrada.isdigit():
                opcao = int(entrada)
            if opcao < 1 or opcao > 3:
                print("Opcao invalida! Digite 1, 2 ou 3.")

        if opcao == 1:
            produto = ""
            while produto != "arroz" and produto != "feijao" and produto != "oleo de soja" and produto != "cafe" and produto != "leite":
                produto = input("Digite o nome do produto: ").lower()
                if produto != "arroz" and produto != "feijao" and produto != "oleo de soja" and produto != "cafe" and produto != "leite":
                    print("Produto nao encontrado! Digite novamente.")

            qtd = 0
            while qtd <= 0:
                entrada_qtd = input("Digite a quantidade (numero inteiro maior que 0): ")
                if entrada_qtd.isdigit():
                    qtd = int(entrada_qtd)
                if qtd <= 0:
                    print("Quantidade invalida!")

            if produto == "arroz":
                subtotal = preco_arroz * qtd
                if qtd > 3:
                    subtotal = subtotal - subtotal * 0.03
                    print("-> Desconto de 3% por volume aplicado!")
                qtd_arroz = qtd_arroz + qtd
                subtotal_arroz = subtotal_arroz + subtotal

            elif produto == "feijao":
                subtotal = preco_feijao * qtd
                if qtd > 3:
                    subtotal = subtotal - subtotal * 0.03
                    print("-> Desconto de 3% por volume aplicado!")
                qtd_feijao = qtd_feijao + qtd
                subtotal_feijao = subtotal_feijao + subtotal

            elif produto == "oleo de soja":
                subtotal = preco_oleo * qtd
                if qtd > 3:
                    subtotal = subtotal - subtotal * 0.03
                    print("-> Desconto de 3% por volume aplicado!")
                qtd_oleo = qtd_oleo + qtd
                subtotal_oleo = subtotal_oleo + subtotal

            elif produto == "cafe":
                subtotal = preco_cafe * qtd
                if qtd > 3:
                    subtotal = subtotal - subtotal * 0.03
                    print("-> Desconto de 3% por volume aplicado!")
                qtd_cafe = qtd_cafe + qtd
                subtotal_cafe = subtotal_cafe + subtotal

            elif produto == "leite":
                subtotal = preco_leite * qtd
                if qtd > 3:
                    subtotal = subtotal - subtotal * 0.03
                    print("-> Desconto de 3% por volume aplicado!")
                qtd_leite = qtd_leite + qtd
                subtotal_leite = subtotal_leite + subtotal

            print(str(qtd) + " x " + produto + " adicionado(s).")

        elif opcao == 2:
            total = subtotal_arroz + subtotal_feijao + subtotal_oleo + subtotal_cafe + subtotal_leite
            print("Total parcial da compra: R$ " + str(total))

        elif opcao == 3:
            total_bruto = subtotal_arroz + subtotal_feijao + subtotal_oleo + subtotal_cafe + subtotal_leite

            if total_bruto == 0:
                print("Carrinho vazio. Nenhuma compra finalizada.")
                sair = True
            else:
                print("\n==================== RECIBO ===================")
                if qtd_arroz > 0:
                    print(str(qtd_arroz) + " x Arroz (R$ " + str(preco_arroz) + "/un) R$ " + str(subtotal_arroz))
                if qtd_feijao > 0:
                    print(str(qtd_feijao) + " x Feijao (R$ " + str(preco_feijao) + "/un) R$ " + str(subtotal_feijao))
                if qtd_oleo > 0:
                    print(str(qtd_oleo) + " x Oleo de soja (R$ " + str(preco_oleo) + "/un) R$ " + str(subtotal_oleo))
                if qtd_cafe > 0:
                    print(str(qtd_cafe) + " x Cafe (R$ " + str(preco_cafe) + "/un) R$ " + str(subtotal_cafe))
                if qtd_leite > 0:
                    print(str(qtd_leite) + " x Leite (R$ " + str(preco_leite) + "/un) R$ " + str(subtotal_leite))

                desconto_final = 0
                perc = "0%"
                if total_bruto > 200:
                    desconto_final = total_bruto * 0.15
                    perc = "15%"
                elif total_bruto >= 100:
                    desconto_final = total_bruto * 0.10
                    perc = "10%"

                valor_final = total_bruto - desconto_final

                print("-----------------------------------------------")
                print("Total Bruto: R$ " + str(total_bruto))
                print("Desconto da Compra (" + perc + "): R$ " + str(desconto_final))
                print("-----------------------------------------------")
                print("Valor Final a Pagar: R$ " + str(valor_final))
                print("===============================================")
                print("Obrigado pela sua compra!")

                sair = True

supermercado()
