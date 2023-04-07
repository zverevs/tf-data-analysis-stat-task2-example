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
    
    left_bound = np.sqrt(n * (x ** 2).mean() / (14 * chi2.ppf(q=1 - alpha / 2, df=2 * n)))
    right_bound = np.sqrt(n * (x ** 2).mean() / (14 * chi2.ppf(q=alpha / 2, df=2 * n)))
    return (left_bound, right_bound)
