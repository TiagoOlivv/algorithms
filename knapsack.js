// criando os itens
var itens = [
  {
    id: 1,
    nome: "item 1",
    peso: 3,
    valor: 40
  },
  {
    id: 2,
    nome: "item 1",
    peso: 3,
    valor: 40
  },
  {
    id: 3,
    nome: "item 1",
    peso: 3,
    valor: 40
  },
  {
    id: 4,
    nome: "item 2",
    peso: 5,
    valor: 100
  },
  {
    id: 5,
    nome: "item 2",
    peso: 5,
    valor: 100
  },
  {
    id: 6,
    nome: "item 3",
    peso: 2,
    valor: 50
  },
  {
    id: 7,
    nome: "item 3",
    peso: 2,
    valor: 50
  },
  {
    id: 8,
    nome: "item 3",
    peso: 2,
    valor: 50
  },
  {
    id: 9,
    nome: "item 3",
    peso: 2,
    valor: 50
  },
  {
    id: 10,
    nome: "item 3",
    peso: 2,
    valor: 50
  }
];

//criando variaveis necessarias
var contadorMochila = 0;
var selecionados = [];
var max;
var valorMochila = 0;

//definindo capacidade maxima da mochila
const capacidade = 20;

//funcao para remover item da mochila para fazer proxima verificacao
var removeByAttr = function(arr, attr, value) {
  var i = arr.length;
  while (i--) {
    if (
      arr[i] &&
      arr[i].hasOwnProperty(attr) &&
      (arguments.length > 2 && arr[i][attr] === value)
    ) {
      arr.splice(i, 1);
    }
  }
};

do {
  //encontra o item com maior valor
  max = itens.reduce(function(anterior, atual) {
    return anterior.valor > atual.valor ? anterior : atual;
  });
  //se ainda tiver espaco na mochila ele inclui o elemento com peso maximo
  if (max.peso + contadorMochila <= capacidade) {
    selecionados.push(max);
    contadorMochila += max.peso; //ele aumenta o valor do contador da mochila
    valorMochila += max.valor; //ele aumenta o valor da mochila
    removeByAttr(itens, "id", max.id); //remove o item com maior valor da relacao inicial de itens
  } else {
    //caso o item com peso maximo nao couber na mochila ele apenas remove esse item da relacao inicial para a proxima verificacao
    removeByAttr(itens, "id", max.id);
  }
} while (capacidade > contadorMochila && itens.length > 0); //roda o loop ate que a capacidade esgote ou ate que a relacao inicial de itens esteja vazia

selecionados;
valorMochila;

//Gerando visualização no arquivo HTML

var rows = selecionados;
var html = "<table border='1|1' align='center'>";
html +=
  '<tr><th colspan="4">Escolhidos</th></tr><tr><td>id:</td><td>nome:</td><td>peso:</td><td>valor:</td></tr>';
for (var i = 0; i < rows.length; i++) {
  html += "<tr>";
  html += "<td>" + rows[i].id + "</td>";
  html += "<td>" + rows[i].nome + "</td>";
  html += "<td>" + rows[i].peso + "</td>";
  html += "<td>" + rows[i].valor + "</td>";

  html += "</tr>";
}
html += "</table>";
document.getElementById("itens").innerHTML = html;

document.getElementById("valor").innerHTML = valorMochila;
