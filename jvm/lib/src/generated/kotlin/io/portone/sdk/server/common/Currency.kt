package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 통화 단위 */
@Serializable
public sealed interface Currency {
  public val value: String
  /** 대한민국 원화 */
  @SerialName("KRW")
  public data object Krw : Currency {
    override val value: String = "KRW"
  }
  /** 미국 달러 */
  @SerialName("USD")
  public data object Usd : Currency {
    override val value: String = "USD"
  }
  /** 일본 엔화 */
  @SerialName("JPY")
  public data object Jpy : Currency {
    override val value: String = "JPY"
  }
  /** UAE Dirham */
  @SerialName("AED")
  public data object Aed : Currency {
    override val value: String = "AED"
  }
  /** Afghani */
  @SerialName("AFN")
  public data object Afn : Currency {
    override val value: String = "AFN"
  }
  /** Lek */
  @SerialName("ALL")
  public data object All : Currency {
    override val value: String = "ALL"
  }
  /** Armenian Dram */
  @SerialName("AMD")
  public data object Amd : Currency {
    override val value: String = "AMD"
  }
  /** Netherlands Antillean Guilder */
  @SerialName("ANG")
  public data object Ang : Currency {
    override val value: String = "ANG"
  }
  /** Kwanza */
  @SerialName("AOA")
  public data object Aoa : Currency {
    override val value: String = "AOA"
  }
  /** Argentine Peso */
  @SerialName("ARS")
  public data object Ars : Currency {
    override val value: String = "ARS"
  }
  /** Australian Dollar */
  @SerialName("AUD")
  public data object Aud : Currency {
    override val value: String = "AUD"
  }
  /** Aruban Florin */
  @SerialName("AWG")
  public data object Awg : Currency {
    override val value: String = "AWG"
  }
  /** Azerbaijan Manat */
  @SerialName("AZN")
  public data object Azn : Currency {
    override val value: String = "AZN"
  }
  /** Convertible Mark */
  @SerialName("BAM")
  public data object Bam : Currency {
    override val value: String = "BAM"
  }
  /** Barbados Dollar */
  @SerialName("BBD")
  public data object Bbd : Currency {
    override val value: String = "BBD"
  }
  /** Taka */
  @SerialName("BDT")
  public data object Bdt : Currency {
    override val value: String = "BDT"
  }
  /** Bulgarian Lev */
  @SerialName("BGN")
  public data object Bgn : Currency {
    override val value: String = "BGN"
  }
  /** Bahraini Dinar */
  @SerialName("BHD")
  public data object Bhd : Currency {
    override val value: String = "BHD"
  }
  /** Burundi Franc */
  @SerialName("BIF")
  public data object Bif : Currency {
    override val value: String = "BIF"
  }
  /** Bermudian Dollar */
  @SerialName("BMD")
  public data object Bmd : Currency {
    override val value: String = "BMD"
  }
  /** Brunei Dollar */
  @SerialName("BND")
  public data object Bnd : Currency {
    override val value: String = "BND"
  }
  /** Boliviano */
  @SerialName("BOB")
  public data object Bob : Currency {
    override val value: String = "BOB"
  }
  /** Mvdol */
  @SerialName("BOV")
  public data object Bov : Currency {
    override val value: String = "BOV"
  }
  /** Brazilian Real */
  @SerialName("BRL")
  public data object Brl : Currency {
    override val value: String = "BRL"
  }
  /** Bahamian Dollar */
  @SerialName("BSD")
  public data object Bsd : Currency {
    override val value: String = "BSD"
  }
  /** Ngultrum */
  @SerialName("BTN")
  public data object Btn : Currency {
    override val value: String = "BTN"
  }
  /** Pula */
  @SerialName("BWP")
  public data object Bwp : Currency {
    override val value: String = "BWP"
  }
  /** Belarusian Ruble */
  @SerialName("BYN")
  public data object Byn : Currency {
    override val value: String = "BYN"
  }
  /** Belize Dollar */
  @SerialName("BZD")
  public data object Bzd : Currency {
    override val value: String = "BZD"
  }
  /** Canadian Dollar */
  @SerialName("CAD")
  public data object Cad : Currency {
    override val value: String = "CAD"
  }
  /** Congolese Franc */
  @SerialName("CDF")
  public data object Cdf : Currency {
    override val value: String = "CDF"
  }
  /** WIR Euro */
  @SerialName("CHE")
  public data object Che : Currency {
    override val value: String = "CHE"
  }
  /** Swiss Franc */
  @SerialName("CHF")
  public data object Chf : Currency {
    override val value: String = "CHF"
  }
  /** WIR Franc */
  @SerialName("CHW")
  public data object Chw : Currency {
    override val value: String = "CHW"
  }
  /** Unidad de Fomento */
  @SerialName("CLF")
  public data object Clf : Currency {
    override val value: String = "CLF"
  }
  /** Chilean Peso */
  @SerialName("CLP")
  public data object Clp : Currency {
    override val value: String = "CLP"
  }
  /** Yuan Renminbi */
  @SerialName("CNY")
  public data object Cny : Currency {
    override val value: String = "CNY"
  }
  /** Colombian Peso */
  @SerialName("COP")
  public data object Cop : Currency {
    override val value: String = "COP"
  }
  /** Unidad de Valor Real */
  @SerialName("COU")
  public data object Cou : Currency {
    override val value: String = "COU"
  }
  /** Costa Rican Colon */
  @SerialName("CRC")
  public data object Crc : Currency {
    override val value: String = "CRC"
  }
  /** Peso Convertible */
  @SerialName("CUC")
  public data object Cuc : Currency {
    override val value: String = "CUC"
  }
  /** Cuban Peso */
  @SerialName("CUP")
  public data object Cup : Currency {
    override val value: String = "CUP"
  }
  /** Cabo Verde Escudo */
  @SerialName("CVE")
  public data object Cve : Currency {
    override val value: String = "CVE"
  }
  /** Czech Koruna */
  @SerialName("CZK")
  public data object Czk : Currency {
    override val value: String = "CZK"
  }
  /** Djibouti Franc */
  @SerialName("DJF")
  public data object Djf : Currency {
    override val value: String = "DJF"
  }
  /** Danish Krone */
  @SerialName("DKK")
  public data object Dkk : Currency {
    override val value: String = "DKK"
  }
  /** Dominican Peso */
  @SerialName("DOP")
  public data object Dop : Currency {
    override val value: String = "DOP"
  }
  /** Algerian Dinar */
  @SerialName("DZD")
  public data object Dzd : Currency {
    override val value: String = "DZD"
  }
  /** Egyptian Pound */
  @SerialName("EGP")
  public data object Egp : Currency {
    override val value: String = "EGP"
  }
  /** Nakfa */
  @SerialName("ERN")
  public data object Ern : Currency {
    override val value: String = "ERN"
  }
  /** Ethiopian Birr */
  @SerialName("ETB")
  public data object Etb : Currency {
    override val value: String = "ETB"
  }
  /** Euro */
  @SerialName("EUR")
  public data object Eur : Currency {
    override val value: String = "EUR"
  }
  /** Fiji Dollar */
  @SerialName("FJD")
  public data object Fjd : Currency {
    override val value: String = "FJD"
  }
  /** Falkland Islands Pound */
  @SerialName("FKP")
  public data object Fkp : Currency {
    override val value: String = "FKP"
  }
  /** Pound Sterling */
  @SerialName("GBP")
  public data object Gbp : Currency {
    override val value: String = "GBP"
  }
  /** Lari */
  @SerialName("GEL")
  public data object Gel : Currency {
    override val value: String = "GEL"
  }
  /** Ghana Cedi */
  @SerialName("GHS")
  public data object Ghs : Currency {
    override val value: String = "GHS"
  }
  /** Gibraltar Pound */
  @SerialName("GIP")
  public data object Gip : Currency {
    override val value: String = "GIP"
  }
  /** Dalasi */
  @SerialName("GMD")
  public data object Gmd : Currency {
    override val value: String = "GMD"
  }
  /** Guinean Franc */
  @SerialName("GNF")
  public data object Gnf : Currency {
    override val value: String = "GNF"
  }
  /** Quetzal */
  @SerialName("GTQ")
  public data object Gtq : Currency {
    override val value: String = "GTQ"
  }
  /** Guyana Dollar */
  @SerialName("GYD")
  public data object Gyd : Currency {
    override val value: String = "GYD"
  }
  /** Hong Kong Dollar */
  @SerialName("HKD")
  public data object Hkd : Currency {
    override val value: String = "HKD"
  }
  /** Lempira */
  @SerialName("HNL")
  public data object Hnl : Currency {
    override val value: String = "HNL"
  }
  /** Kuna (Replaced by EUR) */
  @SerialName("HRK")
  public data object Hrk : Currency {
    override val value: String = "HRK"
  }
  /** Gourde */
  @SerialName("HTG")
  public data object Htg : Currency {
    override val value: String = "HTG"
  }
  /** Forint */
  @SerialName("HUF")
  public data object Huf : Currency {
    override val value: String = "HUF"
  }
  /** Rupiah */
  @SerialName("IDR")
  public data object Idr : Currency {
    override val value: String = "IDR"
  }
  /** New Israeli Sheqel */
  @SerialName("ILS")
  public data object Ils : Currency {
    override val value: String = "ILS"
  }
  /** Indian Rupee */
  @SerialName("INR")
  public data object Inr : Currency {
    override val value: String = "INR"
  }
  /** Iraqi Dinar */
  @SerialName("IQD")
  public data object Iqd : Currency {
    override val value: String = "IQD"
  }
  /** Iranian Rial */
  @SerialName("IRR")
  public data object Irr : Currency {
    override val value: String = "IRR"
  }
  /** Iceland Krona */
  @SerialName("ISK")
  public data object Isk : Currency {
    override val value: String = "ISK"
  }
  /** Jamaican Dollar */
  @SerialName("JMD")
  public data object Jmd : Currency {
    override val value: String = "JMD"
  }
  /** Jordanian Dinar */
  @SerialName("JOD")
  public data object Jod : Currency {
    override val value: String = "JOD"
  }
  /** Kenyan Shilling */
  @SerialName("KES")
  public data object Kes : Currency {
    override val value: String = "KES"
  }
  /** Som */
  @SerialName("KGS")
  public data object Kgs : Currency {
    override val value: String = "KGS"
  }
  /** Riel */
  @SerialName("KHR")
  public data object Khr : Currency {
    override val value: String = "KHR"
  }
  /** Comorian Franc */
  @SerialName("KMF")
  public data object Kmf : Currency {
    override val value: String = "KMF"
  }
  /** North Korean Won */
  @SerialName("KPW")
  public data object Kpw : Currency {
    override val value: String = "KPW"
  }
  /** Kuwaiti Dinar */
  @SerialName("KWD")
  public data object Kwd : Currency {
    override val value: String = "KWD"
  }
  /** Cayman Islands Dollar */
  @SerialName("KYD")
  public data object Kyd : Currency {
    override val value: String = "KYD"
  }
  /** Tenge */
  @SerialName("KZT")
  public data object Kzt : Currency {
    override val value: String = "KZT"
  }
  /** Lao Kip */
  @SerialName("LAK")
  public data object Lak : Currency {
    override val value: String = "LAK"
  }
  /** Lebanese Pound */
  @SerialName("LBP")
  public data object Lbp : Currency {
    override val value: String = "LBP"
  }
  /** Sri Lanka Rupee */
  @SerialName("LKR")
  public data object Lkr : Currency {
    override val value: String = "LKR"
  }
  /** Liberian Dollar */
  @SerialName("LRD")
  public data object Lrd : Currency {
    override val value: String = "LRD"
  }
  /** Loti */
  @SerialName("LSL")
  public data object Lsl : Currency {
    override val value: String = "LSL"
  }
  /** Libyan Dinar */
  @SerialName("LYD")
  public data object Lyd : Currency {
    override val value: String = "LYD"
  }
  /** Moroccan Dirham */
  @SerialName("MAD")
  public data object Mad : Currency {
    override val value: String = "MAD"
  }
  /** Moldovan Leu */
  @SerialName("MDL")
  public data object Mdl : Currency {
    override val value: String = "MDL"
  }
  /** Malagasy Ariary */
  @SerialName("MGA")
  public data object Mga : Currency {
    override val value: String = "MGA"
  }
  /** Denar */
  @SerialName("MKD")
  public data object Mkd : Currency {
    override val value: String = "MKD"
  }
  /** Kyat */
  @SerialName("MMK")
  public data object Mmk : Currency {
    override val value: String = "MMK"
  }
  /** Tugrik */
  @SerialName("MNT")
  public data object Mnt : Currency {
    override val value: String = "MNT"
  }
  /** Pataca */
  @SerialName("MOP")
  public data object Mop : Currency {
    override val value: String = "MOP"
  }
  /** Ouguiya */
  @SerialName("MRU")
  public data object Mru : Currency {
    override val value: String = "MRU"
  }
  /** Mauritius Rupee */
  @SerialName("MUR")
  public data object Mur : Currency {
    override val value: String = "MUR"
  }
  /** Rufiyaa */
  @SerialName("MVR")
  public data object Mvr : Currency {
    override val value: String = "MVR"
  }
  /** Malawi Kwacha */
  @SerialName("MWK")
  public data object Mwk : Currency {
    override val value: String = "MWK"
  }
  /** Mexican Peso */
  @SerialName("MXN")
  public data object Mxn : Currency {
    override val value: String = "MXN"
  }
  /** Mexican Unidad de Inversion (UDI) */
  @SerialName("MXV")
  public data object Mxv : Currency {
    override val value: String = "MXV"
  }
  /** Malaysian Ringgit */
  @SerialName("MYR")
  public data object Myr : Currency {
    override val value: String = "MYR"
  }
  /** Mozambique Metical */
  @SerialName("MZN")
  public data object Mzn : Currency {
    override val value: String = "MZN"
  }
  /** Namibia Dollar */
  @SerialName("NAD")
  public data object Nad : Currency {
    override val value: String = "NAD"
  }
  /** Naira */
  @SerialName("NGN")
  public data object Ngn : Currency {
    override val value: String = "NGN"
  }
  /** Cordoba Oro */
  @SerialName("NIO")
  public data object Nio : Currency {
    override val value: String = "NIO"
  }
  /** Norwegian Krone */
  @SerialName("NOK")
  public data object Nok : Currency {
    override val value: String = "NOK"
  }
  /** Nepalese Rupee */
  @SerialName("NPR")
  public data object Npr : Currency {
    override val value: String = "NPR"
  }
  /** New Zealand Dollar */
  @SerialName("NZD")
  public data object Nzd : Currency {
    override val value: String = "NZD"
  }
  /** Rial Omani */
  @SerialName("OMR")
  public data object Omr : Currency {
    override val value: String = "OMR"
  }
  /** Balboa */
  @SerialName("PAB")
  public data object Pab : Currency {
    override val value: String = "PAB"
  }
  /** Sol */
  @SerialName("PEN")
  public data object Pen : Currency {
    override val value: String = "PEN"
  }
  /** Kina */
  @SerialName("PGK")
  public data object Pgk : Currency {
    override val value: String = "PGK"
  }
  /** Philippine Peso */
  @SerialName("PHP")
  public data object Php : Currency {
    override val value: String = "PHP"
  }
  /** Pakistan Rupee */
  @SerialName("PKR")
  public data object Pkr : Currency {
    override val value: String = "PKR"
  }
  /** Zloty */
  @SerialName("PLN")
  public data object Pln : Currency {
    override val value: String = "PLN"
  }
  /** Guarani */
  @SerialName("PYG")
  public data object Pyg : Currency {
    override val value: String = "PYG"
  }
  /** Qatari Rial */
  @SerialName("QAR")
  public data object Qar : Currency {
    override val value: String = "QAR"
  }
  /** Romanian Leu */
  @SerialName("RON")
  public data object Ron : Currency {
    override val value: String = "RON"
  }
  /** Serbian Dinar */
  @SerialName("RSD")
  public data object Rsd : Currency {
    override val value: String = "RSD"
  }
  /** Russian Ruble */
  @SerialName("RUB")
  public data object Rub : Currency {
    override val value: String = "RUB"
  }
  /** Rwanda Franc */
  @SerialName("RWF")
  public data object Rwf : Currency {
    override val value: String = "RWF"
  }
  /** Saudi Riyal */
  @SerialName("SAR")
  public data object Sar : Currency {
    override val value: String = "SAR"
  }
  /** Solomon Islands Dollar */
  @SerialName("SBD")
  public data object Sbd : Currency {
    override val value: String = "SBD"
  }
  /** Seychelles Rupee */
  @SerialName("SCR")
  public data object Scr : Currency {
    override val value: String = "SCR"
  }
  /** Sudanese Pound */
  @SerialName("SDG")
  public data object Sdg : Currency {
    override val value: String = "SDG"
  }
  /** Swedish Krona */
  @SerialName("SEK")
  public data object Sek : Currency {
    override val value: String = "SEK"
  }
  /** Singapore Dollar */
  @SerialName("SGD")
  public data object Sgd : Currency {
    override val value: String = "SGD"
  }
  /** Saint Helena Pound */
  @SerialName("SHP")
  public data object Shp : Currency {
    override val value: String = "SHP"
  }
  /** Leone */
  @SerialName("SLE")
  public data object Sle : Currency {
    override val value: String = "SLE"
  }
  /** Leone */
  @SerialName("SLL")
  public data object Sll : Currency {
    override val value: String = "SLL"
  }
  /** Somali Shilling */
  @SerialName("SOS")
  public data object Sos : Currency {
    override val value: String = "SOS"
  }
  /** Surinam Dollar */
  @SerialName("SRD")
  public data object Srd : Currency {
    override val value: String = "SRD"
  }
  /** South Sudanese Pound */
  @SerialName("SSP")
  public data object Ssp : Currency {
    override val value: String = "SSP"
  }
  /** Dobra */
  @SerialName("STN")
  public data object Stn : Currency {
    override val value: String = "STN"
  }
  /** El Salvador Colon */
  @SerialName("SVC")
  public data object Svc : Currency {
    override val value: String = "SVC"
  }
  /** Syrian Pound */
  @SerialName("SYP")
  public data object Syp : Currency {
    override val value: String = "SYP"
  }
  /** Lilangeni */
  @SerialName("SZL")
  public data object Szl : Currency {
    override val value: String = "SZL"
  }
  /** Baht */
  @SerialName("THB")
  public data object Thb : Currency {
    override val value: String = "THB"
  }
  /** Somoni */
  @SerialName("TJS")
  public data object Tjs : Currency {
    override val value: String = "TJS"
  }
  /** Turkmenistan New Manat */
  @SerialName("TMT")
  public data object Tmt : Currency {
    override val value: String = "TMT"
  }
  /** Tunisian Dinar */
  @SerialName("TND")
  public data object Tnd : Currency {
    override val value: String = "TND"
  }
  /** Pa’anga */
  @SerialName("TOP")
  public data object Top : Currency {
    override val value: String = "TOP"
  }
  /** Turkish Lira */
  @SerialName("TRY")
  public data object Try : Currency {
    override val value: String = "TRY"
  }
  /** Trinidad and Tobago Dollar */
  @SerialName("TTD")
  public data object Ttd : Currency {
    override val value: String = "TTD"
  }
  /** New Taiwan Dollar */
  @SerialName("TWD")
  public data object Twd : Currency {
    override val value: String = "TWD"
  }
  /** Tanzanian Shilling */
  @SerialName("TZS")
  public data object Tzs : Currency {
    override val value: String = "TZS"
  }
  /** Hryvnia */
  @SerialName("UAH")
  public data object Uah : Currency {
    override val value: String = "UAH"
  }
  /** Uganda Shilling */
  @SerialName("UGX")
  public data object Ugx : Currency {
    override val value: String = "UGX"
  }
  /** US Dollar (Next day) */
  @SerialName("USN")
  public data object Usn : Currency {
    override val value: String = "USN"
  }
  /** Uruguay Peso en Unidades Indexadas (UI) */
  @SerialName("UYI")
  public data object Uyi : Currency {
    override val value: String = "UYI"
  }
  /** Peso Uruguayo */
  @SerialName("UYU")
  public data object Uyu : Currency {
    override val value: String = "UYU"
  }
  /** Unidad Previsional */
  @SerialName("UYW")
  public data object Uyw : Currency {
    override val value: String = "UYW"
  }
  /** Uzbekistan Sum */
  @SerialName("UZS")
  public data object Uzs : Currency {
    override val value: String = "UZS"
  }
  /** Bolívar Soberano */
  @SerialName("VED")
  public data object Ved : Currency {
    override val value: String = "VED"
  }
  /** Bolívar Soberano */
  @SerialName("VES")
  public data object Ves : Currency {
    override val value: String = "VES"
  }
  /** Dong */
  @SerialName("VND")
  public data object Vnd : Currency {
    override val value: String = "VND"
  }
  /** Vatu */
  @SerialName("VUV")
  public data object Vuv : Currency {
    override val value: String = "VUV"
  }
  /** Tala */
  @SerialName("WST")
  public data object Wst : Currency {
    override val value: String = "WST"
  }
  /** CFA Franc BEAC */
  @SerialName("XAF")
  public data object Xaf : Currency {
    override val value: String = "XAF"
  }
  /** Silver */
  @SerialName("XAG")
  public data object Xag : Currency {
    override val value: String = "XAG"
  }
  /** Gold */
  @SerialName("XAU")
  public data object Xau : Currency {
    override val value: String = "XAU"
  }
  /** Bond Markets Unit European Composite Unit (EURCO) */
  @SerialName("XBA")
  public data object Xba : Currency {
    override val value: String = "XBA"
  }
  /** Bond Markets Unit European Monetary Unit (E.M.U.-6) */
  @SerialName("XBB")
  public data object Xbb : Currency {
    override val value: String = "XBB"
  }
  /** Bond Markets Unit European Unit of Account 9 (E.U.A.-9) */
  @SerialName("XBC")
  public data object Xbc : Currency {
    override val value: String = "XBC"
  }
  /** Bond Markets Unit European Unit of Account 17 (E.U.A.-17) */
  @SerialName("XBD")
  public data object Xbd : Currency {
    override val value: String = "XBD"
  }
  /** East Caribbean Dollar */
  @SerialName("XCD")
  public data object Xcd : Currency {
    override val value: String = "XCD"
  }
  /** SDR (Special Drawing Right) */
  @SerialName("XDR")
  public data object Xdr : Currency {
    override val value: String = "XDR"
  }
  /** CFA Franc BCEAO */
  @SerialName("XOF")
  public data object Xof : Currency {
    override val value: String = "XOF"
  }
  /** Palladium */
  @SerialName("XPD")
  public data object Xpd : Currency {
    override val value: String = "XPD"
  }
  /** CFP Franc */
  @SerialName("XPF")
  public data object Xpf : Currency {
    override val value: String = "XPF"
  }
  /** Platinum */
  @SerialName("XPT")
  public data object Xpt : Currency {
    override val value: String = "XPT"
  }
  /** Sucre */
  @SerialName("XSU")
  public data object Xsu : Currency {
    override val value: String = "XSU"
  }
  /** Codes specifically reserved for testing purposes */
  @SerialName("XTS")
  public data object Xts : Currency {
    override val value: String = "XTS"
  }
  /** ADB Unit of Account */
  @SerialName("XUA")
  public data object Xua : Currency {
    override val value: String = "XUA"
  }
  /** The codes assigned for transactions where no currency is involved */
  @SerialName("XXX")
  public data object Xxx : Currency {
    override val value: String = "XXX"
  }
  /** Yemeni Rial */
  @SerialName("YER")
  public data object Yer : Currency {
    override val value: String = "YER"
  }
  /** Rand */
  @SerialName("ZAR")
  public data object Zar : Currency {
    override val value: String = "ZAR"
  }
  /** Zambian Kwacha */
  @SerialName("ZMW")
  public data object Zmw : Currency {
    override val value: String = "ZMW"
  }
  /** Zimbabwe Dollar */
  @SerialName("ZWL")
  public data object Zwl : Currency {
    override val value: String = "ZWL"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Currency
}
