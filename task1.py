from timeit import timeit
from random import randint

# Функція для знаходження мінімальної кількості монет за жадібним методом
def find_coins_greedy(amount, available_coins):
    result = {}
    # Сортуємо монети у зворотньому порядку для використання найбільшої доступної монети першою
    for coin in sorted(available_coins, reverse=True):
        # Поки сума не нульова та поточна монета менша або рівна сумі
        while amount >= coin:
            # Записуємо кількість монет даного номіналу в результат
            result[coin] = result.get(coin, 0) + 1
            # Зменшуємо суму на номінал монети
            amount -= coin
    return result

# Функція для знаходження мінімальної кількості монет за динамічним програмуванням
def find_min_coins(amount, available_coins):
    # Ініціалізуємо динамічний масив
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    # Для кожного номіналу монети
    for coin in available_coins:
        # Проходимося по всіх сумах від номіналу монети до поточної суми
        for i in range(coin, amount + 1):
            # Знаходимо мінімальну кількість монет для поточної суми
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Якщо неможливо зібрати суму
    if dp[amount] == float("inf"):
        return {}

    # Відновлюємо монети, які використовувались для зібрання суми
    result_coins = {}
    i = amount
    while i > 0:
        for coin in available_coins:
            if i - coin >= 0 and dp[i] == dp[i - coin] + 1:
                result_coins[coin] = result_coins.get(coin, 0) + 1
                i -= coin
                break

    return result_coins

# Функція для виведення результатів вимірювання часу виконання алгоритмів
def print_timing(algorithm_name, sample_size, execution_time):
    print(f"{algorithm_name} ({sample_size} сума): {execution_time:.6f} секунд")

if __name__ == "__main__":
    # Базові тести
    coins = [50, 25, 10, 5, 2, 1]
    amount = 113
    print(find_coins_greedy(amount, coins))
    print(find_min_coins(amount, coins))
    print(f"\n")

    # Перформанс тести
    for amount in [
        randint(100, 1000),
        randint(1000, 10000),
        randint(10000, 100000),
        randint(100000, 1000000),
        randint(1000000, 10000000),
        # randint(10000000, 100000000),
    ]:
        print_timing(
            "Greedy",
            amount,
            timeit(
                "print(find_coins_greedy(amount, coins))", 
                globals=globals(), 
                number=1
            ),
        )
        print_timing(
            "Dynamic",
            amount,
            timeit("print(find_min_coins(amount, coins))", 
            globals=globals(), 
            number=1
            ),
        )
        print(f"\n")
