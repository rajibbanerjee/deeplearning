import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import math

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.gca().set_aspect('equal')
e=0.2

def plot_vector(v,subscript):
    DATA = np.random.rand(5,5)
    cmap = plt.cm.jet
    cNorm  = colors.Normalize(vmin=np.min(DATA[:,4]), vmax=np.max(DATA[:,4]))
    scalarMap = cmx.ScalarMappable(norm=cNorm,cmap=cmap)
    colorVal = scalarMap.to_rgba(DATA[2,4])
    plt.arrow(0,0,v[0],v[1],color=colorVal, head_width=0.05, head_length=0.1)
    plt.text(v[0]+e, v[1]+e, '$V_'+subscript+'$ = ['+str(np.round(v[0], 2))+', '+str(np.round(v[1], 2))+'], Length: '+str(np.round(length_of_vectors(v),2)), color=colorVal)
    
 
def sin_theta(theta_in_degree):
    return np.sin((np.pi/180)*theta_in_degree)
def cos_theta(theta_in_degree):
    return np.cos((np.pi/180)*theta_in_degree)

def length_of_vectors(v):
    return np.round(np.sqrt(np.dot(np.transpose(v), v)), 4)

def angle_between_vector(v1, v2):
    theta = np.dot(v1, v2)/(length_of_vectors(v1)*length_of_vectors(v2))
    return (180/np.pi)*(math.acos(theta))

#-------------------------Do Not Change the code above ----------------

# Use W_rotational for only rotation
# Use W_Linear_1 for no rotation/translation
# Use W_linear_4 for streching by 4
# Use W_mixed for rotation/translation

theta = 40
W_rotational = [[cos_theta(theta), -(sin_theta(theta))], [sin_theta(theta), cos_theta(theta)]]
W_linear_1 = [[1,0], [0, 1]]
W_linear_4 = [[4,0], [0, 4]]
W_Mixed = [[1,2], [1, 1]]


# See the effect of stretching a vector
v1 = [2,1]
v2 = np.dot(W_linear_4, v1)
plot_vector(v1,'1')
plot_vector(v2,'2')
print("Length of V1: "+str(np.round(length_of_vectors(v1), 2)))
print("Length of V1: "+str(length_of_vectors(v2)))
print("Angle between Vector: "+str(angle_between_vector(v1, v2)))

plt.grid('True')
plt.show()
