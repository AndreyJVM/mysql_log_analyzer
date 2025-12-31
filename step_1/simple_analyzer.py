#!/usr/bin/env python3
"""
Простой анализатор логов MySQL
Версия 1.0 - Минимальная функциональность
"""

import sys

def count_errors_in_log(log_path):
    """
    Читает файл логов и считает строки с ERROR
    """
    try:
        # Открываем файл
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()
        
        # Считаем ошибки
        error_count = 0
        error_lines = []
        
        for line in lines:
            if 'ERROR' in line.upper():  # Ищем ERROR в любом регистре
                error_count += 1
                error_lines.append(line.strip())
        
        return error_count, error_lines, len(lines)
        
    except FileNotFoundError:
        print(f"Файл не найден: {log_path}")
        return 0, [], 0
    except PermissionError:
        print(f"Нет прав на чтение файла: {log_path}")
        return 0, [], 0
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return 0, [], 0

def main():
    """
    Главная функция
    """
    print("=" * 50)
    print("   MySQL LOG ANALYZER - Minimal Version")
    print("=" * 50)
    
    # Путь к логу ошибок MySQL
    # (стандартный путь в Ubuntu)
    log_file = "/var/log/mysql/error.log"
    
    print(f"\nАнализирую файл: {log_file}")
    print("Пожалуйста, подождите...\n")
    
    # Анализируем лог
    error_count, error_lines, total_lines = count_errors_in_log(log_file)
    
    # Выводим результаты
    print("=" * 50)
    print("РЕЗУЛЬТАТЫ АНАЛИЗА:")
    print("=" * 50)
    
    print(f"Всего строк в логе: {total_lines}")
    print(f"Найдено ошибок: {error_count}")
    
    if total_lines > 0:
        error_percentage = (error_count / total_lines) * 100
        print(f"Процент ошибок: {error_percentage:.2f}%")
    
    # Показываем последние ошибки
    if error_lines:
        print(f"\nПоследние {min(5, len(error_lines))} ошибок:")
        for i, error in enumerate(error_lines[-5:], 1):
            # Обрезаем длинные строки для красоты
            if len(error) > 100:
                error = error[:97] + "..."
            print(f"  {i}. {error}")
    
    # Даем простую оценку
    print("\n💡 ОЦЕНКА СИТУАЦИИ:")
    if error_count == 0:
        print("  Отлично! Ошибок не обнаружено.")
    elif error_count < 5:
        print("  Есть несколько ошибок, но ничего критичного.")
    else:
        print("  Внимание! Обнаружено много ошибок. Рекомендуется проверить MySQL.")
    
    print("\n" + "=" * 50)
    print("Анализ завершен!")

if __name__ == "__main__":
    main()