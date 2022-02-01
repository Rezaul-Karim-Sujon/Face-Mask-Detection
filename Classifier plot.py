import matplotlib.pyplot as plt
x = [0,1]
ModelName = ['MobileNetV2','Optimized MobileNetV2']
accuracy=[94.2,98.6]
withmask=[94.84,98.95]
withoutmask=[96.05,98.7]
plt.xticks(x, ModelName)
plt.xticks(range(2), ModelName, rotation=0) #writes strings with 45 degree angle
plt.plot(x,accuracy,'X',color='red',label="Accuracy")
plt.plot(x,accuracy,color='red')
plt.text(0,accuracy[0]-.2,accuracy[0],color='red')
plt.text(1,accuracy[1]-.2,accuracy[1],color='red')

plt.plot(x,withmask,'X',color='green',label="F1 score with mask")
plt.plot(x,withmask,color='green')
plt.text(0,withmask[0]-.2,withmask[0],color='green')
plt.text(1,withmask[1]-.2,withmask[1],color='green')

plt.plot(x,withoutmask,'X',color='blue',label="F1 score without mask")
plt.plot(x,withoutmask,color='blue')
plt.text(0,withoutmask[0]-.2,withoutmask[0],color='blue')
plt.text(1,withoutmask[1]-.2,withoutmask[1],color='blue')

plt.title("Training Accuracy")
plt.xlabel("Percentage")
plt.ylabel("Model")
plt.legend()
#plt.show()
plt.savefig("Classifier.png")