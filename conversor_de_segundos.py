tempoEmSegundos = int(input("Digite o tempo em segundos: "));

tempoEmMinutos = tempoEmSegundos // 60;
restoEmSegundos = tempoEmSegundos % 60;
 
tempoEmHoras = tempoEmMinutos // 60;
tempoEmMinutos = tempoEmMinutos % 60;

tempoEmDias = tempoEmHoras // 24;
tempoEmHoras = tempoEmHoras % 24;

print(tempoEmDias, 'dias', tempoEmHoras, 'horas' , tempoEmMinutos, ' min',  restoEmSegundos, 'seg .');

