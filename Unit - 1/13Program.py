
price = int(input("Enter the Price : "));
notes = [10,50,100]

if price < min(notes):
    print("Your Value is less Then ")
else:
    # notes.sort(reverse=True)
    notes.reverse()
 
    print(f"{notes[0]}  {notes[1]}  {notes[2]}")
 
    for f1 in range((price // notes[0]) + 1):
        for f2 in range((price // notes[1]) + 1):
            for f3 in range((price // notes[2])+1):
                if f1*notes[0] + f2*notes[1] + f3*notes[2] == price:
                    print(f"{f1}  {f2}  {f3}")
