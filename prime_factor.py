import time

def prime_factors_for(n):
    factors = []

    # 2 va 3 ga bo‘linishlarni ajratib olish
    for p in [2, 3]:
        while n % p == 0:
            factors.append(p)
            n //= p

    # 6k ± 1 shaklidagi sonlarni tekshirish
    for i in range(5, int(n**0.5) + 1, 6):
        while n % i == 0:
            factors.append(i)
            n //= i
        while n % (i + 2) == 0:
            factors.append(i + 2)
            n //= (i + 2)

    # Agar n hali ham 1 dan katta bo‘lsa, u tub son
    if n > 1:
        factors.append(n)

    return factors

# 🧪 Sinov uchun son
n = 10000000000

# ⏱️ Vaqtni o‘lchash
start_time = time.time()
factors = prime_factors(n)
end_time = time.time()

# 🧾 Natijani chiqarish
print(f"{n} =", factors)
print(f"⏱️ Bajarilish vaqti: {end_time - start_time:.6f} soniya")
