def decrypt_flag(encrypted_flag):
    runed = []
    z = "\x00"

    for v in encrypted_flag:
        runed.append(chr(ord(v) - ord(z)))
        z = runed[-1]

    return ''.join(runed)

def main():
    try:
        with open("the", "r") as file:
            encrypted_flag = file.read().strip()
            flag = decrypt_flag(encrypted_flag)
            print("Decrypted flag: ", flag)
    except Exception as e:
        print(e)
    finally:
        file.close()

if __name__ == "__main__":
    main()

