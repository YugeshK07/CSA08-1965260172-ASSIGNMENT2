# Q4 - Compare string building methods
import time
import statistics

def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text

def build_join(parts):
    return ";".join(parts)

def build_fstring(parts):
    # Each line is formatted with an f-string; join once at the end.
    return "".join(f"{p};" for p in parts)

def measure(fn, parts, repeats=3):
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = fn(parts)
        times.append(time.perf_counter() - start)
    return statistics.mean(times), result

for n in (1000, 10000, 200000):
    items = [f"Item{i}:Rs.{i % 50}" for i in range(n)]
    plus_time, a = measure(build_plus, items)
    join_time, b = measure(build_join, items)
    f_time, c = measure(build_fstring, items)
    print(n, "lines; output lengths:", len(a), len(b), len(c))
    print(f"+= {plus_time:.6f}s | join {join_time:.6f}s | f-string {f_time:.6f}s")
