import numpy as np

def compute_jacobian(q_list, rows, cols):
    qr1, qr2, qr3, qr4, qr5, qr6, qr7 = q_list

    Jacobian = [[0 for j in range(cols)] for i in range(rows)]

    Jacobian[0][0] = np.sin(qr1)*(np.sin(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) - np.cos(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50)) + np.cos(qr1)*(np.sin(qr2)*(np.cos(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) + np.sin(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50)) - np.cos(qr2)*(np.cos(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) - np.sin(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + 61/200))
    Jacobian[0][1] = np.sin(qr1)*(np.cos(qr2)*(np.cos(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) + np.sin(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50)) + np.sin(qr2)*(np.cos(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) - np.sin(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + 61/200))
    Jacobian[0][2] = np.cos(qr1)*(np.cos(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) + np.sin(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50)) - np.sin(qr1)*np.sin(qr2)*(np.sin(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) - np.cos(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50))
    Jacobian[0][3] = np.sin(qr1)*(np.cos(qr2)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000)) + np.sin(qr2)*np.sin(qr3)*(np.cos(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) - np.sin(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50))) + np.cos(qr1)*np.cos(qr3)*(np.cos(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) - np.sin(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50))
    Jacobian[0][4] = np.sin(qr1)*(np.sin(qr2)*(np.cos(qr3)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10) - np.cos(qr4)*np.sin(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10)) - np.cos(qr2)*np.sin(qr4)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10)) - np.cos(qr1)*(np.sin(qr3)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10) + np.cos(qr3)*np.cos(qr4)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10))
    Jacobian[0][5] = np.sin(qr1)*(np.cos(qr2)*((np.cos(qr4)*np.cos(qr7)*np.sin(qr6))/10 + (np.cos(qr6)*np.cos(qr7)*np.sin(qr4)*np.sin(qr5))/10) - np.sin(qr2)*(np.sin(qr3)*((np.cos(qr7)*np.sin(qr4)*np.sin(qr6))/10 - (np.cos(qr4)*np.cos(qr6)*np.cos(qr7)*np.sin(qr5))/10) + (np.cos(qr3)*np.cos(qr5)*np.cos(qr6)*np.cos(qr7))/10)) - np.cos(qr1)*(np.cos(qr3)*((np.cos(qr7)*np.sin(qr4)*np.sin(qr6))/10 - (np.cos(qr4)*np.cos(qr6)*np.cos(qr7)*np.sin(qr5))/10) - (np.cos(qr5)*np.cos(qr6)*np.cos(qr7)*np.sin(qr3))/10)
    Jacobian[0][6] = np.sin(qr1)*(np.cos(qr2)*(np.sin(qr4)*((np.cos(qr5)*np.cos(qr7))/10 - (np.sin(qr5)*np.sin(qr6)*np.sin(qr7))/10) + (np.cos(qr4)*np.cos(qr6)*np.sin(qr7))/10) + np.sin(qr2)*(np.sin(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.cos(qr7))/10 - (np.sin(qr5)*np.sin(qr6)*np.sin(qr7))/10) - (np.cos(qr6)*np.sin(qr4)*np.sin(qr7))/10) + np.cos(qr3)*((np.cos(qr7)*np.sin(qr5))/10 + (np.cos(qr5)*np.sin(qr6)*np.sin(qr7))/10))) + np.cos(qr1)*(np.cos(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.cos(qr7))/10 - (np.sin(qr5)*np.sin(qr6)*np.sin(qr7))/10) - (np.cos(qr6)*np.sin(qr4)*np.sin(qr7))/10) - np.sin(qr3)*((np.cos(qr7)*np.sin(qr5))/10 + (np.cos(qr5)*np.sin(qr6)*np.sin(qr7))/10))
    Jacobian[1][0] = 0
    Jacobian[1][1] = np.cos(qr2)*(np.cos(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) - np.sin(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + 61/200) - np.sin(qr2)*(np.cos(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) + np.sin(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50))
    Jacobian[1][2] = np.cos(qr2)*(np.sin(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) - np.cos(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50))
    Jacobian[1][3] = np.cos(qr2)*np.sin(qr3)*(np.cos(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) - np.sin(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50)) - np.sin(qr2)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000))
    Jacobian[1][4] = np.cos(qr2)*(np.cos(qr3)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10) - np.cos(qr4)*np.sin(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10)) + np.sin(qr2)*np.sin(qr4)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10)
    Jacobian[1][5] = np.sin(qr2)*((np.cos(qr4)*np.cos(qr7)*np.sin(qr6))/10 + (np.cos(qr6)*np.cos(qr7)*np.sin(qr4)*np.sin(qr5))/10) - np.cos(qr2)*(np.sin(qr3)*((np.cos(qr7)*np.sin(qr4)*np.sin(qr6))/10 - (np.cos(qr4)*np.cos(qr6)*np.cos(qr7)*np.sin(qr5))/10) + (np.cos(qr3)*np.cos(qr5)*np.cos(qr6)*np.cos(qr7))/10)
    Jacobian[1][6] = np.cos(qr2)*(np.sin(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.cos(qr7))/10 - (np.sin(qr5)*np.sin(qr6)*np.sin(qr7))/10) - (np.cos(qr6)*np.sin(qr4)*np.sin(qr7))/10) + np.cos(qr3)*((np.cos(qr7)*np.sin(qr5))/10 + (np.cos(qr5)*np.sin(qr6)*np.sin(qr7))/10)) - np.sin(qr2)*(np.sin(qr4)*((np.cos(qr5)*np.cos(qr7))/10 - (np.sin(qr5)*np.sin(qr6)*np.sin(qr7))/10) + (np.cos(qr4)*np.cos(qr6)*np.sin(qr7))/10)
    Jacobian[2][0] = np.cos(qr1)*(np.sin(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) - np.cos(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50)) - np.sin(qr1)*(np.sin(qr2)*(np.cos(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) + np.sin(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50)) - np.cos(qr2)*(np.cos(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) - np.sin(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + 61/200))
    Jacobian[2][1] = np.cos(qr1)*(np.cos(qr2)*(np.cos(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) + np.sin(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50)) + np.sin(qr2)*(np.cos(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) - np.sin(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + 61/200))
    Jacobian[2][2] = np.sin(qr1)*(np.cos(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) + np.sin(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50)) - np.cos(qr1)*np.sin(qr2)*(np.sin(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) - np.cos(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50))
    Jacobian[2][3] = np.cos(qr1)*(np.cos(qr2)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000)) + np.sin(qr2)*np.sin(qr3)*(np.cos(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) - np.sin(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50))) - np.cos(qr3)*np.sin(qr1)*(np.cos(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) - np.sin(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50))
    Jacobian[2][4] = np.cos(qr1)*(np.sin(qr2)*(np.cos(qr3)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10) - np.cos(qr4)*np.sin(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10)) - np.cos(qr2)*np.sin(qr4)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10)) + np.sin(qr1)*(np.sin(qr3)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10) + np.cos(qr3)*np.cos(qr4)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10))
    Jacobian[2][5] = np.cos(qr1)*(np.cos(qr2)*((np.cos(qr4)*np.cos(qr7)*np.sin(qr6))/10 + (np.cos(qr6)*np.cos(qr7)*np.sin(qr4)*np.sin(qr5))/10) - np.sin(qr2)*(np.sin(qr3)*((np.cos(qr7)*np.sin(qr4)*np.sin(qr6))/10 - (np.cos(qr4)*np.cos(qr6)*np.cos(qr7)*np.sin(qr5))/10) + (np.cos(qr3)*np.cos(qr5)*np.cos(qr6)*np.cos(qr7))/10)) + np.sin(qr1)*(np.cos(qr3)*((np.cos(qr7)*np.sin(qr4)*np.sin(qr6))/10 - (np.cos(qr4)*np.cos(qr6)*np.cos(qr7)*np.sin(qr5))/10) - (np.cos(qr5)*np.cos(qr6)*np.cos(qr7)*np.sin(qr3))/10)
    Jacobian[2][6] = np.cos(qr1)*(np.cos(qr2)*(np.sin(qr4)*((np.cos(qr5)*np.cos(qr7))/10 - (np.sin(qr5)*np.sin(qr6)*np.sin(qr7))/10) + (np.cos(qr4)*np.cos(qr6)*np.sin(qr7))/10) + np.sin(qr2)*(np.sin(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.cos(qr7))/10 - (np.sin(qr5)*np.sin(qr6)*np.sin(qr7))/10) - (np.cos(qr6)*np.sin(qr4)*np.sin(qr7))/10) + np.cos(qr3)*((np.cos(qr7)*np.sin(qr5))/10 + (np.cos(qr5)*np.sin(qr6)*np.sin(qr7))/10))) - np.sin(qr1)*(np.cos(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.cos(qr7))/10 - (np.sin(qr5)*np.sin(qr6)*np.sin(qr7))/10) - (np.cos(qr6)*np.sin(qr4)*np.sin(qr7))/10) - np.sin(qr3)*((np.cos(qr7)*np.sin(qr5))/10 + (np.cos(qr5)*np.sin(qr6)*np.sin(qr7))/10))

    return np.array(Jacobian)

