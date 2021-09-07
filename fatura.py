# programa que receba (entrada de dados através do teclado) o 
# nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura 
# e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima. 
# Note que o programa imprime a saída em duas linhas diferentes. 
# Note também que, como não é preciso realizar cálculos, 
# o valor não precisa ser convertido para número, pode ser tratado como texto.

customerName = input('Digite o nome do cliente: ');
dueDay =  input('Digite o dia de vencimento: ');
dueMonth = input('Digite o mês de vencimento: ');
billValue = input('Digite o valor da fatura: ');

print('Olá,', customerName);
print('A sua fatura com vencimento em', dueDay ,'de' , dueMonth , 'no valor de R$' , billValue ,'está fechada.');