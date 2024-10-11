package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bCompanyStateBusinessStatus
import io.portone.sdk.server.b2b.B2bTaxInvoicePurposeType
import io.portone.sdk.server.b2b.B2bTaxInvoiceStatus
import io.portone.sdk.server.b2b.B2bTaxType
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 세금계산서 요약 */
@Serializable
public data class B2bTaxInvoiceSummary(
  /** 과세 유형 */
  val taxType: B2bTaxType,
  /** 공급가액 합계 */
  val supplyCostTotalAmount: Long,
  /** 세액 합계 */
  val taxTotalAmount: Long,
  /** 영수/청구 */
  val purposeType: B2bTaxInvoicePurposeType,
  /** 공급자 사업자등록번호 */
  val supplierBrn: String,
  /** 공급자 상호 */
  val supplierName: String,
  /** 공급받는자 사업자등록번호 */
  val recipientBrn: String,
  /** 공급받는자 상호 */
  val recipientName: String,
  /** 상태 */
  val status: B2bTaxInvoiceStatus,
  /** 상태 변경 일시 */
  val statusUpdatedAt: Instant,
  /** 공급자 문서번호 */
  val supplierDocumentKey: String? = null,
  /** 공급받는자 문서번호 */
  val recipientDocumentKey: String? = null,
  /** 공급받는자 영업 상태 */
  val recipientBusinessStatus: B2bCompanyStateBusinessStatus? = null,
  /**
   * 공급받는자 휴폐업일자
   *
   * 상태가 CLOSED, SUSPENDED 상태인 경우에만 결과값 반환
   */
  val recipientClosedSuspendedDate: String? = null,
  /** 발행 일시 */
  val issuedAt: Instant? = null,
  /** 개봉 일시 */
  val openedAt: Instant? = null,
  /**
   * 국세청 승인번호
   *
   * 세금계산서 발행(전자서명) 시점에 자동으로 부여
   */
  val ntsApproveNumber: String? = null,
  /** 국세청 전송 결과 */
  val ntsResult: String? = null,
  /** 국세청 전송 일시 */
  val ntsSentAt: Instant? = null,
  /** 국세청 결과 수신 일시 */
  val ntsResultReceivedAt: Instant? = null,
  /**
   * 국세청 결과 코드
   *
   * 국세청 발급 결과 코드로 영문 3자리 + 숫자 3자리로 구성됨
   */
  val ntsResultCode: String? = null,
)