def compute_xc(q_list):

    qr1, qr2, qr3, qr4, qr5, qr6, qr7 = q_list
    xc = [0 for i in range(3)]

    xc[0] = np.sin(qr1)*(np.sin(qr2)*(np.cos(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) + np.sin(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50)) - np.cos(qr2)*(np.cos(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) - np.sin(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + 61/200)) - np.cos(qr1)*(np.sin(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) - np.cos(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50))
    xc[1] = np.cos(qr2)*(np.cos(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) + np.sin(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50)) + np.sin(qr2)*(np.cos(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) - np.sin(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + 61/200) - 52/625
    xc[2] = np.sin(qr1)*(np.sin(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) - np.cos(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50)) + np.cos(qr1)*(np.sin(qr2)*(np.cos(qr3)*((np.sin(qr5)*np.sin(qr7))/10 - (np.cos(qr5)*np.cos(qr7)*np.sin(qr6))/10) + np.sin(qr3)*(np.cos(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + np.sin(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) + 1/50)) - np.cos(qr2)*(np.cos(qr4)*((np.cos(qr6)*np.cos(qr7))/10 + 1483/5000) - np.sin(qr4)*((np.cos(qr5)*np.sin(qr7))/10 + (np.cos(qr7)*np.sin(qr5)*np.sin(qr6))/10 - 1/50) + 61/200))

    return np.array(xc)    

def compute_ori_error(q_list):

    qr1, qr2, qr3, qr4, qr5, qr6, qr7 = q_list
    error = [0 for i in range(3)]

    # 현재 방향과 목표 방향과의 차이

    r_x = 0
    r_y = 0
    r_z = 0.5

    error[0] = (np.cos(qr1)*(np.cos(qr2)*(np.sin(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) + np.cos(qr4)*np.cos(qr6)*np.sin(qr7)) + np.sin(qr2)*(np.sin(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) - np.cos(qr6)*np.sin(qr4)*np.sin(qr7)) + np.cos(qr3)*(np.cos(qr7)*np.sin(qr5) + np.cos(qr5)*np.sin(qr6)*np.sin(qr7)))) - np.sin(qr1)*(np.cos(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) - np.cos(qr6)*np.sin(qr4)*np.sin(qr7)) - np.sin(qr3)*(np.cos(qr7)*np.sin(qr5) + np.cos(qr5)*np.sin(qr6)*np.sin(qr7))))*(np.cos(r_z)*np.sin(r_x) - np.cos(r_x)*np.sin(r_y)*np.sin(r_z)) + np.sin(r_y)*(np.sin(qr2)*(np.sin(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) - np.cos(qr4)*np.cos(qr6)*np.cos(qr7)) - np.cos(qr2)*(np.sin(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) + np.cos(qr6)*np.cos(qr7)*np.sin(qr4)) + np.cos(qr3)*(np.sin(qr5)*np.sin(qr7) - np.cos(qr5)*np.cos(qr7)*np.sin(qr6)))) + (np.sin(qr1)*(np.cos(qr3)*(np.sin(qr4)*np.sin(qr6) - np.cos(qr4)*np.cos(qr6)*np.sin(qr5)) - np.cos(qr5)*np.cos(qr6)*np.sin(qr3)) - np.cos(qr1)*(np.sin(qr2)*(np.sin(qr3)*(np.sin(qr4)*np.sin(qr6) - np.cos(qr4)*np.cos(qr6)*np.sin(qr5)) + np.cos(qr3)*np.cos(qr5)*np.cos(qr6)) - np.cos(qr2)*(np.cos(qr4)*np.sin(qr6) + np.cos(qr6)*np.sin(qr4)*np.sin(qr5))))*(np.cos(r_x)*np.cos(r_z) + np.sin(r_x)*np.sin(r_y)*np.sin(r_z)) - np.cos(r_x)*np.cos(r_y)*(np.sin(qr2)*(np.sin(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) + np.cos(qr4)*np.cos(qr6)*np.sin(qr7)) - np.cos(qr2)*(np.sin(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) - np.cos(qr6)*np.sin(qr4)*np.sin(qr7)) + np.cos(qr3)*(np.cos(qr7)*np.sin(qr5) + np.cos(qr5)*np.sin(qr6)*np.sin(qr7)))) - np.cos(r_y)*np.sin(r_z)*(np.cos(qr1)*(np.cos(qr2)*(np.sin(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) - np.cos(qr4)*np.cos(qr6)*np.cos(qr7)) + np.sin(qr2)*(np.sin(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) + np.cos(qr6)*np.cos(qr7)*np.sin(qr4)) + np.cos(qr3)*(np.sin(qr5)*np.sin(qr7) - np.cos(qr5)*np.cos(qr7)*np.sin(qr6)))) - np.sin(qr1)*(np.cos(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) + np.cos(qr6)*np.cos(qr7)*np.sin(qr4)) - np.sin(qr3)*(np.sin(qr5)*np.sin(qr7) - np.cos(qr5)*np.cos(qr7)*np.sin(qr6)))) + np.cos(r_y)*np.sin(r_x)*(np.cos(qr2)*(np.sin(qr3)*(np.sin(qr4)*np.sin(qr6) - np.cos(qr4)*np.cos(qr6)*np.sin(qr5)) + np.cos(qr3)*np.cos(qr5)*np.cos(qr6)) + np.sin(qr2)*(np.cos(qr4)*np.sin(qr6) + np.cos(qr6)*np.sin(qr4)*np.sin(qr5)))
    error[1] = (np.cos(qr1)*(np.cos(qr2)*(np.sin(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) + np.cos(qr4)*np.cos(qr6)*np.sin(qr7)) + np.sin(qr2)*(np.sin(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) - np.cos(qr6)*np.sin(qr4)*np.sin(qr7)) + np.cos(qr3)*(np.cos(qr7)*np.sin(qr5) + np.cos(qr5)*np.sin(qr6)*np.sin(qr7)))) - np.sin(qr1)*(np.cos(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) - np.cos(qr6)*np.sin(qr4)*np.sin(qr7)) - np.sin(qr3)*(np.cos(qr7)*np.sin(qr5) + np.cos(qr5)*np.sin(qr6)*np.sin(qr7))))*(np.sin(r_x)*np.sin(r_z) + np.cos(r_x)*np.cos(r_z)*np.sin(r_y)) + np.sin(r_y)*(np.sin(qr1)*(np.cos(qr2)*(np.sin(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) - np.cos(qr4)*np.cos(qr6)*np.cos(qr7)) + np.sin(qr2)*(np.sin(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) + np.cos(qr6)*np.cos(qr7)*np.sin(qr4)) + np.cos(qr3)*(np.sin(qr5)*np.sin(qr7) - np.cos(qr5)*np.cos(qr7)*np.sin(qr6)))) + np.cos(qr1)*(np.cos(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) + np.cos(qr6)*np.cos(qr7)*np.sin(qr4)) - np.sin(qr3)*(np.sin(qr5)*np.sin(qr7) - np.cos(qr5)*np.cos(qr7)*np.sin(qr6)))) + (np.sin(qr1)*(np.cos(qr3)*(np.sin(qr4)*np.sin(qr6) - np.cos(qr4)*np.cos(qr6)*np.sin(qr5)) - np.cos(qr5)*np.cos(qr6)*np.sin(qr3)) - np.cos(qr1)*(np.sin(qr2)*(np.sin(qr3)*(np.sin(qr4)*np.sin(qr6) - np.cos(qr4)*np.cos(qr6)*np.sin(qr5)) + np.cos(qr3)*np.cos(qr5)*np.cos(qr6)) - np.cos(qr2)*(np.cos(qr4)*np.sin(qr6) + np.cos(qr6)*np.sin(qr4)*np.sin(qr5))))*(np.cos(r_x)*np.sin(r_z) - np.cos(r_z)*np.sin(r_x)*np.sin(r_y)) - np.cos(r_y)*np.sin(r_x)*(np.cos(qr1)*(np.cos(qr3)*(np.sin(qr4)*np.sin(qr6) - np.cos(qr4)*np.cos(qr6)*np.sin(qr5)) - np.cos(qr5)*np.cos(qr6)*np.sin(qr3)) + np.sin(qr1)*(np.sin(qr2)*(np.sin(qr3)*(np.sin(qr4)*np.sin(qr6) - np.cos(qr4)*np.cos(qr6)*np.sin(qr5)) + np.cos(qr3)*np.cos(qr5)*np.cos(qr6)) - np.cos(qr2)*(np.cos(qr4)*np.sin(qr6) + np.cos(qr6)*np.sin(qr4)*np.sin(qr5)))) + np.cos(r_y)*np.cos(r_z)*(np.cos(qr1)*(np.cos(qr2)*(np.sin(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) - np.cos(qr4)*np.cos(qr6)*np.cos(qr7)) + np.sin(qr2)*(np.sin(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) + np.cos(qr6)*np.cos(qr7)*np.sin(qr4)) + np.cos(qr3)*(np.sin(qr5)*np.sin(qr7) - np.cos(qr5)*np.cos(qr7)*np.sin(qr6)))) - np.sin(qr1)*(np.cos(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) + np.cos(qr6)*np.cos(qr7)*np.sin(qr4)) - np.sin(qr3)*(np.sin(qr5)*np.sin(qr7) - np.cos(qr5)*np.cos(qr7)*np.sin(qr6)))) - np.cos(r_x)*np.cos(r_y)*(np.sin(qr1)*(np.cos(qr2)*(np.sin(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) + np.cos(qr4)*np.cos(qr6)*np.sin(qr7)) + np.sin(qr2)*(np.sin(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) - np.cos(qr6)*np.sin(qr4)*np.sin(qr7)) + np.cos(qr3)*(np.cos(qr7)*np.sin(qr5) + np.cos(qr5)*np.sin(qr6)*np.sin(qr7)))) + np.cos(qr1)*(np.cos(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) - np.cos(qr6)*np.sin(qr4)*np.sin(qr7)) - np.sin(qr3)*(np.cos(qr7)*np.sin(qr5) + np.cos(qr5)*np.sin(qr6)*np.sin(qr7))))
    error[2] = (np.sin(qr2)*(np.sin(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) + np.cos(qr4)*np.cos(qr6)*np.sin(qr7)) - np.cos(qr2)*(np.sin(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) - np.cos(qr6)*np.sin(qr4)*np.sin(qr7)) + np.cos(qr3)*(np.cos(qr7)*np.sin(qr5) + np.cos(qr5)*np.sin(qr6)*np.sin(qr7))))*(np.sin(r_x)*np.sin(r_z) + np.cos(r_x)*np.cos(r_z)*np.sin(r_y)) + (np.cos(qr2)*(np.sin(qr3)*(np.sin(qr4)*np.sin(qr6) - np.cos(qr4)*np.cos(qr6)*np.sin(qr5)) + np.cos(qr3)*np.cos(qr5)*np.cos(qr6)) + np.sin(qr2)*(np.cos(qr4)*np.sin(qr6) + np.cos(qr6)*np.sin(qr4)*np.sin(qr5)))*(np.cos(r_x)*np.sin(r_z) - np.cos(r_z)*np.sin(r_x)*np.sin(r_y)) - (np.sin(qr1)*(np.cos(qr2)*(np.sin(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) + np.cos(qr4)*np.cos(qr6)*np.sin(qr7)) + np.sin(qr2)*(np.sin(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) - np.cos(qr6)*np.sin(qr4)*np.sin(qr7)) + np.cos(qr3)*(np.cos(qr7)*np.sin(qr5) + np.cos(qr5)*np.sin(qr6)*np.sin(qr7)))) + np.cos(qr1)*(np.cos(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.cos(qr7) - np.sin(qr5)*np.sin(qr6)*np.sin(qr7)) - np.cos(qr6)*np.sin(qr4)*np.sin(qr7)) - np.sin(qr3)*(np.cos(qr7)*np.sin(qr5) + np.cos(qr5)*np.sin(qr6)*np.sin(qr7))))*(np.cos(r_z)*np.sin(r_x) - np.cos(r_x)*np.sin(r_y)*np.sin(r_z)) + (np.cos(qr1)*(np.cos(qr3)*(np.sin(qr4)*np.sin(qr6) - np.cos(qr4)*np.cos(qr6)*np.sin(qr5)) - np.cos(qr5)*np.cos(qr6)*np.sin(qr3)) + np.sin(qr1)*(np.sin(qr2)*(np.sin(qr3)*(np.sin(qr4)*np.sin(qr6) - np.cos(qr4)*np.cos(qr6)*np.sin(qr5)) + np.cos(qr3)*np.cos(qr5)*np.cos(qr6)) - np.cos(qr2)*(np.cos(qr4)*np.sin(qr6) + np.cos(qr6)*np.sin(qr4)*np.sin(qr5))))*(np.cos(r_x)*np.cos(r_z) + np.sin(r_x)*np.sin(r_y)*np.sin(r_z)) + np.cos(r_y)*np.cos(r_z)*(np.sin(qr2)*(np.sin(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) - np.cos(qr4)*np.cos(qr6)*np.cos(qr7)) - np.cos(qr2)*(np.sin(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) + np.cos(qr6)*np.cos(qr7)*np.sin(qr4)) + np.cos(qr3)*(np.sin(qr5)*np.sin(qr7) - np.cos(qr5)*np.cos(qr7)*np.sin(qr6)))) + np.cos(r_y)*np.sin(r_z)*(np.sin(qr1)*(np.cos(qr2)*(np.sin(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) - np.cos(qr4)*np.cos(qr6)*np.cos(qr7)) + np.sin(qr2)*(np.sin(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) + np.cos(qr6)*np.cos(qr7)*np.sin(qr4)) + np.cos(qr3)*(np.sin(qr5)*np.sin(qr7) - np.cos(qr5)*np.cos(qr7)*np.sin(qr6)))) + np.cos(qr1)*(np.cos(qr3)*(np.cos(qr4)*(np.cos(qr5)*np.sin(qr7) + np.cos(qr7)*np.sin(qr5)*np.sin(qr6)) + np.cos(qr6)*np.cos(qr7)*np.sin(qr4)) - np.sin(qr3)*(np.sin(qr5)*np.sin(qr7) - np.cos(qr5)*np.cos(qr7)*np.sin(qr6))))

    # print("orientation error : ", error)

    return np.array(error)

