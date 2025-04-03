def salvar_carro(marca, modelo, ano, placa):
  print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Palio", "Fiat", 1999, "ABC-1234")
salvar_carro(marca="Palio", modelo="Fiat", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Palio", "modelo": "Fiat", "ano": 1999, "placa": "ABC-1234"})