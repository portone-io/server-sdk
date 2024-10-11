package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bCompanyStateBusinessStatus
import io.portone.sdk.server.b2b.B2bModification
import io.portone.sdk.server.b2b.B2bTaxInvoiceAdditionalContact
import io.portone.sdk.server.b2b.B2bTaxInvoiceCompany
import io.portone.sdk.server.b2b.B2bTaxInvoiceItem
import io.portone.sdk.server.b2b.B2bTaxInvoicePurposeType
import io.portone.sdk.server.b2b.B2bTaxType
import kotlin.Array
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("ISSUANCE_CANCELLED")
public data class B2bTaxInvoiceIssuanceCancelled(
  /** 과세 유형 */
  override val taxType: B2bTaxType,
  /**
   * 작성일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  override val writeDate: String,
  /** 영수/청구 */
  override val purposeType: B2bTaxInvoicePurposeType,
  /** 공급가액 합계 */
  override val supplyCostTotalAmount: Long,
  /** 세액 합계 */
  override val taxTotalAmount: Long,
  /** 합계 금액 */
  override val totalAmount: Long,
  /**
   * 비고
   *
   * 최대 3개
   */
  override val remarks: Array<String>,
  /** 공급자 */
  override val supplier: B2bTaxInvoiceCompany,
  /** 공급받는자 */
  override val recipient: B2bTaxInvoiceCompany,
  /** 문자 전송 여부 */
  override val sendSms: Boolean,
  /**
   * 품목
   *
   * 최대 99개
   */
  override val items: Array<B2bTaxInvoiceItem>,
  /**
   * 추가 담당자
   *
   * 최대 3개
   */
  override val contacts: Array<B2bTaxInvoiceAdditionalContact>,
  /** 상태 변경 일시 */
  override val statusUpdatedAt: Instant,
  /** 발행 일시 */
  val issuedAt: Instant,
  /**
   * 국세청 승인번호
   *
   * 세금계산서 발행(전자서명) 시점에 자동으로 부여
   */
  val ntsApproveNumber: String,
  /** 일련번호 */
  override val serialNum: String? = null,
  /**
   * 책번호 - 권
   *
   * 입력 범위(4자리) : 0 ~ 9999
   */
  override val bookVolume: Int? = null,
  /**
   * 책번호 - 호
   *
   * 입력 범위(4자리) : 0 ~ 9999
   */
  override val bookIssue: Int? = null,
  /** 현금 */
  override val cashAmount: Long? = null,
  /** 수표 */
  override val checkAmount: Long? = null,
  /** 외상 */
  override val creditAmount: Long? = null,
  /** 수표 */
  override val noteAmount: Long? = null,
  /** 공급자 문서번호 */
  override val supplierDocumentKey: String? = null,
  /** 공급받는자 문서번호 */
  override val recipientDocumentKey: String? = null,
  /** 수정 사유 기재 */
  override val modification: B2bModification? = null,
  /** 공급받는자 영업 상태 */
  val recipientBusinessStatus: B2bCompanyStateBusinessStatus? = null,
  /**
   * 공급받는자 휴폐업일자
   *
   * 상태가 CLOSED, SUSPENDED 상태인 경우에만 결과값 반환
   */
  val recipientClosedSuspendedDate: String? = null,
): B2bTaxInvoice,
