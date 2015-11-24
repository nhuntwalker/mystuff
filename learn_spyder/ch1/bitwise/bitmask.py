# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 07:25:14 2015

@author: Nick

Class that represents a bit mask. It has methods representing all the bitwise 
operations plus some additional features. The methods return a new BitMask 
object or a boolean result. See the bits module for more on the operations 
provided.
"""

class BitMask(int):
    def AND(self, bm):
        return BitMask(self & bm)
        
    def NOT(self):
        return BitMask(~self)
            
    def OR(self, bm):
        return BitMask(self | bm)
    
    def XOR(self, bm):
        return BitMask(self ^ bm)
    
    def shiftleft(self, num):
        return BitMask(self << num)
    
    def shiftright(self, num):
        return BitMask(self > num)
    
    def bit(self, num):
        mask = 1 << num # all 0 except idx
        return bool(self & mask)
    
    def setbit(self, idx):
        mask = 1 << idx #all 0 except idx
        return BitMask(self | mask)
    
    def zerobit(self, idx):
        mask = ~(1 << idx) # all 1 except idx
        return BitMask(self & mask)
    
    def listbits(self, start=0, end=-1):
        end = end if end < 0 else end + 2
        return [int(c) for c in bin(self)[start+2: end]]
