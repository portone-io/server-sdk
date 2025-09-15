package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bCompanyStateBusinessStatus
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceDocumentModificationType
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceIssuanceType
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceItem
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoicePurposeType
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceStatus
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceTaxationType
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 요약 */
@Serializable
public data class B2bTaxInvoiceSummary(
  /** 세금계산서 아이디 */
  val id: String,
  /** 과세 유형 */
  val taxationType: B2bTaxInvoiceTaxationType,
  /** 문서 유형 */
  val documentModificationType: B2bTaxInvoiceDocumentModificationType,
  /** 지연 발행 여부 */
  val isDelayed: Boolean? = null,
  /** 발행 유형 */
  val issuanceType: B2bTaxInvoiceIssuanceType,
  /** 일괄 발행 아이디 */
  val bulkTaxInvoiceId: String? = null,
  /** 지급 아이디 */
  val payoutId: String? = null,
  /** 공급가액 합계 */
  val totalSupplyAmount: Long,
  /** 세액 합계 */
  val totalTaxAmount: Long,
  /** 합계 금액 */
  val totalAmount: Long,
  /** 영수/청구 */
  val purposeType: B2bTaxInvoicePurposeType,
  /** 공급자 사업자등록번호 */
  val supplierBrn: String,
  /** 공급자 상호 */
  val supplierName: String,
  /** 공급자 대표자 성명 */
  val supplierRepresentativeName: String,
  /** 공급자 문서번호 */
  val supplierDocumentKey: String? = null,
  /** 공급받는자 사업자등록번호 */
  val recipientBrn: String,
  /** 공급받는자 상호 */
  val recipientName: String,
  /** 공급받는자 대표자 성명 */
  val recipientRepresentativeName: String,
  /** 공급받는자 문서번호 */
  val recipientDocumentKey: String? = null,
  /** 공급받는자 영업 상태 */
  val recipientBusinessStatus: B2bCompanyStateBusinessStatus? = null,
  /**
   * 공급받는자 휴폐업일자
   *
   * 상태가 CLOSED, SUSPENDED 상태인 경우에만 결과값 반환
   * (yyyy-MM-dd)
   */
  val recipientClosedSuspendedDate: String? = null,
  /**
   * 작성일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val writeDate: String,
  /**
   * 발행 마감일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val issuanceDueDate: String,
  /** 상태 */
  val status: B2bTaxInvoiceStatus,
  /** 임시 저장 일시 */
  val draftedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 발행 요청 일시 */
  val requestedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 발행 일시 */
  val issuedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 개봉 일시 */
  val openedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 상태 변경 일시 */
  val statusUpdatedAt: @Serializable(InstantSerializer::class) Instant,
  /** 국세청 전송 일시 */
  val ntsSentAt: @Serializable(InstantSerializer::class) Instant? = null,
  /**
   * 국세청 승인번호
   *
   * 세금계산서 발행(전자서명) 시점에 자동으로 부여
   */
  val ntsApprovalNumber: String? = null,
  /** 국세청 전송 결과 */
  val ntsResult: String? = null,
  /** 국세청 결과 수신 일시 */
  val ntsResultReceivedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /**
   * 국세청 결과 코드
   *
   * 국세청 발급 결과 코드로 영문 3자리 + 숫자 3자리로 구성됨
   */
  val ntsResultCode: String? = null,
  /** 메모 */
  val memo: String? = null,
  /**
   * 품목
   *
   * 최대 99개
   */
  val items: List<B2bTaxInvoiceItem>,
)


