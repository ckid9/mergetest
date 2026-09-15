import time

# ❌ МЕДЛЕННО: exec() парсит строку каждый раз
formula = "x * 2 + y / 3"
x, y = 10, 20
print('remote change')
start = time.time()
for _ in range(100000):
    exec(f"result = {formula}")  # Парсится 100 000 раз!
print(f"Без compile(): {time.time() - start:.3f}с")

# ✅ БЫСТРО: компилируем один раз, выполняем много раз
compiled = compile(formula, "<string>", "eval")
start = time.time()
for _ in range(100000):
    result = eval(compiled)  # Просто выполняется
print(f"С compile(): {time.time() - start:.3f}с")
