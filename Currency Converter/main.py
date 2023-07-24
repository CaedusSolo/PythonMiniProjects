import tkinter as tk 
from tkinter import ttk
import requests

currency_list = {
    'ALL': 'Albania Lek',
    'AFN': 'Afghanistan Afghani',
    'ARS': 'Argentina Peso',
    "AMD" : "Armenian Dram",
    'AWG': 'Aruba Guilder',
    'AUD': 'Australia Dollar',
    'AZN': 'Azerbaijan New Manat',
    'BSD': 'Bahamas Dollar',
    'BBD': 'Barbados Dollar',
    'BDT': 'Bangladeshi taka',
    'BYR': 'Belarus Ruble',
    'BZD': 'Belize Dollar',
    'BMD': 'Bermuda Dollar',
    'BOB': 'Bolivia Boliviano',
    'BAM': 'Bosnia and Herzegovina Convertible Marka',
    'BWP': 'Botswana Pula',
    'BGN': 'Bulgaria Lev',
    'BRL': 'Brazil Real',
    'BND': 'Brunei Darussalam Dollar',
    'KHR': 'Cambodia Riel',
    'CAD': 'Canada Dollar',
    'KYD': 'Cayman Islands Dollar',
    'CLP': 'Chile Peso',
    'CNY': 'China Yuan Renminbi',
    'COP': 'Colombia Peso',
    'CRC': 'Costa Rica Colon',
    'HRK': 'Croatia Kuna',
    'CUP': 'Cuba Peso',
    'CZK': 'Czech Republic Koruna',
    'DKK': 'Denmark Krone',
    'DOP': 'Dominican Republic Peso',
    'XCD': 'East Caribbean Dollar',
    'EGP': 'Egypt Pound',
    'SVC': 'El Salvador Colon',
    'EEK': 'Estonia Kroon',
    'EUR': 'Euro Member Countries',
    'FKP': 'Falkland Islands (Malvinas) Pound',
    'FJD': 'Fiji Dollar',
    'GHC': 'Ghana Cedis',
    'GIP': 'Gibraltar Pound',
    'GTQ': 'Guatemala Quetzal',
    'GGP': 'Guernsey Pound',
    'GYD': 'Guyana Dollar',
    'HNL': 'Honduras Lempira',
    'HKD': 'Hong Kong Dollar',
    'HUF': 'Hungary Forint',
    'ISK': 'Iceland Krona',
    'INR': 'India Rupee',
    'IDR': 'Indonesia Rupiah',
    'IRR': 'Iran Rial',
    'IMP': 'Isle of Man Pound',
    'ILS': 'Israel Shekel',
    'JMD': 'Jamaica Dollar',
    'JPY': 'Japan Yen',
    'JEP': 'Jersey Pound',
    'KZT': 'Kazakhstan Tenge',
    'KRW': 'Korea (South) Won',
    'KGS': 'Kyrgyzstan Som',
    'LAK': 'Laos Kip',
    'LVL': 'Latvia Lat',
    'LBP': 'Lebanon Pound',
    'LRD': 'Liberia Dollar',
    'LTL': 'Lithuania Litas',
    'MKD': 'Macedonia Denar',
    'MYR': 'Malaysia Ringgit',
    'MUR': 'Mauritius Rupee',
    'MXN': 'Mexico Peso',
    'MNT': 'Mongolia Tughrik',
    'MZN': 'Mozambique Metical',
    'NAD': 'Namibia Dollar',
    'NPR': 'Nepal Rupee',
    'ANG': 'Netherlands Antilles Guilder',
    'NZD': 'New Zealand Dollar',
    'NIO': 'Nicaragua Cordoba',
    'NGN': 'Nigeria Naira',
    'NOK': 'Norway Krone',
    'OMR': 'Oman Rial',
    'PKR': 'Pakistan Rupee',
    'PAB': 'Panama Balboa',
    'PYG': 'Paraguay Guarani',
    'PEN': 'Peru Nuevo Sol',
    'PHP': 'Philippines Peso',
    'PLN': 'Poland Zloty',
    'QAR': 'Qatar Riyal',
    'RON': 'Romania New Leu',
    'RUB': 'Russia Ruble',
    'SHP': 'Saint Helena Pound',
    'SAR': 'Saudi Arabia Riyal',
    'RSD': 'Serbia Dinar',
    'SCR': 'Seychelles Rupee',
    'SGD': 'Singapore Dollar',
    'SBD': 'Solomon Islands Dollar',
    'SOS': 'Somalia Shilling',
    'ZAR': 'South Africa Rand',
    'LKR': 'Sri Lanka Rupee',
    'SEK': 'Sweden Krona',
    'CHF': 'Switzerland Franc',
    'SRD': 'Suriname Dollar',
    'SYP': 'Syria Pound',
    'TWD': 'Taiwan New Dollar',
    'THB': 'Thailand Baht',
    'TTD': 'Trinidad and Tobago Dollar',
    'TRY': 'Turkey Lira',
    'TRL': 'Turkey Lira',
    'TVD': 'Tuvalu Dollar',
    'UAH': 'Ukraine Hryvna',
    'GBP': 'United Kingdom Pound',
    'USD': 'United States Dollar',
    'UYU': 'Uruguay Peso',
    'UZS': 'Uzbekistan Som',
    'VEF': 'Venezuela Bolivar',
    'VND': 'Viet Nam Dong',
    'YER': 'Yemen Rial',
    'ZWD': 'Zimbabwe Dollar'
}

class CurrencyConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.config(padx=50,pady=50,bg="#483248")
        self.root.resizable(False,False)
        self.root.title("Currency Converter")

        self.frame = tk.Frame(self.root,padx=30,pady=30,bg="#301934")
        self.frame.pack()

        self.title_label = tk.Label(self.frame,bg="#301934",fg="white",
                                    font=("poppins",25,"bold"),text="Currency Converter",anchor="center",
                                    pady=20)
        self.title_label.grid(row=0,column=0)
        self.root.rowconfigure((0,2,4,6),weight=1)

        self.amount_label = tk.Label(self.frame,bg="#301934",fg="white",font=("poppins",14,"normal"),
                                     text="Amount",padx=5,pady=5,anchor="w")
        self.amount_label.grid(row=1,column=0,sticky="w")
        self.amount_entry = tk.Entry(self.frame,bg="#301934",fg="white",font=("poppins",16,"normal"),
                                     insertbackground="white")
        self.amount_entry.focus()
        self.amount_entry.grid(row=2,column=0,padx=5,pady=5,sticky="w")

        self.from_label = tk.Label(self.frame,bg="#301934",fg="white",font=("poppins",14,"normal"),
                                   text="From",padx=5,pady=15,anchor="w")
        self.from_label.grid(row=3,column=0,sticky="w")
        self.from_combobox = ttk.Combobox(self.frame,
                                          values=[f"{key} ({value}) " for (key,value) in currency_list.items()],
                                          font=("poppins",16,"normal"),
                                          foreground="black",background="#301934")
        self.from_combobox.grid(row=4,column=0,sticky="w",pady=(0,20))

        self.to_label = tk.Label(self.frame,bg="#301934",fg="white",font=("poppins",14,"normal"),
                                 text="To",padx=5,pady=5,anchor="w")
        self.to_label.grid(row=5,column=0,sticky="w")
        self.to_combobox = ttk.Combobox(self.frame,
                                          values=[f"{key} ({value}) " for (key,value) in currency_list.items()],
                                          font=("poppins",16,"normal"),
                                          foreground="black",background="#301934")
        self.to_combobox.grid(row=6,column=0,sticky="w",pady=(10,30))

        self.exchange_rate_label = tk.Label(self.frame,bg="#301934",fg="white",font=("poppins",18,"bold"),
                                            anchor="w",padx=5,pady=5)
        self.exchange_rate_label.grid(row=7,column=0,sticky="w")

        self.get_rate_button = tk.Button(self.frame,bg="white",fg="black",borderwidth=2,
                                        text="Get Exchange Rate",padx=5,pady=3,font=("poppins",18,"normal"),
                                        anchor="center",width=17,justify="center",
                                        command=self.get_exchange_rate)
        self.get_rate_button.grid(row=8,column=0,sticky="sw",pady=(0,25))

        self.root.mainloop()

    
    def get_exchange_rate(self):
        api_key = "62da31bf50491e5bf44229f0"
        from_currency = self.from_combobox.get()[:3]
        to_currency = self.to_combobox.get()[:3]
        amount = int(self.amount_entry.get())
        end_point = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"

        response = requests.get(end_point)
        response.raise_for_status()
        data = response.json()["conversion_rates"][to_currency]

        self.exchange_rate_label.config(text=f"{amount} {from_currency} = {(data * amount):.2f} {to_currency}")
    
currency_converter = CurrencyConverter()