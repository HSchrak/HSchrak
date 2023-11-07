#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:37:51 2023

@author: hschrak
"""

import qrcode

def main():
        myqr = MyQR(size=50, padding=5)
        myqr.create_qrcode('sample.png', fg='orange', bg= 'black')


class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)
        
    def create_qrcode(self, file_name: str, fg: str, bg: str):
        user_input = str(input('Enter text: '))
        
        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)
            
            print('Successfully created ({file_name})')
        except Exception as e:
            print(f'Error: {e}')
            

        
if __name__=='__main__':
    main()
        