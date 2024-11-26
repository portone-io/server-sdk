/** 통합검색 항목 */
export type BillingKeyTextSearchField =
	| "CARD_BIN"
	| "CARD_NUMBER"
	| "PG_MERCHANT_ID"
	| "CUSTOMER_NAME"
	| "CUSTOMER_EMAIL"
	| "CUSTOMER_PHONE_NUMBER"
	| "CUSTOMER_ADDRESS"
	| "CUSTOMER_ZIPCODE"
	| "USER_AGENT"
	| "BILLING_KEY"
	| "CHANNEL_GROUP_NAME"
	| string & {}
