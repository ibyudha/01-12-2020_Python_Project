# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:25:07 2020

@author: yudha
"""

from tkinter import * 
import random 
import time as t
import datetime 
  
basis = Tk() 
basis.geometry("800x600") 
basis.title("Pesan Rahasia oleh Gus Yudha") 
Kepala = Frame(basis, width = 800, relief = SUNKEN) 
Kepala.pack(side = TOP) 
framePertama = Frame(basis, width = 800, height = 600, relief = SUNKEN) 
framePertama.pack(side = LEFT) 

# ============================================== 
#                  Waktu 
# ============================================== 
waktuSekarang = t.asctime(t.localtime(t.time())) 
infoLabel = Label(Kepala, font = ('helvetica', 20, 'bold'), text = "PESAN RAHASIA OLEH GUS YUDHA \n VIGENERE CIPHER", fg = "Black", bd = 10, anchor='w')        
infoLabel.grid(row = 0, column = 0) 
infoLabel = Label(Kepala, font=('arial', 20, 'bold'), text = waktuSekarang, fg = "Steel Blue", bd = 10, anchor = 'w')                  
infoLabel.grid(row = 1, column = 0) 
  
nama = StringVar()
pesan = StringVar()
kunci = StringVar()
mode = StringVar()
hasil = StringVar()
  
# Fungsi Reset
def Reset(): 
    nama.set("") 
    pesan.set("") 
    kunci.set("") 
    mode.set("") 
    hasil.set("") 
  
# Nama
labelNama = Label(framePertama, font = ('arial', 16, 'bold'), text = "NAMA", bd = 16, anchor = "w")          
labelNama.grid(row = 0, column = 0) 
formNama = Entry(framePertama, font = ('arial', 16, 'bold'), textvariable = nama, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right')                 
formNama.grid(row = 0, column = 1) 
  
# Pesan 
labelPesan = Label(framePertama, font = ('arial', 16, 'bold'), text = "PESAN", bd = 16, anchor = "w") 
labelPesan.grid(row = 1, column = 0) 
formPesan = Entry(framePertama, font = ('arial', 16, 'bold'), textvariable = pesan, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right')        
formPesan.grid(row = 1, column = 1) 

# Kunci
labelKunci = Label(framePertama, font = ('arial', 16, 'bold'), text = "KUNCI", bd = 16, anchor = "w")      
labelKunci.grid(row = 2, column = 0) 
formKunci = Entry(framePertama, font = ('arial', 16, 'bold'), textvariable = kunci, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right')      
formKunci.grid(row = 2, column = 1) 

# Mode ()
labelMode = Label(framePertama, font = ('arial', 16, 'bold'), text = "MODE(E/D)", bd = 16, anchor = "w") 
labelMode.grid(row = 3, column = 0) 
formMode = Entry(framePertama, font = ('arial', 16, 'bold'), textvariable = mode, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right')        
formMode.grid(row = 3, column = 1) 

# Hasil
labelHasil = Label(framePertama, font = ('arial', 16, 'bold'), text = "HASIL", bd = 16, anchor = "w")        
labelHasil.grid(row = 2, column = 2) 
formHasil = Entry(framePertama, font = ('arial', 16, 'bold'),  textvariable = hasil, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right')          
formHasil.grid(row = 2, column = 3) 
  
# Vigenère cipher 
import base64 
  
# Fungsi untuk encode
def encode(kunci, isiPesan): 
    enc = [] 
      
    for i in range(len(isiPesan)): 
        kunci_c = kunci[i % len(kunci)] 
        enc_c = chr((ord(isiPesan[i]) +
                     ord(kunci_c)) % 256) 
                       
        enc.append(enc_c) 
          
    return base64.urlsafe_b64encode("".join(enc).encode()).decode() 
  
# Fungsi untuk decode
def decode(kunci, enc): 
    dec = [] 
      
    enc = base64.urlsafe_b64decode(enc).decode() 
    for i in range(len(enc)): 
        kunci_c = kunci[i % len(kunci)] 
        dec_c = chr((256 + ord(enc[i]) -
                           ord(kunci_c)) % 256) 
                             
        dec.append(dec_c) 
    return "".join(dec) 
  
  
def prosesInputnya(): 
    print("Pesan = ", (pesan.get())) 
  
    isiPesan = pesan.get() 
    k = kunci.get() 
    m = mode.get() 
  
    if (m == 'e' or m == 'E'): 
        hasil.set(encode(k, isiPesan)) 
    else: 
        hasil.set(decode(k, isiPesan)) 
  
# Tombol Proses 
tombolP = Button(framePertama, padx = 16, pady = 16, bd = 16, fg = "black", font = ('arial', 16, 'bold'), width = 10, text = "Proses", bg = "green", command = prosesInputnya)
tombolP.grid(row = 4, column = 1)
# Tombol Reset
tombolR = Button(framePertama, padx = 16, pady = 16, bd = 16, fg = "black", font = ('arial', 16, 'bold'), width = 10, text = "Reset", bg = "red", command = Reset)
tombolR.grid(row = 4, column = 3) 

# Jaga tampilan
window.mainloop() 
