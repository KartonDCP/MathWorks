import matplotlib.pyplot as plt

def plotData(data):
    """
        Функция позволяет выполнить визуализацию данных в декартовой 
        системе координат с подписанным осями (численность населения 
        и прибыль)
    """
    
    # ====================== Ваш код здесь ======================
    # Инструкция: визуализируйте данные с использованием функций 
    # figure и plot. Подпишите оси с использованием функций xlabel
    # и ylabel, предполагая, что аргументами этих функций являются
    # численность населения по x и прибыль по y 
    
    plt.figure()
    plt.plot(data[:, 0], data[:, 1], 'rx', markersize=5, label='Train Data')
    plt.legend(loc='upper right', shadow=True, fontsize=12, numpoints=1)
    plt.xlabel('Population count, 10k count')
    plt.ylabel('income, 10k $')
    plt.grid()

    
    # ============================================================