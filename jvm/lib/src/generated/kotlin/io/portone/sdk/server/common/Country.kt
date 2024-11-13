package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 국가 */
@Serializable
public sealed class Country {
  /** Andorra */
  @SerialName("AD")
  public data object Ad : Country()
  /** United Arab Emirates (the) */
  @SerialName("AE")
  public data object Ae : Country()
  /** Afghanistan */
  @SerialName("AF")
  public data object Af : Country()
  /** Antigua and Barbuda */
  @SerialName("AG")
  public data object Ag : Country()
  /** Anguilla */
  @SerialName("AI")
  public data object Ai : Country()
  /** Albania */
  @SerialName("AL")
  public data object Al : Country()
  /** Armenia */
  @SerialName("AM")
  public data object Am : Country()
  /** Angola */
  @SerialName("AO")
  public data object Ao : Country()
  /** Antarctica */
  @SerialName("AQ")
  public data object Aq : Country()
  /** Argentina */
  @SerialName("AR")
  public data object Ar : Country()
  /** American Samoa */
  @SerialName("AS")
  public data object As : Country()
  /** Austria */
  @SerialName("AT")
  public data object At : Country()
  /** Australia */
  @SerialName("AU")
  public data object Au : Country()
  /** Aruba */
  @SerialName("AW")
  public data object Aw : Country()
  /** Åland Islands */
  @SerialName("AX")
  public data object Ax : Country()
  /** Azerbaijan */
  @SerialName("AZ")
  public data object Az : Country()
  /** Bosnia and Herzegovina */
  @SerialName("BA")
  public data object Ba : Country()
  /** Barbados */
  @SerialName("BB")
  public data object Bb : Country()
  /** Bangladesh */
  @SerialName("BD")
  public data object Bd : Country()
  /** Belgium */
  @SerialName("BE")
  public data object Be : Country()
  /** Burkina Faso */
  @SerialName("BF")
  public data object Bf : Country()
  /** Bulgaria */
  @SerialName("BG")
  public data object Bg : Country()
  /** Bahrain */
  @SerialName("BH")
  public data object Bh : Country()
  /** Burundi */
  @SerialName("BI")
  public data object Bi : Country()
  /** Benin */
  @SerialName("BJ")
  public data object Bj : Country()
  /** Saint Barthélemy */
  @SerialName("BL")
  public data object Bl : Country()
  /** Bermuda */
  @SerialName("BM")
  public data object Bm : Country()
  /** Brunei Darussalam */
  @SerialName("BN")
  public data object Bn : Country()
  /** Bolivia (Plurinational State of) */
  @SerialName("BO")
  public data object Bo : Country()
  /** Bonaire, Sint Eustatius and Saba */
  @SerialName("BQ")
  public data object Bq : Country()
  /** Brazil */
  @SerialName("BR")
  public data object Br : Country()
  /** Bahamas (the) */
  @SerialName("BS")
  public data object Bs : Country()
  /** Bhutan */
  @SerialName("BT")
  public data object Bt : Country()
  /** Bouvet Island */
  @SerialName("BV")
  public data object Bv : Country()
  /** Botswana */
  @SerialName("BW")
  public data object Bw : Country()
  /** Belarus */
  @SerialName("BY")
  public data object By : Country()
  /** Belize */
  @SerialName("BZ")
  public data object Bz : Country()
  /** Canada */
  @SerialName("CA")
  public data object Ca : Country()
  /** Cocos (Keeling) Islands (the) */
  @SerialName("CC")
  public data object Cc : Country()
  /** Congo (the Democratic Republic of the) */
  @SerialName("CD")
  public data object Cd : Country()
  /** Central African Republic (the) */
  @SerialName("CF")
  public data object Cf : Country()
  /** Congo (the) */
  @SerialName("CG")
  public data object Cg : Country()
  /** Switzerland */
  @SerialName("CH")
  public data object Ch : Country()
  /** Côte d'Ivoire */
  @SerialName("CI")
  public data object Ci : Country()
  /** Cook Islands (the) */
  @SerialName("CK")
  public data object Ck : Country()
  /** Chile */
  @SerialName("CL")
  public data object Cl : Country()
  /** Cameroon */
  @SerialName("CM")
  public data object Cm : Country()
  /** China */
  @SerialName("CN")
  public data object Cn : Country()
  /** Colombia */
  @SerialName("CO")
  public data object Co : Country()
  /** Costa Rica */
  @SerialName("CR")
  public data object Cr : Country()
  /** Cuba */
  @SerialName("CU")
  public data object Cu : Country()
  /** Cabo Verde */
  @SerialName("CV")
  public data object Cv : Country()
  /** Curaçao */
  @SerialName("CW")
  public data object Cw : Country()
  /** Christmas Island */
  @SerialName("CX")
  public data object Cx : Country()
  /** Cyprus */
  @SerialName("CY")
  public data object Cy : Country()
  /** Czechia */
  @SerialName("CZ")
  public data object Cz : Country()
  /** Germany */
  @SerialName("DE")
  public data object De : Country()
  /** Djibouti */
  @SerialName("DJ")
  public data object Dj : Country()
  /** Denmark */
  @SerialName("DK")
  public data object Dk : Country()
  /** Dominica */
  @SerialName("DM")
  public data object Dm : Country()
  /** Dominican Republic (the) */
  @SerialName("DO")
  public data object Do : Country()
  /** Algeria */
  @SerialName("DZ")
  public data object Dz : Country()
  /** Ecuador */
  @SerialName("EC")
  public data object Ec : Country()
  /** Estonia */
  @SerialName("EE")
  public data object Ee : Country()
  /** Egypt */
  @SerialName("EG")
  public data object Eg : Country()
  /** Western Sahara */
  @SerialName("EH")
  public data object Eh : Country()
  /** Eritrea */
  @SerialName("ER")
  public data object Er : Country()
  /** Spain */
  @SerialName("ES")
  public data object Es : Country()
  /** Ethiopia */
  @SerialName("ET")
  public data object Et : Country()
  /** Finland */
  @SerialName("FI")
  public data object Fi : Country()
  /** Fiji */
  @SerialName("FJ")
  public data object Fj : Country()
  /** Falkland Islands (the) [Malvinas] */
  @SerialName("FK")
  public data object Fk : Country()
  /** Micronesia (Federated States of) */
  @SerialName("FM")
  public data object Fm : Country()
  /** Faroe Islands (the) */
  @SerialName("FO")
  public data object Fo : Country()
  /** France */
  @SerialName("FR")
  public data object Fr : Country()
  /** Gabon */
  @SerialName("GA")
  public data object Ga : Country()
  /** United Kingdom of Great Britain and Northern Ireland (the) */
  @SerialName("GB")
  public data object Gb : Country()
  /** Grenada */
  @SerialName("GD")
  public data object Gd : Country()
  /** Georgia */
  @SerialName("GE")
  public data object Ge : Country()
  /** French Guiana */
  @SerialName("GF")
  public data object Gf : Country()
  /** Guernsey */
  @SerialName("GG")
  public data object Gg : Country()
  /** Ghana */
  @SerialName("GH")
  public data object Gh : Country()
  /** Gibraltar */
  @SerialName("GI")
  public data object Gi : Country()
  /** Greenland */
  @SerialName("GL")
  public data object Gl : Country()
  /** Gambia (the) */
  @SerialName("GM")
  public data object Gm : Country()
  /** Guinea */
  @SerialName("GN")
  public data object Gn : Country()
  /** Guadeloupe */
  @SerialName("GP")
  public data object Gp : Country()
  /** Equatorial Guinea */
  @SerialName("GQ")
  public data object Gq : Country()
  /** Greece */
  @SerialName("GR")
  public data object Gr : Country()
  /** South Georgia and the South Sandwich Islands */
  @SerialName("GS")
  public data object Gs : Country()
  /** Guatemala */
  @SerialName("GT")
  public data object Gt : Country()
  /** Guam */
  @SerialName("GU")
  public data object Gu : Country()
  /** Guinea-Bissau */
  @SerialName("GW")
  public data object Gw : Country()
  /** Guyana */
  @SerialName("GY")
  public data object Gy : Country()
  /** Hong Kong */
  @SerialName("HK")
  public data object Hk : Country()
  /** Heard Island and McDonald Islands */
  @SerialName("HM")
  public data object Hm : Country()
  /** Honduras */
  @SerialName("HN")
  public data object Hn : Country()
  /** Croatia */
  @SerialName("HR")
  public data object Hr : Country()
  /** Haiti */
  @SerialName("HT")
  public data object Ht : Country()
  /** Hungary */
  @SerialName("HU")
  public data object Hu : Country()
  /** Indonesia */
  @SerialName("ID")
  public data object Id : Country()
  /** Ireland */
  @SerialName("IE")
  public data object Ie : Country()
  /** Israel */
  @SerialName("IL")
  public data object Il : Country()
  /** Isle of Man */
  @SerialName("IM")
  public data object Im : Country()
  /** India */
  @SerialName("IN")
  public data object In : Country()
  /** British Indian Ocean Territory (the) */
  @SerialName("IO")
  public data object Io : Country()
  /** Iraq */
  @SerialName("IQ")
  public data object Iq : Country()
  /** Iran (Islamic Republic of) */
  @SerialName("IR")
  public data object Ir : Country()
  /** Iceland */
  @SerialName("IS")
  public data object Is : Country()
  /** Italy */
  @SerialName("IT")
  public data object It : Country()
  /** Jersey */
  @SerialName("JE")
  public data object Je : Country()
  /** Jamaica */
  @SerialName("JM")
  public data object Jm : Country()
  /** Jordan */
  @SerialName("JO")
  public data object Jo : Country()
  /** Japan */
  @SerialName("JP")
  public data object Jp : Country()
  /** Kenya */
  @SerialName("KE")
  public data object Ke : Country()
  /** Kyrgyzstan */
  @SerialName("KG")
  public data object Kg : Country()
  /** Cambodia */
  @SerialName("KH")
  public data object Kh : Country()
  /** Kiribati */
  @SerialName("KI")
  public data object Ki : Country()
  /** Comoros (the) */
  @SerialName("KM")
  public data object Km : Country()
  /** Saint Kitts and Nevis */
  @SerialName("KN")
  public data object Kn : Country()
  /** Korea (the Democratic People's Republic of) */
  @SerialName("KP")
  public data object Kp : Country()
  /** Korea (the Republic of) */
  @SerialName("KR")
  public data object Kr : Country()
  /** Kuwait */
  @SerialName("KW")
  public data object Kw : Country()
  /** Cayman Islands (the) */
  @SerialName("KY")
  public data object Ky : Country()
  /** Kazakhstan */
  @SerialName("KZ")
  public data object Kz : Country()
  /** Lao People's Democratic Republic (the) */
  @SerialName("LA")
  public data object La : Country()
  /** Lebanon */
  @SerialName("LB")
  public data object Lb : Country()
  /** Saint Lucia */
  @SerialName("LC")
  public data object Lc : Country()
  /** Liechtenstein */
  @SerialName("LI")
  public data object Li : Country()
  /** Sri Lanka */
  @SerialName("LK")
  public data object Lk : Country()
  /** Liberia */
  @SerialName("LR")
  public data object Lr : Country()
  /** Lesotho */
  @SerialName("LS")
  public data object Ls : Country()
  /** Lithuania */
  @SerialName("LT")
  public data object Lt : Country()
  /** Luxembourg */
  @SerialName("LU")
  public data object Lu : Country()
  /** Latvia */
  @SerialName("LV")
  public data object Lv : Country()
  /** Libya */
  @SerialName("LY")
  public data object Ly : Country()
  /** Morocco */
  @SerialName("MA")
  public data object Ma : Country()
  /** Monaco */
  @SerialName("MC")
  public data object Mc : Country()
  /** Moldova (the Republic of) */
  @SerialName("MD")
  public data object Md : Country()
  /** Montenegro */
  @SerialName("ME")
  public data object Me : Country()
  /** Saint Martin (French part) */
  @SerialName("MF")
  public data object Mf : Country()
  /** Madagascar */
  @SerialName("MG")
  public data object Mg : Country()
  /** Marshall Islands (the) */
  @SerialName("MH")
  public data object Mh : Country()
  /** North Macedonia */
  @SerialName("MK")
  public data object Mk : Country()
  /** Mali */
  @SerialName("ML")
  public data object Ml : Country()
  /** Myanmar */
  @SerialName("MM")
  public data object Mm : Country()
  /** Mongolia */
  @SerialName("MN")
  public data object Mn : Country()
  /** Macao */
  @SerialName("MO")
  public data object Mo : Country()
  /** Northern Mariana Islands (the) */
  @SerialName("MP")
  public data object Mp : Country()
  /** Martinique */
  @SerialName("MQ")
  public data object Mq : Country()
  /** Mauritania */
  @SerialName("MR")
  public data object Mr : Country()
  /** Montserrat */
  @SerialName("MS")
  public data object Ms : Country()
  /** Malta */
  @SerialName("MT")
  public data object Mt : Country()
  /** Mauritius */
  @SerialName("MU")
  public data object Mu : Country()
  /** Maldives */
  @SerialName("MV")
  public data object Mv : Country()
  /** Malawi */
  @SerialName("MW")
  public data object Mw : Country()
  /** Mexico */
  @SerialName("MX")
  public data object Mx : Country()
  /** Malaysia */
  @SerialName("MY")
  public data object My : Country()
  /** Mozambique */
  @SerialName("MZ")
  public data object Mz : Country()
  /** Namibia */
  @SerialName("NA")
  public data object Na : Country()
  /** New Caledonia */
  @SerialName("NC")
  public data object Nc : Country()
  /** Niger (the) */
  @SerialName("NE")
  public data object Ne : Country()
  /** Norfolk Island */
  @SerialName("NF")
  public data object Nf : Country()
  /** Nigeria */
  @SerialName("NG")
  public data object Ng : Country()
  /** Nicaragua */
  @SerialName("NI")
  public data object Ni : Country()
  /** Netherlands (Kingdom of the) */
  @SerialName("NL")
  public data object Nl : Country()
  /** Norway */
  @SerialName("NO")
  public data object No : Country()
  /** Nepal */
  @SerialName("NP")
  public data object Np : Country()
  /** Nauru */
  @SerialName("NR")
  public data object Nr : Country()
  /** Niue */
  @SerialName("NU")
  public data object Nu : Country()
  /** New Zealand */
  @SerialName("NZ")
  public data object Nz : Country()
  /** Oman */
  @SerialName("OM")
  public data object Om : Country()
  /** Panama */
  @SerialName("PA")
  public data object Pa : Country()
  /** Peru */
  @SerialName("PE")
  public data object Pe : Country()
  /** French Polynesia */
  @SerialName("PF")
  public data object Pf : Country()
  /** Papua New Guinea */
  @SerialName("PG")
  public data object Pg : Country()
  /** Philippines (the) */
  @SerialName("PH")
  public data object Ph : Country()
  /** Pakistan */
  @SerialName("PK")
  public data object Pk : Country()
  /** Poland */
  @SerialName("PL")
  public data object Pl : Country()
  /** Saint Pierre and Miquelon */
  @SerialName("PM")
  public data object Pm : Country()
  /** Pitcairn */
  @SerialName("PN")
  public data object Pn : Country()
  /** Puerto Rico */
  @SerialName("PR")
  public data object Pr : Country()
  /** Palestine, State of */
  @SerialName("PS")
  public data object Ps : Country()
  /** Portugal */
  @SerialName("PT")
  public data object Pt : Country()
  /** Palau */
  @SerialName("PW")
  public data object Pw : Country()
  /** Paraguay */
  @SerialName("PY")
  public data object Py : Country()
  /** Qatar */
  @SerialName("QA")
  public data object Qa : Country()
  /** Réunion */
  @SerialName("RE")
  public data object Re : Country()
  /** Romania */
  @SerialName("RO")
  public data object Ro : Country()
  /** Serbia */
  @SerialName("RS")
  public data object Rs : Country()
  /** Russian Federation (the) */
  @SerialName("RU")
  public data object Ru : Country()
  /** Rwanda */
  @SerialName("RW")
  public data object Rw : Country()
  /** Saudi Arabia */
  @SerialName("SA")
  public data object Sa : Country()
  /** Solomon Islands */
  @SerialName("SB")
  public data object Sb : Country()
  /** Seychelles */
  @SerialName("SC")
  public data object Sc : Country()
  /** Sudan (the) */
  @SerialName("SD")
  public data object Sd : Country()
  /** Sweden */
  @SerialName("SE")
  public data object Se : Country()
  /** Singapore */
  @SerialName("SG")
  public data object Sg : Country()
  /** Saint Helena, Ascension and Tristan da Cunha */
  @SerialName("SH")
  public data object Sh : Country()
  /** Slovenia */
  @SerialName("SI")
  public data object Si : Country()
  /** Svalbard and Jan Mayen */
  @SerialName("SJ")
  public data object Sj : Country()
  /** Slovakia */
  @SerialName("SK")
  public data object Sk : Country()
  /** Sierra Leone */
  @SerialName("SL")
  public data object Sl : Country()
  /** San Marino */
  @SerialName("SM")
  public data object Sm : Country()
  /** Senegal */
  @SerialName("SN")
  public data object Sn : Country()
  /** Somalia */
  @SerialName("SO")
  public data object So : Country()
  /** Suriname */
  @SerialName("SR")
  public data object Sr : Country()
  /** South Sudan */
  @SerialName("SS")
  public data object Ss : Country()
  /** Sao Tome and Principe */
  @SerialName("ST")
  public data object St : Country()
  /** El Salvador */
  @SerialName("SV")
  public data object Sv : Country()
  /** Sint Maarten (Dutch part) */
  @SerialName("SX")
  public data object Sx : Country()
  /** Syrian Arab Republic (the) */
  @SerialName("SY")
  public data object Sy : Country()
  /** Eswatini */
  @SerialName("SZ")
  public data object Sz : Country()
  /** Turks and Caicos Islands (the) */
  @SerialName("TC")
  public data object Tc : Country()
  /** Chad */
  @SerialName("TD")
  public data object Td : Country()
  /** French Southern Territories (the) */
  @SerialName("TF")
  public data object Tf : Country()
  /** Togo */
  @SerialName("TG")
  public data object Tg : Country()
  /** Thailand */
  @SerialName("TH")
  public data object Th : Country()
  /** Tajikistan */
  @SerialName("TJ")
  public data object Tj : Country()
  /** Tokelau */
  @SerialName("TK")
  public data object Tk : Country()
  /** Timor-Leste */
  @SerialName("TL")
  public data object Tl : Country()
  /** Turkmenistan */
  @SerialName("TM")
  public data object Tm : Country()
  /** Tunisia */
  @SerialName("TN")
  public data object Tn : Country()
  /** Tonga */
  @SerialName("TO")
  public data object To : Country()
  /** Türkiye */
  @SerialName("TR")
  public data object Tr : Country()
  /** Trinidad and Tobago */
  @SerialName("TT")
  public data object Tt : Country()
  /** Tuvalu */
  @SerialName("TV")
  public data object Tv : Country()
  /** Taiwan (Province of China) */
  @SerialName("TW")
  public data object Tw : Country()
  /** Tanzania, the United Republic of */
  @SerialName("TZ")
  public data object Tz : Country()
  /** Ukraine */
  @SerialName("UA")
  public data object Ua : Country()
  /** Uganda */
  @SerialName("UG")
  public data object Ug : Country()
  /** United States Minor Outlying Islands (the) */
  @SerialName("UM")
  public data object Um : Country()
  /** United States of America (the) */
  @SerialName("US")
  public data object Us : Country()
  /** Uruguay */
  @SerialName("UY")
  public data object Uy : Country()
  /** Uzbekistan */
  @SerialName("UZ")
  public data object Uz : Country()
  /** Holy See (the) */
  @SerialName("VA")
  public data object Va : Country()
  /** Saint Vincent and the Grenadines */
  @SerialName("VC")
  public data object Vc : Country()
  /** Venezuela (Bolivarian Republic of) */
  @SerialName("VE")
  public data object Ve : Country()
  /** Virgin Islands (British) */
  @SerialName("VG")
  public data object Vg : Country()
  /** Virgin Islands (U.S.) */
  @SerialName("VI")
  public data object Vi : Country()
  /** Viet Nam */
  @SerialName("VN")
  public data object Vn : Country()
  /** Vanuatu */
  @SerialName("VU")
  public data object Vu : Country()
  /** Wallis and Futuna */
  @SerialName("WF")
  public data object Wf : Country()
  /** Samoa */
  @SerialName("WS")
  public data object Ws : Country()
  /** Yemen */
  @SerialName("YE")
  public data object Ye : Country()
  /** Mayotte */
  @SerialName("YT")
  public data object Yt : Country()
  /** South Africa */
  @SerialName("ZA")
  public data object Za : Country()
  /** Zambia */
  @SerialName("ZM")
  public data object Zm : Country()
  /** Zimbabwe */
  @SerialName("ZW")
  public data object Zw : Country()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : Country()
}
