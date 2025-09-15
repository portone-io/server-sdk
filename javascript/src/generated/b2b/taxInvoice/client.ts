import { TaxInvoiceError } from "./TaxInvoiceError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { B2BCannotChangeTaxTypeError } from "../../../generated/b2b/taxInvoice/B2BCannotChangeTaxTypeError"
import type { B2BTaxInvoiceStatusNotSendingCompletedError } from "../../../generated/b2b/taxInvoice/B2BTaxInvoiceStatusNotSendingCompletedError"
import type { B2bBulkTaxInvoice } from "../../../generated/b2b/taxInvoice/B2bBulkTaxInvoice"
import type { B2bBulkTaxInvoiceNotFoundError } from "../../../generated/b2b/taxInvoice/B2bBulkTaxInvoiceNotFoundError"
import type { B2bDocumentKeyCannotBeChangedError } from "../../../generated/b2b/taxInvoice/B2bDocumentKeyCannotBeChangedError"
import type { B2bExternalServiceError } from "../../../generated/common/B2bExternalServiceError"
import type { B2bFileNotFoundError } from "../../../generated/b2b/taxInvoice/B2bFileNotFoundError"
import type { B2bIdAlreadyExistsError } from "../../../generated/b2b/taxInvoice/B2bIdAlreadyExistsError"
import type { B2bIssuanceTypeMismatchError } from "../../../generated/b2b/taxInvoice/B2bIssuanceTypeMismatchError"
import type { B2bModificationNotProvidedError } from "../../../generated/b2b/taxInvoice/B2bModificationNotProvidedError"
import type { B2bNotEnabledError } from "../../../generated/common/B2bNotEnabledError"
import type { B2bOriginalTaxInvoiceNotFoundError } from "../../../generated/b2b/taxInvoice/B2bOriginalTaxInvoiceNotFoundError"
import type { B2bRecipientNotFoundError } from "../../../generated/b2b/taxInvoice/B2bRecipientNotFoundError"
import type { B2bSupplierNotFoundError } from "../../../generated/b2b/taxInvoice/B2bSupplierNotFoundError"
import type { B2bTaxInvoice } from "../../../generated/b2b/taxInvoice/B2bTaxInvoice"
import type { B2bTaxInvoiceAttachmentNotFoundError } from "../../../generated/b2b/taxInvoice/B2bTaxInvoiceAttachmentNotFoundError"
import type { B2bTaxInvoiceInput } from "../../../generated/b2b/taxInvoice/B2bTaxInvoiceInput"
import type { B2bTaxInvoiceKeyType } from "../../../generated/b2b/taxInvoice/B2bTaxInvoiceKeyType"
import type { B2bTaxInvoiceModificationCreateBody } from "../../../generated/b2b/taxInvoice/B2bTaxInvoiceModificationCreateBody"
import type { B2bTaxInvoiceNoRecipientDocumentKeyError } from "../../../generated/b2b/taxInvoice/B2bTaxInvoiceNoRecipientDocumentKeyError"
import type { B2bTaxInvoiceNoSupplierDocumentKeyError } from "../../../generated/b2b/taxInvoice/B2bTaxInvoiceNoSupplierDocumentKeyError"
import type { B2bTaxInvoiceNonDeletableStatusError } from "../../../generated/b2b/taxInvoice/B2bTaxInvoiceNonDeletableStatusError"
import type { B2bTaxInvoiceNotDraftedStatusError } from "../../../generated/b2b/taxInvoice/B2bTaxInvoiceNotDraftedStatusError"
import type { B2bTaxInvoiceNotFoundError } from "../../../generated/b2b/taxInvoice/B2bTaxInvoiceNotFoundError"
import type { B2bTaxInvoiceNotIssuedStatusError } from "../../../generated/b2b/taxInvoice/B2bTaxInvoiceNotIssuedStatusError"
import type { B2bTaxInvoiceNotRequestedStatusError } from "../../../generated/b2b/taxInvoice/B2bTaxInvoiceNotRequestedStatusError"
import type { B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError } from "../../../generated/b2b/taxInvoice/B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError"
import type { B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError } from "../../../generated/b2b/taxInvoice/B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError"
import type { CancelB2bTaxInvoiceIssuanceResponse } from "../../../generated/b2b/taxInvoice/CancelB2bTaxInvoiceIssuanceResponse"
import type { CancelB2bTaxInvoiceRequestResponse } from "../../../generated/b2b/taxInvoice/CancelB2bTaxInvoiceRequestResponse"
import type { CreateB2bFileUploadUrlPayload } from "../../../generated/b2b/taxInvoice/CreateB2bFileUploadUrlPayload"
import type { DeleteB2bTaxInvoiceResponse } from "../../../generated/b2b/taxInvoice/DeleteB2bTaxInvoiceResponse"
import type { DraftB2bTaxInvoiceResponse } from "../../../generated/b2b/taxInvoice/DraftB2bTaxInvoiceResponse"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetB2bTaxInvoiceAttachmentsResponse } from "../../../generated/b2b/taxInvoice/GetB2bTaxInvoiceAttachmentsResponse"
import type { GetB2bTaxInvoicePdfDownloadUrlResponse } from "../../../generated/b2b/taxInvoice/GetB2bTaxInvoicePdfDownloadUrlResponse"
import type { GetB2bTaxInvoicePopupUrlResponse } from "../../../generated/b2b/taxInvoice/GetB2bTaxInvoicePopupUrlResponse"
import type { GetB2bTaxInvoicePrintUrlResponse } from "../../../generated/b2b/taxInvoice/GetB2bTaxInvoicePrintUrlResponse"
import type { GetB2bTaxInvoicesBodyFilter } from "../../../generated/b2b/taxInvoice/GetB2bTaxInvoicesBodyFilter"
import type { GetB2bTaxInvoicesResponse } from "../../../generated/b2b/taxInvoice/GetB2bTaxInvoicesResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { IssueB2bTaxInvoiceImmediatelyResponse } from "../../../generated/b2b/taxInvoice/IssueB2bTaxInvoiceImmediatelyResponse"
import type { IssueB2bTaxInvoiceResponse } from "../../../generated/b2b/taxInvoice/IssueB2bTaxInvoiceResponse"
import type { RefuseB2bTaxInvoiceRequestResponse } from "../../../generated/b2b/taxInvoice/RefuseB2bTaxInvoiceRequestResponse"
import type { RequestB2bTaxInvoiceResponse } from "../../../generated/b2b/taxInvoice/RequestB2bTaxInvoiceResponse"
import type { RequestB2bTaxInvoiceReverseIssuanceResponse } from "../../../generated/b2b/taxInvoice/RequestB2bTaxInvoiceReverseIssuanceResponse"
import type { SendToNtsB2bTaxInvoiceResponse } from "../../../generated/b2b/taxInvoice/SendToNtsB2bTaxInvoiceResponse"
import type { TaxInvoicesSheetField } from "../../../generated/b2b/taxInvoice/TaxInvoicesSheetField"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
import type { UpdateB2bTaxInvoiceDraftResponse } from "../../../generated/b2b/taxInvoice/UpdateB2bTaxInvoiceDraftResponse"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function TaxInvoiceClient(init: PortOneClientInit): TaxInvoiceClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getB2bBulkTaxInvoice: async (
			options: {
				bulkTaxInvoiceId: string,
				test?: boolean,
			}
		): Promise<B2bBulkTaxInvoice> => {
			const {
				bulkTaxInvoiceId,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/bulk-tax-invoices/${encodeURIComponent(bulkTaxInvoiceId)}?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetB2bBulkTaxInvoiceError(await response.json())
			}
			return response.json()
		},
		createB2bFileUploadUrl: async (
			options: {
				test?: boolean,
				fileName: string,
			}
		): Promise<CreateB2bFileUploadUrlPayload> => {
			const {
				test,
				fileName,
			} = options
			const requestBody = JSON.stringify({
				fileName,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/file-upload-url?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new CreateB2bFileUploadUrlError(await response.json())
			}
			return response.json()
		},
		downloadB2bTaxInvoicesSheet: async (
			options?: {
				filter?: GetB2bTaxInvoicesBodyFilter,
				fields?: TaxInvoicesSheetField[],
				test?: boolean,
			}
		): Promise<string> => {
			const filter = options?.filter
			const fields = options?.fields
			const test = options?.test
			const requestBody = JSON.stringify({
				filter,
				fields,
				test,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices-sheet?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new DownloadB2bTaxInvoicesSheetError(await response.json())
			}
			return response.text()
		},
		updateB2bTaxInvoiceDraft: async (
			options: {
				test?: boolean,
				brn?: string,
				taxInvoiceKey: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				taxInvoice: B2bTaxInvoiceInput,
				memo?: string,
			}
		): Promise<UpdateB2bTaxInvoiceDraftResponse> => {
			const {
				test,
				brn,
				taxInvoiceKey,
				taxInvoiceKeyType,
				taxInvoice,
				memo,
			} = options
			const requestBody = JSON.stringify({
				brn,
				taxInvoiceKey,
				taxInvoiceKeyType,
				taxInvoice,
				memo,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/draft?${query}`, baseUrl),
				{
					method: "PUT",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new UpdateB2bTaxInvoiceDraftError(await response.json())
			}
			return response.json()
		},
		draftB2bTaxInvoice: async (
			options: {
				test?: boolean,
				taxInvoice: B2bTaxInvoiceInput,
				modification?: B2bTaxInvoiceModificationCreateBody,
				memo?: string,
			}
		): Promise<DraftB2bTaxInvoiceResponse> => {
			const {
				test,
				taxInvoice,
				modification,
				memo,
			} = options
			const requestBody = JSON.stringify({
				taxInvoice,
				modification,
				memo,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/draft?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new DraftB2bTaxInvoiceError(await response.json())
			}
			return response.json()
		},
		issueB2bTaxInvoiceImmediately: async (
			options: {
				test?: boolean,
				taxInvoice: B2bTaxInvoiceInput,
				memo?: string,
				modification?: B2bTaxInvoiceModificationCreateBody,
			}
		): Promise<IssueB2bTaxInvoiceImmediatelyResponse> => {
			const {
				test,
				taxInvoice,
				memo,
				modification,
			} = options
			const requestBody = JSON.stringify({
				taxInvoice,
				memo,
				modification,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/issue-immediately?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new IssueB2bTaxInvoiceImmediatelyError(await response.json())
			}
			return response.json()
		},
		requestB2bTaxInvoiceReverseIssuance: async (
			options: {
				test?: boolean,
				taxInvoice: B2bTaxInvoiceInput,
				memo?: string,
				modification?: B2bTaxInvoiceModificationCreateBody,
			}
		): Promise<RequestB2bTaxInvoiceReverseIssuanceResponse> => {
			const {
				test,
				taxInvoice,
				memo,
				modification,
			} = options
			const requestBody = JSON.stringify({
				taxInvoice,
				memo,
				modification,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/request-reverse-issuance?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new RequestB2bTaxInvoiceReverseIssuanceError(await response.json())
			}
			return response.json()
		},
		attachB2bTaxInvoiceFile: async (
			options: {
				taxInvoiceKey: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				test?: boolean,
				fileId: string,
			}
		): Promise<void> => {
			const {
				taxInvoiceKey,
				brn,
				taxInvoiceKeyType,
				test,
				fileId,
			} = options
			const requestBody = JSON.stringify({
				fileId,
			})
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}/attach-file?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new AttachB2bTaxInvoiceFileError(await response.json())
			}
		},
		deleteB2bTaxInvoiceAttachment: async (
			options: {
				taxInvoiceKey: string,
				attachmentId: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				test?: boolean,
			}
		): Promise<void> => {
			const {
				taxInvoiceKey,
				attachmentId,
				brn,
				taxInvoiceKeyType,
				test,
			} = options
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}/attachments/${encodeURIComponent(attachmentId)}?${query}`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new DeleteB2bTaxInvoiceAttachmentError(await response.json())
			}
		},
		getB2bTaxInvoiceAttachments: async (
			options: {
				taxInvoiceKey: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				test?: boolean,
			}
		): Promise<GetB2bTaxInvoiceAttachmentsResponse> => {
			const {
				taxInvoiceKey,
				brn,
				taxInvoiceKeyType,
				test,
			} = options
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}/attachments?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetB2bTaxInvoiceAttachmentsError(await response.json())
			}
			return response.json()
		},
		cancelB2bTaxInvoiceIssuance: async (
			options: {
				taxInvoiceKey: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				test?: boolean,
				memo?: string,
			}
		): Promise<CancelB2bTaxInvoiceIssuanceResponse> => {
			const {
				taxInvoiceKey,
				brn,
				taxInvoiceKeyType,
				test,
				memo,
			} = options
			const requestBody = JSON.stringify({
				memo,
			})
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}/cancel-issuance?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new CancelB2bTaxInvoiceIssuanceError(await response.json())
			}
			return response.json()
		},
		cancelB2bTaxInvoiceRequest: async (
			options: {
				taxInvoiceKey: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				test?: boolean,
				memo?: string,
			}
		): Promise<CancelB2bTaxInvoiceRequestResponse> => {
			const {
				taxInvoiceKey,
				brn,
				taxInvoiceKeyType,
				test,
				memo,
			} = options
			const requestBody = JSON.stringify({
				memo,
			})
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}/cancel-request?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new CancelB2bTaxInvoiceRequestError(await response.json())
			}
			return response.json()
		},
		issueB2bTaxInvoice: async (
			options: {
				taxInvoiceKey: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				test?: boolean,
				memo?: string,
				emailSubject?: string,
			}
		): Promise<IssueB2bTaxInvoiceResponse> => {
			const {
				taxInvoiceKey,
				brn,
				taxInvoiceKeyType,
				test,
				memo,
				emailSubject,
			} = options
			const requestBody = JSON.stringify({
				memo,
				emailSubject,
			})
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}/issue?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new IssueB2bTaxInvoiceError(await response.json())
			}
			return response.json()
		},
		getB2bTaxInvoicePdfDownloadUrl: async (
			options: {
				taxInvoiceKey: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				test?: boolean,
			}
		): Promise<GetB2bTaxInvoicePdfDownloadUrlResponse> => {
			const {
				taxInvoiceKey,
				brn,
				taxInvoiceKeyType,
				test,
			} = options
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}/pdf-download-url?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetB2bTaxInvoicePdfDownloadUrlError(await response.json())
			}
			return response.json()
		},
		getB2bTaxInvoicePopupUrl: async (
			options: {
				taxInvoiceKey: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				includeMenu?: boolean,
				test?: boolean,
			}
		): Promise<GetB2bTaxInvoicePopupUrlResponse> => {
			const {
				taxInvoiceKey,
				brn,
				taxInvoiceKeyType,
				includeMenu,
				test,
			} = options
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["includeMenu", includeMenu],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}/popup-url?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetB2bTaxInvoicePopupUrlError(await response.json())
			}
			return response.json()
		},
		getB2bTaxInvoicePrintUrl: async (
			options: {
				taxInvoiceKey: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				test?: boolean,
			}
		): Promise<GetB2bTaxInvoicePrintUrlResponse> => {
			const {
				taxInvoiceKey,
				brn,
				taxInvoiceKeyType,
				test,
			} = options
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}/print-url?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetB2bTaxInvoicePrintUrlError(await response.json())
			}
			return response.json()
		},
		refuseB2bTaxInvoiceRequest: async (
			options: {
				taxInvoiceKey: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				test?: boolean,
				memo?: string,
			}
		): Promise<RefuseB2bTaxInvoiceRequestResponse> => {
			const {
				taxInvoiceKey,
				brn,
				taxInvoiceKeyType,
				test,
				memo,
			} = options
			const requestBody = JSON.stringify({
				memo,
			})
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}/refuse-request?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new RefuseB2bTaxInvoiceRequestError(await response.json())
			}
			return response.json()
		},
		requestB2bTaxInvoice: async (
			options: {
				taxInvoiceKey: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				test?: boolean,
			}
		): Promise<RequestB2bTaxInvoiceResponse> => {
			const {
				taxInvoiceKey,
				brn,
				taxInvoiceKeyType,
				test,
			} = options
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}/request?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new requestB2bTaxInvoiceError(await response.json())
			}
			return response.json()
		},
		sendToNtsB2bTaxInvoice: async (
			options: {
				taxInvoiceKey: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				test?: boolean,
			}
		): Promise<SendToNtsB2bTaxInvoiceResponse> => {
			const {
				taxInvoiceKey,
				brn,
				taxInvoiceKeyType,
				test,
			} = options
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}/send-to-nts?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new SendToNtsB2bTaxInvoiceError(await response.json())
			}
			return response.json()
		},
		getB2bTaxInvoice: async (
			options: {
				taxInvoiceKey: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				test?: boolean,
			}
		): Promise<B2bTaxInvoice> => {
			const {
				taxInvoiceKey,
				brn,
				taxInvoiceKeyType,
				test,
			} = options
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetB2bTaxInvoiceError(await response.json())
			}
			return response.json()
		},
		deleteB2bTaxInvoice: async (
			options: {
				taxInvoiceKey: string,
				brn?: string,
				taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
				test?: boolean,
			}
		): Promise<DeleteB2bTaxInvoiceResponse> => {
			const {
				taxInvoiceKey,
				brn,
				taxInvoiceKeyType,
				test,
			} = options
			const query = [
				["brn", brn],
				["taxInvoiceKeyType", taxInvoiceKeyType],
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices/${encodeURIComponent(taxInvoiceKey)}?${query}`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new DeleteB2bTaxInvoiceError(await response.json())
			}
			return response.json()
		},
		getB2bTaxInvoices: async (
			options?: {
				test?: boolean,
				pageNumber?: number,
				pageSize?: number,
				filter?: GetB2bTaxInvoicesBodyFilter,
			}
		): Promise<GetB2bTaxInvoicesResponse> => {
			const test = options?.test
			const pageNumber = options?.pageNumber
			const pageSize = options?.pageSize
			const filter = options?.filter
			const requestBody = JSON.stringify({
				test,
				pageNumber,
				pageSize,
				filter,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/tax-invoices?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetB2bTaxInvoicesError(await response.json())
			}
			return response.json()
		},
	}
}
export type TaxInvoiceClient = {
	/**
	 * 일괄 세금계산서 조회
	 *
	 * 등록된 일괄 세금계산서를 일괄 세금계산서 아이디로 조회합니다.
	 *
	 * @throws {@link GetB2bBulkTaxInvoiceError}
	 */
	getB2bBulkTaxInvoice: (
		options: {
			/** 일괄 세금계산서 아이디 */
			bulkTaxInvoiceId: string,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<B2bBulkTaxInvoice>
	/**
	 * 파일 업로드 URL 생성
	 *
	 * S3 파일 업로드를 위한 URL을 생성합니다.
	 *
	 * @throws {@link CreateB2bFileUploadUrlError}
	 */
	createB2bFileUploadUrl: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 파일 이름 */
			fileName: string,
		}
	) => Promise<CreateB2bFileUploadUrlPayload>
	/**
	 * 세금계산서 엑셀 파일(csv) 다운로드
	 *
	 * 세금계산서를 엑셀 파일(csv)로 다운로드합니다.
	 *
	 * @throws {@link DownloadB2bTaxInvoicesSheetError}
	 */
	downloadB2bTaxInvoicesSheet: (
		options?: {
			filter?: GetB2bTaxInvoicesBodyFilter,
			/** 다운로드 할 시트 컬럼 */
			fields?: TaxInvoicesSheetField[],
			test?: boolean,
		}
	) => Promise<string>
	/**
	 * 세금계산서 임시저장 수정
	 *
	 * 임시 저장된 세금계산서를 수정합니다.
	 *
	 * @throws {@link UpdateB2bTaxInvoiceDraftError}
	 */
	updateB2bTaxInvoiceDraft: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/**
			 * 사업자등록번호
			 *
			 * taxInvoiceKeyType이 TAX_INVOICE_ID가 아닌 경우 필수 값입니다.
			 */
			brn?: string,
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/**
			 * 문서 번호 유형
			 *
			 * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/** 세금계산서 임시저장 수정 정보 */
			taxInvoice: B2bTaxInvoiceInput,
			/** 메모 */
			memo?: string,
		}
	) => Promise<UpdateB2bTaxInvoiceDraftResponse>
	/**
	 * 세금계산서 임시 저장
	 *
	 * 세금계산서 임시 저장을 요청합니다.
	 *
	 * @throws {@link DraftB2bTaxInvoiceError}
	 */
	draftB2bTaxInvoice: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 세금계산서 생성 요청 정보 */
			taxInvoice: B2bTaxInvoiceInput,
			/** 수정 세금계산서 입력 정보 */
			modification?: B2bTaxInvoiceModificationCreateBody,
			/** 메모 */
			memo?: string,
		}
	) => Promise<DraftB2bTaxInvoiceResponse>
	/**
	 * 세금계산서 즉시 정발행
	 *
	 * 세금계산서를 즉시 정발행합니다. 임시저장 API와 정발행 API 기능을 한 번의 프로세스로 처리합니다.
	 *
	 * @throws {@link IssueB2bTaxInvoiceImmediatelyError}
	 */
	issueB2bTaxInvoiceImmediately: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 세금계산서 생성 요청 정보 */
			taxInvoice: B2bTaxInvoiceInput,
			/** 메모 */
			memo?: string,
			/** 수정 세금계산서 입력 정보 */
			modification?: B2bTaxInvoiceModificationCreateBody,
		}
	) => Promise<IssueB2bTaxInvoiceImmediatelyResponse>
	/**
	 * 세금계산서 역발행 즉시 요청
	 *
	 * 공급자에게 세금계산서 역발행을 즉시 요청합니다. 임시저장 API와 역발행 요청 API 기능을 한 번의 프로세스로 처리합니다.
	 *
	 * @throws {@link RequestB2bTaxInvoiceReverseIssuanceError}
	 */
	requestB2bTaxInvoiceReverseIssuance: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 세금계산서 생성 요청 정보 */
			taxInvoice: B2bTaxInvoiceInput,
			/** 메모 */
			memo?: string,
			/** 수정 세금계산서 입력 정보 */
			modification?: B2bTaxInvoiceModificationCreateBody,
		}
	) => Promise<RequestB2bTaxInvoiceReverseIssuanceResponse>
	/**
	 * 세금계산서 파일 첨부
	 *
	 * 세금계산서에 파일을 첨부합니다.
	 *
	 * @throws {@link AttachB2bTaxInvoiceFileError}
	 */
	attachB2bTaxInvoiceFile: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 파일 아이디 */
			fileId: string,
		}
	) => Promise<void>
	/**
	 * 세금계산서 첨부파일 삭제
	 *
	 * 세금계산서 첨부파일을 삭제합니다.
	 *
	 * @throws {@link DeleteB2bTaxInvoiceAttachmentError}
	 */
	deleteB2bTaxInvoiceAttachment: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 첨부파일 아이디 */
			attachmentId: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<void>
	/**
	 * 세금계산서 첨부파일 목록 조회
	 *
	 * 세금계산서에 첨부된 파일 목록을 조회합니다.
	 *
	 * @throws {@link GetB2bTaxInvoiceAttachmentsError}
	 */
	getB2bTaxInvoiceAttachments: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<GetB2bTaxInvoiceAttachmentsResponse>
	/**
	 * 세금계산서 취소 (공급자에 의한 취소)
	 *
	 * 발행 완료된 세금계산서를 공급자가 국세청 전송 전에 취소합니다.
	 *
	 * @throws {@link CancelB2bTaxInvoiceIssuanceError}
	 */
	cancelB2bTaxInvoiceIssuance: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 메모 */
			memo?: string,
		}
	) => Promise<CancelB2bTaxInvoiceIssuanceResponse>
	/**
	 * 세금계산서 역발행 요청 취소 (공급받는자에 의한 취소)
	 *
	 * 공급자가 세금계산서 발행을 승인하기 전에 공급받는자가 해당 역발행 요청을 취소합니다.
	 *
	 * @throws {@link CancelB2bTaxInvoiceRequestError}
	 */
	cancelB2bTaxInvoiceRequest: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 메모 */
			memo?: string,
		}
	) => Promise<CancelB2bTaxInvoiceRequestResponse>
	/**
	 * 세금계산서 발행 승인
	 *
	 * 역발행의 경우 역발행요청(REQUESTED) 상태, 정발행의 경우 임시저장(DRAFTED) 상태의 세금계산서에 대해 발행을 승인합니다.
	 *
	 * @throws {@link IssueB2bTaxInvoiceError}
	 */
	issueB2bTaxInvoice: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 메모 */
			memo?: string,
			/** 이메일 제목 */
			emailSubject?: string,
		}
	) => Promise<IssueB2bTaxInvoiceResponse>
	/**
	 * 세금 계산서 PDF 다운로드 URL 조회
	 *
	 * 등록된 세금 계산서 PDF 다운로드 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.
	 *
	 * @throws {@link GetB2bTaxInvoicePdfDownloadUrlError}
	 */
	getB2bTaxInvoicePdfDownloadUrl: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<GetB2bTaxInvoicePdfDownloadUrlResponse>
	/**
	 * 세금 계산서 팝업 URL 조회
	 *
	 * 등록된 세금 계산서 팝업 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.
	 *
	 * @throws {@link GetB2bTaxInvoicePopupUrlError}
	 */
	getB2bTaxInvoicePopupUrl: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 메뉴 포함 여부
			 *
			 * 팝업 URL에 메뉴 레이아웃을 포함 여부를 결정합니다. 기본 값은 true입니다.
			 */
			includeMenu?: boolean,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<GetB2bTaxInvoicePopupUrlResponse>
	/**
	 * 세금 계산서 프린트 URL 조회
	 *
	 * 등록된 세금 계산서 프린트 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.
	 *
	 * @throws {@link GetB2bTaxInvoicePrintUrlError}
	 */
	getB2bTaxInvoicePrintUrl: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<GetB2bTaxInvoicePrintUrlResponse>
	/**
	 * 세금계산서 역발행 요청 거부
	 *
	 * 공급자가 공급받는자로부터 요청받은 세금계산서 역발행 건을 거부합니다.
	 *
	 * @throws {@link RefuseB2bTaxInvoiceRequestError}
	 */
	refuseB2bTaxInvoiceRequest: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 메모 */
			memo?: string,
		}
	) => Promise<RefuseB2bTaxInvoiceRequestResponse>
	/**
	 * 세금계산서 역발행 요청
	 *
	 * 임시저장(REGISTERED) 상태의 역발행 세금계산서를 공급자에게 발행 요청합니다. 요청이 완료되면 (역)발행대기 상태로 전환됩니다.
	 *
	 * @throws {@link requestB2bTaxInvoiceError}
	 */
	requestB2bTaxInvoice: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<RequestB2bTaxInvoiceResponse>
	/**
	 * 세금계산서 국세청 즉시 전송
	 *
	 * 발행이 완료된 세금계산서를 국세청에 즉시 전송합니다.
	 *
	 * @throws {@link SendToNtsB2bTaxInvoiceError}
	 */
	sendToNtsB2bTaxInvoice: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<SendToNtsB2bTaxInvoiceResponse>
	/**
	 * 세금 계산서 조회
	 *
	 * 등록된 세금 계산서를 세금계산서 아이디로 조회합니다.
	 *
	 * @throws {@link GetB2bTaxInvoiceError}
	 */
	getB2bTaxInvoice: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<B2bTaxInvoice>
	/**
	 * 세금계산서 삭제
	 *
	 * 세금계산서를 삭제합니다.
	 *
	 * @throws {@link DeleteB2bTaxInvoiceError}
	 */
	deleteB2bTaxInvoice: (
		options: {
			/** 세금계산서 문서 번호 */
			taxInvoiceKey: string,
			/** 사업자등록번호 */
			brn?: string,
			/**
			 * 문서 번호 유형
			 *
			 * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
			 */
			taxInvoiceKeyType?: B2bTaxInvoiceKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<DeleteB2bTaxInvoiceResponse>
	/**
	 * 세금 계산서 다건조회
	 *
	 * 조회 기간 내 등록된 세금 계산서를 다건 조회합니다.
	 *
	 * @throws {@link GetB2bTaxInvoicesError}
	 */
	getB2bTaxInvoices: (
		options?: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/**
			 * 페이지 번호
			 *
			 * 0부터 시작하는 페이지 번호. 기본 값은 0.
			 * (int32)
			 */
			pageNumber?: number,
			/**
			 * 페이지 크기
			 *
			 * 각 페이지 당 포함할 객체 수. 기본 값은 500이며 최대 1000까지 요청가능합니다.
			 * (int32)
			 */
			pageSize?: number,
			/** 필터 */
			filter?: GetB2bTaxInvoicesBodyFilter,
		}
	) => Promise<GetB2bTaxInvoicesResponse>
}
export class GetB2bBulkTaxInvoiceError extends TaxInvoiceError {
	declare readonly data: B2bBulkTaxInvoiceNotFoundError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bBulkTaxInvoiceNotFoundError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetB2bBulkTaxInvoiceError.prototype)
		this.name = "GetB2bBulkTaxInvoiceError"
	}
}
export class CreateB2bFileUploadUrlError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CreateB2bFileUploadUrlError.prototype)
		this.name = "CreateB2bFileUploadUrlError"
	}
}
export class DownloadB2bTaxInvoicesSheetError extends TaxInvoiceError {
	declare readonly data: InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, DownloadB2bTaxInvoicesSheetError.prototype)
		this.name = "DownloadB2bTaxInvoicesSheetError"
	}
}
export class UpdateB2bTaxInvoiceDraftError extends TaxInvoiceError {
	declare readonly data: B2BCannotChangeTaxTypeError | B2bDocumentKeyCannotBeChangedError | B2bExternalServiceError | B2bIdAlreadyExistsError | B2bIssuanceTypeMismatchError | B2bModificationNotProvidedError | B2bNotEnabledError | B2bOriginalTaxInvoiceNotFoundError | B2bRecipientNotFoundError | B2bSupplierNotFoundError | B2bTaxInvoiceNotDraftedStatusError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError | B2BTaxInvoiceStatusNotSendingCompletedError | B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2BCannotChangeTaxTypeError | B2bDocumentKeyCannotBeChangedError | B2bExternalServiceError | B2bIdAlreadyExistsError | B2bIssuanceTypeMismatchError | B2bModificationNotProvidedError | B2bNotEnabledError | B2bOriginalTaxInvoiceNotFoundError | B2bRecipientNotFoundError | B2bSupplierNotFoundError | B2bTaxInvoiceNotDraftedStatusError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError | B2BTaxInvoiceStatusNotSendingCompletedError | B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, UpdateB2bTaxInvoiceDraftError.prototype)
		this.name = "UpdateB2bTaxInvoiceDraftError"
	}
}
export class DraftB2bTaxInvoiceError extends TaxInvoiceError {
	declare readonly data: B2BCannotChangeTaxTypeError | B2bExternalServiceError | B2bIdAlreadyExistsError | B2bIssuanceTypeMismatchError | B2bModificationNotProvidedError | B2bNotEnabledError | B2bOriginalTaxInvoiceNotFoundError | B2bRecipientNotFoundError | B2bSupplierNotFoundError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError | B2BTaxInvoiceStatusNotSendingCompletedError | B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2BCannotChangeTaxTypeError | B2bExternalServiceError | B2bIdAlreadyExistsError | B2bIssuanceTypeMismatchError | B2bModificationNotProvidedError | B2bNotEnabledError | B2bOriginalTaxInvoiceNotFoundError | B2bRecipientNotFoundError | B2bSupplierNotFoundError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError | B2BTaxInvoiceStatusNotSendingCompletedError | B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, DraftB2bTaxInvoiceError.prototype)
		this.name = "DraftB2bTaxInvoiceError"
	}
}
export class IssueB2bTaxInvoiceImmediatelyError extends TaxInvoiceError {
	declare readonly data: B2BCannotChangeTaxTypeError | B2bExternalServiceError | B2bIdAlreadyExistsError | B2bIssuanceTypeMismatchError | B2bModificationNotProvidedError | B2bNotEnabledError | B2bOriginalTaxInvoiceNotFoundError | B2bRecipientNotFoundError | B2bSupplierNotFoundError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError | B2BTaxInvoiceStatusNotSendingCompletedError | B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2BCannotChangeTaxTypeError | B2bExternalServiceError | B2bIdAlreadyExistsError | B2bIssuanceTypeMismatchError | B2bModificationNotProvidedError | B2bNotEnabledError | B2bOriginalTaxInvoiceNotFoundError | B2bRecipientNotFoundError | B2bSupplierNotFoundError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError | B2BTaxInvoiceStatusNotSendingCompletedError | B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, IssueB2bTaxInvoiceImmediatelyError.prototype)
		this.name = "IssueB2bTaxInvoiceImmediatelyError"
	}
}
export class RequestB2bTaxInvoiceReverseIssuanceError extends TaxInvoiceError {
	declare readonly data: B2BCannotChangeTaxTypeError | B2bExternalServiceError | B2bIdAlreadyExistsError | B2bIssuanceTypeMismatchError | B2bModificationNotProvidedError | B2bNotEnabledError | B2bOriginalTaxInvoiceNotFoundError | B2bRecipientNotFoundError | B2bSupplierNotFoundError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError | B2BTaxInvoiceStatusNotSendingCompletedError | B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2BCannotChangeTaxTypeError | B2bExternalServiceError | B2bIdAlreadyExistsError | B2bIssuanceTypeMismatchError | B2bModificationNotProvidedError | B2bNotEnabledError | B2bOriginalTaxInvoiceNotFoundError | B2bRecipientNotFoundError | B2bSupplierNotFoundError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError | B2BTaxInvoiceStatusNotSendingCompletedError | B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, RequestB2bTaxInvoiceReverseIssuanceError.prototype)
		this.name = "RequestB2bTaxInvoiceReverseIssuanceError"
	}
}
export class AttachB2bTaxInvoiceFileError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bFileNotFoundError | B2bNotEnabledError | B2bTaxInvoiceNotDraftedStatusError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bFileNotFoundError | B2bNotEnabledError | B2bTaxInvoiceNotDraftedStatusError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, AttachB2bTaxInvoiceFileError.prototype)
		this.name = "AttachB2bTaxInvoiceFileError"
	}
}
export class DeleteB2bTaxInvoiceAttachmentError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceAttachmentNotFoundError | B2bTaxInvoiceNotDraftedStatusError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceAttachmentNotFoundError | B2bTaxInvoiceNotDraftedStatusError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, DeleteB2bTaxInvoiceAttachmentError.prototype)
		this.name = "DeleteB2bTaxInvoiceAttachmentError"
	}
}
export class GetB2bTaxInvoiceAttachmentsError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetB2bTaxInvoiceAttachmentsError.prototype)
		this.name = "GetB2bTaxInvoiceAttachmentsError"
	}
}
export class CancelB2bTaxInvoiceIssuanceError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceNotIssuedStatusError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceNotIssuedStatusError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CancelB2bTaxInvoiceIssuanceError.prototype)
		this.name = "CancelB2bTaxInvoiceIssuanceError"
	}
}
export class CancelB2bTaxInvoiceRequestError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceNotRequestedStatusError | B2bTaxInvoiceNoRecipientDocumentKeyError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceNotRequestedStatusError | B2bTaxInvoiceNoRecipientDocumentKeyError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CancelB2bTaxInvoiceRequestError.prototype)
		this.name = "CancelB2bTaxInvoiceRequestError"
	}
}
export class IssueB2bTaxInvoiceError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotDraftedStatusError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceNotRequestedStatusError | B2bTaxInvoiceNoSupplierDocumentKeyError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotDraftedStatusError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceNotRequestedStatusError | B2bTaxInvoiceNoSupplierDocumentKeyError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, IssueB2bTaxInvoiceError.prototype)
		this.name = "IssueB2bTaxInvoiceError"
	}
}
export class GetB2bTaxInvoicePdfDownloadUrlError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetB2bTaxInvoicePdfDownloadUrlError.prototype)
		this.name = "GetB2bTaxInvoicePdfDownloadUrlError"
	}
}
export class GetB2bTaxInvoicePopupUrlError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetB2bTaxInvoicePopupUrlError.prototype)
		this.name = "GetB2bTaxInvoicePopupUrlError"
	}
}
export class GetB2bTaxInvoicePrintUrlError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetB2bTaxInvoicePrintUrlError.prototype)
		this.name = "GetB2bTaxInvoicePrintUrlError"
	}
}
export class RefuseB2bTaxInvoiceRequestError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceNotRequestedStatusError | B2bTaxInvoiceNoSupplierDocumentKeyError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceNotRequestedStatusError | B2bTaxInvoiceNoSupplierDocumentKeyError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, RefuseB2bTaxInvoiceRequestError.prototype)
		this.name = "RefuseB2bTaxInvoiceRequestError"
	}
}
export class requestB2bTaxInvoiceError extends TaxInvoiceError {
	declare readonly data: B2BCannotChangeTaxTypeError | B2bExternalServiceError | B2bIssuanceTypeMismatchError | B2bModificationNotProvidedError | B2bNotEnabledError | B2bOriginalTaxInvoiceNotFoundError | B2bTaxInvoiceNotDraftedStatusError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceNoRecipientDocumentKeyError | B2BTaxInvoiceStatusNotSendingCompletedError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2BCannotChangeTaxTypeError | B2bExternalServiceError | B2bIssuanceTypeMismatchError | B2bModificationNotProvidedError | B2bNotEnabledError | B2bOriginalTaxInvoiceNotFoundError | B2bTaxInvoiceNotDraftedStatusError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceNoRecipientDocumentKeyError | B2BTaxInvoiceStatusNotSendingCompletedError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, requestB2bTaxInvoiceError.prototype)
		this.name = "requestB2bTaxInvoiceError"
	}
}
export class SendToNtsB2bTaxInvoiceError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceNotIssuedStatusError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | B2bTaxInvoiceNotIssuedStatusError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, SendToNtsB2bTaxInvoiceError.prototype)
		this.name = "SendToNtsB2bTaxInvoiceError"
	}
}
export class GetB2bTaxInvoiceError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetB2bTaxInvoiceError.prototype)
		this.name = "GetB2bTaxInvoiceError"
	}
}
export class DeleteB2bTaxInvoiceError extends TaxInvoiceError {
	declare readonly data: B2bBulkTaxInvoiceNotFoundError | B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNonDeletableStatusError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bBulkTaxInvoiceNotFoundError | B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNonDeletableStatusError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, DeleteB2bTaxInvoiceError.prototype)
		this.name = "DeleteB2bTaxInvoiceError"
	}
}
export class GetB2bTaxInvoicesError extends TaxInvoiceError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | B2bTaxInvoiceNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetB2bTaxInvoicesError.prototype)
		this.name = "GetB2bTaxInvoicesError"
	}
}
