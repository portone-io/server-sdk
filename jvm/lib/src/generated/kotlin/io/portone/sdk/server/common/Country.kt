package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 국가 */
@Serializable
public sealed interface Country {
  public val value: String
  /** Andorra */
  @SerialName("AD")
  public data object Ad : Country {
    override val value: String = "AD"
  }
  /** United Arab Emirates (the) */
  @SerialName("AE")
  public data object Ae : Country {
    override val value: String = "AE"
  }
  /** Afghanistan */
  @SerialName("AF")
  public data object Af : Country {
    override val value: String = "AF"
  }
  /** Antigua and Barbuda */
  @SerialName("AG")
  public data object Ag : Country {
    override val value: String = "AG"
  }
  /** Anguilla */
  @SerialName("AI")
  public data object Ai : Country {
    override val value: String = "AI"
  }
  /** Albania */
  @SerialName("AL")
  public data object Al : Country {
    override val value: String = "AL"
  }
  /** Armenia */
  @SerialName("AM")
  public data object Am : Country {
    override val value: String = "AM"
  }
  /** Angola */
  @SerialName("AO")
  public data object Ao : Country {
    override val value: String = "AO"
  }
  /** Antarctica */
  @SerialName("AQ")
  public data object Aq : Country {
    override val value: String = "AQ"
  }
  /** Argentina */
  @SerialName("AR")
  public data object Ar : Country {
    override val value: String = "AR"
  }
  /** American Samoa */
  @SerialName("AS")
  public data object As : Country {
    override val value: String = "AS"
  }
  /** Austria */
  @SerialName("AT")
  public data object At : Country {
    override val value: String = "AT"
  }
  /** Australia */
  @SerialName("AU")
  public data object Au : Country {
    override val value: String = "AU"
  }
  /** Aruba */
  @SerialName("AW")
  public data object Aw : Country {
    override val value: String = "AW"
  }
  /** Åland Islands */
  @SerialName("AX")
  public data object Ax : Country {
    override val value: String = "AX"
  }
  /** Azerbaijan */
  @SerialName("AZ")
  public data object Az : Country {
    override val value: String = "AZ"
  }
  /** Bosnia and Herzegovina */
  @SerialName("BA")
  public data object Ba : Country {
    override val value: String = "BA"
  }
  /** Barbados */
  @SerialName("BB")
  public data object Bb : Country {
    override val value: String = "BB"
  }
  /** Bangladesh */
  @SerialName("BD")
  public data object Bd : Country {
    override val value: String = "BD"
  }
  /** Belgium */
  @SerialName("BE")
  public data object Be : Country {
    override val value: String = "BE"
  }
  /** Burkina Faso */
  @SerialName("BF")
  public data object Bf : Country {
    override val value: String = "BF"
  }
  /** Bulgaria */
  @SerialName("BG")
  public data object Bg : Country {
    override val value: String = "BG"
  }
  /** Bahrain */
  @SerialName("BH")
  public data object Bh : Country {
    override val value: String = "BH"
  }
  /** Burundi */
  @SerialName("BI")
  public data object Bi : Country {
    override val value: String = "BI"
  }
  /** Benin */
  @SerialName("BJ")
  public data object Bj : Country {
    override val value: String = "BJ"
  }
  /** Saint Barthélemy */
  @SerialName("BL")
  public data object Bl : Country {
    override val value: String = "BL"
  }
  /** Bermuda */
  @SerialName("BM")
  public data object Bm : Country {
    override val value: String = "BM"
  }
  /** Brunei Darussalam */
  @SerialName("BN")
  public data object Bn : Country {
    override val value: String = "BN"
  }
  /** Bolivia (Plurinational State of) */
  @SerialName("BO")
  public data object Bo : Country {
    override val value: String = "BO"
  }
  /** Bonaire, Sint Eustatius and Saba */
  @SerialName("BQ")
  public data object Bq : Country {
    override val value: String = "BQ"
  }
  /** Brazil */
  @SerialName("BR")
  public data object Br : Country {
    override val value: String = "BR"
  }
  /** Bahamas (the) */
  @SerialName("BS")
  public data object Bs : Country {
    override val value: String = "BS"
  }
  /** Bhutan */
  @SerialName("BT")
  public data object Bt : Country {
    override val value: String = "BT"
  }
  /** Bouvet Island */
  @SerialName("BV")
  public data object Bv : Country {
    override val value: String = "BV"
  }
  /** Botswana */
  @SerialName("BW")
  public data object Bw : Country {
    override val value: String = "BW"
  }
  /** Belarus */
  @SerialName("BY")
  public data object By : Country {
    override val value: String = "BY"
  }
  /** Belize */
  @SerialName("BZ")
  public data object Bz : Country {
    override val value: String = "BZ"
  }
  /** Canada */
  @SerialName("CA")
  public data object Ca : Country {
    override val value: String = "CA"
  }
  /** Cocos (Keeling) Islands (the) */
  @SerialName("CC")
  public data object Cc : Country {
    override val value: String = "CC"
  }
  /** Congo (the Democratic Republic of the) */
  @SerialName("CD")
  public data object Cd : Country {
    override val value: String = "CD"
  }
  /** Central African Republic (the) */
  @SerialName("CF")
  public data object Cf : Country {
    override val value: String = "CF"
  }
  /** Congo (the) */
  @SerialName("CG")
  public data object Cg : Country {
    override val value: String = "CG"
  }
  /** Switzerland */
  @SerialName("CH")
  public data object Ch : Country {
    override val value: String = "CH"
  }
  /** Côte d'Ivoire */
  @SerialName("CI")
  public data object Ci : Country {
    override val value: String = "CI"
  }
  /** Cook Islands (the) */
  @SerialName("CK")
  public data object Ck : Country {
    override val value: String = "CK"
  }
  /** Chile */
  @SerialName("CL")
  public data object Cl : Country {
    override val value: String = "CL"
  }
  /** Cameroon */
  @SerialName("CM")
  public data object Cm : Country {
    override val value: String = "CM"
  }
  /** China */
  @SerialName("CN")
  public data object Cn : Country {
    override val value: String = "CN"
  }
  /** Colombia */
  @SerialName("CO")
  public data object Co : Country {
    override val value: String = "CO"
  }
  /** Costa Rica */
  @SerialName("CR")
  public data object Cr : Country {
    override val value: String = "CR"
  }
  /** Cuba */
  @SerialName("CU")
  public data object Cu : Country {
    override val value: String = "CU"
  }
  /** Cabo Verde */
  @SerialName("CV")
  public data object Cv : Country {
    override val value: String = "CV"
  }
  /** Curaçao */
  @SerialName("CW")
  public data object Cw : Country {
    override val value: String = "CW"
  }
  /** Christmas Island */
  @SerialName("CX")
  public data object Cx : Country {
    override val value: String = "CX"
  }
  /** Cyprus */
  @SerialName("CY")
  public data object Cy : Country {
    override val value: String = "CY"
  }
  /** Czechia */
  @SerialName("CZ")
  public data object Cz : Country {
    override val value: String = "CZ"
  }
  /** Germany */
  @SerialName("DE")
  public data object De : Country {
    override val value: String = "DE"
  }
  /** Djibouti */
  @SerialName("DJ")
  public data object Dj : Country {
    override val value: String = "DJ"
  }
  /** Denmark */
  @SerialName("DK")
  public data object Dk : Country {
    override val value: String = "DK"
  }
  /** Dominica */
  @SerialName("DM")
  public data object Dm : Country {
    override val value: String = "DM"
  }
  /** Dominican Republic (the) */
  @SerialName("DO")
  public data object Do : Country {
    override val value: String = "DO"
  }
  /** Algeria */
  @SerialName("DZ")
  public data object Dz : Country {
    override val value: String = "DZ"
  }
  /** Ecuador */
  @SerialName("EC")
  public data object Ec : Country {
    override val value: String = "EC"
  }
  /** Estonia */
  @SerialName("EE")
  public data object Ee : Country {
    override val value: String = "EE"
  }
  /** Egypt */
  @SerialName("EG")
  public data object Eg : Country {
    override val value: String = "EG"
  }
  /** Western Sahara */
  @SerialName("EH")
  public data object Eh : Country {
    override val value: String = "EH"
  }
  /** Eritrea */
  @SerialName("ER")
  public data object Er : Country {
    override val value: String = "ER"
  }
  /** Spain */
  @SerialName("ES")
  public data object Es : Country {
    override val value: String = "ES"
  }
  /** Ethiopia */
  @SerialName("ET")
  public data object Et : Country {
    override val value: String = "ET"
  }
  /** Finland */
  @SerialName("FI")
  public data object Fi : Country {
    override val value: String = "FI"
  }
  /** Fiji */
  @SerialName("FJ")
  public data object Fj : Country {
    override val value: String = "FJ"
  }
  /** Falkland Islands (the) [Malvinas] */
  @SerialName("FK")
  public data object Fk : Country {
    override val value: String = "FK"
  }
  /** Micronesia (Federated States of) */
  @SerialName("FM")
  public data object Fm : Country {
    override val value: String = "FM"
  }
  /** Faroe Islands (the) */
  @SerialName("FO")
  public data object Fo : Country {
    override val value: String = "FO"
  }
  /** France */
  @SerialName("FR")
  public data object Fr : Country {
    override val value: String = "FR"
  }
  /** Gabon */
  @SerialName("GA")
  public data object Ga : Country {
    override val value: String = "GA"
  }
  /** United Kingdom of Great Britain and Northern Ireland (the) */
  @SerialName("GB")
  public data object Gb : Country {
    override val value: String = "GB"
  }
  /** Grenada */
  @SerialName("GD")
  public data object Gd : Country {
    override val value: String = "GD"
  }
  /** Georgia */
  @SerialName("GE")
  public data object Ge : Country {
    override val value: String = "GE"
  }
  /** French Guiana */
  @SerialName("GF")
  public data object Gf : Country {
    override val value: String = "GF"
  }
  /** Guernsey */
  @SerialName("GG")
  public data object Gg : Country {
    override val value: String = "GG"
  }
  /** Ghana */
  @SerialName("GH")
  public data object Gh : Country {
    override val value: String = "GH"
  }
  /** Gibraltar */
  @SerialName("GI")
  public data object Gi : Country {
    override val value: String = "GI"
  }
  /** Greenland */
  @SerialName("GL")
  public data object Gl : Country {
    override val value: String = "GL"
  }
  /** Gambia (the) */
  @SerialName("GM")
  public data object Gm : Country {
    override val value: String = "GM"
  }
  /** Guinea */
  @SerialName("GN")
  public data object Gn : Country {
    override val value: String = "GN"
  }
  /** Guadeloupe */
  @SerialName("GP")
  public data object Gp : Country {
    override val value: String = "GP"
  }
  /** Equatorial Guinea */
  @SerialName("GQ")
  public data object Gq : Country {
    override val value: String = "GQ"
  }
  /** Greece */
  @SerialName("GR")
  public data object Gr : Country {
    override val value: String = "GR"
  }
  /** South Georgia and the South Sandwich Islands */
  @SerialName("GS")
  public data object Gs : Country {
    override val value: String = "GS"
  }
  /** Guatemala */
  @SerialName("GT")
  public data object Gt : Country {
    override val value: String = "GT"
  }
  /** Guam */
  @SerialName("GU")
  public data object Gu : Country {
    override val value: String = "GU"
  }
  /** Guinea-Bissau */
  @SerialName("GW")
  public data object Gw : Country {
    override val value: String = "GW"
  }
  /** Guyana */
  @SerialName("GY")
  public data object Gy : Country {
    override val value: String = "GY"
  }
  /** Hong Kong */
  @SerialName("HK")
  public data object Hk : Country {
    override val value: String = "HK"
  }
  /** Heard Island and McDonald Islands */
  @SerialName("HM")
  public data object Hm : Country {
    override val value: String = "HM"
  }
  /** Honduras */
  @SerialName("HN")
  public data object Hn : Country {
    override val value: String = "HN"
  }
  /** Croatia */
  @SerialName("HR")
  public data object Hr : Country {
    override val value: String = "HR"
  }
  /** Haiti */
  @SerialName("HT")
  public data object Ht : Country {
    override val value: String = "HT"
  }
  /** Hungary */
  @SerialName("HU")
  public data object Hu : Country {
    override val value: String = "HU"
  }
  /** Indonesia */
  @SerialName("ID")
  public data object Id : Country {
    override val value: String = "ID"
  }
  /** Ireland */
  @SerialName("IE")
  public data object Ie : Country {
    override val value: String = "IE"
  }
  /** Israel */
  @SerialName("IL")
  public data object Il : Country {
    override val value: String = "IL"
  }
  /** Isle of Man */
  @SerialName("IM")
  public data object Im : Country {
    override val value: String = "IM"
  }
  /** India */
  @SerialName("IN")
  public data object In : Country {
    override val value: String = "IN"
  }
  /** British Indian Ocean Territory (the) */
  @SerialName("IO")
  public data object Io : Country {
    override val value: String = "IO"
  }
  /** Iraq */
  @SerialName("IQ")
  public data object Iq : Country {
    override val value: String = "IQ"
  }
  /** Iran (Islamic Republic of) */
  @SerialName("IR")
  public data object Ir : Country {
    override val value: String = "IR"
  }
  /** Iceland */
  @SerialName("IS")
  public data object Is : Country {
    override val value: String = "IS"
  }
  /** Italy */
  @SerialName("IT")
  public data object It : Country {
    override val value: String = "IT"
  }
  /** Jersey */
  @SerialName("JE")
  public data object Je : Country {
    override val value: String = "JE"
  }
  /** Jamaica */
  @SerialName("JM")
  public data object Jm : Country {
    override val value: String = "JM"
  }
  /** Jordan */
  @SerialName("JO")
  public data object Jo : Country {
    override val value: String = "JO"
  }
  /** Japan */
  @SerialName("JP")
  public data object Jp : Country {
    override val value: String = "JP"
  }
  /** Kenya */
  @SerialName("KE")
  public data object Ke : Country {
    override val value: String = "KE"
  }
  /** Kyrgyzstan */
  @SerialName("KG")
  public data object Kg : Country {
    override val value: String = "KG"
  }
  /** Cambodia */
  @SerialName("KH")
  public data object Kh : Country {
    override val value: String = "KH"
  }
  /** Kiribati */
  @SerialName("KI")
  public data object Ki : Country {
    override val value: String = "KI"
  }
  /** Comoros (the) */
  @SerialName("KM")
  public data object Km : Country {
    override val value: String = "KM"
  }
  /** Saint Kitts and Nevis */
  @SerialName("KN")
  public data object Kn : Country {
    override val value: String = "KN"
  }
  /** Korea (the Democratic People's Republic of) */
  @SerialName("KP")
  public data object Kp : Country {
    override val value: String = "KP"
  }
  /** Korea (the Republic of) */
  @SerialName("KR")
  public data object Kr : Country {
    override val value: String = "KR"
  }
  /** Kuwait */
  @SerialName("KW")
  public data object Kw : Country {
    override val value: String = "KW"
  }
  /** Cayman Islands (the) */
  @SerialName("KY")
  public data object Ky : Country {
    override val value: String = "KY"
  }
  /** Kazakhstan */
  @SerialName("KZ")
  public data object Kz : Country {
    override val value: String = "KZ"
  }
  /** Lao People's Democratic Republic (the) */
  @SerialName("LA")
  public data object La : Country {
    override val value: String = "LA"
  }
  /** Lebanon */
  @SerialName("LB")
  public data object Lb : Country {
    override val value: String = "LB"
  }
  /** Saint Lucia */
  @SerialName("LC")
  public data object Lc : Country {
    override val value: String = "LC"
  }
  /** Liechtenstein */
  @SerialName("LI")
  public data object Li : Country {
    override val value: String = "LI"
  }
  /** Sri Lanka */
  @SerialName("LK")
  public data object Lk : Country {
    override val value: String = "LK"
  }
  /** Liberia */
  @SerialName("LR")
  public data object Lr : Country {
    override val value: String = "LR"
  }
  /** Lesotho */
  @SerialName("LS")
  public data object Ls : Country {
    override val value: String = "LS"
  }
  /** Lithuania */
  @SerialName("LT")
  public data object Lt : Country {
    override val value: String = "LT"
  }
  /** Luxembourg */
  @SerialName("LU")
  public data object Lu : Country {
    override val value: String = "LU"
  }
  /** Latvia */
  @SerialName("LV")
  public data object Lv : Country {
    override val value: String = "LV"
  }
  /** Libya */
  @SerialName("LY")
  public data object Ly : Country {
    override val value: String = "LY"
  }
  /** Morocco */
  @SerialName("MA")
  public data object Ma : Country {
    override val value: String = "MA"
  }
  /** Monaco */
  @SerialName("MC")
  public data object Mc : Country {
    override val value: String = "MC"
  }
  /** Moldova (the Republic of) */
  @SerialName("MD")
  public data object Md : Country {
    override val value: String = "MD"
  }
  /** Montenegro */
  @SerialName("ME")
  public data object Me : Country {
    override val value: String = "ME"
  }
  /** Saint Martin (French part) */
  @SerialName("MF")
  public data object Mf : Country {
    override val value: String = "MF"
  }
  /** Madagascar */
  @SerialName("MG")
  public data object Mg : Country {
    override val value: String = "MG"
  }
  /** Marshall Islands (the) */
  @SerialName("MH")
  public data object Mh : Country {
    override val value: String = "MH"
  }
  /** North Macedonia */
  @SerialName("MK")
  public data object Mk : Country {
    override val value: String = "MK"
  }
  /** Mali */
  @SerialName("ML")
  public data object Ml : Country {
    override val value: String = "ML"
  }
  /** Myanmar */
  @SerialName("MM")
  public data object Mm : Country {
    override val value: String = "MM"
  }
  /** Mongolia */
  @SerialName("MN")
  public data object Mn : Country {
    override val value: String = "MN"
  }
  /** Macao */
  @SerialName("MO")
  public data object Mo : Country {
    override val value: String = "MO"
  }
  /** Northern Mariana Islands (the) */
  @SerialName("MP")
  public data object Mp : Country {
    override val value: String = "MP"
  }
  /** Martinique */
  @SerialName("MQ")
  public data object Mq : Country {
    override val value: String = "MQ"
  }
  /** Mauritania */
  @SerialName("MR")
  public data object Mr : Country {
    override val value: String = "MR"
  }
  /** Montserrat */
  @SerialName("MS")
  public data object Ms : Country {
    override val value: String = "MS"
  }
  /** Malta */
  @SerialName("MT")
  public data object Mt : Country {
    override val value: String = "MT"
  }
  /** Mauritius */
  @SerialName("MU")
  public data object Mu : Country {
    override val value: String = "MU"
  }
  /** Maldives */
  @SerialName("MV")
  public data object Mv : Country {
    override val value: String = "MV"
  }
  /** Malawi */
  @SerialName("MW")
  public data object Mw : Country {
    override val value: String = "MW"
  }
  /** Mexico */
  @SerialName("MX")
  public data object Mx : Country {
    override val value: String = "MX"
  }
  /** Malaysia */
  @SerialName("MY")
  public data object My : Country {
    override val value: String = "MY"
  }
  /** Mozambique */
  @SerialName("MZ")
  public data object Mz : Country {
    override val value: String = "MZ"
  }
  /** Namibia */
  @SerialName("NA")
  public data object Na : Country {
    override val value: String = "NA"
  }
  /** New Caledonia */
  @SerialName("NC")
  public data object Nc : Country {
    override val value: String = "NC"
  }
  /** Niger (the) */
  @SerialName("NE")
  public data object Ne : Country {
    override val value: String = "NE"
  }
  /** Norfolk Island */
  @SerialName("NF")
  public data object Nf : Country {
    override val value: String = "NF"
  }
  /** Nigeria */
  @SerialName("NG")
  public data object Ng : Country {
    override val value: String = "NG"
  }
  /** Nicaragua */
  @SerialName("NI")
  public data object Ni : Country {
    override val value: String = "NI"
  }
  /** Netherlands (Kingdom of the) */
  @SerialName("NL")
  public data object Nl : Country {
    override val value: String = "NL"
  }
  /** Norway */
  @SerialName("NO")
  public data object No : Country {
    override val value: String = "NO"
  }
  /** Nepal */
  @SerialName("NP")
  public data object Np : Country {
    override val value: String = "NP"
  }
  /** Nauru */
  @SerialName("NR")
  public data object Nr : Country {
    override val value: String = "NR"
  }
  /** Niue */
  @SerialName("NU")
  public data object Nu : Country {
    override val value: String = "NU"
  }
  /** New Zealand */
  @SerialName("NZ")
  public data object Nz : Country {
    override val value: String = "NZ"
  }
  /** Oman */
  @SerialName("OM")
  public data object Om : Country {
    override val value: String = "OM"
  }
  /** Panama */
  @SerialName("PA")
  public data object Pa : Country {
    override val value: String = "PA"
  }
  /** Peru */
  @SerialName("PE")
  public data object Pe : Country {
    override val value: String = "PE"
  }
  /** French Polynesia */
  @SerialName("PF")
  public data object Pf : Country {
    override val value: String = "PF"
  }
  /** Papua New Guinea */
  @SerialName("PG")
  public data object Pg : Country {
    override val value: String = "PG"
  }
  /** Philippines (the) */
  @SerialName("PH")
  public data object Ph : Country {
    override val value: String = "PH"
  }
  /** Pakistan */
  @SerialName("PK")
  public data object Pk : Country {
    override val value: String = "PK"
  }
  /** Poland */
  @SerialName("PL")
  public data object Pl : Country {
    override val value: String = "PL"
  }
  /** Saint Pierre and Miquelon */
  @SerialName("PM")
  public data object Pm : Country {
    override val value: String = "PM"
  }
  /** Pitcairn */
  @SerialName("PN")
  public data object Pn : Country {
    override val value: String = "PN"
  }
  /** Puerto Rico */
  @SerialName("PR")
  public data object Pr : Country {
    override val value: String = "PR"
  }
  /** Palestine, State of */
  @SerialName("PS")
  public data object Ps : Country {
    override val value: String = "PS"
  }
  /** Portugal */
  @SerialName("PT")
  public data object Pt : Country {
    override val value: String = "PT"
  }
  /** Palau */
  @SerialName("PW")
  public data object Pw : Country {
    override val value: String = "PW"
  }
  /** Paraguay */
  @SerialName("PY")
  public data object Py : Country {
    override val value: String = "PY"
  }
  /** Qatar */
  @SerialName("QA")
  public data object Qa : Country {
    override val value: String = "QA"
  }
  /** Réunion */
  @SerialName("RE")
  public data object Re : Country {
    override val value: String = "RE"
  }
  /** Romania */
  @SerialName("RO")
  public data object Ro : Country {
    override val value: String = "RO"
  }
  /** Serbia */
  @SerialName("RS")
  public data object Rs : Country {
    override val value: String = "RS"
  }
  /** Russian Federation (the) */
  @SerialName("RU")
  public data object Ru : Country {
    override val value: String = "RU"
  }
  /** Rwanda */
  @SerialName("RW")
  public data object Rw : Country {
    override val value: String = "RW"
  }
  /** Saudi Arabia */
  @SerialName("SA")
  public data object Sa : Country {
    override val value: String = "SA"
  }
  /** Solomon Islands */
  @SerialName("SB")
  public data object Sb : Country {
    override val value: String = "SB"
  }
  /** Seychelles */
  @SerialName("SC")
  public data object Sc : Country {
    override val value: String = "SC"
  }
  /** Sudan (the) */
  @SerialName("SD")
  public data object Sd : Country {
    override val value: String = "SD"
  }
  /** Sweden */
  @SerialName("SE")
  public data object Se : Country {
    override val value: String = "SE"
  }
  /** Singapore */
  @SerialName("SG")
  public data object Sg : Country {
    override val value: String = "SG"
  }
  /** Saint Helena, Ascension and Tristan da Cunha */
  @SerialName("SH")
  public data object Sh : Country {
    override val value: String = "SH"
  }
  /** Slovenia */
  @SerialName("SI")
  public data object Si : Country {
    override val value: String = "SI"
  }
  /** Svalbard and Jan Mayen */
  @SerialName("SJ")
  public data object Sj : Country {
    override val value: String = "SJ"
  }
  /** Slovakia */
  @SerialName("SK")
  public data object Sk : Country {
    override val value: String = "SK"
  }
  /** Sierra Leone */
  @SerialName("SL")
  public data object Sl : Country {
    override val value: String = "SL"
  }
  /** San Marino */
  @SerialName("SM")
  public data object Sm : Country {
    override val value: String = "SM"
  }
  /** Senegal */
  @SerialName("SN")
  public data object Sn : Country {
    override val value: String = "SN"
  }
  /** Somalia */
  @SerialName("SO")
  public data object So : Country {
    override val value: String = "SO"
  }
  /** Suriname */
  @SerialName("SR")
  public data object Sr : Country {
    override val value: String = "SR"
  }
  /** South Sudan */
  @SerialName("SS")
  public data object Ss : Country {
    override val value: String = "SS"
  }
  /** Sao Tome and Principe */
  @SerialName("ST")
  public data object St : Country {
    override val value: String = "ST"
  }
  /** El Salvador */
  @SerialName("SV")
  public data object Sv : Country {
    override val value: String = "SV"
  }
  /** Sint Maarten (Dutch part) */
  @SerialName("SX")
  public data object Sx : Country {
    override val value: String = "SX"
  }
  /** Syrian Arab Republic (the) */
  @SerialName("SY")
  public data object Sy : Country {
    override val value: String = "SY"
  }
  /** Eswatini */
  @SerialName("SZ")
  public data object Sz : Country {
    override val value: String = "SZ"
  }
  /** Turks and Caicos Islands (the) */
  @SerialName("TC")
  public data object Tc : Country {
    override val value: String = "TC"
  }
  /** Chad */
  @SerialName("TD")
  public data object Td : Country {
    override val value: String = "TD"
  }
  /** French Southern Territories (the) */
  @SerialName("TF")
  public data object Tf : Country {
    override val value: String = "TF"
  }
  /** Togo */
  @SerialName("TG")
  public data object Tg : Country {
    override val value: String = "TG"
  }
  /** Thailand */
  @SerialName("TH")
  public data object Th : Country {
    override val value: String = "TH"
  }
  /** Tajikistan */
  @SerialName("TJ")
  public data object Tj : Country {
    override val value: String = "TJ"
  }
  /** Tokelau */
  @SerialName("TK")
  public data object Tk : Country {
    override val value: String = "TK"
  }
  /** Timor-Leste */
  @SerialName("TL")
  public data object Tl : Country {
    override val value: String = "TL"
  }
  /** Turkmenistan */
  @SerialName("TM")
  public data object Tm : Country {
    override val value: String = "TM"
  }
  /** Tunisia */
  @SerialName("TN")
  public data object Tn : Country {
    override val value: String = "TN"
  }
  /** Tonga */
  @SerialName("TO")
  public data object To : Country {
    override val value: String = "TO"
  }
  /** Türkiye */
  @SerialName("TR")
  public data object Tr : Country {
    override val value: String = "TR"
  }
  /** Trinidad and Tobago */
  @SerialName("TT")
  public data object Tt : Country {
    override val value: String = "TT"
  }
  /** Tuvalu */
  @SerialName("TV")
  public data object Tv : Country {
    override val value: String = "TV"
  }
  /** Taiwan (Province of China) */
  @SerialName("TW")
  public data object Tw : Country {
    override val value: String = "TW"
  }
  /** Tanzania, the United Republic of */
  @SerialName("TZ")
  public data object Tz : Country {
    override val value: String = "TZ"
  }
  /** Ukraine */
  @SerialName("UA")
  public data object Ua : Country {
    override val value: String = "UA"
  }
  /** Uganda */
  @SerialName("UG")
  public data object Ug : Country {
    override val value: String = "UG"
  }
  /** United States Minor Outlying Islands (the) */
  @SerialName("UM")
  public data object Um : Country {
    override val value: String = "UM"
  }
  /** United States of America (the) */
  @SerialName("US")
  public data object Us : Country {
    override val value: String = "US"
  }
  /** Uruguay */
  @SerialName("UY")
  public data object Uy : Country {
    override val value: String = "UY"
  }
  /** Uzbekistan */
  @SerialName("UZ")
  public data object Uz : Country {
    override val value: String = "UZ"
  }
  /** Holy See (the) */
  @SerialName("VA")
  public data object Va : Country {
    override val value: String = "VA"
  }
  /** Saint Vincent and the Grenadines */
  @SerialName("VC")
  public data object Vc : Country {
    override val value: String = "VC"
  }
  /** Venezuela (Bolivarian Republic of) */
  @SerialName("VE")
  public data object Ve : Country {
    override val value: String = "VE"
  }
  /** Virgin Islands (British) */
  @SerialName("VG")
  public data object Vg : Country {
    override val value: String = "VG"
  }
  /** Virgin Islands (U.S.) */
  @SerialName("VI")
  public data object Vi : Country {
    override val value: String = "VI"
  }
  /** Viet Nam */
  @SerialName("VN")
  public data object Vn : Country {
    override val value: String = "VN"
  }
  /** Vanuatu */
  @SerialName("VU")
  public data object Vu : Country {
    override val value: String = "VU"
  }
  /** Wallis and Futuna */
  @SerialName("WF")
  public data object Wf : Country {
    override val value: String = "WF"
  }
  /** Samoa */
  @SerialName("WS")
  public data object Ws : Country {
    override val value: String = "WS"
  }
  /** Yemen */
  @SerialName("YE")
  public data object Ye : Country {
    override val value: String = "YE"
  }
  /** Mayotte */
  @SerialName("YT")
  public data object Yt : Country {
    override val value: String = "YT"
  }
  /** South Africa */
  @SerialName("ZA")
  public data object Za : Country {
    override val value: String = "ZA"
  }
  /** Zambia */
  @SerialName("ZM")
  public data object Zm : Country {
    override val value: String = "ZM"
  }
  /** Zimbabwe */
  @SerialName("ZW")
  public data object Zw : Country {
    override val value: String = "ZW"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Country
}
