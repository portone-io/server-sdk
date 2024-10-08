/** 국가 */
export type Country =
	/** Andorra */
	| "AD"
	/** United Arab Emirates (the) */
	| "AE"
	/** Afghanistan */
	| "AF"
	/** Antigua and Barbuda */
	| "AG"
	/** Anguilla */
	| "AI"
	/** Albania */
	| "AL"
	/** Armenia */
	| "AM"
	/** Angola */
	| "AO"
	/** Antarctica */
	| "AQ"
	/** Argentina */
	| "AR"
	/** American Samoa */
	| "AS"
	/** Austria */
	| "AT"
	/** Australia */
	| "AU"
	/** Aruba */
	| "AW"
	/** Åland Islands */
	| "AX"
	/** Azerbaijan */
	| "AZ"
	/** Bosnia and Herzegovina */
	| "BA"
	/** Barbados */
	| "BB"
	/** Bangladesh */
	| "BD"
	/** Belgium */
	| "BE"
	/** Burkina Faso */
	| "BF"
	/** Bulgaria */
	| "BG"
	/** Bahrain */
	| "BH"
	/** Burundi */
	| "BI"
	/** Benin */
	| "BJ"
	/** Saint Barthélemy */
	| "BL"
	/** Bermuda */
	| "BM"
	/** Brunei Darussalam */
	| "BN"
	/** Bolivia (Plurinational State of) */
	| "BO"
	/** Bonaire, Sint Eustatius and Saba */
	| "BQ"
	/** Brazil */
	| "BR"
	/** Bahamas (the) */
	| "BS"
	/** Bhutan */
	| "BT"
	/** Bouvet Island */
	| "BV"
	/** Botswana */
	| "BW"
	/** Belarus */
	| "BY"
	/** Belize */
	| "BZ"
	/** Canada */
	| "CA"
	/** Cocos (Keeling) Islands (the) */
	| "CC"
	/** Congo (the Democratic Republic of the) */
	| "CD"
	/** Central African Republic (the) */
	| "CF"
	/** Congo (the) */
	| "CG"
	/** Switzerland */
	| "CH"
	/** Côte d'Ivoire */
	| "CI"
	/** Cook Islands (the) */
	| "CK"
	/** Chile */
	| "CL"
	/** Cameroon */
	| "CM"
	/** China */
	| "CN"
	/** Colombia */
	| "CO"
	/** Costa Rica */
	| "CR"
	/** Cuba */
	| "CU"
	/** Cabo Verde */
	| "CV"
	/** Curaçao */
	| "CW"
	/** Christmas Island */
	| "CX"
	/** Cyprus */
	| "CY"
	/** Czechia */
	| "CZ"
	/** Germany */
	| "DE"
	/** Djibouti */
	| "DJ"
	/** Denmark */
	| "DK"
	/** Dominica */
	| "DM"
	/** Dominican Republic (the) */
	| "DO"
	/** Algeria */
	| "DZ"
	/** Ecuador */
	| "EC"
	/** Estonia */
	| "EE"
	/** Egypt */
	| "EG"
	/** Western Sahara */
	| "EH"
	/** Eritrea */
	| "ER"
	/** Spain */
	| "ES"
	/** Ethiopia */
	| "ET"
	/** Finland */
	| "FI"
	/** Fiji */
	| "FJ"
	/** Falkland Islands (the) [Malvinas] */
	| "FK"
	/** Micronesia (Federated States of) */
	| "FM"
	/** Faroe Islands (the) */
	| "FO"
	/** France */
	| "FR"
	/** Gabon */
	| "GA"
	/** United Kingdom of Great Britain and Northern Ireland (the) */
	| "GB"
	/** Grenada */
	| "GD"
	/** Georgia */
	| "GE"
	/** French Guiana */
	| "GF"
	/** Guernsey */
	| "GG"
	/** Ghana */
	| "GH"
	/** Gibraltar */
	| "GI"
	/** Greenland */
	| "GL"
	/** Gambia (the) */
	| "GM"
	/** Guinea */
	| "GN"
	/** Guadeloupe */
	| "GP"
	/** Equatorial Guinea */
	| "GQ"
	/** Greece */
	| "GR"
	/** South Georgia and the South Sandwich Islands */
	| "GS"
	/** Guatemala */
	| "GT"
	/** Guam */
	| "GU"
	/** Guinea-Bissau */
	| "GW"
	/** Guyana */
	| "GY"
	/** Hong Kong */
	| "HK"
	/** Heard Island and McDonald Islands */
	| "HM"
	/** Honduras */
	| "HN"
	/** Croatia */
	| "HR"
	/** Haiti */
	| "HT"
	/** Hungary */
	| "HU"
	/** Indonesia */
	| "ID"
	/** Ireland */
	| "IE"
	/** Israel */
	| "IL"
	/** Isle of Man */
	| "IM"
	/** India */
	| "IN"
	/** British Indian Ocean Territory (the) */
	| "IO"
	/** Iraq */
	| "IQ"
	/** Iran (Islamic Republic of) */
	| "IR"
	/** Iceland */
	| "IS"
	/** Italy */
	| "IT"
	/** Jersey */
	| "JE"
	/** Jamaica */
	| "JM"
	/** Jordan */
	| "JO"
	/** Japan */
	| "JP"
	/** Kenya */
	| "KE"
	/** Kyrgyzstan */
	| "KG"
	/** Cambodia */
	| "KH"
	/** Kiribati */
	| "KI"
	/** Comoros (the) */
	| "KM"
	/** Saint Kitts and Nevis */
	| "KN"
	/** Korea (the Democratic People's Republic of) */
	| "KP"
	/** Korea (the Republic of) */
	| "KR"
	/** Kuwait */
	| "KW"
	/** Cayman Islands (the) */
	| "KY"
	/** Kazakhstan */
	| "KZ"
	/** Lao People's Democratic Republic (the) */
	| "LA"
	/** Lebanon */
	| "LB"
	/** Saint Lucia */
	| "LC"
	/** Liechtenstein */
	| "LI"
	/** Sri Lanka */
	| "LK"
	/** Liberia */
	| "LR"
	/** Lesotho */
	| "LS"
	/** Lithuania */
	| "LT"
	/** Luxembourg */
	| "LU"
	/** Latvia */
	| "LV"
	/** Libya */
	| "LY"
	/** Morocco */
	| "MA"
	/** Monaco */
	| "MC"
	/** Moldova (the Republic of) */
	| "MD"
	/** Montenegro */
	| "ME"
	/** Saint Martin (French part) */
	| "MF"
	/** Madagascar */
	| "MG"
	/** Marshall Islands (the) */
	| "MH"
	/** North Macedonia */
	| "MK"
	/** Mali */
	| "ML"
	/** Myanmar */
	| "MM"
	/** Mongolia */
	| "MN"
	/** Macao */
	| "MO"
	/** Northern Mariana Islands (the) */
	| "MP"
	/** Martinique */
	| "MQ"
	/** Mauritania */
	| "MR"
	/** Montserrat */
	| "MS"
	/** Malta */
	| "MT"
	/** Mauritius */
	| "MU"
	/** Maldives */
	| "MV"
	/** Malawi */
	| "MW"
	/** Mexico */
	| "MX"
	/** Malaysia */
	| "MY"
	/** Mozambique */
	| "MZ"
	/** Namibia */
	| "NA"
	/** New Caledonia */
	| "NC"
	/** Niger (the) */
	| "NE"
	/** Norfolk Island */
	| "NF"
	/** Nigeria */
	| "NG"
	/** Nicaragua */
	| "NI"
	/** Netherlands (Kingdom of the) */
	| "NL"
	/** Norway */
	| "NO"
	/** Nepal */
	| "NP"
	/** Nauru */
	| "NR"
	/** Niue */
	| "NU"
	/** New Zealand */
	| "NZ"
	/** Oman */
	| "OM"
	/** Panama */
	| "PA"
	/** Peru */
	| "PE"
	/** French Polynesia */
	| "PF"
	/** Papua New Guinea */
	| "PG"
	/** Philippines (the) */
	| "PH"
	/** Pakistan */
	| "PK"
	/** Poland */
	| "PL"
	/** Saint Pierre and Miquelon */
	| "PM"
	/** Pitcairn */
	| "PN"
	/** Puerto Rico */
	| "PR"
	/** Palestine, State of */
	| "PS"
	/** Portugal */
	| "PT"
	/** Palau */
	| "PW"
	/** Paraguay */
	| "PY"
	/** Qatar */
	| "QA"
	/** Réunion */
	| "RE"
	/** Romania */
	| "RO"
	/** Serbia */
	| "RS"
	/** Russian Federation (the) */
	| "RU"
	/** Rwanda */
	| "RW"
	/** Saudi Arabia */
	| "SA"
	/** Solomon Islands */
	| "SB"
	/** Seychelles */
	| "SC"
	/** Sudan (the) */
	| "SD"
	/** Sweden */
	| "SE"
	/** Singapore */
	| "SG"
	/** Saint Helena, Ascension and Tristan da Cunha */
	| "SH"
	/** Slovenia */
	| "SI"
	/** Svalbard and Jan Mayen */
	| "SJ"
	/** Slovakia */
	| "SK"
	/** Sierra Leone */
	| "SL"
	/** San Marino */
	| "SM"
	/** Senegal */
	| "SN"
	/** Somalia */
	| "SO"
	/** Suriname */
	| "SR"
	/** South Sudan */
	| "SS"
	/** Sao Tome and Principe */
	| "ST"
	/** El Salvador */
	| "SV"
	/** Sint Maarten (Dutch part) */
	| "SX"
	/** Syrian Arab Republic (the) */
	| "SY"
	/** Eswatini */
	| "SZ"
	/** Turks and Caicos Islands (the) */
	| "TC"
	/** Chad */
	| "TD"
	/** French Southern Territories (the) */
	| "TF"
	/** Togo */
	| "TG"
	/** Thailand */
	| "TH"
	/** Tajikistan */
	| "TJ"
	/** Tokelau */
	| "TK"
	/** Timor-Leste */
	| "TL"
	/** Turkmenistan */
	| "TM"
	/** Tunisia */
	| "TN"
	/** Tonga */
	| "TO"
	/** Türkiye */
	| "TR"
	/** Trinidad and Tobago */
	| "TT"
	/** Tuvalu */
	| "TV"
	/** Taiwan (Province of China) */
	| "TW"
	/** Tanzania, the United Republic of */
	| "TZ"
	/** Ukraine */
	| "UA"
	/** Uganda */
	| "UG"
	/** United States Minor Outlying Islands (the) */
	| "UM"
	/** United States of America (the) */
	| "US"
	/** Uruguay */
	| "UY"
	/** Uzbekistan */
	| "UZ"
	/** Holy See (the) */
	| "VA"
	/** Saint Vincent and the Grenadines */
	| "VC"
	/** Venezuela (Bolivarian Republic of) */
	| "VE"
	/** Virgin Islands (British) */
	| "VG"
	/** Virgin Islands (U.S.) */
	| "VI"
	/** Viet Nam */
	| "VN"
	/** Vanuatu */
	| "VU"
	/** Wallis and Futuna */
	| "WF"
	/** Samoa */
	| "WS"
	/** Yemen */
	| "YE"
	/** Mayotte */
	| "YT"
	/** South Africa */
	| "ZA"
	/** Zambia */
	| "ZM"
	/** Zimbabwe */
	| "ZW"
