package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 통화 단위 */
@Serializable(CurrencySerializer::class)
public sealed interface Currency {
  public val value: String
  /** 대한민국 원화 */
  public data object Krw : Currency {
    override val value: String = "KRW"
  }
  /** 미국 달러 */
  public data object Usd : Currency {
    override val value: String = "USD"
  }
  /** 일본 엔화 */
  public data object Jpy : Currency {
    override val value: String = "JPY"
  }
  /** UAE Dirham */
  public data object Aed : Currency {
    override val value: String = "AED"
  }
  /** Afghani */
  public data object Afn : Currency {
    override val value: String = "AFN"
  }
  /** Lek */
  public data object All : Currency {
    override val value: String = "ALL"
  }
  /** Armenian Dram */
  public data object Amd : Currency {
    override val value: String = "AMD"
  }
  /** Netherlands Antillean Guilder */
  public data object Ang : Currency {
    override val value: String = "ANG"
  }
  /** Kwanza */
  public data object Aoa : Currency {
    override val value: String = "AOA"
  }
  /** Argentine Peso */
  public data object Ars : Currency {
    override val value: String = "ARS"
  }
  /** Australian Dollar */
  public data object Aud : Currency {
    override val value: String = "AUD"
  }
  /** Aruban Florin */
  public data object Awg : Currency {
    override val value: String = "AWG"
  }
  /** Azerbaijan Manat */
  public data object Azn : Currency {
    override val value: String = "AZN"
  }
  /** Convertible Mark */
  public data object Bam : Currency {
    override val value: String = "BAM"
  }
  /** Barbados Dollar */
  public data object Bbd : Currency {
    override val value: String = "BBD"
  }
  /** Taka */
  public data object Bdt : Currency {
    override val value: String = "BDT"
  }
  /** Bulgarian Lev */
  public data object Bgn : Currency {
    override val value: String = "BGN"
  }
  /** Bahraini Dinar */
  public data object Bhd : Currency {
    override val value: String = "BHD"
  }
  /** Burundi Franc */
  public data object Bif : Currency {
    override val value: String = "BIF"
  }
  /** Bermudian Dollar */
  public data object Bmd : Currency {
    override val value: String = "BMD"
  }
  /** Brunei Dollar */
  public data object Bnd : Currency {
    override val value: String = "BND"
  }
  /** Boliviano */
  public data object Bob : Currency {
    override val value: String = "BOB"
  }
  /** Mvdol */
  public data object Bov : Currency {
    override val value: String = "BOV"
  }
  /** Brazilian Real */
  public data object Brl : Currency {
    override val value: String = "BRL"
  }
  /** Bahamian Dollar */
  public data object Bsd : Currency {
    override val value: String = "BSD"
  }
  /** Ngultrum */
  public data object Btn : Currency {
    override val value: String = "BTN"
  }
  /** Pula */
  public data object Bwp : Currency {
    override val value: String = "BWP"
  }
  /** Belarusian Ruble */
  public data object Byn : Currency {
    override val value: String = "BYN"
  }
  /** Belize Dollar */
  public data object Bzd : Currency {
    override val value: String = "BZD"
  }
  /** Canadian Dollar */
  public data object Cad : Currency {
    override val value: String = "CAD"
  }
  /** Congolese Franc */
  public data object Cdf : Currency {
    override val value: String = "CDF"
  }
  /** WIR Euro */
  public data object Che : Currency {
    override val value: String = "CHE"
  }
  /** Swiss Franc */
  public data object Chf : Currency {
    override val value: String = "CHF"
  }
  /** WIR Franc */
  public data object Chw : Currency {
    override val value: String = "CHW"
  }
  /** Unidad de Fomento */
  public data object Clf : Currency {
    override val value: String = "CLF"
  }
  /** Chilean Peso */
  public data object Clp : Currency {
    override val value: String = "CLP"
  }
  /** Yuan Renminbi */
  public data object Cny : Currency {
    override val value: String = "CNY"
  }
  /** Colombian Peso */
  public data object Cop : Currency {
    override val value: String = "COP"
  }
  /** Unidad de Valor Real */
  public data object Cou : Currency {
    override val value: String = "COU"
  }
  /** Costa Rican Colon */
  public data object Crc : Currency {
    override val value: String = "CRC"
  }
  /** Peso Convertible */
  public data object Cuc : Currency {
    override val value: String = "CUC"
  }
  /** Cuban Peso */
  public data object Cup : Currency {
    override val value: String = "CUP"
  }
  /** Cabo Verde Escudo */
  public data object Cve : Currency {
    override val value: String = "CVE"
  }
  /** Czech Koruna */
  public data object Czk : Currency {
    override val value: String = "CZK"
  }
  /** Djibouti Franc */
  public data object Djf : Currency {
    override val value: String = "DJF"
  }
  /** Danish Krone */
  public data object Dkk : Currency {
    override val value: String = "DKK"
  }
  /** Dominican Peso */
  public data object Dop : Currency {
    override val value: String = "DOP"
  }
  /** Algerian Dinar */
  public data object Dzd : Currency {
    override val value: String = "DZD"
  }
  /** Egyptian Pound */
  public data object Egp : Currency {
    override val value: String = "EGP"
  }
  /** Nakfa */
  public data object Ern : Currency {
    override val value: String = "ERN"
  }
  /** Ethiopian Birr */
  public data object Etb : Currency {
    override val value: String = "ETB"
  }
  /** Euro */
  public data object Eur : Currency {
    override val value: String = "EUR"
  }
  /** Fiji Dollar */
  public data object Fjd : Currency {
    override val value: String = "FJD"
  }
  /** Falkland Islands Pound */
  public data object Fkp : Currency {
    override val value: String = "FKP"
  }
  /** Pound Sterling */
  public data object Gbp : Currency {
    override val value: String = "GBP"
  }
  /** Lari */
  public data object Gel : Currency {
    override val value: String = "GEL"
  }
  /** Ghana Cedi */
  public data object Ghs : Currency {
    override val value: String = "GHS"
  }
  /** Gibraltar Pound */
  public data object Gip : Currency {
    override val value: String = "GIP"
  }
  /** Dalasi */
  public data object Gmd : Currency {
    override val value: String = "GMD"
  }
  /** Guinean Franc */
  public data object Gnf : Currency {
    override val value: String = "GNF"
  }
  /** Quetzal */
  public data object Gtq : Currency {
    override val value: String = "GTQ"
  }
  /** Guyana Dollar */
  public data object Gyd : Currency {
    override val value: String = "GYD"
  }
  /** Hong Kong Dollar */
  public data object Hkd : Currency {
    override val value: String = "HKD"
  }
  /** Lempira */
  public data object Hnl : Currency {
    override val value: String = "HNL"
  }
  /** Kuna (Replaced by EUR) */
  public data object Hrk : Currency {
    override val value: String = "HRK"
  }
  /** Gourde */
  public data object Htg : Currency {
    override val value: String = "HTG"
  }
  /** Forint */
  public data object Huf : Currency {
    override val value: String = "HUF"
  }
  /** Rupiah */
  public data object Idr : Currency {
    override val value: String = "IDR"
  }
  /** New Israeli Sheqel */
  public data object Ils : Currency {
    override val value: String = "ILS"
  }
  /** Indian Rupee */
  public data object Inr : Currency {
    override val value: String = "INR"
  }
  /** Iraqi Dinar */
  public data object Iqd : Currency {
    override val value: String = "IQD"
  }
  /** Iranian Rial */
  public data object Irr : Currency {
    override val value: String = "IRR"
  }
  /** Iceland Krona */
  public data object Isk : Currency {
    override val value: String = "ISK"
  }
  /** Jamaican Dollar */
  public data object Jmd : Currency {
    override val value: String = "JMD"
  }
  /** Jordanian Dinar */
  public data object Jod : Currency {
    override val value: String = "JOD"
  }
  /** Kenyan Shilling */
  public data object Kes : Currency {
    override val value: String = "KES"
  }
  /** Som */
  public data object Kgs : Currency {
    override val value: String = "KGS"
  }
  /** Riel */
  public data object Khr : Currency {
    override val value: String = "KHR"
  }
  /** Comorian Franc */
  public data object Kmf : Currency {
    override val value: String = "KMF"
  }
  /** North Korean Won */
  public data object Kpw : Currency {
    override val value: String = "KPW"
  }
  /** Kuwaiti Dinar */
  public data object Kwd : Currency {
    override val value: String = "KWD"
  }
  /** Cayman Islands Dollar */
  public data object Kyd : Currency {
    override val value: String = "KYD"
  }
  /** Tenge */
  public data object Kzt : Currency {
    override val value: String = "KZT"
  }
  /** Lao Kip */
  public data object Lak : Currency {
    override val value: String = "LAK"
  }
  /** Lebanese Pound */
  public data object Lbp : Currency {
    override val value: String = "LBP"
  }
  /** Sri Lanka Rupee */
  public data object Lkr : Currency {
    override val value: String = "LKR"
  }
  /** Liberian Dollar */
  public data object Lrd : Currency {
    override val value: String = "LRD"
  }
  /** Loti */
  public data object Lsl : Currency {
    override val value: String = "LSL"
  }
  /** Libyan Dinar */
  public data object Lyd : Currency {
    override val value: String = "LYD"
  }
  /** Moroccan Dirham */
  public data object Mad : Currency {
    override val value: String = "MAD"
  }
  /** Moldovan Leu */
  public data object Mdl : Currency {
    override val value: String = "MDL"
  }
  /** Malagasy Ariary */
  public data object Mga : Currency {
    override val value: String = "MGA"
  }
  /** Denar */
  public data object Mkd : Currency {
    override val value: String = "MKD"
  }
  /** Kyat */
  public data object Mmk : Currency {
    override val value: String = "MMK"
  }
  /** Tugrik */
  public data object Mnt : Currency {
    override val value: String = "MNT"
  }
  /** Pataca */
  public data object Mop : Currency {
    override val value: String = "MOP"
  }
  /** Ouguiya */
  public data object Mru : Currency {
    override val value: String = "MRU"
  }
  /** Mauritius Rupee */
  public data object Mur : Currency {
    override val value: String = "MUR"
  }
  /** Rufiyaa */
  public data object Mvr : Currency {
    override val value: String = "MVR"
  }
  /** Malawi Kwacha */
  public data object Mwk : Currency {
    override val value: String = "MWK"
  }
  /** Mexican Peso */
  public data object Mxn : Currency {
    override val value: String = "MXN"
  }
  /** Mexican Unidad de Inversion (UDI) */
  public data object Mxv : Currency {
    override val value: String = "MXV"
  }
  /** Malaysian Ringgit */
  public data object Myr : Currency {
    override val value: String = "MYR"
  }
  /** Mozambique Metical */
  public data object Mzn : Currency {
    override val value: String = "MZN"
  }
  /** Namibia Dollar */
  public data object Nad : Currency {
    override val value: String = "NAD"
  }
  /** Naira */
  public data object Ngn : Currency {
    override val value: String = "NGN"
  }
  /** Cordoba Oro */
  public data object Nio : Currency {
    override val value: String = "NIO"
  }
  /** Norwegian Krone */
  public data object Nok : Currency {
    override val value: String = "NOK"
  }
  /** Nepalese Rupee */
  public data object Npr : Currency {
    override val value: String = "NPR"
  }
  /** New Zealand Dollar */
  public data object Nzd : Currency {
    override val value: String = "NZD"
  }
  /** Rial Omani */
  public data object Omr : Currency {
    override val value: String = "OMR"
  }
  /** Balboa */
  public data object Pab : Currency {
    override val value: String = "PAB"
  }
  /** Sol */
  public data object Pen : Currency {
    override val value: String = "PEN"
  }
  /** Kina */
  public data object Pgk : Currency {
    override val value: String = "PGK"
  }
  /** Philippine Peso */
  public data object Php : Currency {
    override val value: String = "PHP"
  }
  /** Pakistan Rupee */
  public data object Pkr : Currency {
    override val value: String = "PKR"
  }
  /** Zloty */
  public data object Pln : Currency {
    override val value: String = "PLN"
  }
  /** Guarani */
  public data object Pyg : Currency {
    override val value: String = "PYG"
  }
  /** Qatari Rial */
  public data object Qar : Currency {
    override val value: String = "QAR"
  }
  /** Romanian Leu */
  public data object Ron : Currency {
    override val value: String = "RON"
  }
  /** Serbian Dinar */
  public data object Rsd : Currency {
    override val value: String = "RSD"
  }
  /** Russian Ruble */
  public data object Rub : Currency {
    override val value: String = "RUB"
  }
  /** Rwanda Franc */
  public data object Rwf : Currency {
    override val value: String = "RWF"
  }
  /** Saudi Riyal */
  public data object Sar : Currency {
    override val value: String = "SAR"
  }
  /** Solomon Islands Dollar */
  public data object Sbd : Currency {
    override val value: String = "SBD"
  }
  /** Seychelles Rupee */
  public data object Scr : Currency {
    override val value: String = "SCR"
  }
  /** Sudanese Pound */
  public data object Sdg : Currency {
    override val value: String = "SDG"
  }
  /** Swedish Krona */
  public data object Sek : Currency {
    override val value: String = "SEK"
  }
  /** Singapore Dollar */
  public data object Sgd : Currency {
    override val value: String = "SGD"
  }
  /** Saint Helena Pound */
  public data object Shp : Currency {
    override val value: String = "SHP"
  }
  /** Leone */
  public data object Sle : Currency {
    override val value: String = "SLE"
  }
  /** Leone */
  public data object Sll : Currency {
    override val value: String = "SLL"
  }
  /** Somali Shilling */
  public data object Sos : Currency {
    override val value: String = "SOS"
  }
  /** Surinam Dollar */
  public data object Srd : Currency {
    override val value: String = "SRD"
  }
  /** South Sudanese Pound */
  public data object Ssp : Currency {
    override val value: String = "SSP"
  }
  /** Dobra */
  public data object Stn : Currency {
    override val value: String = "STN"
  }
  /** El Salvador Colon */
  public data object Svc : Currency {
    override val value: String = "SVC"
  }
  /** Syrian Pound */
  public data object Syp : Currency {
    override val value: String = "SYP"
  }
  /** Lilangeni */
  public data object Szl : Currency {
    override val value: String = "SZL"
  }
  /** Baht */
  public data object Thb : Currency {
    override val value: String = "THB"
  }
  /** Somoni */
  public data object Tjs : Currency {
    override val value: String = "TJS"
  }
  /** Turkmenistan New Manat */
  public data object Tmt : Currency {
    override val value: String = "TMT"
  }
  /** Tunisian Dinar */
  public data object Tnd : Currency {
    override val value: String = "TND"
  }
  /** Pa’anga */
  public data object Top : Currency {
    override val value: String = "TOP"
  }
  /** Turkish Lira */
  public data object Try : Currency {
    override val value: String = "TRY"
  }
  /** Trinidad and Tobago Dollar */
  public data object Ttd : Currency {
    override val value: String = "TTD"
  }
  /** New Taiwan Dollar */
  public data object Twd : Currency {
    override val value: String = "TWD"
  }
  /** Tanzanian Shilling */
  public data object Tzs : Currency {
    override val value: String = "TZS"
  }
  /** Hryvnia */
  public data object Uah : Currency {
    override val value: String = "UAH"
  }
  /** Uganda Shilling */
  public data object Ugx : Currency {
    override val value: String = "UGX"
  }
  /** US Dollar (Next day) */
  public data object Usn : Currency {
    override val value: String = "USN"
  }
  /** Uruguay Peso en Unidades Indexadas (UI) */
  public data object Uyi : Currency {
    override val value: String = "UYI"
  }
  /** Peso Uruguayo */
  public data object Uyu : Currency {
    override val value: String = "UYU"
  }
  /** Unidad Previsional */
  public data object Uyw : Currency {
    override val value: String = "UYW"
  }
  /** Uzbekistan Sum */
  public data object Uzs : Currency {
    override val value: String = "UZS"
  }
  /** Bolívar Soberano */
  public data object Ved : Currency {
    override val value: String = "VED"
  }
  /** Bolívar Soberano */
  public data object Ves : Currency {
    override val value: String = "VES"
  }
  /** Dong */
  public data object Vnd : Currency {
    override val value: String = "VND"
  }
  /** Vatu */
  public data object Vuv : Currency {
    override val value: String = "VUV"
  }
  /** Tala */
  public data object Wst : Currency {
    override val value: String = "WST"
  }
  /** CFA Franc BEAC */
  public data object Xaf : Currency {
    override val value: String = "XAF"
  }
  /** Silver */
  public data object Xag : Currency {
    override val value: String = "XAG"
  }
  /** Gold */
  public data object Xau : Currency {
    override val value: String = "XAU"
  }
  /** Bond Markets Unit European Composite Unit (EURCO) */
  public data object Xba : Currency {
    override val value: String = "XBA"
  }
  /** Bond Markets Unit European Monetary Unit (E.M.U.-6) */
  public data object Xbb : Currency {
    override val value: String = "XBB"
  }
  /** Bond Markets Unit European Unit of Account 9 (E.U.A.-9) */
  public data object Xbc : Currency {
    override val value: String = "XBC"
  }
  /** Bond Markets Unit European Unit of Account 17 (E.U.A.-17) */
  public data object Xbd : Currency {
    override val value: String = "XBD"
  }
  /** East Caribbean Dollar */
  public data object Xcd : Currency {
    override val value: String = "XCD"
  }
  /** SDR (Special Drawing Right) */
  public data object Xdr : Currency {
    override val value: String = "XDR"
  }
  /** CFA Franc BCEAO */
  public data object Xof : Currency {
    override val value: String = "XOF"
  }
  /** Palladium */
  public data object Xpd : Currency {
    override val value: String = "XPD"
  }
  /** CFP Franc */
  public data object Xpf : Currency {
    override val value: String = "XPF"
  }
  /** Platinum */
  public data object Xpt : Currency {
    override val value: String = "XPT"
  }
  /** Sucre */
  public data object Xsu : Currency {
    override val value: String = "XSU"
  }
  /** Codes specifically reserved for testing purposes */
  public data object Xts : Currency {
    override val value: String = "XTS"
  }
  /** ADB Unit of Account */
  public data object Xua : Currency {
    override val value: String = "XUA"
  }
  /** The codes assigned for transactions where no currency is involved */
  public data object Xxx : Currency {
    override val value: String = "XXX"
  }
  /** Yemeni Rial */
  public data object Yer : Currency {
    override val value: String = "YER"
  }
  /** Rand */
  public data object Zar : Currency {
    override val value: String = "ZAR"
  }
  /** Zambian Kwacha */
  public data object Zmw : Currency {
    override val value: String = "ZMW"
  }
  /** Zimbabwe Dollar */
  public data object Zwl : Currency {
    override val value: String = "ZWL"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Currency
}


private object CurrencySerializer : KSerializer<Currency> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Currency::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): Currency {
    val value = decoder.decodeString()
    return when (value) {
      "KRW" -> Currency.Krw
      "USD" -> Currency.Usd
      "JPY" -> Currency.Jpy
      "AED" -> Currency.Aed
      "AFN" -> Currency.Afn
      "ALL" -> Currency.All
      "AMD" -> Currency.Amd
      "ANG" -> Currency.Ang
      "AOA" -> Currency.Aoa
      "ARS" -> Currency.Ars
      "AUD" -> Currency.Aud
      "AWG" -> Currency.Awg
      "AZN" -> Currency.Azn
      "BAM" -> Currency.Bam
      "BBD" -> Currency.Bbd
      "BDT" -> Currency.Bdt
      "BGN" -> Currency.Bgn
      "BHD" -> Currency.Bhd
      "BIF" -> Currency.Bif
      "BMD" -> Currency.Bmd
      "BND" -> Currency.Bnd
      "BOB" -> Currency.Bob
      "BOV" -> Currency.Bov
      "BRL" -> Currency.Brl
      "BSD" -> Currency.Bsd
      "BTN" -> Currency.Btn
      "BWP" -> Currency.Bwp
      "BYN" -> Currency.Byn
      "BZD" -> Currency.Bzd
      "CAD" -> Currency.Cad
      "CDF" -> Currency.Cdf
      "CHE" -> Currency.Che
      "CHF" -> Currency.Chf
      "CHW" -> Currency.Chw
      "CLF" -> Currency.Clf
      "CLP" -> Currency.Clp
      "CNY" -> Currency.Cny
      "COP" -> Currency.Cop
      "COU" -> Currency.Cou
      "CRC" -> Currency.Crc
      "CUC" -> Currency.Cuc
      "CUP" -> Currency.Cup
      "CVE" -> Currency.Cve
      "CZK" -> Currency.Czk
      "DJF" -> Currency.Djf
      "DKK" -> Currency.Dkk
      "DOP" -> Currency.Dop
      "DZD" -> Currency.Dzd
      "EGP" -> Currency.Egp
      "ERN" -> Currency.Ern
      "ETB" -> Currency.Etb
      "EUR" -> Currency.Eur
      "FJD" -> Currency.Fjd
      "FKP" -> Currency.Fkp
      "GBP" -> Currency.Gbp
      "GEL" -> Currency.Gel
      "GHS" -> Currency.Ghs
      "GIP" -> Currency.Gip
      "GMD" -> Currency.Gmd
      "GNF" -> Currency.Gnf
      "GTQ" -> Currency.Gtq
      "GYD" -> Currency.Gyd
      "HKD" -> Currency.Hkd
      "HNL" -> Currency.Hnl
      "HRK" -> Currency.Hrk
      "HTG" -> Currency.Htg
      "HUF" -> Currency.Huf
      "IDR" -> Currency.Idr
      "ILS" -> Currency.Ils
      "INR" -> Currency.Inr
      "IQD" -> Currency.Iqd
      "IRR" -> Currency.Irr
      "ISK" -> Currency.Isk
      "JMD" -> Currency.Jmd
      "JOD" -> Currency.Jod
      "KES" -> Currency.Kes
      "KGS" -> Currency.Kgs
      "KHR" -> Currency.Khr
      "KMF" -> Currency.Kmf
      "KPW" -> Currency.Kpw
      "KWD" -> Currency.Kwd
      "KYD" -> Currency.Kyd
      "KZT" -> Currency.Kzt
      "LAK" -> Currency.Lak
      "LBP" -> Currency.Lbp
      "LKR" -> Currency.Lkr
      "LRD" -> Currency.Lrd
      "LSL" -> Currency.Lsl
      "LYD" -> Currency.Lyd
      "MAD" -> Currency.Mad
      "MDL" -> Currency.Mdl
      "MGA" -> Currency.Mga
      "MKD" -> Currency.Mkd
      "MMK" -> Currency.Mmk
      "MNT" -> Currency.Mnt
      "MOP" -> Currency.Mop
      "MRU" -> Currency.Mru
      "MUR" -> Currency.Mur
      "MVR" -> Currency.Mvr
      "MWK" -> Currency.Mwk
      "MXN" -> Currency.Mxn
      "MXV" -> Currency.Mxv
      "MYR" -> Currency.Myr
      "MZN" -> Currency.Mzn
      "NAD" -> Currency.Nad
      "NGN" -> Currency.Ngn
      "NIO" -> Currency.Nio
      "NOK" -> Currency.Nok
      "NPR" -> Currency.Npr
      "NZD" -> Currency.Nzd
      "OMR" -> Currency.Omr
      "PAB" -> Currency.Pab
      "PEN" -> Currency.Pen
      "PGK" -> Currency.Pgk
      "PHP" -> Currency.Php
      "PKR" -> Currency.Pkr
      "PLN" -> Currency.Pln
      "PYG" -> Currency.Pyg
      "QAR" -> Currency.Qar
      "RON" -> Currency.Ron
      "RSD" -> Currency.Rsd
      "RUB" -> Currency.Rub
      "RWF" -> Currency.Rwf
      "SAR" -> Currency.Sar
      "SBD" -> Currency.Sbd
      "SCR" -> Currency.Scr
      "SDG" -> Currency.Sdg
      "SEK" -> Currency.Sek
      "SGD" -> Currency.Sgd
      "SHP" -> Currency.Shp
      "SLE" -> Currency.Sle
      "SLL" -> Currency.Sll
      "SOS" -> Currency.Sos
      "SRD" -> Currency.Srd
      "SSP" -> Currency.Ssp
      "STN" -> Currency.Stn
      "SVC" -> Currency.Svc
      "SYP" -> Currency.Syp
      "SZL" -> Currency.Szl
      "THB" -> Currency.Thb
      "TJS" -> Currency.Tjs
      "TMT" -> Currency.Tmt
      "TND" -> Currency.Tnd
      "TOP" -> Currency.Top
      "TRY" -> Currency.Try
      "TTD" -> Currency.Ttd
      "TWD" -> Currency.Twd
      "TZS" -> Currency.Tzs
      "UAH" -> Currency.Uah
      "UGX" -> Currency.Ugx
      "USN" -> Currency.Usn
      "UYI" -> Currency.Uyi
      "UYU" -> Currency.Uyu
      "UYW" -> Currency.Uyw
      "UZS" -> Currency.Uzs
      "VED" -> Currency.Ved
      "VES" -> Currency.Ves
      "VND" -> Currency.Vnd
      "VUV" -> Currency.Vuv
      "WST" -> Currency.Wst
      "XAF" -> Currency.Xaf
      "XAG" -> Currency.Xag
      "XAU" -> Currency.Xau
      "XBA" -> Currency.Xba
      "XBB" -> Currency.Xbb
      "XBC" -> Currency.Xbc
      "XBD" -> Currency.Xbd
      "XCD" -> Currency.Xcd
      "XDR" -> Currency.Xdr
      "XOF" -> Currency.Xof
      "XPD" -> Currency.Xpd
      "XPF" -> Currency.Xpf
      "XPT" -> Currency.Xpt
      "XSU" -> Currency.Xsu
      "XTS" -> Currency.Xts
      "XUA" -> Currency.Xua
      "XXX" -> Currency.Xxx
      "YER" -> Currency.Yer
      "ZAR" -> Currency.Zar
      "ZMW" -> Currency.Zmw
      "ZWL" -> Currency.Zwl
      else -> Currency.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: Currency) = encoder.encodeString(value.value)
}
