import numpy as np




def normalEqn(X, y):
    """ 
        Функция позволяет вычислить параметры модели для линейной
        регресии с использованием нормальных уравнений
    """
    
    # ====================== Ваш код здесь ======================
    # Инструкция: выполнить вычисление параметров модели для линейной 
    # регрессии с использованием норамаьных уравнений

    # ============================================================
    
    return np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)