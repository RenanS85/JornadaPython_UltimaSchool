from Modulo_1.utilidades.uteis import leiaFloat,leiaInt

preco_prod = leiaFloat('Dgite o preço do produto: R$: ')
form_pgmt = leiaInt('Escolha a forma de pagamento:'
                       '\nDIGITE 1 para pagamento a com dinheito'
                       '\nDIGITE 2 para cartão de crédito'
                       '\nForma de pagameanto: ')

preco_dinheiro = preco_prod - (preco_prod * 0.15)
preco_cartaoavista = preco_prod - (preco_prod * 0.10)
preco_parc2x = preco_prod
preco_parc_maisde2x = preco_prod + (preco_prod * 0.10)

if form_pgmt == 1:
    print('O valor é {:.2f}, no dinheiro'.format(preco_dinheiro))

if form_pgmt == 2:
    vai_parcelar = (int(input('Selecione a forma de parcelamento:'
                              '\n DIGITE 1 para cartão de crédito a vista'
                              '\n DIGITE 2 para parcelar'
                              '\n FORMA DE PAGAMENTO: ')))

if form_pgmt == 2 and vai_parcelar == 1:
    print('O valor é {:.2f}, no crédito a vista'.format(preco_cartaoavista))

if form_pgmt == 2 and vai_parcelar == 2:
    numero_parcelas = (int(input('Selecione o numero de parcelas'
                                 '\nentre 2 e 12'
                                 '\n DIGITE O NÚMERO DE PARCELAS: ')))

if numero_parcelas == 2:
    print('O valor é {:.2f}, em 2 parcelas de {:.2f}'.format(preco_parc2x, preco_parc2x / 2))
elif numero_parcelas > 2:
    print('O valor é {:.2f}, em {} parcelas de {:.2f}'.format(preco_parc_maisde2x, numero_parcelas,
                                                              preco_parc2x / numero_parcelas))
