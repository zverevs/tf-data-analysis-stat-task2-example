import pandas as pd
import numpy as np
from scipy.stats import chi2
from scipy.stats import norm


chat_id = 235789175 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)  
    alpha = 1 - p 
    s2 = np.var(x, ddof=0)

    chi2_alpha_2 = chi2.ppf(1 - alpha/2, df=2*n) 
    chi2_1_minus_alpha_2 = chi2.ppf(alpha/2, df=2*n) 
    left = np.sqrt((2 * n * s2) / chi2_alpha_2)
    right = np.sqrt((2 * n * s2) / chi2_1_minus_alpha_2)
    return left, right
