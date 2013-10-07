from math import *
import numpy as np
import os

##class Account:
##    def __init__(self, name, account_number, initial_amount):
##        self._name = name
##        self._no = account_number
##        self._balance = initial_amount
##
##    def deposit(self, amount):
##        self._balance += amount
##
##    def withdrawal(self, amount):
##        self._balance -= amount
##
##    def get_balance(self):
##        return self._balance
##
##    def dump(self):
##        s = '%s, %s, balance: %s' % (self._name, self._no, self._balance)
##        print s

class Person:
    def __init__(self, name, mobile_phone=None, office_phone=None,
                 private_phone=None, email=None):
        self.name = name
        self.mobile = mobile_phone
        self.office = office_phone
        self.private = private_phone
        self.email = email

    def add_mobile_phone(self, number):
        self.mobile = number

    def add_office_phone(self, number):
        self.office = number

    def add_private_phone(self, number):
        self.private = number

    def add_email(self, address):
        self.email = address

    def dump(self):
        s = self.name + '\n'
        if self.mobile is not None:
            s += 'mobile phone:     %s\n' % self.mobile
        if self.office is not None:
            s += 'office phone:     %s\n' % self.office
        if self.private is not None:
            s += 'private phone:    %s\n' % self.private
        if self.email is not None:
            s += 'email address:    %s\n' % self.email
        print s
