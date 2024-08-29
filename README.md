# Cpu
Cpu 2 bits diagram
Create a digital electronic schematic for a simple 2-bit CPU with a program counter and the following instructions:

1. **Instruction 0**: Load Accumulator (Loads a value into the accumulator).

2. **Instruction 1**: Load B (Loads a value into B).

3. **Instruction 2**: Add Accumulator and B (Adds the values ​​of the accumulator and B, storing the result in the accumulator).

### Main Components
1. **Program Counter (PC)**: A 2-bit counter to store the address of the next instruction.

2. **Instruction Register (IR)**: A 2-bit register to store the current instruction.

3. **Accumulator (ACC)**: A 2-bit register to store the result of operations.

4. **Register B (B)**: A 2-bit register to store the second operand.

5. **Instruction Memory**: A simple memory to store instructions (each instruction is 2 bits).
6. **Control Unit (CU)**: Controls the data flow and CPU operations.
7. **Adder (ALU)**: Performs the addition operation between the accumulator and B.

### Simplified Digital Electronic Schematic

1. **Instruction Memory**:
- Size: 4x2 bits (4 memory locations, each with 2 bits).
- Stores the instructions to be executed.

2. **Program Counter (PC)**:
- A 2-bit counter (Q0 and Q1) that automatically increments after each clock cycle.
- Output: Connected to the Instruction Memory input.

3. **Instruction Register (IR)**:
- A 2-bit register to store the current instruction.
- Input: Connected to the Instruction Memory output.
- Output: Connected to the Control Unit (CU).

4. **Accumulator (ACC)**:
- A 2-bit register.
- Input: Connected to the ALU output and the Control Unit.

5. **Register B (B)**:
- A 2-bit register.
- Input: Connected to the Control Unit.

6. **Addder (ALU)**:
- A 2-bit ALU capable of adding two operands.
- Inputs: Accumulator (ACC) and Register B (B).
- Output: Connected to the Accumulator (ACC).

7. **Control Unit (CU)**:
- Decodes the instruction stored in the IR.
- Controls the operation of the Accumulator, Register B, and the ALU.
- Controls the selection of instructions and increments the PC.

### Operation
1. **Instruction 0 (Load Accumulator)**:
- Loads a value from memory or a bus into the Accumulator (ACC).
- UC activates data input to ACC.

2. **Instruction 1 (Load B)**:
- Loads a value from memory or a bus into Register B.
- UC activates data input to B.

3. **Instruction 2 (Add ACC and B)**:
- UC activates the ALU to add the values ​​in ACC and B.
- The result is stored back in the Accumulator.

### Visual Schematic

Here is the simplified textual description of the schematic. To generate a real electronic schematic, it would be necessary to use circuit design software such as Logisim or Quartus, but the basic schematic would consist of:

- **PC** → **Instruction Memory** → **IR** → **UC**
- **UC** → **ACC** ↔ **ALU** ↔ **B**

### Step-by-Step Operation

1. The **PC** indicates the position of the instruction in Memory.
2. The instruction is loaded into the **IR**.
3. The **UC** decodes the instruction:
- Instruction 0: Loads the value into **ACC**.
- Instruction 1: Loads the value into **B**.
- Instruction 2: Adds **ACC** and **B** and stores the result in **ACC**.
4. The **PC** is incremented and the next instruction is loaded.

This simplified scheme can be expanded to include more instructions and operations, but the basic structure described here provides a view of how a simple 2-bit CPU might work.
