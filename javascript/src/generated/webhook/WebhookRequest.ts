import type { WebhookBillingKeyRequestDeleted } from "./../webhook/WebhookBillingKeyRequestDeleted"
import type { WebhookBillingKeyRequestFailed } from "./../webhook/WebhookBillingKeyRequestFailed"
import type { WebhookBillingKeyRequestIssued } from "./../webhook/WebhookBillingKeyRequestIssued"
import type { WebhookBillingKeyRequestReady } from "./../webhook/WebhookBillingKeyRequestReady"
import type { WebhookBillingKeyRequestUpdated } from "./../webhook/WebhookBillingKeyRequestUpdated"
import type { WebhookTransactionRequestCancelPending } from "./../webhook/WebhookTransactionRequestCancelPending"
import type { WebhookTransactionRequestCancelled } from "./../webhook/WebhookTransactionRequestCancelled"
import type { WebhookTransactionRequestFailed } from "./../webhook/WebhookTransactionRequestFailed"
import type { WebhookTransactionRequestPaid } from "./../webhook/WebhookTransactionRequestPaid"
import type { WebhookTransactionRequestPartialCancelled } from "./../webhook/WebhookTransactionRequestPartialCancelled"
import type { WebhookTransactionRequestPayPending } from "./../webhook/WebhookTransactionRequestPayPending"
import type { WebhookTransactionRequestReady } from "./../webhook/WebhookTransactionRequestReady"
import type { WebhookTransactionRequestVirtualAccountIssued } from "./../webhook/WebhookTransactionRequestVirtualAccountIssued"

/** 웹훅 형식 */
export type WebhookRequest =
	/** 결제창이 열렸을 때 */
	| WebhookTransactionRequestReady
	/** 결제(예약 결제 포함)가 승인되었을 때 (모든 결제 수단) */
	| WebhookTransactionRequestPaid
	/** 가상계좌가 발급되었을 때 */
	| WebhookTransactionRequestVirtualAccountIssued
	/** 결제가 부분 취소되었을 때 */
	| WebhookTransactionRequestPartialCancelled
	/** 결제가 완전 취소되었을 때 */
	| WebhookTransactionRequestCancelled
	/** 결제(예약 결제 포함)가 실패했을 때 */
	| WebhookTransactionRequestFailed
	/** 결제 승인 대기 상태가 되었을 때 (해외 결제시 발생 가능) */
	| WebhookTransactionRequestPayPending
	/** (결제 취소가 비동기로 수행되는 경우) 결제 취소를 요청했을 때 */
	| WebhookTransactionRequestCancelPending
	/** 빌링키 발급창이 열렸을 때 */
	| WebhookBillingKeyRequestReady
	/** 빌링키가 발급되었을 때 */
	| WebhookBillingKeyRequestIssued
	/** 빌링키 발급이 실패했을 때 */
	| WebhookBillingKeyRequestFailed
	/** 빌링키가 삭제되었을 때 */
	| WebhookBillingKeyRequestDeleted
	/** 빌링키가 업데이트되었을 때 */
	| WebhookBillingKeyRequestUpdated
