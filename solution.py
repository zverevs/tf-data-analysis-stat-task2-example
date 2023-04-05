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
    s = np.sqrt(np.sum(x**2) / n)
    alpha = 1 - p
    df = 2*n
    chi2_left = chi2.ppf(alpha/2, df)
    chi2_right = chi2.ppf(1 - alpha/2, df)
    left_bound = np.sqrt((n-1)*s**2 / chi2_right)
    right_bound = np.sqrt((n-1)*s**2 / chi2_left)
    return (left_bound, right_bound)
