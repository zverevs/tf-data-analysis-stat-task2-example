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
    s2 = np.mean(x**2)  
    alpha = 1 - p
    sigma_hat = np.sqrt(s2 / 14)  
    chi2_left = chi2.ppf(alpha/2, n-1)
    chi2_right = chi2.ppf(1 - alpha/2, n-1)
    left_bound = np.sqrt((n-1)*sigma_hat**2 / chi2_right)
    right_bound = np.sqrt((n-1)*sigma_hat**2 / chi2_left)
    return (left_bound, right_bound)
