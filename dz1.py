def find_min_coins( nominal1, nominal2, target_amount):
    max_nominal1_count = target_amount // nominal1
    min_coins = float('inf')

    for count1 in range(max_nominal1_count + 1):
    remaining_amount = target_amount - count1 * nomanal1
    count2 = remaining_amount // nominal2
    total_coins = count1 + count2

    if remaining_amount % nomanal2 == 0 and total_coins < min_coins:

        nin_coins = total_coins

    return min_coins

nomanal1 = 4
nominal2 = 7
target_amount = 4
result = find_min_coins(nominal1, nominal2, target_amount)
print(f"мінімальна кулькість монет для суми {target_amount} - {result}")