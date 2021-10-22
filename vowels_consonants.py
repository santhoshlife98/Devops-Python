''' Author @santhosh.bheeman '''

def check_vowels_consonants(s):
    vow = []
    cons = []
    for i in s:
        #print(i)
        if i in "aeiou":
            vow.append(i)
        elif i not in "aeiuo":
            cons.append(i)

    print("The vowels are:",''.join(vow))
    print("The consonants are:",''.join(cons))

if __name__ == '__main__':
    s=input("Enter the string: ")
    check_vowels_consonants(s)
