/** 통화 단위 */
export type Currency =
	/** Rial Omani */
	| "OMR"
	/** Peso Convertible */
	| "CUC"
	/** Barbados Dollar */
	| "BBD"
	/** Zloty */
	| "PLN"
	/** El Salvador Colon */
	| "SVC"
	/** Bermudian Dollar */
	| "BMD"
	/** Somoni */
	| "TJS"
	/** Tunisian Dinar */
	| "TND"
	/** Guinean Franc */
	| "GNF"
	/** Sudanese Pound */
	| "SDG"
	/** Ouguiya */
	| "MRU"
	/** Bond Markets Unit European Monetary Unit (E.M.U.-6) */
	| "XBB"
	/** Pakistan Rupee */
	| "PKR"
	/** Falkland Islands Pound */
	| "FKP"
	/** Mauritius Rupee */
	| "MUR"
	/** CFA Franc BEAC */
	| "XAF"
	/** Saudi Riyal */
	| "SAR"
	/** Canadian Dollar */
	| "CAD"
	/** Hong Kong Dollar */
	| "HKD"
	/** Guarani */
	| "PYG"
	/** Malagasy Ariary */
	| "MGA"
	/** Uruguay Peso en Unidades Indexadas (UI) */
	| "UYI"
	/** Australian Dollar */
	| "AUD"
	/** Armenian Dram */
	| "AMD"
	/** Yemeni Rial */
	| "YER"
	/** WIR Euro */
	| "CHE"
	/** Kyat */
	| "MMK"
	/** Swedish Krona */
	| "SEK"
	/** Turkish Lira */
	| "TRY"
	/** Bond Markets Unit European Unit of Account 9 (E.U.A.-9) */
	| "XBC"
	/** Kenyan Shilling */
	| "KES"
	/** Lari */
	| "GEL"
	/** Quetzal */
	| "GTQ"
	/** Tanzanian Shilling */
	| "TZS"
	/** Cuban Peso */
	| "CUP"
	/** Lek */
	| "ALL"
	/** Nakfa */
	| "ERN"
	/** Brazilian Real */
	| "BRL"
	/** Uganda Shilling */
	| "UGX"
	/** ADB Unit of Account */
	| "XUA"
	/** Gibraltar Pound */
	| "GIP"
	/** Mozambique Metical */
	| "MZN"
	/** 대한민국 원화 */
	| "KRW"
	/** Jordanian Dinar */
	| "JOD"
	/** Iraqi Dinar */
	| "IQD"
	/** Vatu */
	| "VUV"
	/** The codes assigned for transactions where no currency is involved */
	| "XXX"
	/** Uzbekistan Sum */
	| "UZS"
	/** Mvdol */
	| "BOV"
	/** Hryvnia */
	| "UAH"
	/** Sol */
	| "PEN"
	/** Comorian Franc */
	| "KMF"
	/** Dominican Peso */
	| "DOP"
	/** Taka */
	| "BDT"
	/** Sri Lanka Rupee */
	| "LKR"
	/** Fiji Dollar */
	| "FJD"
	/** Loti */
	| "LSL"
	/** Bahamian Dollar */
	| "BSD"
	/** Surinam Dollar */
	| "SRD"
	/** Codes specifically reserved for testing purposes */
	| "XTS"
	/** Saint Helena Pound */
	| "SHP"
	/** Liberian Dollar */
	| "LRD"
	/** Qatari Rial */
	| "QAR"
	/** Brunei Dollar */
	| "BND"
	/** Congolese Franc */
	| "CDF"
	/** Leone */
	| "SLE"
	/** US Dollar (Next day) */
	| "USN"
	/** Bolívar Soberano */
	| "VES"
	/** Turkmenistan New Manat */
	| "TMT"
	/** WIR Franc */
	| "CHW"
	/** Bulgarian Lev */
	| "BGN"
	/** Jamaican Dollar */
	| "JMD"
	/** Lilangeni */
	| "SZL"
	/** Czech Koruna */
	| "CZK"
	/** Zambian Kwacha */
	| "ZMW"
	/** Peso Uruguayo */
	| "UYU"
	/** Nepalese Rupee */
	| "NPR"
	/** Egyptian Pound */
	| "EGP"
	/** Azerbaijan Manat */
	| "AZN"
	/** Chilean Peso */
	| "CLP"
	/** Pataca */
	| "MOP"
	/** Seychelles Rupee */
	| "SCR"
	/** Gourde */
	| "HTG"
	/** Dong */
	| "VND"
	/** Lao Kip */
	| "LAK"
	/** Ngultrum */
	| "BTN"
	/** Pound Sterling */
	| "GBP"
	/** South Sudanese Pound */
	| "SSP"
	/** Palladium */
	| "XPD"
	/** New Taiwan Dollar */
	| "TWD"
	/** Algerian Dinar */
	| "DZD"
	/** Mexican Peso */
	| "MXN"
	/** SDR (Special Drawing Right) */
	| "XDR"
	/** Zimbabwe Dollar */
	| "ZWL"
	/** Aruban Florin */
	| "AWG"
	/** Baht */
	| "THB"
	/** Iceland Krona */
	| "ISK"
	/** Lebanese Pound */
	| "LBP"
	/** Singapore Dollar */
	| "SGD"
	/** Malawi Kwacha */
	| "MWK"
	/** Tenge */
	| "KZT"
	/** Costa Rican Colon */
	| "CRC"
	/** Tala */
	| "WST"
	/** Djibouti Franc */
	| "DJF"
	/** Libyan Dinar */
	| "LYD"
	/** Naira */
	| "NGN"
	/** Burundi Franc */
	| "BIF"
	/** UAE Dirham */
	| "AED"
	/** Swiss Franc */
	| "CHF"
	/** Rwanda Franc */
	| "RWF"
	/** Bond Markets Unit European Unit of Account 17 (E.U.A.-17) */
	| "XBD"
	/** Indian Rupee */
	| "INR"
	/** Unidad de Fomento */
	| "CLF"
	/** CFA Franc BCEAO */
	| "XOF"
	/** Unidad de Valor Real */
	| "COU"
	/** Mexican Unidad de Inversion (UDI) */
	| "MXV"
	/** Kina */
	| "PGK"
	/** Yuan Renminbi */
	| "CNY"
	/** Syrian Pound */
	| "SYP"
	/** Bolívar Soberano */
	| "VED"
	/** Romanian Leu */
	| "RON"
	/** Afghani */
	| "AFN"
	/** Philippine Peso */
	| "PHP"
	/** Moldovan Leu */
	| "MDL"
	/** Riel */
	| "KHR"
	/** Platinum */
	| "XPT"
	/** Colombian Peso */
	| "COP"
	/** Danish Krone */
	| "DKK"
	/** Cayman Islands Dollar */
	| "KYD"
	/** CFP Franc */
	| "XPF"
	/** Dalasi */
	| "GMD"
	/** Rufiyaa */
	| "MVR"
	/** Dobra */
	| "STN"
	/** Trinidad and Tobago Dollar */
	| "TTD"
	/** Balboa */
	| "PAB"
	/** Gold */
	| "XAU"
	/** Silver */
	| "XAG"
	/** 일본 엔화 */
	| "JPY"
	/** Pa’anga */
	| "TOP"
	/** Pula */
	| "BWP"
	/** Denar */
	| "MKD"
	/** Argentine Peso */
	| "ARS"
	/** Forint */
	| "HUF"
	/** Malaysian Ringgit */
	| "MYR"
	/** 미국 달러 */
	| "USD"
	/** Leone */
	| "SLL"
	/** Moroccan Dirham */
	| "MAD"
	/** Russian Ruble */
	| "RUB"
	/** Tugrik */
	| "MNT"
	/** Boliviano */
	| "BOB"
	/** Guyana Dollar */
	| "GYD"
	/** Solomon Islands Dollar */
	| "SBD"
	/** Bond Markets Unit European Composite Unit (EURCO) */
	| "XBA"
	/** Bahraini Dinar */
	| "BHD"
	/** Lempira */
	| "HNL"
	/** Unidad Previsional */
	| "UYW"
	/** New Zealand Dollar */
	| "NZD"
	/** East Caribbean Dollar */
	| "XCD"
	/** Sucre */
	| "XSU"
	/** Som */
	| "KGS"
	/** Kwanza */
	| "AOA"
	/** Belize Dollar */
	| "BZD"
	/** Rupiah */
	| "IDR"
	/** Somali Shilling */
	| "SOS"
	/** Cordoba Oro */
	| "NIO"
	/** Ghana Cedi */
	| "GHS"
	/** Netherlands Antillean Guilder */
	| "ANG"
	/** Serbian Dinar */
	| "RSD"
	/** New Israeli Sheqel */
	| "ILS"
	/** Norwegian Krone */
	| "NOK"
	/** Kuwaiti Dinar */
	| "KWD"
	/** Namibia Dollar */
	| "NAD"
	/** Ethiopian Birr */
	| "ETB"
	/** Belarusian Ruble */
	| "BYN"
	/** North Korean Won */
	| "KPW"
	/** Euro */
	| "EUR"
	/** Cabo Verde Escudo */
	| "CVE"
	/** Rand */
	| "ZAR"
	/** Iranian Rial */
	| "IRR"
	/** Kuna (Replaced by EUR) */
	| "HRK"
	/** Convertible Mark */
	| "BAM"
