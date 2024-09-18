def hamming_encode(data):
    """Функция для кодирования данных с использованием кода Хэмминга (7,4)."""
    data = list(map(int, data))

    # Позиции контрольных битов
    p1 = data[0] ^ data[1] ^ data[3]
    p2 = data[0] ^ data[2] ^ data[3]
    p3 = data[1] ^ data[2] ^ data[3]

    return f"{p1}{p2}{data[0]}{p3}{data[1]}{data[2]}{data[3]}"

def hamming_decode(data):
    """Функция для декодирования и проверки данных с использованием кода Хэмминга (7,4)."""
    data = list(map(int, data))

    # Проверка контрольных битов
    p1 = data[0] ^ data[2] ^ data[4] ^ data[6]
    p2 = data[1] ^ data[2] ^ data[5] ^ data[6]
    p3 = data[3] ^ data[4] ^ data[5] ^ data[6]

    # Вычисляем позицию ошибки
    error_position = p1 + (p2 * 2) + (p3 * 4)

    if error_position != 0:
        # Исправляем ошибку
        data[error_position - 1] = 1 - data[error_position - 1]  # Инвертируем бит

    # Возвращаем исправленные данные и позицию ошибки (если была)
    return f"{data[2]}{data[4]}{data[5]}{data[6]}", error_position if error_position != 0 else None