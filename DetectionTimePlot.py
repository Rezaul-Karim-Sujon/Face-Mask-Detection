import matplotlib.pyplot as plt
x = [0,1]
ModelName = ['DSFD','Open-CV DNN']
GPU=[87,200]
CPU=[27,60]
plt.xticks(x, ModelName)
plt.xticks(range(2), ModelName, rotation=0) #writes strings with 45 degree angle
plt.plot(x,GPU,'X',color='red',label="FPS in GPU")
plt.plot(x,GPU,color='red')
plt.text(0.05,GPU[0],GPU[0],color='red')
plt.text(1-.1,GPU[1],GPU[1],color='red')

plt.plot(x,CPU,'X',color='green',label="FPS in CPU")
plt.plot(x,CPU,color='green')
plt.text(0.05,CPU[0],CPU[0],color='green')
plt.text(1-.1,CPU[1],CPU[1],color='green')

plt.title("Detection TIme")
plt.ylabel("Frame Per Second")
plt.xlabel("Model")
plt.legend()
#plt.show()
plt.savefig("Classifier.png")