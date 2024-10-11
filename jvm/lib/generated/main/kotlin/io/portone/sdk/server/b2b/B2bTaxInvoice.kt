package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bModification
import io.portone.sdk.server.b2b.B2bTaxInvoiceAdditionalContact
import io.portone.sdk.server.b2b.B2bTaxInvoiceCompany
import io.portone.sdk.server.b2b.B2bTaxInvoiceItem
import io.portone.sdk.server.b2b.B2bTaxInvoicePurposeType
import io.portone.sdk.server.b2b.B2bTaxType
import kotlin.Array
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("status")
public sealed interface B2bTaxInvoice {
  /** 과세 유형 */
  val taxType: B2bTaxType
  /** 일련번호 */
  val serialNum: String?
  /**
   * 책번호 - 권
   *
   * 입력 범위(4자리) : 0 ~ 9999
   */
  val bookVolume: Int?
  /**
   * 책번호 - 호
   *
   * 입력 범위(4자리) : 0 ~ 9999
   */
  val bookIssue: Int?
  /**
   * 작성일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  val writeDate: String
  /** 영수/청구 */
  val purposeType: B2bTaxInvoicePurposeType
  /** 공급가액 합계 */
  val supplyCostTotalAmount: Long
  /** 세액 합계 */
  val taxTotalAmount: Long
  /** 합계 금액 */
  val totalAmount: Long
  /** 현금 */
  val cashAmount: Long?
  /** 수표 */
  val checkAmount: Long?
  /** 외상 */
  val creditAmount: Long?
  /** 수표 */
  val noteAmount: Long?
  /**
   * 비고
   *
   * 최대 3개
   */
  val remarks: Array<String>
  /** 공급자 문서번호 */
  val supplierDocumentKey: String?
  /** 공급자 */
  val supplier: B2bTaxInvoiceCompany
  /** 공급받는자 문서번호 */
  val recipientDocumentKey: String?
  /** 공급받는자 */
  val recipient: B2bTaxInvoiceCompany
  /** 문자 전송 여부 */
  val sendSms: Boolean
  /** 수정 사유 기재 */
  val modification: B2bModification?
  /**
   * 품목
   *
   * 최대 99개
   */
  val items: Array<B2bTaxInvoiceItem>
  /**
   * 추가 담당자
   *
   * 최대 3개
   */
  val contacts: Array<B2bTaxInvoiceAdditionalContact>
  /** 상태 변경 일시 */
  val statusUpdatedAt: Instant,
}
