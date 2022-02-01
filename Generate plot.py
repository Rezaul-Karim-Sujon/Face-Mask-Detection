import matplotlib.pyplot as plt
accuracy=[0.9160,0.9223,0.9430,0.9549,0.9675,0.9744,.9787,.9803,.9843,.9859,.9866,.9875,.9892,.9895,.9898,.9898,.9895,.9888,.9908,.9912]
ValueAccuracy=[0.8960,0.9091,0.9295,0.9380,0.9512,0.9575,.9669,.9671,.9643,.9759,.9766,.9781,.9795,.9854,.9830,.9839,.9855,.9861,.9830,.9870]
loss=[0.2022,0.1920,0.1711,0.1675,0.1530,0.0991,0.0825,0.0618,0.0543,0.0472,0.0436,0.0421,0.0343,.0332,.0344,.0293,.0266,.0310,.0292,0.0256]
ValueLoss=[0.2151,0.2085,0.2011,0.1975,0.1918,0.1528,.1373,.1269,.1198,.1103,.1011,.0821,.0524,.0389,.0425,.0510,0.0439,0.0325,0.0419,0.0349]
Average_accuracy=0.00
for i in accuracy:
    Average_accuracy+=i
N=len(accuracy)
print(len(ValueLoss))

#plot for testing accuracy
plt.style.use("ggplot")
plt.figure()
plt.plot(accuracy,label="train_acc")
plt.plot(ValueAccuracy,label="Val_acc")
plt.title("Training Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Accuracy")
plt.legend(loc="lower right")
plt.savefig("AccuracyPlot.png")

#plot for testing loss
plt.style.use("ggplot")
plt.figure()
plt.plot(loss,label="train_loss")
plt.plot(ValueLoss,label="Val_loss")
plt.title("Training loss")
plt.xlabel("Epoch #")
plt.ylabel("Loss")
plt.legend(loc="upper right")
plt.savefig("LossPlot.png")
