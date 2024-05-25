# É sempre importante olhar a documentação; https://matplotlib.org/stable/index.html
#Importar a biblioteca;
import matplotlib.pyplot as plt 
# Tipos de gráficos: Ao invés de utilizar o plt.plot vc utiliza: Ex: .bar() para de barra;
#Parâmetros/ variáveis;
x = [1,2,3,4]
y = [2,3,4,3]
#Você também pode declarar dessa forma:
#plt.axis(xmin=1, xmax=2, ymin=0,ymax=3)
plt.plot(x,y, label="dados") # Label é um parâmetro para adicionar na legenda;
plt.ylabel("Eixo y") # nome na lateral do eixo y;
plt.xlabel("Eixo x")
plt.title("Títtulo do gráficos") # Título;
# plt.xticks([0,4,6,8,9]) Escala;
#plt.yticks([]) ; Os tikcs são os numéros entre o outros; Ex: 1,(1.5), 2, (2.3), 3, etc...
plt.legend() # pega o "Label='dados" e adiciona como legenda no lado superior do gráfico;
plt.plot(x,y, linestyle="dashed", color="g", lw=10) # Estilo de linha, 'dashed' é potilhado; pode ser: dois pontos(':');
# As cores são expressar por: y, g, b, w, etc...
# Lw = Largura da linha do gráfico;
plt.show() # Imprimir o gráfico;