def compute_jacobian_omega(q_list, rows, cols):

    qr1, qr2, qr3, qr4, qr5, qr6, qr7 = q_list
    Jacobian_w = [[0 for j in range(cols)] for i in range(rows)]

    Jacobian_w[0][0] = 0
    Jacobian_w[0][1] = np.cos(qr1)
    Jacobian_w[0][2] = np.cos(qr2)*np.sin(qr1)
    Jacobian_w[0][3] = np.cos(qr1)*np.sin(qr3) - np.cos(qr3)*np.sin(qr1)*np.sin(qr2)
    Jacobian_w[0][4] = np.cos(qr2)*np.cos(qr4)*np.sin(qr1) - np.sin(qr4)*(np.cos(qr1)*np.cos(qr3) + np.sin(qr1)*np.sin(qr2)*np.sin(qr3))
    Jacobian_w[0][5] = np.sin(qr5)*(np.cos(qr1)*np.sin(qr3) - np.cos(qr3)*np.sin(qr1)*np.sin(qr2)) - np.cos(qr5)*(np.cos(qr4)*(np.cos(qr1)*np.cos(qr3) + np.sin(qr1)*np.sin(qr2)*np.sin(qr3)) + np.cos(qr2)*np.sin(qr1)*np.sin(qr4))
    Jacobian_w[0][6] = np.cos(qr7)*(np.cos(qr5)*(np.cos(qr4)*(np.cos(qr1)*np.cos(qr3) + np.sin(qr1)*np.sin(qr2)*np.sin(qr3)) + np.cos(qr2)*np.sin(qr1)*np.sin(qr4)) - np.sin(qr5)*(np.cos(qr1)*np.sin(qr3) - np.cos(qr3)*np.sin(qr1)*np.sin(qr2))) - np.sin(qr7)*(np.cos(qr6)*(np.sin(qr4)*(np.cos(qr1)*np.cos(qr3) + np.sin(qr1)*np.sin(qr2)*np.sin(qr3)) - np.cos(qr2)*np.cos(qr4)*np.sin(qr1)) + np.sin(qr6)*(np.sin(qr5)*(np.cos(qr4)*(np.cos(qr1)*np.cos(qr3) + np.sin(qr1)*np.sin(qr2)*np.sin(qr3)) + np.cos(qr2)*np.sin(qr1)*np.sin(qr4)) + np.cos(qr5)*(np.cos(qr1)*np.sin(qr3) - np.cos(qr3)*np.sin(qr1)*np.sin(qr2))))
    Jacobian_w[1][0] = 1
    Jacobian_w[1][1] = 0 
    Jacobian_w[1][2] = -np.sin(qr2)
    Jacobian_w[1][3] = -np.cos(qr2)*np.cos(qr3)
    Jacobian_w[1][4] = - np.cos(qr4)*np.sin(qr2) - np.cos(qr2)*np.sin(qr3)*np.sin(qr4)
    Jacobian_w[1][5] = np.cos(qr5)*(np.sin(qr2)*np.sin(qr4) - np.cos(qr2)*np.cos(qr4)*np.sin(qr3)) - np.cos(qr2)*np.cos(qr3)*np.sin(qr5)
    Jacobian_w[1][6] = np.sin(qr7)*(np.sin(qr6)*(np.sin(qr5)*(np.sin(qr2)*np.sin(qr4) - np.cos(qr2)*np.cos(qr4)*np.sin(qr3)) + np.cos(qr2)*np.cos(qr3)*np.cos(qr5)) - np.cos(qr6)*(np.cos(qr4)*np.sin(qr2) + np.cos(qr2)*np.sin(qr3)*np.sin(qr4))) - np.cos(qr7)*(np.cos(qr5)*(np.sin(qr2)*np.sin(qr4) - np.cos(qr2)*np.cos(qr4)*np.sin(qr3)) - np.cos(qr2)*np.cos(qr3)*np.sin(qr5))
    Jacobian_w[2][0] = 0
    Jacobian_w[2][1] = -np.sin(qr1)
    Jacobian_w[2][2] = np.cos(qr1)*np.cos(qr2)
    Jacobian_w[2][3] = - np.sin(qr1)*np.sin(qr3) - np.cos(qr1)*np.cos(qr3)*np.sin(qr2)
    Jacobian_w[2][4] = np.sin(qr4)*(np.cos(qr3)*np.sin(qr1) - np.cos(qr1)*np.sin(qr2)*np.sin(qr3)) + np.cos(qr1)*np.cos(qr2)*np.cos(qr4)
    Jacobian_w[2][5] = np.cos(qr5)*(np.cos(qr4)*(np.cos(qr3)*np.sin(qr1) - np.cos(qr1)*np.sin(qr2)*np.sin(qr3)) - np.cos(qr1)*np.cos(qr2)*np.sin(qr4)) - np.sin(qr5)*(np.sin(qr1)*np.sin(qr3) + np.cos(qr1)*np.cos(qr3)*np.sin(qr2))
    Jacobian_w[2][6] = np.sin(qr7)*(np.cos(qr6)*(np.sin(qr4)*(np.cos(qr3)*np.sin(qr1) - np.cos(qr1)*np.sin(qr2)*np.sin(qr3)) + np.cos(qr1)*np.cos(qr2)*np.cos(qr4)) + np.sin(qr6)*(np.sin(qr5)*(np.cos(qr4)*(np.cos(qr3)*np.sin(qr1) - np.cos(qr1)*np.sin(qr2)*np.sin(qr3)) - np.cos(qr1)*np.cos(qr2)*np.sin(qr4)) + np.cos(qr5)*(np.sin(qr1)*np.sin(qr3) + np.cos(qr1)*np.cos(qr3)*np.sin(qr2)))) - np.cos(qr7)*(np.cos(qr5)*(np.cos(qr4)*(np.cos(qr3)*np.sin(qr1) - np.cos(qr1)*np.sin(qr2)*np.sin(qr3)) - np.cos(qr1)*np.cos(qr2)*np.sin(qr4)) - np.sin(qr5)*(np.sin(qr1)*np.sin(qr3) + np.cos(qr1)*np.cos(qr3)*np.sin(qr2)))

    return np.array(Jacobian_w)

