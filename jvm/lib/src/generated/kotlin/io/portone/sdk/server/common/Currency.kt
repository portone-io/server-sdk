package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 통화 단위 */
@Serializable
public sealed class Currency {
  /** 대한민국 원화 */
  @SerialName("KRW")
  public data object Krw : Currency()
  /** 미국 달러 */
  @SerialName("USD")
  public data object Usd : Currency()
  /** 일본 엔화 */
  @SerialName("JPY")
  public data object Jpy : Currency()
  /** UAE Dirham */
  @SerialName("AED")
  public data object Aed : Currency()
  /** Afghani */
  @SerialName("AFN")
  public data object Afn : Currency()
  /** Lek */
  @SerialName("ALL")
  public data object All : Currency()
  /** Armenian Dram */
  @SerialName("AMD")
  public data object Amd : Currency()
  /** Netherlands Antillean Guilder */
  @SerialName("ANG")
  public data object Ang : Currency()
  /** Kwanza */
  @SerialName("AOA")
  public data object Aoa : Currency()
  /** Argentine Peso */
  @SerialName("ARS")
  public data object Ars : Currency()
  /** Australian Dollar */
  @SerialName("AUD")
  public data object Aud : Currency()
  /** Aruban Florin */
  @SerialName("AWG")
  public data object Awg : Currency()
  /** Azerbaijan Manat */
  @SerialName("AZN")
  public data object Azn : Currency()
  /** Convertible Mark */
  @SerialName("BAM")
  public data object Bam : Currency()
  /** Barbados Dollar */
  @SerialName("BBD")
  public data object Bbd : Currency()
  /** Taka */
  @SerialName("BDT")
  public data object Bdt : Currency()
  /** Bulgarian Lev */
  @SerialName("BGN")
  public data object Bgn : Currency()
  /** Bahraini Dinar */
  @SerialName("BHD")
  public data object Bhd : Currency()
  /** Burundi Franc */
  @SerialName("BIF")
  public data object Bif : Currency()
  /** Bermudian Dollar */
  @SerialName("BMD")
  public data object Bmd : Currency()
  /** Brunei Dollar */
  @SerialName("BND")
  public data object Bnd : Currency()
  /** Boliviano */
  @SerialName("BOB")
  public data object Bob : Currency()
  /** Mvdol */
  @SerialName("BOV")
  public data object Bov : Currency()
  /** Brazilian Real */
  @SerialName("BRL")
  public data object Brl : Currency()
  /** Bahamian Dollar */
  @SerialName("BSD")
  public data object Bsd : Currency()
  /** Ngultrum */
  @SerialName("BTN")
  public data object Btn : Currency()
  /** Pula */
  @SerialName("BWP")
  public data object Bwp : Currency()
  /** Belarusian Ruble */
  @SerialName("BYN")
  public data object Byn : Currency()
  /** Belize Dollar */
  @SerialName("BZD")
  public data object Bzd : Currency()
  /** Canadian Dollar */
  @SerialName("CAD")
  public data object Cad : Currency()
  /** Congolese Franc */
  @SerialName("CDF")
  public data object Cdf : Currency()
  /** WIR Euro */
  @SerialName("CHE")
  public data object Che : Currency()
  /** Swiss Franc */
  @SerialName("CHF")
  public data object Chf : Currency()
  /** WIR Franc */
  @SerialName("CHW")
  public data object Chw : Currency()
  /** Unidad de Fomento */
  @SerialName("CLF")
  public data object Clf : Currency()
  /** Chilean Peso */
  @SerialName("CLP")
  public data object Clp : Currency()
  /** Yuan Renminbi */
  @SerialName("CNY")
  public data object Cny : Currency()
  /** Colombian Peso */
  @SerialName("COP")
  public data object Cop : Currency()
  /** Unidad de Valor Real */
  @SerialName("COU")
  public data object Cou : Currency()
  /** Costa Rican Colon */
  @SerialName("CRC")
  public data object Crc : Currency()
  /** Peso Convertible */
  @SerialName("CUC")
  public data object Cuc : Currency()
  /** Cuban Peso */
  @SerialName("CUP")
  public data object Cup : Currency()
  /** Cabo Verde Escudo */
  @SerialName("CVE")
  public data object Cve : Currency()
  /** Czech Koruna */
  @SerialName("CZK")
  public data object Czk : Currency()
  /** Djibouti Franc */
  @SerialName("DJF")
  public data object Djf : Currency()
  /** Danish Krone */
  @SerialName("DKK")
  public data object Dkk : Currency()
  /** Dominican Peso */
  @SerialName("DOP")
  public data object Dop : Currency()
  /** Algerian Dinar */
  @SerialName("DZD")
  public data object Dzd : Currency()
  /** Egyptian Pound */
  @SerialName("EGP")
  public data object Egp : Currency()
  /** Nakfa */
  @SerialName("ERN")
  public data object Ern : Currency()
  /** Ethiopian Birr */
  @SerialName("ETB")
  public data object Etb : Currency()
  /** Euro */
  @SerialName("EUR")
  public data object Eur : Currency()
  /** Fiji Dollar */
  @SerialName("FJD")
  public data object Fjd : Currency()
  /** Falkland Islands Pound */
  @SerialName("FKP")
  public data object Fkp : Currency()
  /** Pound Sterling */
  @SerialName("GBP")
  public data object Gbp : Currency()
  /** Lari */
  @SerialName("GEL")
  public data object Gel : Currency()
  /** Ghana Cedi */
  @SerialName("GHS")
  public data object Ghs : Currency()
  /** Gibraltar Pound */
  @SerialName("GIP")
  public data object Gip : Currency()
  /** Dalasi */
  @SerialName("GMD")
  public data object Gmd : Currency()
  /** Guinean Franc */
  @SerialName("GNF")
  public data object Gnf : Currency()
  /** Quetzal */
  @SerialName("GTQ")
  public data object Gtq : Currency()
  /** Guyana Dollar */
  @SerialName("GYD")
  public data object Gyd : Currency()
  /** Hong Kong Dollar */
  @SerialName("HKD")
  public data object Hkd : Currency()
  /** Lempira */
  @SerialName("HNL")
  public data object Hnl : Currency()
  /** Kuna (Replaced by EUR) */
  @SerialName("HRK")
  public data object Hrk : Currency()
  /** Gourde */
  @SerialName("HTG")
  public data object Htg : Currency()
  /** Forint */
  @SerialName("HUF")
  public data object Huf : Currency()
  /** Rupiah */
  @SerialName("IDR")
  public data object Idr : Currency()
  /** New Israeli Sheqel */
  @SerialName("ILS")
  public data object Ils : Currency()
  /** Indian Rupee */
  @SerialName("INR")
  public data object Inr : Currency()
  /** Iraqi Dinar */
  @SerialName("IQD")
  public data object Iqd : Currency()
  /** Iranian Rial */
  @SerialName("IRR")
  public data object Irr : Currency()
  /** Iceland Krona */
  @SerialName("ISK")
  public data object Isk : Currency()
  /** Jamaican Dollar */
  @SerialName("JMD")
  public data object Jmd : Currency()
  /** Jordanian Dinar */
  @SerialName("JOD")
  public data object Jod : Currency()
  /** Kenyan Shilling */
  @SerialName("KES")
  public data object Kes : Currency()
  /** Som */
  @SerialName("KGS")
  public data object Kgs : Currency()
  /** Riel */
  @SerialName("KHR")
  public data object Khr : Currency()
  /** Comorian Franc */
  @SerialName("KMF")
  public data object Kmf : Currency()
  /** North Korean Won */
  @SerialName("KPW")
  public data object Kpw : Currency()
  /** Kuwaiti Dinar */
  @SerialName("KWD")
  public data object Kwd : Currency()
  /** Cayman Islands Dollar */
  @SerialName("KYD")
  public data object Kyd : Currency()
  /** Tenge */
  @SerialName("KZT")
  public data object Kzt : Currency()
  /** Lao Kip */
  @SerialName("LAK")
  public data object Lak : Currency()
  /** Lebanese Pound */
  @SerialName("LBP")
  public data object Lbp : Currency()
  /** Sri Lanka Rupee */
  @SerialName("LKR")
  public data object Lkr : Currency()
  /** Liberian Dollar */
  @SerialName("LRD")
  public data object Lrd : Currency()
  /** Loti */
  @SerialName("LSL")
  public data object Lsl : Currency()
  /** Libyan Dinar */
  @SerialName("LYD")
  public data object Lyd : Currency()
  /** Moroccan Dirham */
  @SerialName("MAD")
  public data object Mad : Currency()
  /** Moldovan Leu */
  @SerialName("MDL")
  public data object Mdl : Currency()
  /** Malagasy Ariary */
  @SerialName("MGA")
  public data object Mga : Currency()
  /** Denar */
  @SerialName("MKD")
  public data object Mkd : Currency()
  /** Kyat */
  @SerialName("MMK")
  public data object Mmk : Currency()
  /** Tugrik */
  @SerialName("MNT")
  public data object Mnt : Currency()
  /** Pataca */
  @SerialName("MOP")
  public data object Mop : Currency()
  /** Ouguiya */
  @SerialName("MRU")
  public data object Mru : Currency()
  /** Mauritius Rupee */
  @SerialName("MUR")
  public data object Mur : Currency()
  /** Rufiyaa */
  @SerialName("MVR")
  public data object Mvr : Currency()
  /** Malawi Kwacha */
  @SerialName("MWK")
  public data object Mwk : Currency()
  /** Mexican Peso */
  @SerialName("MXN")
  public data object Mxn : Currency()
  /** Mexican Unidad de Inversion (UDI) */
  @SerialName("MXV")
  public data object Mxv : Currency()
  /** Malaysian Ringgit */
  @SerialName("MYR")
  public data object Myr : Currency()
  /** Mozambique Metical */
  @SerialName("MZN")
  public data object Mzn : Currency()
  /** Namibia Dollar */
  @SerialName("NAD")
  public data object Nad : Currency()
  /** Naira */
  @SerialName("NGN")
  public data object Ngn : Currency()
  /** Cordoba Oro */
  @SerialName("NIO")
  public data object Nio : Currency()
  /** Norwegian Krone */
  @SerialName("NOK")
  public data object Nok : Currency()
  /** Nepalese Rupee */
  @SerialName("NPR")
  public data object Npr : Currency()
  /** New Zealand Dollar */
  @SerialName("NZD")
  public data object Nzd : Currency()
  /** Rial Omani */
  @SerialName("OMR")
  public data object Omr : Currency()
  /** Balboa */
  @SerialName("PAB")
  public data object Pab : Currency()
  /** Sol */
  @SerialName("PEN")
  public data object Pen : Currency()
  /** Kina */
  @SerialName("PGK")
  public data object Pgk : Currency()
  /** Philippine Peso */
  @SerialName("PHP")
  public data object Php : Currency()
  /** Pakistan Rupee */
  @SerialName("PKR")
  public data object Pkr : Currency()
  /** Zloty */
  @SerialName("PLN")
  public data object Pln : Currency()
  /** Guarani */
  @SerialName("PYG")
  public data object Pyg : Currency()
  /** Qatari Rial */
  @SerialName("QAR")
  public data object Qar : Currency()
  /** Romanian Leu */
  @SerialName("RON")
  public data object Ron : Currency()
  /** Serbian Dinar */
  @SerialName("RSD")
  public data object Rsd : Currency()
  /** Russian Ruble */
  @SerialName("RUB")
  public data object Rub : Currency()
  /** Rwanda Franc */
  @SerialName("RWF")
  public data object Rwf : Currency()
  /** Saudi Riyal */
  @SerialName("SAR")
  public data object Sar : Currency()
  /** Solomon Islands Dollar */
  @SerialName("SBD")
  public data object Sbd : Currency()
  /** Seychelles Rupee */
  @SerialName("SCR")
  public data object Scr : Currency()
  /** Sudanese Pound */
  @SerialName("SDG")
  public data object Sdg : Currency()
  /** Swedish Krona */
  @SerialName("SEK")
  public data object Sek : Currency()
  /** Singapore Dollar */
  @SerialName("SGD")
  public data object Sgd : Currency()
  /** Saint Helena Pound */
  @SerialName("SHP")
  public data object Shp : Currency()
  /** Leone */
  @SerialName("SLE")
  public data object Sle : Currency()
  /** Leone */
  @SerialName("SLL")
  public data object Sll : Currency()
  /** Somali Shilling */
  @SerialName("SOS")
  public data object Sos : Currency()
  /** Surinam Dollar */
  @SerialName("SRD")
  public data object Srd : Currency()
  /** South Sudanese Pound */
  @SerialName("SSP")
  public data object Ssp : Currency()
  /** Dobra */
  @SerialName("STN")
  public data object Stn : Currency()
  /** El Salvador Colon */
  @SerialName("SVC")
  public data object Svc : Currency()
  /** Syrian Pound */
  @SerialName("SYP")
  public data object Syp : Currency()
  /** Lilangeni */
  @SerialName("SZL")
  public data object Szl : Currency()
  /** Baht */
  @SerialName("THB")
  public data object Thb : Currency()
  /** Somoni */
  @SerialName("TJS")
  public data object Tjs : Currency()
  /** Turkmenistan New Manat */
  @SerialName("TMT")
  public data object Tmt : Currency()
  /** Tunisian Dinar */
  @SerialName("TND")
  public data object Tnd : Currency()
  /** Pa’anga */
  @SerialName("TOP")
  public data object Top : Currency()
  /** Turkish Lira */
  @SerialName("TRY")
  public data object Try : Currency()
  /** Trinidad and Tobago Dollar */
  @SerialName("TTD")
  public data object Ttd : Currency()
  /** New Taiwan Dollar */
  @SerialName("TWD")
  public data object Twd : Currency()
  /** Tanzanian Shilling */
  @SerialName("TZS")
  public data object Tzs : Currency()
  /** Hryvnia */
  @SerialName("UAH")
  public data object Uah : Currency()
  /** Uganda Shilling */
  @SerialName("UGX")
  public data object Ugx : Currency()
  /** US Dollar (Next day) */
  @SerialName("USN")
  public data object Usn : Currency()
  /** Uruguay Peso en Unidades Indexadas (UI) */
  @SerialName("UYI")
  public data object Uyi : Currency()
  /** Peso Uruguayo */
  @SerialName("UYU")
  public data object Uyu : Currency()
  /** Unidad Previsional */
  @SerialName("UYW")
  public data object Uyw : Currency()
  /** Uzbekistan Sum */
  @SerialName("UZS")
  public data object Uzs : Currency()
  /** Bolívar Soberano */
  @SerialName("VED")
  public data object Ved : Currency()
  /** Bolívar Soberano */
  @SerialName("VES")
  public data object Ves : Currency()
  /** Dong */
  @SerialName("VND")
  public data object Vnd : Currency()
  /** Vatu */
  @SerialName("VUV")
  public data object Vuv : Currency()
  /** Tala */
  @SerialName("WST")
  public data object Wst : Currency()
  /** CFA Franc BEAC */
  @SerialName("XAF")
  public data object Xaf : Currency()
  /** Silver */
  @SerialName("XAG")
  public data object Xag : Currency()
  /** Gold */
  @SerialName("XAU")
  public data object Xau : Currency()
  /** Bond Markets Unit European Composite Unit (EURCO) */
  @SerialName("XBA")
  public data object Xba : Currency()
  /** Bond Markets Unit European Monetary Unit (E.M.U.-6) */
  @SerialName("XBB")
  public data object Xbb : Currency()
  /** Bond Markets Unit European Unit of Account 9 (E.U.A.-9) */
  @SerialName("XBC")
  public data object Xbc : Currency()
  /** Bond Markets Unit European Unit of Account 17 (E.U.A.-17) */
  @SerialName("XBD")
  public data object Xbd : Currency()
  /** East Caribbean Dollar */
  @SerialName("XCD")
  public data object Xcd : Currency()
  /** SDR (Special Drawing Right) */
  @SerialName("XDR")
  public data object Xdr : Currency()
  /** CFA Franc BCEAO */
  @SerialName("XOF")
  public data object Xof : Currency()
  /** Palladium */
  @SerialName("XPD")
  public data object Xpd : Currency()
  /** CFP Franc */
  @SerialName("XPF")
  public data object Xpf : Currency()
  /** Platinum */
  @SerialName("XPT")
  public data object Xpt : Currency()
  /** Sucre */
  @SerialName("XSU")
  public data object Xsu : Currency()
  /** Codes specifically reserved for testing purposes */
  @SerialName("XTS")
  public data object Xts : Currency()
  /** ADB Unit of Account */
  @SerialName("XUA")
  public data object Xua : Currency()
  /** The codes assigned for transactions where no currency is involved */
  @SerialName("XXX")
  public data object Xxx : Currency()
  /** Yemeni Rial */
  @SerialName("YER")
  public data object Yer : Currency()
  /** Rand */
  @SerialName("ZAR")
  public data object Zar : Currency()
  /** Zambian Kwacha */
  @SerialName("ZMW")
  public data object Zmw : Currency()
  /** Zimbabwe Dollar */
  @SerialName("ZWL")
  public data object Zwl : Currency()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : Currency()
}
