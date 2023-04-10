import pandas as pd
import numpy as np
from scipy import stats

chat_id = 277684942 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    return stats.cramervonmises_2samp(x, y).pvalue < 0.09 # Ваш ответ, True или False
