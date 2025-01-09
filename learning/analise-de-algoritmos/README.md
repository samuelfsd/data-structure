### Análise de algoritmos

Para o estudo da análise de algoritmos deve-se sempre questionar quais tópicos são relevantes para uma determinada análise.

- eficiência e desempenho
- ele é correto ? 
- legibilidade, simplicidade, modularidade, facilidade de manutenção...

Determinar qual seria a eficiência medindo o custo de processamento (ponto bastante importante) e memória daquele algoritmo.

Quais motivos para se estudar a eficiência de um algoritmo

- Conseguir verificar em diferentes tamanhos de entrada quais seriam os comportamentos dos algoritmos
- Comparar diferentes soluções para o mesmo problema

Quais os tipos de se analisar a eficiência ?

- Análise empírica (método preciso porém custoso)

Para isso é preciso um método mais simples, com isso existe o método analítico. Onde, a partir de um algoritmo, podemos saber a sua função de custo. Uma função matemática.

Usando o métodos primitivos vamos conseguir por meio do uso de constantes medir o custo das operações

- Avaliação de expressões booleana ( i >= 2; i == 2, etc, isso para o computador é muito rápido)
- Operações matemáticas ( *, -, +, % )
- Retorno de métodos ( return x )
- Atribuições (i = 2)
- Acesso à variáveis e posições arbitrárias de um array ( arr[i] )

```tsx
function multiplicaRestoPorParteInteira(i: Number, j: Number): Number {
    const resto = i % j;
    const pInteira = i / j;
    const resultado = resto * pInteira;
    
    return resultado;
}
```

Quais seriam os passos para o processo de análise ? 

1. Identificar primitivas

```
c1 -> atribuição (resto =)
c2 -> operação aritmética (i % j)
c3 -> atribuição (pInteira =)
c4 -> operação aritmética (i / j)
c5 -> atribuição (resultado =)
c6 -> operação aritmética (resto * pInteira)
c7 -> retorno de método (return resultado)
```

2. Identificar quantas vezes cada uma das primitivas é executada. 

```
1 * c1
1 * c2
1 * c3
1 * c4
1 * c5
1 * c6
1 * c7


```

3. Somar o custo total.

```
<!-- Note,  na nossa visão N é sempre o tamanho da entrada -->
<!-- Note, essa função não depende de N então o seu tempo independe to tamanho da entrada -->

f(n) = c1 + c2 + c3 + c4 + c5 + c6 + c7

```