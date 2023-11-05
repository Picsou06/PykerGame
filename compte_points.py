import pygame
from pygame import *
import class_Cartes
import class_JeuDeCartes
import class_PlayerHand

def paires(l):
    pts = 0
    tmp = []
    tmp = tmp + l 
    i = len(l) -1
    while i > 0:    
        if l[i] == l[i-1]:
            pts = 27 + l[i]
            tmp.pop(i)
            tmp.pop(i-1)
            i = 0
        else:
            i = i-1
    j = len(tmp) -1
    while j > 0:
        
        if tmp[j] == tmp[j-1]:
            pts = pts + 14 + tmp[j-1]
            j = 0
        else:
            j = j-1    
    
    return pts
    

def brelan(l):
    pts = 0
    i = len(l) -1
    while i > 1:
        if l[i] == l[i-1] == l[i-2]:
            pts = pts + 68 + l[i-1]
            i = 0
        else:
            i = i-1
    return pts   

def suite(l):
    pts = 0
    i = len(l) -1
    
    while i > 3:
        if l[i] - 1 == l[i-1]:
            if l[i-1] - 1 == l[i-2]:
                if l[i-2] - 1 == l[i-3]:
                    if l[i-3] - 1 == l[i-4]:
                        pts =  82 + l[i] + l[i-1] + l[i-2] + l[i-3] + l[i-4]
                        i = 0
                    else :
                        i = i-1
                else : 
                    i = i-1
            else : 
                i = i-1
        else : 
            i = i-1
    return pts

def couleur(L):
    pts = 0
    i = len(L) - 1

    while i >= 4:
        if L[i].get_couleur() == L[i-1].get_couleur() == L[i-2].get_couleur() == L[i-3].get_couleur() == L[i-4].get_couleur():
            pts = 142 + L[i].get_valeur() + L[i-1].get_valeur() + L[i-2].get_valeur() + L[i-3].get_valeur() + L[i-4].get_valeur()
            i = 0
        else:
            i = i - 1
    return pts

     
def full(l):
    pts = 0
    i = len(l) -1
    r = True
    r2 = True
    tmp = []
    tmp = tmp + l

    while i > 1 and r == True:
        if l[i] == l[i-1] == l[i-2]:
            r = False
            b = l[i]
            tmp.pop(i)
            tmp.pop(i-1)
            tmp.pop(i-2)
        else:
            i = i-1
    
    j = len(tmp) -1 
    
    while j > 0 and r2 == True:
        if tmp[j] == tmp[j-1]:
            r2 = False
            d = tmp[j]
        else:
            j = j-1
    if r == False and r2 == False:
        pts = 202 + 68*b + 27*d
    return pts

def carre(l):
    pts = 0
    i = len(l) -1
    while i > 2:
        if l[i] == l[i-1] == l[i-2] == l[i-3]:
            pts = 1505 + l[i]
            i = 0
        else:
            i = i-1
    return pts

def quinte_flush(l, L):
    pts = 0
    i = len(l)-1
    tmp = []
  
    while i > 3:        
        if l[i] - l[i-1] == 1: 
            if l[i-1] - l[i-2] == 1:
                if l[i-2] - l[i-3] == 1:
                    if l[i-3] - l[i-4] == 1:
                        tmp.append(L[i-4])
                        tmp.append(L[i-3])
                        tmp.append(L[i-2])
                        tmp.append(L[i-1])
                        tmp.append(L[i])        
                        i = 0
                    else:
                        i = i-1
                else:
                    i = i-1
            else : 
                i = i-1            
        else : 
            i = i-1
   
    j = len(tmp)-1
    if j > 3:
        if tmp[j].get_couleur() == tmp[j-1].get_couleur():
            if tmp[j-1].get_couleur() == tmp[j-2].get_couleur():
                if tmp[j-2].get_couleur() == tmp[j-3].get_couleur():
                    if tmp[j-3].get_couleur() == tmp[j-4].get_couleur():
                        pts = 1520
    return pts

def quinte_flush_royale(l, L):
    pts = 0
    i = len(l) - 1
    r = False
    tmp = []
    while i >= 4 and not r:
        if l[i] - 1 == l[i-1]:  
            if l[i-1] - 1 == l[i-2]:
                if l[i-2] - 1 == l[i-3]:
                    if l[i-3] - 1 == l[i-4]:
                        r = True
                        tmp.append(L[i-4])
                        tmp.append(L[i-3])
                        tmp.append(L[i-2])
                        tmp.append(L[i-1])
                        tmp.append(L[i])
                    else:
                        i = i-1
                else:
                    i= i-1
            else:
                i = i-1
        else:
            i = i - 1
    
    if r and L[i].get_couleur() == L[i-1].get_couleur() == L[i-2].get_couleur() == L[i-3].get_couleur() == L[i-4].get_couleur() and l[i] == 14:
        pts = 1521
    return pts


def nbr_pts(p,board):
    L = p + board
    l = []
    
    N = len(L)
    for n in range(1,N):
        cle = L[n]
        j = n-1
        while j>=0 and L[j].est_superieure_a(cle):
            L[j+1] = L[j] # decalage
            j = j-1
        L[j+1] = cle

    for j in L:
        l.append(j.get_valeur())
    
    if len(L) >= 5 :
        if quinte_flush_royale(l,L) == 1521:
            return quinte_flush_royale(l,L)
        else:
            if quinte_flush(l,L) == 1520:
                return quinte_flush(l,L)
            else :
                if 1507 <= carre(l) <= 1519:
                    return carre(l)
                else :
                    if 419 <= full(l) <= 1505 :
                        return full(l)
                    else:
                        if 162 <= couleur(L) <= 202:
                            return couleur(L)
                        else:
                            if 102 <= suite(l) <= 142:
                                return suite(l)
                            else:
                                if 70 <= brelan(l) <= 82:
                                    return brelan(l)
                                else:
                                    if 29 <= paires(l) <= 41 or 46 <= paires(l) <= 68:
                                        return paires(l)
                                    else:
                                        mx = l.pop()
                                        return max(l) + mx
    if len(L) == 4:
        if 1507 <= carre(l) <= 1519 :
            return carre(l)
        else:
            if 70 <= brelan(l) <= 82:
                return brelan(l)
            else:
                if 29 <= paires(l) <= 41 or 46 <= paires(l) <= 68:
                    return paires(l)
                else:
                    mx = l.pop()
                    return max(l) + mx
    if len(L) == 3:
        if 70 <= brelan(l) <= 82:
            return brelan(l)
        else:
            if 29 <= paires(l) <= 41 or 46 <= paires(l) <= 68:
                return paires(l)
            else:
                mx = l.pop()
                return max(l) + mx
    if len(L) == 2:
        if 29 <= paires(l) <= 41 or 46 <= paires(l) <= 68:
            return paires(l)
        else:
            mx = l.pop()
            return max(l) + mx