        #3d
        if value==0x3d:
            print("neg")
        #3C
        if value==0x3C:
            print("not")
        #3B
        if value==0x3B:
            print("xor")
        #3A
        if value==0x3A:
            print("or")
        #2C
        if value==0x2C:
            print("mov [r6],r7")
        #2B
        if value==0x2B:
            print("mov [r4],r5")
        #2A
        if value==0x2A:
            print("mov [r2],r3")
        #29
        if value==0x29:
            print("mov [r0],r1")
        #28
        if value==0x28:
            print("mov [r6],[r7]")
        #27
        if value==0x27:
            print("mov [r4],[r5]")
        #26
        if value==0x26:
            print("mov [r2],[r3]")
        #25
        if value==0x25:
            print("mov [r0],[r1]")
        #24
        if value==0x24:
            print("div")
        #23
        if value==0x23:
            print("mul")
        #22
        if value==0x22:
            print("sub")
        #21
        if value==0x21:
            print("add")
        #20
        if value==0x20:
            print("pop r7")
        #1F
        if value==0x1F:
            print("pop r5")
        #1E
        if value==0x1E:
            print("pop r4")
        #1D
        if value==0x1D:
            print("pop r3")
        #1C
        if value==0x1C:
            print("pop r2")
        #1B
        if value==0x1B:
            print("pop r1")
        #1A
        if value==0x1A:
            print("pop r0")
        #19
        if value==0x19:
            print("pop r6")
        #18
        if value==0x18:
            print("push r7")
        #16
        if value==0x16:
            print("push r6")
        #15
        if value==0x15:
            print("push r5")
        #14
        if value==0x14:
            print("push r4")
        #13
        if value==0x13:
            print("push r3")
        #12
        if value==0x12:
            print("push r2")
        #11
        if value==0x11:
            print("push r1")
        #10
        if value==0x10:
            print("push r0")
        #0f
        if value==0x0f:
            print("jb 0x0")
        #0E
        if value==0x0E:
            print("jno 0x0")
        #0D
        if value==0x0D:
            print("jo 0x0")
        #0C
        if value==0x0C:
            print("jnc 0X0")
        #0B
        if value==0x0B:
            print("jc 0x0")
        #0A
        if value==0x0A:
            print("jmp 0x0")
        #09
        if value==0x09:
            print("jz 0x0")
        #08
        if value==0x08:
            print("jnz 0x0")
        #07
        if value==0x07:
            print("ret")
        #06
        if value==0x06:
            print("call 0x0")
        #05
        if value==0x05:
            print("popm 0x0")
        #04
        if value==0x04:
            print("pushm 0x0")
        #03
        if value==0x03:
            print("syscall")
        #02
        if value==0x02:
            print("pop")
        #01
        if value==0x01:
            print("push 0x0")
        #00
        if value==0x00:
            print("nop")
    
