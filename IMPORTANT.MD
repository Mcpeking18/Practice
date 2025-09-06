# In this file i write stuff i wanna look at and just important stuff


### just cleaning thingy num to be in float or int when printing
```py
for i in num:
    try:
        temp = float(i)
        if temp.is_integer():
            cleaned_list.append(int(i))
        else:
            cleaned_list.append(temp)
    except ValueError:
        notnum+=1
```
**can be written as**
```py
for i in num:
    try:
        temp = float(i)
        cleaned_list.append(temp if not temp.is_integer() else int(i))
    except ValueError:
        notnum += 1
```