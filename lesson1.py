def strcounter1(s): #решение за N**2
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)

strcounter1('aabbbbccd')

def strcounter2(s): # решение за N * M
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)

strcounter2('aabbbbccd')

def strcounter3(s): # решение за N
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    for sym, count in syms_counter.items():
        print(sym, count)
strcounter3('aabbbbccd')

# git config --global user.name "Имя"
# git config --global user.email "Почта" 
# git config --list
# git status
# git init
# git status
# git add .
# git status
# git commit -m 'initial'
# git status
# git show
# git remote add origin URL #git remote remove origin
# git branch -M main
# git push -u origin main
