package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 국가 */
@Serializable(CountrySerializer::class)
public sealed interface Country {
  public val value: String
  /** Andorra */
  public data object Ad : Country {
    override val value: String = "AD"
  }
  /** United Arab Emirates (the) */
  public data object Ae : Country {
    override val value: String = "AE"
  }
  /** Afghanistan */
  public data object Af : Country {
    override val value: String = "AF"
  }
  /** Antigua and Barbuda */
  public data object Ag : Country {
    override val value: String = "AG"
  }
  /** Anguilla */
  public data object Ai : Country {
    override val value: String = "AI"
  }
  /** Albania */
  public data object Al : Country {
    override val value: String = "AL"
  }
  /** Armenia */
  public data object Am : Country {
    override val value: String = "AM"
  }
  /** Angola */
  public data object Ao : Country {
    override val value: String = "AO"
  }
  /** Antarctica */
  public data object Aq : Country {
    override val value: String = "AQ"
  }
  /** Argentina */
  public data object Ar : Country {
    override val value: String = "AR"
  }
  /** American Samoa */
  public data object As : Country {
    override val value: String = "AS"
  }
  /** Austria */
  public data object At : Country {
    override val value: String = "AT"
  }
  /** Australia */
  public data object Au : Country {
    override val value: String = "AU"
  }
  /** Aruba */
  public data object Aw : Country {
    override val value: String = "AW"
  }
  /** Åland Islands */
  public data object Ax : Country {
    override val value: String = "AX"
  }
  /** Azerbaijan */
  public data object Az : Country {
    override val value: String = "AZ"
  }
  /** Bosnia and Herzegovina */
  public data object Ba : Country {
    override val value: String = "BA"
  }
  /** Barbados */
  public data object Bb : Country {
    override val value: String = "BB"
  }
  /** Bangladesh */
  public data object Bd : Country {
    override val value: String = "BD"
  }
  /** Belgium */
  public data object Be : Country {
    override val value: String = "BE"
  }
  /** Burkina Faso */
  public data object Bf : Country {
    override val value: String = "BF"
  }
  /** Bulgaria */
  public data object Bg : Country {
    override val value: String = "BG"
  }
  /** Bahrain */
  public data object Bh : Country {
    override val value: String = "BH"
  }
  /** Burundi */
  public data object Bi : Country {
    override val value: String = "BI"
  }
  /** Benin */
  public data object Bj : Country {
    override val value: String = "BJ"
  }
  /** Saint Barthélemy */
  public data object Bl : Country {
    override val value: String = "BL"
  }
  /** Bermuda */
  public data object Bm : Country {
    override val value: String = "BM"
  }
  /** Brunei Darussalam */
  public data object Bn : Country {
    override val value: String = "BN"
  }
  /** Bolivia (Plurinational State of) */
  public data object Bo : Country {
    override val value: String = "BO"
  }
  /** Bonaire, Sint Eustatius and Saba */
  public data object Bq : Country {
    override val value: String = "BQ"
  }
  /** Brazil */
  public data object Br : Country {
    override val value: String = "BR"
  }
  /** Bahamas (the) */
  public data object Bs : Country {
    override val value: String = "BS"
  }
  /** Bhutan */
  public data object Bt : Country {
    override val value: String = "BT"
  }
  /** Bouvet Island */
  public data object Bv : Country {
    override val value: String = "BV"
  }
  /** Botswana */
  public data object Bw : Country {
    override val value: String = "BW"
  }
  /** Belarus */
  public data object By : Country {
    override val value: String = "BY"
  }
  /** Belize */
  public data object Bz : Country {
    override val value: String = "BZ"
  }
  /** Canada */
  public data object Ca : Country {
    override val value: String = "CA"
  }
  /** Cocos (Keeling) Islands (the) */
  public data object Cc : Country {
    override val value: String = "CC"
  }
  /** Congo (the Democratic Republic of the) */
  public data object Cd : Country {
    override val value: String = "CD"
  }
  /** Central African Republic (the) */
  public data object Cf : Country {
    override val value: String = "CF"
  }
  /** Congo (the) */
  public data object Cg : Country {
    override val value: String = "CG"
  }
  /** Switzerland */
  public data object Ch : Country {
    override val value: String = "CH"
  }
  /** Côte d'Ivoire */
  public data object Ci : Country {
    override val value: String = "CI"
  }
  /** Cook Islands (the) */
  public data object Ck : Country {
    override val value: String = "CK"
  }
  /** Chile */
  public data object Cl : Country {
    override val value: String = "CL"
  }
  /** Cameroon */
  public data object Cm : Country {
    override val value: String = "CM"
  }
  /** China */
  public data object Cn : Country {
    override val value: String = "CN"
  }
  /** Colombia */
  public data object Co : Country {
    override val value: String = "CO"
  }
  /** Costa Rica */
  public data object Cr : Country {
    override val value: String = "CR"
  }
  /** Cuba */
  public data object Cu : Country {
    override val value: String = "CU"
  }
  /** Cabo Verde */
  public data object Cv : Country {
    override val value: String = "CV"
  }
  /** Curaçao */
  public data object Cw : Country {
    override val value: String = "CW"
  }
  /** Christmas Island */
  public data object Cx : Country {
    override val value: String = "CX"
  }
  /** Cyprus */
  public data object Cy : Country {
    override val value: String = "CY"
  }
  /** Czechia */
  public data object Cz : Country {
    override val value: String = "CZ"
  }
  /** Germany */
  public data object De : Country {
    override val value: String = "DE"
  }
  /** Djibouti */
  public data object Dj : Country {
    override val value: String = "DJ"
  }
  /** Denmark */
  public data object Dk : Country {
    override val value: String = "DK"
  }
  /** Dominica */
  public data object Dm : Country {
    override val value: String = "DM"
  }
  /** Dominican Republic (the) */
  public data object Do : Country {
    override val value: String = "DO"
  }
  /** Algeria */
  public data object Dz : Country {
    override val value: String = "DZ"
  }
  /** Ecuador */
  public data object Ec : Country {
    override val value: String = "EC"
  }
  /** Estonia */
  public data object Ee : Country {
    override val value: String = "EE"
  }
  /** Egypt */
  public data object Eg : Country {
    override val value: String = "EG"
  }
  /** Western Sahara */
  public data object Eh : Country {
    override val value: String = "EH"
  }
  /** Eritrea */
  public data object Er : Country {
    override val value: String = "ER"
  }
  /** Spain */
  public data object Es : Country {
    override val value: String = "ES"
  }
  /** Ethiopia */
  public data object Et : Country {
    override val value: String = "ET"
  }
  /** Finland */
  public data object Fi : Country {
    override val value: String = "FI"
  }
  /** Fiji */
  public data object Fj : Country {
    override val value: String = "FJ"
  }
  /** Falkland Islands (the) [Malvinas] */
  public data object Fk : Country {
    override val value: String = "FK"
  }
  /** Micronesia (Federated States of) */
  public data object Fm : Country {
    override val value: String = "FM"
  }
  /** Faroe Islands (the) */
  public data object Fo : Country {
    override val value: String = "FO"
  }
  /** France */
  public data object Fr : Country {
    override val value: String = "FR"
  }
  /** Gabon */
  public data object Ga : Country {
    override val value: String = "GA"
  }
  /** United Kingdom of Great Britain and Northern Ireland (the) */
  public data object Gb : Country {
    override val value: String = "GB"
  }
  /** Grenada */
  public data object Gd : Country {
    override val value: String = "GD"
  }
  /** Georgia */
  public data object Ge : Country {
    override val value: String = "GE"
  }
  /** French Guiana */
  public data object Gf : Country {
    override val value: String = "GF"
  }
  /** Guernsey */
  public data object Gg : Country {
    override val value: String = "GG"
  }
  /** Ghana */
  public data object Gh : Country {
    override val value: String = "GH"
  }
  /** Gibraltar */
  public data object Gi : Country {
    override val value: String = "GI"
  }
  /** Greenland */
  public data object Gl : Country {
    override val value: String = "GL"
  }
  /** Gambia (the) */
  public data object Gm : Country {
    override val value: String = "GM"
  }
  /** Guinea */
  public data object Gn : Country {
    override val value: String = "GN"
  }
  /** Guadeloupe */
  public data object Gp : Country {
    override val value: String = "GP"
  }
  /** Equatorial Guinea */
  public data object Gq : Country {
    override val value: String = "GQ"
  }
  /** Greece */
  public data object Gr : Country {
    override val value: String = "GR"
  }
  /** South Georgia and the South Sandwich Islands */
  public data object Gs : Country {
    override val value: String = "GS"
  }
  /** Guatemala */
  public data object Gt : Country {
    override val value: String = "GT"
  }
  /** Guam */
  public data object Gu : Country {
    override val value: String = "GU"
  }
  /** Guinea-Bissau */
  public data object Gw : Country {
    override val value: String = "GW"
  }
  /** Guyana */
  public data object Gy : Country {
    override val value: String = "GY"
  }
  /** Hong Kong */
  public data object Hk : Country {
    override val value: String = "HK"
  }
  /** Heard Island and McDonald Islands */
  public data object Hm : Country {
    override val value: String = "HM"
  }
  /** Honduras */
  public data object Hn : Country {
    override val value: String = "HN"
  }
  /** Croatia */
  public data object Hr : Country {
    override val value: String = "HR"
  }
  /** Haiti */
  public data object Ht : Country {
    override val value: String = "HT"
  }
  /** Hungary */
  public data object Hu : Country {
    override val value: String = "HU"
  }
  /** Indonesia */
  public data object Id : Country {
    override val value: String = "ID"
  }
  /** Ireland */
  public data object Ie : Country {
    override val value: String = "IE"
  }
  /** Israel */
  public data object Il : Country {
    override val value: String = "IL"
  }
  /** Isle of Man */
  public data object Im : Country {
    override val value: String = "IM"
  }
  /** India */
  public data object In : Country {
    override val value: String = "IN"
  }
  /** British Indian Ocean Territory (the) */
  public data object Io : Country {
    override val value: String = "IO"
  }
  /** Iraq */
  public data object Iq : Country {
    override val value: String = "IQ"
  }
  /** Iran (Islamic Republic of) */
  public data object Ir : Country {
    override val value: String = "IR"
  }
  /** Iceland */
  public data object Is : Country {
    override val value: String = "IS"
  }
  /** Italy */
  public data object It : Country {
    override val value: String = "IT"
  }
  /** Jersey */
  public data object Je : Country {
    override val value: String = "JE"
  }
  /** Jamaica */
  public data object Jm : Country {
    override val value: String = "JM"
  }
  /** Jordan */
  public data object Jo : Country {
    override val value: String = "JO"
  }
  /** Japan */
  public data object Jp : Country {
    override val value: String = "JP"
  }
  /** Kenya */
  public data object Ke : Country {
    override val value: String = "KE"
  }
  /** Kyrgyzstan */
  public data object Kg : Country {
    override val value: String = "KG"
  }
  /** Cambodia */
  public data object Kh : Country {
    override val value: String = "KH"
  }
  /** Kiribati */
  public data object Ki : Country {
    override val value: String = "KI"
  }
  /** Comoros (the) */
  public data object Km : Country {
    override val value: String = "KM"
  }
  /** Saint Kitts and Nevis */
  public data object Kn : Country {
    override val value: String = "KN"
  }
  /** Korea (the Democratic People's Republic of) */
  public data object Kp : Country {
    override val value: String = "KP"
  }
  /** Korea (the Republic of) */
  public data object Kr : Country {
    override val value: String = "KR"
  }
  /** Kuwait */
  public data object Kw : Country {
    override val value: String = "KW"
  }
  /** Cayman Islands (the) */
  public data object Ky : Country {
    override val value: String = "KY"
  }
  /** Kazakhstan */
  public data object Kz : Country {
    override val value: String = "KZ"
  }
  /** Lao People's Democratic Republic (the) */
  public data object La : Country {
    override val value: String = "LA"
  }
  /** Lebanon */
  public data object Lb : Country {
    override val value: String = "LB"
  }
  /** Saint Lucia */
  public data object Lc : Country {
    override val value: String = "LC"
  }
  /** Liechtenstein */
  public data object Li : Country {
    override val value: String = "LI"
  }
  /** Sri Lanka */
  public data object Lk : Country {
    override val value: String = "LK"
  }
  /** Liberia */
  public data object Lr : Country {
    override val value: String = "LR"
  }
  /** Lesotho */
  public data object Ls : Country {
    override val value: String = "LS"
  }
  /** Lithuania */
  public data object Lt : Country {
    override val value: String = "LT"
  }
  /** Luxembourg */
  public data object Lu : Country {
    override val value: String = "LU"
  }
  /** Latvia */
  public data object Lv : Country {
    override val value: String = "LV"
  }
  /** Libya */
  public data object Ly : Country {
    override val value: String = "LY"
  }
  /** Morocco */
  public data object Ma : Country {
    override val value: String = "MA"
  }
  /** Monaco */
  public data object Mc : Country {
    override val value: String = "MC"
  }
  /** Moldova (the Republic of) */
  public data object Md : Country {
    override val value: String = "MD"
  }
  /** Montenegro */
  public data object Me : Country {
    override val value: String = "ME"
  }
  /** Saint Martin (French part) */
  public data object Mf : Country {
    override val value: String = "MF"
  }
  /** Madagascar */
  public data object Mg : Country {
    override val value: String = "MG"
  }
  /** Marshall Islands (the) */
  public data object Mh : Country {
    override val value: String = "MH"
  }
  /** North Macedonia */
  public data object Mk : Country {
    override val value: String = "MK"
  }
  /** Mali */
  public data object Ml : Country {
    override val value: String = "ML"
  }
  /** Myanmar */
  public data object Mm : Country {
    override val value: String = "MM"
  }
  /** Mongolia */
  public data object Mn : Country {
    override val value: String = "MN"
  }
  /** Macao */
  public data object Mo : Country {
    override val value: String = "MO"
  }
  /** Northern Mariana Islands (the) */
  public data object Mp : Country {
    override val value: String = "MP"
  }
  /** Martinique */
  public data object Mq : Country {
    override val value: String = "MQ"
  }
  /** Mauritania */
  public data object Mr : Country {
    override val value: String = "MR"
  }
  /** Montserrat */
  public data object Ms : Country {
    override val value: String = "MS"
  }
  /** Malta */
  public data object Mt : Country {
    override val value: String = "MT"
  }
  /** Mauritius */
  public data object Mu : Country {
    override val value: String = "MU"
  }
  /** Maldives */
  public data object Mv : Country {
    override val value: String = "MV"
  }
  /** Malawi */
  public data object Mw : Country {
    override val value: String = "MW"
  }
  /** Mexico */
  public data object Mx : Country {
    override val value: String = "MX"
  }
  /** Malaysia */
  public data object My : Country {
    override val value: String = "MY"
  }
  /** Mozambique */
  public data object Mz : Country {
    override val value: String = "MZ"
  }
  /** Namibia */
  public data object Na : Country {
    override val value: String = "NA"
  }
  /** New Caledonia */
  public data object Nc : Country {
    override val value: String = "NC"
  }
  /** Niger (the) */
  public data object Ne : Country {
    override val value: String = "NE"
  }
  /** Norfolk Island */
  public data object Nf : Country {
    override val value: String = "NF"
  }
  /** Nigeria */
  public data object Ng : Country {
    override val value: String = "NG"
  }
  /** Nicaragua */
  public data object Ni : Country {
    override val value: String = "NI"
  }
  /** Netherlands (Kingdom of the) */
  public data object Nl : Country {
    override val value: String = "NL"
  }
  /** Norway */
  public data object No : Country {
    override val value: String = "NO"
  }
  /** Nepal */
  public data object Np : Country {
    override val value: String = "NP"
  }
  /** Nauru */
  public data object Nr : Country {
    override val value: String = "NR"
  }
  /** Niue */
  public data object Nu : Country {
    override val value: String = "NU"
  }
  /** New Zealand */
  public data object Nz : Country {
    override val value: String = "NZ"
  }
  /** Oman */
  public data object Om : Country {
    override val value: String = "OM"
  }
  /** Panama */
  public data object Pa : Country {
    override val value: String = "PA"
  }
  /** Peru */
  public data object Pe : Country {
    override val value: String = "PE"
  }
  /** French Polynesia */
  public data object Pf : Country {
    override val value: String = "PF"
  }
  /** Papua New Guinea */
  public data object Pg : Country {
    override val value: String = "PG"
  }
  /** Philippines (the) */
  public data object Ph : Country {
    override val value: String = "PH"
  }
  /** Pakistan */
  public data object Pk : Country {
    override val value: String = "PK"
  }
  /** Poland */
  public data object Pl : Country {
    override val value: String = "PL"
  }
  /** Saint Pierre and Miquelon */
  public data object Pm : Country {
    override val value: String = "PM"
  }
  /** Pitcairn */
  public data object Pn : Country {
    override val value: String = "PN"
  }
  /** Puerto Rico */
  public data object Pr : Country {
    override val value: String = "PR"
  }
  /** Palestine, State of */
  public data object Ps : Country {
    override val value: String = "PS"
  }
  /** Portugal */
  public data object Pt : Country {
    override val value: String = "PT"
  }
  /** Palau */
  public data object Pw : Country {
    override val value: String = "PW"
  }
  /** Paraguay */
  public data object Py : Country {
    override val value: String = "PY"
  }
  /** Qatar */
  public data object Qa : Country {
    override val value: String = "QA"
  }
  /** Réunion */
  public data object Re : Country {
    override val value: String = "RE"
  }
  /** Romania */
  public data object Ro : Country {
    override val value: String = "RO"
  }
  /** Serbia */
  public data object Rs : Country {
    override val value: String = "RS"
  }
  /** Russian Federation (the) */
  public data object Ru : Country {
    override val value: String = "RU"
  }
  /** Rwanda */
  public data object Rw : Country {
    override val value: String = "RW"
  }
  /** Saudi Arabia */
  public data object Sa : Country {
    override val value: String = "SA"
  }
  /** Solomon Islands */
  public data object Sb : Country {
    override val value: String = "SB"
  }
  /** Seychelles */
  public data object Sc : Country {
    override val value: String = "SC"
  }
  /** Sudan (the) */
  public data object Sd : Country {
    override val value: String = "SD"
  }
  /** Sweden */
  public data object Se : Country {
    override val value: String = "SE"
  }
  /** Singapore */
  public data object Sg : Country {
    override val value: String = "SG"
  }
  /** Saint Helena, Ascension and Tristan da Cunha */
  public data object Sh : Country {
    override val value: String = "SH"
  }
  /** Slovenia */
  public data object Si : Country {
    override val value: String = "SI"
  }
  /** Svalbard and Jan Mayen */
  public data object Sj : Country {
    override val value: String = "SJ"
  }
  /** Slovakia */
  public data object Sk : Country {
    override val value: String = "SK"
  }
  /** Sierra Leone */
  public data object Sl : Country {
    override val value: String = "SL"
  }
  /** San Marino */
  public data object Sm : Country {
    override val value: String = "SM"
  }
  /** Senegal */
  public data object Sn : Country {
    override val value: String = "SN"
  }
  /** Somalia */
  public data object So : Country {
    override val value: String = "SO"
  }
  /** Suriname */
  public data object Sr : Country {
    override val value: String = "SR"
  }
  /** South Sudan */
  public data object Ss : Country {
    override val value: String = "SS"
  }
  /** Sao Tome and Principe */
  public data object St : Country {
    override val value: String = "ST"
  }
  /** El Salvador */
  public data object Sv : Country {
    override val value: String = "SV"
  }
  /** Sint Maarten (Dutch part) */
  public data object Sx : Country {
    override val value: String = "SX"
  }
  /** Syrian Arab Republic (the) */
  public data object Sy : Country {
    override val value: String = "SY"
  }
  /** Eswatini */
  public data object Sz : Country {
    override val value: String = "SZ"
  }
  /** Turks and Caicos Islands (the) */
  public data object Tc : Country {
    override val value: String = "TC"
  }
  /** Chad */
  public data object Td : Country {
    override val value: String = "TD"
  }
  /** French Southern Territories (the) */
  public data object Tf : Country {
    override val value: String = "TF"
  }
  /** Togo */
  public data object Tg : Country {
    override val value: String = "TG"
  }
  /** Thailand */
  public data object Th : Country {
    override val value: String = "TH"
  }
  /** Tajikistan */
  public data object Tj : Country {
    override val value: String = "TJ"
  }
  /** Tokelau */
  public data object Tk : Country {
    override val value: String = "TK"
  }
  /** Timor-Leste */
  public data object Tl : Country {
    override val value: String = "TL"
  }
  /** Turkmenistan */
  public data object Tm : Country {
    override val value: String = "TM"
  }
  /** Tunisia */
  public data object Tn : Country {
    override val value: String = "TN"
  }
  /** Tonga */
  public data object To : Country {
    override val value: String = "TO"
  }
  /** Türkiye */
  public data object Tr : Country {
    override val value: String = "TR"
  }
  /** Trinidad and Tobago */
  public data object Tt : Country {
    override val value: String = "TT"
  }
  /** Tuvalu */
  public data object Tv : Country {
    override val value: String = "TV"
  }
  /** Taiwan (Province of China) */
  public data object Tw : Country {
    override val value: String = "TW"
  }
  /** Tanzania, the United Republic of */
  public data object Tz : Country {
    override val value: String = "TZ"
  }
  /** Ukraine */
  public data object Ua : Country {
    override val value: String = "UA"
  }
  /** Uganda */
  public data object Ug : Country {
    override val value: String = "UG"
  }
  /** United States Minor Outlying Islands (the) */
  public data object Um : Country {
    override val value: String = "UM"
  }
  /** United States of America (the) */
  public data object Us : Country {
    override val value: String = "US"
  }
  /** Uruguay */
  public data object Uy : Country {
    override val value: String = "UY"
  }
  /** Uzbekistan */
  public data object Uz : Country {
    override val value: String = "UZ"
  }
  /** Holy See (the) */
  public data object Va : Country {
    override val value: String = "VA"
  }
  /** Saint Vincent and the Grenadines */
  public data object Vc : Country {
    override val value: String = "VC"
  }
  /** Venezuela (Bolivarian Republic of) */
  public data object Ve : Country {
    override val value: String = "VE"
  }
  /** Virgin Islands (British) */
  public data object Vg : Country {
    override val value: String = "VG"
  }
  /** Virgin Islands (U.S.) */
  public data object Vi : Country {
    override val value: String = "VI"
  }
  /** Viet Nam */
  public data object Vn : Country {
    override val value: String = "VN"
  }
  /** Vanuatu */
  public data object Vu : Country {
    override val value: String = "VU"
  }
  /** Wallis and Futuna */
  public data object Wf : Country {
    override val value: String = "WF"
  }
  /** Samoa */
  public data object Ws : Country {
    override val value: String = "WS"
  }
  /** Yemen */
  public data object Ye : Country {
    override val value: String = "YE"
  }
  /** Mayotte */
  public data object Yt : Country {
    override val value: String = "YT"
  }
  /** South Africa */
  public data object Za : Country {
    override val value: String = "ZA"
  }
  /** Zambia */
  public data object Zm : Country {
    override val value: String = "ZM"
  }
  /** Zimbabwe */
  public data object Zw : Country {
    override val value: String = "ZW"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Country
}


private object CountrySerializer : KSerializer<Country> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Country::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): Country {
    val value = decoder.decodeString()
    return when (value) {
      "AD" -> Country.Ad
      "AE" -> Country.Ae
      "AF" -> Country.Af
      "AG" -> Country.Ag
      "AI" -> Country.Ai
      "AL" -> Country.Al
      "AM" -> Country.Am
      "AO" -> Country.Ao
      "AQ" -> Country.Aq
      "AR" -> Country.Ar
      "AS" -> Country.As
      "AT" -> Country.At
      "AU" -> Country.Au
      "AW" -> Country.Aw
      "AX" -> Country.Ax
      "AZ" -> Country.Az
      "BA" -> Country.Ba
      "BB" -> Country.Bb
      "BD" -> Country.Bd
      "BE" -> Country.Be
      "BF" -> Country.Bf
      "BG" -> Country.Bg
      "BH" -> Country.Bh
      "BI" -> Country.Bi
      "BJ" -> Country.Bj
      "BL" -> Country.Bl
      "BM" -> Country.Bm
      "BN" -> Country.Bn
      "BO" -> Country.Bo
      "BQ" -> Country.Bq
      "BR" -> Country.Br
      "BS" -> Country.Bs
      "BT" -> Country.Bt
      "BV" -> Country.Bv
      "BW" -> Country.Bw
      "BY" -> Country.By
      "BZ" -> Country.Bz
      "CA" -> Country.Ca
      "CC" -> Country.Cc
      "CD" -> Country.Cd
      "CF" -> Country.Cf
      "CG" -> Country.Cg
      "CH" -> Country.Ch
      "CI" -> Country.Ci
      "CK" -> Country.Ck
      "CL" -> Country.Cl
      "CM" -> Country.Cm
      "CN" -> Country.Cn
      "CO" -> Country.Co
      "CR" -> Country.Cr
      "CU" -> Country.Cu
      "CV" -> Country.Cv
      "CW" -> Country.Cw
      "CX" -> Country.Cx
      "CY" -> Country.Cy
      "CZ" -> Country.Cz
      "DE" -> Country.De
      "DJ" -> Country.Dj
      "DK" -> Country.Dk
      "DM" -> Country.Dm
      "DO" -> Country.Do
      "DZ" -> Country.Dz
      "EC" -> Country.Ec
      "EE" -> Country.Ee
      "EG" -> Country.Eg
      "EH" -> Country.Eh
      "ER" -> Country.Er
      "ES" -> Country.Es
      "ET" -> Country.Et
      "FI" -> Country.Fi
      "FJ" -> Country.Fj
      "FK" -> Country.Fk
      "FM" -> Country.Fm
      "FO" -> Country.Fo
      "FR" -> Country.Fr
      "GA" -> Country.Ga
      "GB" -> Country.Gb
      "GD" -> Country.Gd
      "GE" -> Country.Ge
      "GF" -> Country.Gf
      "GG" -> Country.Gg
      "GH" -> Country.Gh
      "GI" -> Country.Gi
      "GL" -> Country.Gl
      "GM" -> Country.Gm
      "GN" -> Country.Gn
      "GP" -> Country.Gp
      "GQ" -> Country.Gq
      "GR" -> Country.Gr
      "GS" -> Country.Gs
      "GT" -> Country.Gt
      "GU" -> Country.Gu
      "GW" -> Country.Gw
      "GY" -> Country.Gy
      "HK" -> Country.Hk
      "HM" -> Country.Hm
      "HN" -> Country.Hn
      "HR" -> Country.Hr
      "HT" -> Country.Ht
      "HU" -> Country.Hu
      "ID" -> Country.Id
      "IE" -> Country.Ie
      "IL" -> Country.Il
      "IM" -> Country.Im
      "IN" -> Country.In
      "IO" -> Country.Io
      "IQ" -> Country.Iq
      "IR" -> Country.Ir
      "IS" -> Country.Is
      "IT" -> Country.It
      "JE" -> Country.Je
      "JM" -> Country.Jm
      "JO" -> Country.Jo
      "JP" -> Country.Jp
      "KE" -> Country.Ke
      "KG" -> Country.Kg
      "KH" -> Country.Kh
      "KI" -> Country.Ki
      "KM" -> Country.Km
      "KN" -> Country.Kn
      "KP" -> Country.Kp
      "KR" -> Country.Kr
      "KW" -> Country.Kw
      "KY" -> Country.Ky
      "KZ" -> Country.Kz
      "LA" -> Country.La
      "LB" -> Country.Lb
      "LC" -> Country.Lc
      "LI" -> Country.Li
      "LK" -> Country.Lk
      "LR" -> Country.Lr
      "LS" -> Country.Ls
      "LT" -> Country.Lt
      "LU" -> Country.Lu
      "LV" -> Country.Lv
      "LY" -> Country.Ly
      "MA" -> Country.Ma
      "MC" -> Country.Mc
      "MD" -> Country.Md
      "ME" -> Country.Me
      "MF" -> Country.Mf
      "MG" -> Country.Mg
      "MH" -> Country.Mh
      "MK" -> Country.Mk
      "ML" -> Country.Ml
      "MM" -> Country.Mm
      "MN" -> Country.Mn
      "MO" -> Country.Mo
      "MP" -> Country.Mp
      "MQ" -> Country.Mq
      "MR" -> Country.Mr
      "MS" -> Country.Ms
      "MT" -> Country.Mt
      "MU" -> Country.Mu
      "MV" -> Country.Mv
      "MW" -> Country.Mw
      "MX" -> Country.Mx
      "MY" -> Country.My
      "MZ" -> Country.Mz
      "NA" -> Country.Na
      "NC" -> Country.Nc
      "NE" -> Country.Ne
      "NF" -> Country.Nf
      "NG" -> Country.Ng
      "NI" -> Country.Ni
      "NL" -> Country.Nl
      "NO" -> Country.No
      "NP" -> Country.Np
      "NR" -> Country.Nr
      "NU" -> Country.Nu
      "NZ" -> Country.Nz
      "OM" -> Country.Om
      "PA" -> Country.Pa
      "PE" -> Country.Pe
      "PF" -> Country.Pf
      "PG" -> Country.Pg
      "PH" -> Country.Ph
      "PK" -> Country.Pk
      "PL" -> Country.Pl
      "PM" -> Country.Pm
      "PN" -> Country.Pn
      "PR" -> Country.Pr
      "PS" -> Country.Ps
      "PT" -> Country.Pt
      "PW" -> Country.Pw
      "PY" -> Country.Py
      "QA" -> Country.Qa
      "RE" -> Country.Re
      "RO" -> Country.Ro
      "RS" -> Country.Rs
      "RU" -> Country.Ru
      "RW" -> Country.Rw
      "SA" -> Country.Sa
      "SB" -> Country.Sb
      "SC" -> Country.Sc
      "SD" -> Country.Sd
      "SE" -> Country.Se
      "SG" -> Country.Sg
      "SH" -> Country.Sh
      "SI" -> Country.Si
      "SJ" -> Country.Sj
      "SK" -> Country.Sk
      "SL" -> Country.Sl
      "SM" -> Country.Sm
      "SN" -> Country.Sn
      "SO" -> Country.So
      "SR" -> Country.Sr
      "SS" -> Country.Ss
      "ST" -> Country.St
      "SV" -> Country.Sv
      "SX" -> Country.Sx
      "SY" -> Country.Sy
      "SZ" -> Country.Sz
      "TC" -> Country.Tc
      "TD" -> Country.Td
      "TF" -> Country.Tf
      "TG" -> Country.Tg
      "TH" -> Country.Th
      "TJ" -> Country.Tj
      "TK" -> Country.Tk
      "TL" -> Country.Tl
      "TM" -> Country.Tm
      "TN" -> Country.Tn
      "TO" -> Country.To
      "TR" -> Country.Tr
      "TT" -> Country.Tt
      "TV" -> Country.Tv
      "TW" -> Country.Tw
      "TZ" -> Country.Tz
      "UA" -> Country.Ua
      "UG" -> Country.Ug
      "UM" -> Country.Um
      "US" -> Country.Us
      "UY" -> Country.Uy
      "UZ" -> Country.Uz
      "VA" -> Country.Va
      "VC" -> Country.Vc
      "VE" -> Country.Ve
      "VG" -> Country.Vg
      "VI" -> Country.Vi
      "VN" -> Country.Vn
      "VU" -> Country.Vu
      "WF" -> Country.Wf
      "WS" -> Country.Ws
      "YE" -> Country.Ye
      "YT" -> Country.Yt
      "ZA" -> Country.Za
      "ZM" -> Country.Zm
      "ZW" -> Country.Zw
      else -> Country.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: Country) = encoder.encodeString(value.value)
}
