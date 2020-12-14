# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:03:35 2019

@author: hp
"""

def adjust_size(key, length): #key is a string
    if len(key) < length:
        return key + ''.join([chr(0) for i in range(length - len(key))])
    return key[0:length]



def get_number_of_rounds(keylen): #  số vòng lặp Nr ứng với độ dài khóa
    keylen_vs_rounds = {}
    keylen_vs_rounds[16] = 10
    keylen_vs_rounds[24] = 12
    keylen_vs_rounds[32] = 14
    return keylen_vs_rounds[keylen]

def convert_char_array_to_int_array(arr):# trả về danh sách các kí tự dưới dạng code point(chỉ số vị trí của kí tự trong unicode)
    return [ord(i) for i in arr]

def array_xor(arr1, arr2):  #string cg là array: x = 'bach' => x[0] = b
    return [arr1[i] ^ arr2[i] for i in range(len(min(arr1, arr2)))] #min là so sánh chữ đầu trong bẳng chũ cái   => min: a, max:z

def initial_process(message, key, keylen, iv):
    while len(message) % 16 != 0:         #Chia file plaintext thành các khối 128bit(16 kí tự) => Tự động thêm kí tự khoảng trắng chr(0) nếu thiếu
        message += chr(0)
    key = adjust_size(key, keylen)        #Thay đổi độ dài của khóa ứng vs key size đã chọn
    key = convert_char_array_to_int_array(key)
    num_of_rounds = get_number_of_rounds(len(key))
    
    iv = adjust_size(iv, 16)              #Thay đổi độ dài của iv = 16 kí tự
    iv = convert_char_array_to_int_array(iv)
    message = [ord(i) for i in message]   # trả về danh sách các kí tự trong plaintext -> code point(chỉ số của kí tự trong unicode)
    return message, key, num_of_rounds, iv #message,key, iv: những danh sách các sô codepoint