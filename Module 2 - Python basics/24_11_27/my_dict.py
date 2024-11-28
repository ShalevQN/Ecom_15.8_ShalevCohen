# Mom can I have dict? We have dict at home. Dict at home:
from multiprocessing.managers import Value

m_keys = []

m_values = []

my_dict: tuple = (m_keys, m_values)

def keys() -> list:
    return m_keys

def values():
    return m_values

def items() -> list[tuple[str, str]]:
    return list(zip(m_keys, m_values))

def pop(key: str = None) -> str:
    if key is None:
        index = m_keys[-1]
        m_keys.remove(m_keys[-1])
        x = m_values.pop(index)
    if key in m_keys:
        index = m_keys.index(key)
        m_keys.remove(key)
        x = m_values.pop(index)
    else:
        raise IndexError("No key in this dict.")
    return x

def get(key: str, msg: str = None) -> str:
    if key in m_keys:
        index = m_keys.index(key)
        return m_values[index]
    else:
        return msg

def clear() -> None:
    m_keys.clear()
    m_values.clear()

def update(update_dict: dict[str, str]) -> None:
    for key, value in update_dict.items():
        if not key in m_keys:
            setdefault(key, value)
            continue
        index = m_keys.index(key)
        m_values[index] = value

def setdefault(key: str, value:str) -> None:
    if not key in m_keys:
        m_keys.append(key)
        m_values.append(value)


setdefault('name', 'sharon')
setdefault('city', 'Tel aviv')

print("items: ", items())  # [('name', 'sharon'), ('city', 'Tel aviv')]

print("get (name -> sharon): ", get('name', 'not exist'))  # sharon
print("get (age) -> not exist: ", get('age', 'not exist'))  # not exist

print("keys: ", keys())  # ['name', 'city']

print("values: ", values())  # ['sharon', 'tel Aviv']

print("pop: ", pop('name'))  # sharon

print("pop (no input): ", pop()) # ?

print("items: ", items()) # [('city', 'Tel aviv')]

clear()
print("items after pop([]): ", items())  # []