import * as Errors from "..//errors"
import * as MemberCompany from "./MemberCompany"
import * as Contact from "./Contact"
import * as TaxInvoice from "./TaxInvoice"
export type * as MemberCompany from "./MemberCompany"
export type * as Contact from "./Contact"
export type * as TaxInvoice from "./TaxInvoice"
/** @ignore */
export function B2BClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): B2BClient {
	return {
		MemberCompany: MemberCompany.MemberCompanyClient(secret, userAgent, baseUrl, storeId),
		Contact: Contact.ContactClient(secret, userAgent, baseUrl, storeId),
		TaxInvoice: TaxInvoice.TaxInvoiceClient(secret, userAgent, baseUrl, storeId),
	}
}
export type B2BClient = {
	MemberCompany: MemberCompany.MemberCompanyClient
	Contact: Contact.ContactClient
	TaxInvoice: TaxInvoice.TaxInvoiceClient
}

