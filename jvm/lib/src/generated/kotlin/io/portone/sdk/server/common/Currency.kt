package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

/** 통화 단위 */
@Serializable
public enum class Currency {
  /** 대한민국 원화 */
  Krw,
  /** 미국 달러 */
  Usd,
  /** 일본 엔화 */
  Jpy,
  /** UAE Dirham */
  Aed,
  /** Afghani */
  Afn,
  /** Lek */
  All,
  /** Armenian Dram */
  Amd,
  /** Netherlands Antillean Guilder */
  Ang,
  /** Kwanza */
  Aoa,
  /** Argentine Peso */
  Ars,
  /** Australian Dollar */
  Aud,
  /** Aruban Florin */
  Awg,
  /** Azerbaijan Manat */
  Azn,
  /** Convertible Mark */
  Bam,
  /** Barbados Dollar */
  Bbd,
  /** Taka */
  Bdt,
  /** Bulgarian Lev */
  Bgn,
  /** Bahraini Dinar */
  Bhd,
  /** Burundi Franc */
  Bif,
  /** Bermudian Dollar */
  Bmd,
  /** Brunei Dollar */
  Bnd,
  /** Boliviano */
  Bob,
  /** Mvdol */
  Bov,
  /** Brazilian Real */
  Brl,
  /** Bahamian Dollar */
  Bsd,
  /** Ngultrum */
  Btn,
  /** Pula */
  Bwp,
  /** Belarusian Ruble */
  Byn,
  /** Belize Dollar */
  Bzd,
  /** Canadian Dollar */
  Cad,
  /** Congolese Franc */
  Cdf,
  /** WIR Euro */
  Che,
  /** Swiss Franc */
  Chf,
  /** WIR Franc */
  Chw,
  /** Unidad de Fomento */
  Clf,
  /** Chilean Peso */
  Clp,
  /** Yuan Renminbi */
  Cny,
  /** Colombian Peso */
  Cop,
  /** Unidad de Valor Real */
  Cou,
  /** Costa Rican Colon */
  Crc,
  /** Peso Convertible */
  Cuc,
  /** Cuban Peso */
  Cup,
  /** Cabo Verde Escudo */
  Cve,
  /** Czech Koruna */
  Czk,
  /** Djibouti Franc */
  Djf,
  /** Danish Krone */
  Dkk,
  /** Dominican Peso */
  Dop,
  /** Algerian Dinar */
  Dzd,
  /** Egyptian Pound */
  Egp,
  /** Nakfa */
  Ern,
  /** Ethiopian Birr */
  Etb,
  /** Euro */
  Eur,
  /** Fiji Dollar */
  Fjd,
  /** Falkland Islands Pound */
  Fkp,
  /** Pound Sterling */
  Gbp,
  /** Lari */
  Gel,
  /** Ghana Cedi */
  Ghs,
  /** Gibraltar Pound */
  Gip,
  /** Dalasi */
  Gmd,
  /** Guinean Franc */
  Gnf,
  /** Quetzal */
  Gtq,
  /** Guyana Dollar */
  Gyd,
  /** Hong Kong Dollar */
  Hkd,
  /** Lempira */
  Hnl,
  /** Kuna (Replaced by EUR) */
  Hrk,
  /** Gourde */
  Htg,
  /** Forint */
  Huf,
  /** Rupiah */
  Idr,
  /** New Israeli Sheqel */
  Ils,
  /** Indian Rupee */
  Inr,
  /** Iraqi Dinar */
  Iqd,
  /** Iranian Rial */
  Irr,
  /** Iceland Krona */
  Isk,
  /** Jamaican Dollar */
  Jmd,
  /** Jordanian Dinar */
  Jod,
  /** Kenyan Shilling */
  Kes,
  /** Som */
  Kgs,
  /** Riel */
  Khr,
  /** Comorian Franc */
  Kmf,
  /** North Korean Won */
  Kpw,
  /** Kuwaiti Dinar */
  Kwd,
  /** Cayman Islands Dollar */
  Kyd,
  /** Tenge */
  Kzt,
  /** Lao Kip */
  Lak,
  /** Lebanese Pound */
  Lbp,
  /** Sri Lanka Rupee */
  Lkr,
  /** Liberian Dollar */
  Lrd,
  /** Loti */
  Lsl,
  /** Libyan Dinar */
  Lyd,
  /** Moroccan Dirham */
  Mad,
  /** Moldovan Leu */
  Mdl,
  /** Malagasy Ariary */
  Mga,
  /** Denar */
  Mkd,
  /** Kyat */
  Mmk,
  /** Tugrik */
  Mnt,
  /** Pataca */
  Mop,
  /** Ouguiya */
  Mru,
  /** Mauritius Rupee */
  Mur,
  /** Rufiyaa */
  Mvr,
  /** Malawi Kwacha */
  Mwk,
  /** Mexican Peso */
  Mxn,
  /** Mexican Unidad de Inversion (UDI) */
  Mxv,
  /** Malaysian Ringgit */
  Myr,
  /** Mozambique Metical */
  Mzn,
  /** Namibia Dollar */
  Nad,
  /** Naira */
  Ngn,
  /** Cordoba Oro */
  Nio,
  /** Norwegian Krone */
  Nok,
  /** Nepalese Rupee */
  Npr,
  /** New Zealand Dollar */
  Nzd,
  /** Rial Omani */
  Omr,
  /** Balboa */
  Pab,
  /** Sol */
  Pen,
  /** Kina */
  Pgk,
  /** Philippine Peso */
  Php,
  /** Pakistan Rupee */
  Pkr,
  /** Zloty */
  Pln,
  /** Guarani */
  Pyg,
  /** Qatari Rial */
  Qar,
  /** Romanian Leu */
  Ron,
  /** Serbian Dinar */
  Rsd,
  /** Russian Ruble */
  Rub,
  /** Rwanda Franc */
  Rwf,
  /** Saudi Riyal */
  Sar,
  /** Solomon Islands Dollar */
  Sbd,
  /** Seychelles Rupee */
  Scr,
  /** Sudanese Pound */
  Sdg,
  /** Swedish Krona */
  Sek,
  /** Singapore Dollar */
  Sgd,
  /** Saint Helena Pound */
  Shp,
  /** Leone */
  Sle,
  /** Leone */
  Sll,
  /** Somali Shilling */
  Sos,
  /** Surinam Dollar */
  Srd,
  /** South Sudanese Pound */
  Ssp,
  /** Dobra */
  Stn,
  /** El Salvador Colon */
  Svc,
  /** Syrian Pound */
  Syp,
  /** Lilangeni */
  Szl,
  /** Baht */
  Thb,
  /** Somoni */
  Tjs,
  /** Turkmenistan New Manat */
  Tmt,
  /** Tunisian Dinar */
  Tnd,
  /** Pa’anga */
  Top,
  /** Turkish Lira */
  Try,
  /** Trinidad and Tobago Dollar */
  Ttd,
  /** New Taiwan Dollar */
  Twd,
  /** Tanzanian Shilling */
  Tzs,
  /** Hryvnia */
  Uah,
  /** Uganda Shilling */
  Ugx,
  /** US Dollar (Next day) */
  Usn,
  /** Uruguay Peso en Unidades Indexadas (UI) */
  Uyi,
  /** Peso Uruguayo */
  Uyu,
  /** Unidad Previsional */
  Uyw,
  /** Uzbekistan Sum */
  Uzs,
  /** Bolívar Soberano */
  Ved,
  /** Bolívar Soberano */
  Ves,
  /** Dong */
  Vnd,
  /** Vatu */
  Vuv,
  /** Tala */
  Wst,
  /** CFA Franc BEAC */
  Xaf,
  /** Silver */
  Xag,
  /** Gold */
  Xau,
  /** Bond Markets Unit European Composite Unit (EURCO) */
  Xba,
  /** Bond Markets Unit European Monetary Unit (E.M.U.-6) */
  Xbb,
  /** Bond Markets Unit European Unit of Account 9 (E.U.A.-9) */
  Xbc,
  /** Bond Markets Unit European Unit of Account 17 (E.U.A.-17) */
  Xbd,
  /** East Caribbean Dollar */
  Xcd,
  /** SDR (Special Drawing Right) */
  Xdr,
  /** CFA Franc BCEAO */
  Xof,
  /** Palladium */
  Xpd,
  /** CFP Franc */
  Xpf,
  /** Platinum */
  Xpt,
  /** Sucre */
  Xsu,
  /** Codes specifically reserved for testing purposes */
  Xts,
  /** ADB Unit of Account */
  Xua,
  /** The codes assigned for transactions where no currency is involved */
  Xxx,
  /** Yemeni Rial */
  Yer,
  /** Rand */
  Zar,
  /** Zambian Kwacha */
  Zmw,
  /** Zimbabwe Dollar */
  Zwl,
}
