import matplotlib.pyplot as plt
import numpy as np

x=np.array(['Apple','Facefool','Microsoft','OpenAI','netflix'])
y=np.array([10,15,25,30,20])
explode1 = [0.2,0,0,0.1,0]

plt.pie(y,labels=x,explode=explode1,shadow=True)
plt.legend(x)
plt.show()
