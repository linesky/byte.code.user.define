
def clear_input_buffer():
    """Função para esperar o Enter do usuário."""
    input("press enter to continue...")

def execute_instruction(operation, reg, value, registers):
    """Função para simular as instruções."""
    if reg not in registers:
        print(f"invalid register: {reg}")
        return

    if value in registers:
        value = registers[value]
    else:
        try:
            value = int(value)
        except ValueError:
            print(f"invalid value: {value}")
            return

    if operation == "mov":
        registers[reg] = value
    elif operation == "add":
        registers[reg] += value
    elif operation == "sub":
        registers[reg] -= value
    elif operation == "mul":
        registers[reg] *= value
    elif operation == "div":
        if value != 0:
            registers[reg] //= value
        else:
            print("Erro: division by 0!")
    elif operation == "and":
        registers[reg] &= value
    elif operation == "or":
        registers[reg] |= value
    else:
        print(f"invalid intrution: {operation}")

def main():
    filename = input("file name: ")

    try:
        with open(filename, "r") as file:
            registers = {"rax": 0, "rbx": 0, "rcx": 0, "rdx": 0}
            
            for line in file:
                print(line)
                parts = line.strip().split(',')
                if len(parts) != 3:
                    print(f"invalid line: {line.strip()}")
                    continue

                operation, reg, value = parts
                operation, reg, value = operation.strip(), reg.strip(), value.strip()

                execute_instruction(operation, reg, value, registers)
                print(f"rax: {registers['rax']}, rbx: {registers['rbx']}, rcx: {registers['rcx']}, rdx: {registers['rdx']}")
                clear_input_buffer()

    except FileNotFoundError:
        print(f"Erro:file {filename} not found.")

if __name__ == "__main__":
    print("\x1bc\x1b[47;30m")
    main()
