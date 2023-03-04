
def testasm():
    mem = hmem("so2game.exe")
    locate = mem.createAllocate()
    asm = """push 5
    push 1
    push 2
    mov ecx,92B1EC
    call 64CBE0
    ret"""
    mem.writeASM(locate, asm)
    # mem.startThread(locate)
    hex = mem.decimalToHexSigned2(locate)
    print(hex)
    quit()


def testbytes():
    mem = hmem("so2game.exe")
    locate = mem.createAllocate()
    asm = """68 12050000
    6A 01
    6A 02
    B9 ECB19200
    E8 D0CBABFF
    C3                   
"""
    mem.writeBytesASM(locate, asm)
    # mem.startThread(locate)
    hex = mem.decimalToHexSigned2(locate)
    print(hex)
    quit()


def muaCongSun():
    mem = hmem("PlantsVsZombies.exe")
    locate = mem.createAllocate()
    asm = """01 DE
    89 B7 78550000                          
"""
    mem.writeJmp('"PlantsVsZombies.exe"+1E844', locate)
    mem.writeByteArray('"PlantsVsZombies.exe"+1E849', None, "0F1F 00")
    lastlocate = mem.writeBytesASM(locate, asm)
    mem.writeJmp(lastlocate, '"PlantsVsZombies.exe"+1E84C')
    # mem.writeBytesASM('"PlantsVsZombies.exe"+1E844', )
    # # mem.startThread(locate)
    hex = mem.decimalToHexSigned2(locate)

    print(hex)


def muaCayLuon():
    mem = hmem("PlantsVsZombies.exe")
    locate = mem.createAllocate(2048)
    asm = """FF 47 24
    81 47 24 00100000
    8B 47 24
"""
    mem.writeJmp('"PlantsVsZombies.exe"+91E4C', locate, True)

    # mem.writeByteArray('"PlantsVsZombies.exe"+91E52', None, "3B4728")
    # mem.writeJle('"PlantsVsZombies.exe"+91E55', '"PlantsVsZombies.exe"+91E6B')
    lastlocate = mem.writeBytesASM(locate, asm)
    mem.writeJmp(lastlocate, '"PlantsVsZombies.exe"+91E52')
    # mem.writeBytesASM('"PlantsVsZombies.exe"+1E844', )
    # # mem.startThread(locate)
    hex = mem.decimalToHexSigned2(locate)

    print(hex)


def oneHitKoMu():
    mem = hmem("PlantsVsZombies.exe")
    locate = mem.createAllocate(2048)
    asm = """BD 00000000
    89 AF C8000000
"""
    mem.writeJmp('"PlantsVsZombies.exe"+141ce4', locate, True)

    # mem.writeByteArray('"PlantsVsZombies.exe"+91E52', None, "3B4728")
    # mem.writeJle('"PlantsVsZombies.exe"+91E55', '"PlantsVsZombies.exe"+91E6B')
    lastlocate = mem.writeBytesASM(locate, asm)
    mem.writeJmp(lastlocate, '"PlantsVsZombies.exe"+141cea')
    # mem.writeBytesASM('"PlantsVsZombies.exe"+1E844', )
    # # mem.startThread(locate)
    hex = mem.decimalToHexSigned2(locate)

    print(hex)


# muaCongSun()
# muaCayLuon()
# oneHitKoMu()
# quit()


def autoDungItemVL2():
    mem = hmem("so2game.exe")
    locate = mem.createAllocate()
    asm = """push 5
    push 1
    push 2
    mov ecx,92B1EC
    call 64CBE0
    ret"""
    mem.writeASM(locate, asm)
    mem.startThread(locate)
    hex = mem.decimalToHexSigned2(locate)
    print(hex)
    quit()


def chonNhanVatVL2():
    mem = hmem("so2game.exe")
    locate = mem.createAllocate()
    asm = """push 1
    mov ecx,0086DE40
    call 0040D3E0
    ret"""
    mem.writeASM(locate, asm)
    mem.startThread(locate)
    hex = mem.decimalToHexSigned2(locate)
    print(hex)
    quit()


def dichuyenVL2(x, y):
    x = x * 256
    y = y * 512

    mem = hmem("so2game.exe")
    xhex = mem.decimalToHexSigned2(x)
    yhex = mem.decimalToHexSigned2(y)
    locate = mem.createAllocate()
    asm = f"""push 0
    push 0
    push 000000C8
    push {yhex}
    push {xhex}
    push 00000002
    push 0D3D4024
    mov ecx,0092B1EC
    call 0064A400
    ret"""
    mem.writeASM(locate, asm)
    mem.startThread(locate)
    hex = mem.decimalToHexSigned2(locate)
    print(hex)
    quit()


# dichuyenVL2(150, 180)

# locate = mem.createAllocate()
# mem.writeCall(locate, 0x444AA0)
# mem.writeEnd(locate + 0x5)
# mem.startThread(locate)
# locate = mem.createAllocate()
# mem.writeCall(locate, 0x40D6A0)
# mem.writeEnd(locate + 0x5)
# mem.startThread(locate)
