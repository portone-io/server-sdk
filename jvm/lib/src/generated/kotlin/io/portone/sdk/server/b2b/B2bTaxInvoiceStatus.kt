package io.portone.sdk.server.b2b

import kotlinx.serialization.Serializable

@Serializable
public enum class B2bTaxInvoiceStatus {
  /** 임시저장 */
  REGISTERED,
  /** 역발행대기 (전자 서명 요청됨) */
  REQUESTED,
  /** 공급받는자에 의한 발행취소 */
  REQUEST_CANCELLED_BY_RECIPIENT,
  /** 발행완료 */
  ISSUED,
  /** 전송전 */
  BEFORE_SENDING,
  /** 전송대기 */
  WAITING_SENDING,
  /** 전송중 */
  SENDING,
  /** 전송완료 */
  SENDING_COMPLETED,
  /** 전송실패 */
  SENDING_FAILED,
  /** 공급자의 발행거부 */
  REQUEST_REFUSED,
  /** 공급자에 의한 발행 취소 */
  ISSUANCE_CANCELLED_BY_SUPPLIER,
}
