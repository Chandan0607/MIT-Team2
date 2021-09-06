import tkinter
from tkinter.ttk import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import mplfinance as mpf

df = pd.read_csv('result.csv')
symbols = df['symbol'].unique()
symbols=tuple(symbols)

agg_dict = {'open': 'first',
          'high': 'max',
          'low': 'min',
          'close': 'last',
          'volume': 'mean'}


window = tkinter.Tk()
window.title("OHLC")
sym=Label(window,text="Symbol: ")
sym.grid(column=1,row=0,pady=50,padx=100,sticky="w")
symbols_cb=Combobox(window)
symbols_cb['values']=symbols
symbols_cb.current(0)
symbols_cb.grid(column=2,row=0,pady=50,padx=100,sticky="w")
l1=Label(window,text="Range: ")
l1.grid(column=1,row=1,pady=50,padx=100,sticky="w")
range=Combobox(window)
range['values']=("Weekly","Monthly")
range.current(0)
range.grid(column=2,row=1,pady=50,padx=100,sticky="w")
l2=Label(window,text="Type of chart: ")
l2.grid(column=1,row=2,pady=50,padx=100,sticky="w")
chart=Combobox(window)
chart['values']=('ohlc','candle')
chart.current(0)
chart.grid(column=2,row=2,pady=50,padx=100,sticky="w")

def generate_chart():
    db = df[df['symbol'] == symbols_cb.get()].copy()
    db['date'] = pd.to_datetime(db['date'])
    db = db.set_index('date')
    db = db.resample(range.get()[0]).agg(agg_dict)
    mpf.plot(db,type=chart.get(),mav=(3, 5), title=symbols_cb.get())

bt = tkinter.Button(window, text = "Display Chart", command=generate_chart)
bt.grid(column=1,row=3,pady=50,padx=100,sticky="w")


window.mainloop()
