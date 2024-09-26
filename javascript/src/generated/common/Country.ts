/** 국가 */
export type Country =
	/** Cabo Verde */
	| "CV"
	/** Morocco */
	| "MA"
	/** Angola */
	| "AO"
	/** Viet Nam */
	| "VN"
	/** India */
	| "IN"
	/** Kuwait */
	| "KW"
	/** Mali */
	| "ML"
	/** Indonesia */
	| "ID"
	/** Jersey */
	| "JE"
	/** Heard Island and McDonald Islands */
	| "HM"
	/** Egypt */
	| "EG"
	/** Bulgaria */
	| "BG"
	/** Singapore */
	| "SG"
	/** El Salvador */
	| "SV"
	/** Bangladesh */
	| "BD"
	/** Turks and Caicos Islands (the) */
	| "TC"
	/** Thailand */
	| "TH"
	/** Austria */
	| "AT"
	/** Equatorial Guinea */
	| "GQ"
	/** Türkiye */
	| "TR"
	/** Haiti */
	| "HT"
	/** United States Minor Outlying Islands (the) */
	| "UM"
	/** Marshall Islands (the) */
	| "MH"
	/** Malaysia */
	| "MY"
	/** Russian Federation (the) */
	| "RU"
	/** Nicaragua */
	| "NI"
	/** Belize */
	| "BZ"
	/** Korea (the Democratic People's Republic of) */
	| "KP"
	/** Venezuela (Bolivarian Republic of) */
	| "VE"
	/** Israel */
	| "IL"
	/** Grenada */
	| "GD"
	/** Gibraltar */
	| "GI"
	/** Tunisia */
	| "TN"
	/** Dominica */
	| "DM"
	/** Macao */
	| "MO"
	/** Puerto Rico */
	| "PR"
	/** Norfolk Island */
	| "NF"
	/** Taiwan (Province of China) */
	| "TW"
	/** Saint Kitts and Nevis */
	| "KN"
	/** Philippines (the) */
	| "PH"
	/** Wallis and Futuna */
	| "WF"
	/** Jordan */
	| "JO"
	/** Montenegro */
	| "ME"
	/** Spain */
	| "ES"
	/** Azerbaijan */
	| "AZ"
	/** Mauritania */
	| "MR"
	/** San Marino */
	| "SM"
	/** Saint Barthélemy */
	| "BL"
	/** Pakistan */
	| "PK"
	/** New Zealand */
	| "NZ"
	/** Guadeloupe */
	| "GP"
	/** Namibia */
	| "NA"
	/** Jamaica */
	| "JM"
	/** Åland Islands */
	| "AX"
	/** Cameroon */
	| "CM"
	/** United States of America (the) */
	| "US"
	/** Guam */
	| "GU"
	/** Solomon Islands */
	| "SB"
	/** Maldives */
	| "MV"
	/** Slovenia */
	| "SI"
	/** Curaçao */
	| "CW"
	/** Bahrain */
	| "BH"
	/** Virgin Islands (British) */
	| "VG"
	/** Hong Kong */
	| "HK"
	/** Sudan (the) */
	| "SD"
	/** Andorra */
	| "AD"
	/** Romania */
	| "RO"
	/** Luxembourg */
	| "LU"
	/** Saint Vincent and the Grenadines */
	| "VC"
	/** Faroe Islands (the) */
	| "FO"
	/** Greenland */
	| "GL"
	/** Botswana */
	| "BW"
	/** Central African Republic (the) */
	| "CF"
	/** Côte d'Ivoire */
	| "CI"
	/** Kyrgyzstan */
	| "KG"
	/** Bouvet Island */
	| "BV"
	/** Cayman Islands (the) */
	| "KY"
	/** Libya */
	| "LY"
	/** Myanmar */
	| "MM"
	/** Mozambique */
	| "MZ"
	/** Iran (Islamic Republic of) */
	| "IR"
	/** Western Sahara */
	| "EH"
	/** Iraq */
	| "IQ"
	/** Barbados */
	| "BB"
	/** Eswatini */
	| "SZ"
	/** Ireland */
	| "IE"
	/** Falkland Islands (the) [Malvinas] */
	| "FK"
	/** Nepal */
	| "NP"
	/** Belgium */
	| "BE"
	/** Australia */
	| "AU"
	/** Tanzania, the United Republic of */
	| "TZ"
	/** Uruguay */
	| "UY"
	/** Saudi Arabia */
	| "SA"
	/** Zimbabwe */
	| "ZW"
	/** Moldova (the Republic of) */
	| "MD"
	/** Hungary */
	| "HU"
	/** Papua New Guinea */
	| "PG"
	/** Afghanistan */
	| "AF"
	/** Mauritius */
	| "MU"
	/** Sierra Leone */
	| "SL"
	/** Guatemala */
	| "GT"
	/** Bolivia (Plurinational State of) */
	| "BO"
	/** Turkmenistan */
	| "TM"
	/** Niger (the) */
	| "NE"
	/** Chile */
	| "CL"
	/** Finland */
	| "FI"
	/** Mongolia */
	| "MN"
	/** Norway */
	| "NO"
	/** Guernsey */
	| "GG"
	/** Estonia */
	| "EE"
	/** Comoros (the) */
	| "KM"
	/** Lithuania */
	| "LT"
	/** Eritrea */
	| "ER"
	/** Saint Helena, Ascension and Tristan da Cunha */
	| "SH"
	/** Syrian Arab Republic (the) */
	| "SY"
	/** Saint Lucia */
	| "LC"
	/** Cocos (Keeling) Islands (the) */
	| "CC"
	/** Poland */
	| "PL"
	/** Switzerland */
	| "CH"
	/** Sao Tome and Principe */
	| "ST"
	/** Nigeria */
	| "NG"
	/** French Southern Territories (the) */
	| "TF"
	/** Kiribati */
	| "KI"
	/** Latvia */
	| "LV"
	/** Uganda */
	| "UG"
	/** Cyprus */
	| "CY"
	/** Malawi */
	| "MW"
	/** Congo (the) */
	| "CG"
	/** Saint Martin (French part) */
	| "MF"
	/** Saint Pierre and Miquelon */
	| "PM"
	/** Iceland */
	| "IS"
	/** Burundi */
	| "BI"
	/** Tokelau */
	| "TK"
	/** Sweden */
	| "SE"
	/** United Arab Emirates (the) */
	| "AE"
	/** Kazakhstan */
	| "KZ"
	/** Lebanon */
	| "LB"
	/** Argentina */
	| "AR"
	/** South Georgia and the South Sandwich Islands */
	| "GS"
	/** Burkina Faso */
	| "BF"
	/** Djibouti */
	| "DJ"
	/** Bosnia and Herzegovina */
	| "BA"
	/** Svalbard and Jan Mayen */
	| "SJ"
	/** France */
	| "FR"
	/** Gambia (the) */
	| "GM"
	/** Croatia */
	| "HR"
	/** Bahamas (the) */
	| "BS"
	/** Serbia */
	| "RS"
	/** Samoa */
	| "WS"
	/** United Kingdom of Great Britain and Northern Ireland (the) */
	| "GB"
	/** Lesotho */
	| "LS"
	/** Uzbekistan */
	| "UZ"
	/** French Polynesia */
	| "PF"
	/** Antigua and Barbuda */
	| "AG"
	/** Guinea-Bissau */
	| "GW"
	/** Fiji */
	| "FJ"
	/** Colombia */
	| "CO"
	/** Zambia */
	| "ZM"
	/** Antarctica */
	| "AQ"
	/** French Guiana */
	| "GF"
	/** Niue */
	| "NU"
	/** Brunei Darussalam */
	| "BN"
	/** Rwanda */
	| "RW"
	/** Portugal */
	| "PT"
	/** Somalia */
	| "SO"
	/** Malta */
	| "MT"
	/** Palau */
	| "PW"
	/** Cambodia */
	| "KH"
	/** Sint Maarten (Dutch part) */
	| "SX"
	/** Tajikistan */
	| "TJ"
	/** Korea (the Republic of) */
	| "KR"
	/** South Sudan */
	| "SS"
	/** Paraguay */
	| "PY"
	/** Armenia */
	| "AM"
	/** Monaco */
	| "MC"
	/** Christmas Island */
	| "CX"
	/** Trinidad and Tobago */
	| "TT"
	/** Ukraine */
	| "UA"
	/** Liechtenstein */
	| "LI"
	/** Brazil */
	| "BR"
	/** Panama */
	| "PA"
	/** Martinique */
	| "MQ"
	/** Nauru */
	| "NR"
	/** Pitcairn */
	| "PN"
	/** Gabon */
	| "GA"
	/** Togo */
	| "TG"
	/** Micronesia (Federated States of) */
	| "FM"
	/** Guinea */
	| "GN"
	/** Mayotte */
	| "YT"
	/** Congo (the Democratic Republic of the) */
	| "CD"
	/** Madagascar */
	| "MG"
	/** Anguilla */
	| "AI"
	/** Yemen */
	| "YE"
	/** Honduras */
	| "HN"
	/** Italy */
	| "IT"
	/** Réunion */
	| "RE"
	/** Dominican Republic (the) */
	| "DO"
	/** British Indian Ocean Territory (the) */
	| "IO"
	/** Greece */
	| "GR"
	/** American Samoa */
	| "AS"
	/** South Africa */
	| "ZA"
	/** Guyana */
	| "GY"
	/** Belarus */
	| "BY"
	/** Sri Lanka */
	| "LK"
	/** Bhutan */
	| "BT"
	/** Oman */
	| "OM"
	/** Cook Islands (the) */
	| "CK"
	/** Kenya */
	| "KE"
	/** Czechia */
	| "CZ"
	/** Ghana */
	| "GH"
	/** Mexico */
	| "MX"
	/** Slovakia */
	| "SK"
	/** North Macedonia */
	| "MK"
	/** Algeria */
	| "DZ"
	/** Qatar */
	| "QA"
	/** Cuba */
	| "CU"
	/** Benin */
	| "BJ"
	/** Lao People's Democratic Republic (the) */
	| "LA"
	/** Timor-Leste */
	| "TL"
	/** Denmark */
	| "DK"
	/** Virgin Islands (U.S.) */
	| "VI"
	/** Netherlands (Kingdom of the) */
	| "NL"
	/** Canada */
	| "CA"
	/** Bermuda */
	| "BM"
	/** Japan */
	| "JP"
	/** Aruba */
	| "AW"
	/** Tonga */
	| "TO"
	/** China */
	| "CN"
	/** Vanuatu */
	| "VU"
	/** Albania */
	| "AL"
	/** Ethiopia */
	| "ET"
	/** Isle of Man */
	| "IM"
	/** Senegal */
	| "SN"
	/** Peru */
	| "PE"
	/** Bonaire, Sint Eustatius and Saba */
	| "BQ"
	/** New Caledonia */
	| "NC"
	/** Northern Mariana Islands (the) */
	| "MP"
	/** Georgia */
	| "GE"
	/** Costa Rica */
	| "CR"
	/** Holy See (the) */
	| "VA"
	/** Palestine, State of */
	| "PS"
	/** Ecuador */
	| "EC"
	/** Tuvalu */
	| "TV"
	/** Liberia */
	| "LR"
	/** Montserrat */
	| "MS"
	/** Chad */
	| "TD"
	/** Seychelles */
	| "SC"
	/** Germany */
	| "DE"
	/** Suriname */
	| "SR"
