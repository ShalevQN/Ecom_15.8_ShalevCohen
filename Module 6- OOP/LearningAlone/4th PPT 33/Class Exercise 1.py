class Car:
    def __init__(self, type, model, color, speed):
        self.type = type  # heap
        self.model = model  # heap
        self.color = color  # heap
        self.speed = speed  # heap

if __name__ == '__main__':
    toyota = Car("sedan", "corolla", "blue", 150)  # stack, heap

    print(toyota.type, toyota.model)  # stack → heap
    toyota.color = 'red'  # heap (new value)

    toyota.speed = 180  # heap (new value)

    honda = toyota  # stack (same as toyota)
    honda = audi  # stack (now same as audi)
