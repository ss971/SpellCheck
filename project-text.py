import tkinter as tk

import re
from collections import Counter
from string import ascii_lowercase as letters



# def words(text): 
#     return re.findall(r'\w+', text.lower())

# def known(words):
#     "The subset of `words` that appear in the dictionary of word_ct."
#     #print(words(open(r'C:\Users\shamb\The codes\college\big.txt').read()))
#     Counter(words(open(r'C:\Users\shamb\The codes\college\big.txt').read())))

#     return set(w for w in words if w in word_ct)
def words(text): 
    return re.findall(r'\w+', text.lower())

def known(words):
    "The subset of `words` that appear in the dictionary of word_ct."
    return set(w for w in words if w in word_ct)


def edits1(word):
    "All edits that are one edit away from the word."
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from word."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def P(word): 
    "Probability of the word appearing in big.txt"
    # word_ct = Counter(words(open(r'C:\Users\shamb\The codes\college\big.txt').read()))
    global word_ct
    N = sum(word_ct.values())
    return word_ct[word] / N

def correction(word, type): 
    "Most probable spelling correction for word."
    if type == 'mp':
        return max(candidates(word), key = P)
    elif type == 'all':
        return sorted(candidates(word), key=P)


word_ct = Counter(words(open(r'{insert path to big.txt}').read()))

def main(txt):
    global word_ct
    print(word_ct)
#txt = input("Enter text: ").split()

    print("Most probable corrections:")
    for i in txt:
        print(correction(i, 'mp'), end = " ")
    print()

    print("All possibilites of corrections:")
    correct_list = []
    for i in txt:
        if correction(i, 'mp') == i:
            print(i, end = " ")
        else:
            correct_list.append(correction(i, 'all'))
    return correct_list

def text_spellcheck():
    if text.get(1.0,'end-1c') is not None:
        name = text.get(1.0,'end-1c')
        #label = tk.Label(win,text = name)
        print(name)

        suggestion = main(name.split())
        label = tk.Label(win, text = suggestion)  #idk what im doing with the frame thingy but it works for now and i dont know whatll happen if i change it 
        out = tk.Text(win,height = 30, width = 40)
        label.grid(row = 41)
    else:
        pass
        

def reset():
    return 1

win = tk.Tk()
win.geometry('1000x1000')

#leftframe = tk.Frame(win)
#leftframe.grid( row = 0, column = 1)

#midframe = tk.Frame(win)
#midframe.grid(row = 41, column = 1)


text = tk.Text(win, height = 30, width = 40)
text.grid(column=1,row=40)



button_check = tk.Button(win,bg = '#ADD8E6',command=text_spellcheck,text = 'Submit')
button_reset = tk.Button(win,bg = '#ADD8E6',command=reset,text = 'Reset')

button_check.grid()
button_reset.grid()
win.mainloop()
