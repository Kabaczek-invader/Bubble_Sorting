def bubble_sort(tab):
    for j in range(len(tab)):
        for i in range(0, len(tab)-1):
            if tab[i] > tab[i+1]:
                temp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = temp
    return tab
tab = [3, 7, 1, 8, 2, 9, 6]
tabs = bubble_sort(tab.copy())
print(tab)
print(tabs)