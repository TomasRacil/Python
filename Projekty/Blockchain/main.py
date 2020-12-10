from Block import Block

blockchain = []

genesis_block = Block ("Univerzita Obrany", ["1. ceta je na pozici",
                                             "Pripravte se k provedeni lecky.",
                                             "Rozumim, provedu"])

second_block = Block(genesis_block.block_hash, ["Doslo ke kontaktu s nepritelem.",
                                                "Hlaste stav jednotky.",
                                                "Dva zraneni, pozadujeme podporu."])

third_block = Block(second_block.block_hash, ["Rozkaz velitele 3. roty cislo 127 ze dne...",
                                              "Seznam osob s bezpecnostni proverkou stupne Tajne:...",
                                              "Velitelem 7. ukoloveho uskupeni rotace Bravo..."])

print("Block hash: Genesis Block")
print(genesis_block.block_hash)

print("Block hash: Second Block")
print(second_block.block_hash)

print("Block hask: Third Block")
print(third_block.block_hash)