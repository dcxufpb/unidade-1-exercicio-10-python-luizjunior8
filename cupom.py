# coding: utf-8

class Loja:
  
  def __init__(self, nome_loja, logradouro, numero, complemento, bairro, 
               municipio, estado, cep, telefone, observacao, cnpj,
               inscricao_estadual):
    self.nome_loja = nome_loja
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual


  def validar_campos_obrigatorios(self):

    if not self.nome_loja:
        raise Exception("O campo nome da loja é obrigatório")

    if not self.logradouro:
        raise Exception("O campo logradouro do endereço é obrigatório")

    if not self.municipio:
        raise Exception("O campo município do endereço é obrigatório")  

    if not self.estado:
        raise Exception("O campo estado do endereço é obrigatório") 

    if not self.cnpj:
        raise Exception("O campo CNPJ da loja é obrigatório") 

    if not self.inscricao_estadual:
        raise Exception("O campo inscrição estadual da loja é obrigatório")
      

  def dados_loja(self):

    self.validar_campos_obrigatorios()

    _numero = "s/n" if not self.numero else str(self.numero)

    _complemento = ""

    if self.complemento:
       _complemento = " " + self.complemento

    _bairro = ""

    if self.bairro:
        _bairro = self.bairro + " - "

    _cep = ""
    _telefone = ""

    if self.cep:
        _cep = "CEP:" + self.cep

        if self.telefone:
            _telefone = " Tel " + self.telefone

    else:
        _telefone = "Tel " + self.telefone

    _observacao = ""

    if self.observacao:
        _observacao = self.observacao

    typewriter = self.nome_loja + "\n"
    typewriter += self.logradouro + ", " + _numero + _complemento + "\n"
    typewriter += _bairro + self.municipio + " - " + self.estado + "\n"
    typewriter += _cep + _telefone + "\n"
    typewriter += _observacao + "\n"
    typewriter += "CNPJ: " + self.cnpj + "\n"
    typewriter += "IE: " + self.inscricao_estadual

    return typewriter
