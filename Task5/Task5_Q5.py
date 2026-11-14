# Q5 - Mutable default argument and scope

def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

print("Buggy calls:")
print(add_item_buggy("Tea"))
print(add_item_buggy("Vada"))
print("Shared default:", add_item_buggy.__defaults__)

print("Correct independent calls:")
print(add_item("Tea"))
print(add_item("Vada"))

def bill_total(prices, gst_rate=0.05):
    subtotal = sum(prices)
    gst = subtotal * gst_rate
    return subtotal, gst, subtotal + gst

print("Bill:", bill_total([50, 30]))

# Scope examples
global_count = 10
def scope_demo():
    local_count = 2
    return local_count
def change_global():
    global global_count
    global_count += 1
def outer():
    value = "outer"
    def inner():
        nonlocal value
        value = "inner"
    inner()
    return value
print(scope_demo(), global_count)
change_global()
print(global_count, outer())
