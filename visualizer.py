from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation as fa
from adjustText import adjust_text

f=open("tsp_input_1.txt","r")


list_x=[]
list_y=[]

for s in f:
    temp=s
    temp.strip()
    print(temp)
    base=temp.split(' ')
    list_1=[]
    for num in base:
        list_1.append(int(num.strip('\n')))
    list_x.append(list_1[1])
    list_y.append(list_1[2])

fig,plots=plt.subplots(1,2)
plt.style.use("fivethirtyeight")
plots[1].set_title("Travelling salesman visualizer")
plots[1].set_xlabel("X-axis")
plots[1].set_ylabel("Y-axis")
plots[0].set_title("cities plot")
plots[0].set_xlabel("X-axis")
plots[0].set_ylabel("Y-axis")
plots[0].scatter(list_x,list_y,color="red")
for i_x, i_y in zip(list_x, list_y):
    plots[0].text(i_x, i_y, '({}, {})'.format(i_x, i_y),size=10)
f.close()
f=open("tsp_output",'r')

order=[]
for s in f:
    temp=s
    temp.strip()
    print(temp)
    base=temp.split(' ')
    list_1=[]
    for num in base:
        list_1.append(int(num.strip('\n')))
    order.append(list_1[0])


new_list_x=[]
new_list_y=[]
print(len(list_x))
print(len(order))
for i in range(1,len(order)):
    new_list_x.append(list_x[order[i]])
    new_list_y.append(list_y[order[i]])

plots[1].scatter(new_list_x,new_list_y,color="red",label="cities")


count=0
temp_x=[]
temp_y=[]
def animate(i):
    global count
    if count==len(new_list_x):
        return
    temp_x.append(new_list_x[count])
    temp_y.append(new_list_y[count])
    temp1=[]
    temp1.append(plots[1].text(new_list_x[count],new_list_y[count],count+1))
    adjust_text(temp1, only_move={'points':'y', 'temp1':'y'},
    arrowprops=dict(arrowstyle="->", color='r', lw=0.8))
    plots[1].plot(temp_x,temp_y,color="k",linewidth=2)
    count+=1

ani=fa(fig,animate,frames=60,interval=100,save_count=100)
plt.get_current_fig_manager().window.state('zoomed')

plt.legend()
plt.show()
f.close()
