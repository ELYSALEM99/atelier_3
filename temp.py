# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def somme1_exercice1 (lst):
    s=0
    for i in range(len(lst)):
        s=s+lst[i]
    return s

def somme2_exercice1 (lst):
    s=0
    for i,e in enumerate(lst):
        s=s+e
    return s

def somme3_exercice1 (lst):
    s=0
    i=0
    while i<5:
        s=s+lst[i]
        i=i+1 
    return s

def test_exercice1 ():
    lst = [2,4,1,1,10]
    if somme1_exercice1(lst)==sum(lst):
        print("vrai")
    else:
        print("faux")
        print(somme3_exercice1(lst))

def moyenne (lst):
    s=0
    for i,e in enumerate(lst):
        s=s+i     
    return somme1_exercice1(lst)/s

def nb_sup1 (lst,e):
    sup=[]
    for i in range(len(lst)):
        if lst[i]>e:
            sup.append(lst[i])
    return sup

def nb_sup2 (lst,n):
    sup=[]
    for i,e in enumerate(lst):
        if lst[i]>n:
            sup.append(lst[i])
    return sup

def moy_sub (lst,n):
    return moyenne(nb_sup2(lst, n))

def val_max(lst):
    max=0
    for i in range(len(lst)):
        if max<lst[i]:
            max=lst[i]
    return max
        
def ind_max(lst):
    for i in range(len(lst)):
        if val_max(lst)==lst[i]:
            return i

def position1(lst,e):
    for i in range(len(lst)):
        if e==lst[i]:
            return i
        if i==len(lst)-1:
            return -1
        
def position2(lst,e):
    i=0
    while e!=lst[i]:
        if i==len(lst)-1:
            return -1
        i=i+1
    return i

def nb_occurrences(lst:list,e:int)->int:
    """
    

    Parameters
    ----------
    lst : list
        DESCRIPTION.
    e : int
        DESCRIPTION.

    Returns
    -------
    int
        DESCRIPTION.

    """
    cpt=0
    for i in range(len(lst)):
        if e==lst[i]:
            cpt=cpt+1
    return cpt

def est_triee1(lst):
    cpt=0
    result=False
    for i in range(len(lst)-1):
        if lst[i]<=lst[i+1]:
            cpt=cpt+1
    if cpt==len(lst)-1:
        result=True
    return result

def est_triee2(lst):
    i=0
    result=False
    while((i<=len(lst)-2) and (lst[i]<=lst[i+1])):
        i=i+1
    if i==len(lst)-2:
            result=True
    return result
        
def a_repetitions(lst):
    t=[]
    i=0
    result=False
    while(result==False and i<len(lst)):
        if lst[i] in t:
            result=True
        else:
            t.append(lst[i])
        i=i+1
    return result
        
def separer(lst:list)->list:
    """

    Parameters
    ----------
    lst : list
         lst étant supposée non triée.

    Returns
    -------
    lsep : list
        lsep sera remplie au fur et à mesure du parcours de L, en plaçant les 
        nombres négatifs à gauche et les nombres positifs à droite Les zéros 
        seront situées entre les nombres négatifs et les nombres positifs.

    """
    l_nega=[]
    l_zer=[]
    l_posi=[]
    lsep=[]
    for i in range(len(lst)):
        if lst[i]<0:
            l_nega.append(lst[i])
        elif lst[i]==0:
            l_zer.append(lst[i])
        else:
            l_posi.append(lst[i])
    lsep=l_nega+l_zer+l_posi
    return lsep

    
lst_test =[2,1,5,9,10]
test_sep =[0,1,-8,4,0,2,-9,4,-10,0,-4,6,-20,0]
test_exercice1 ()
print(moyenne(lst_test))
print(nb_sup2(lst_test,1))
print(moy_sub(lst_test,1))
print(val_max(lst_test))
print(ind_max(lst_test))
print(position1(lst_test,10))
print(position2(lst_test,2))
print(nb_occurrences(lst_test,3))
print(est_triee1(lst_test))
print(est_triee2(lst_test))
print(a_repetitions(lst_test))
print(separer(test_sep))
