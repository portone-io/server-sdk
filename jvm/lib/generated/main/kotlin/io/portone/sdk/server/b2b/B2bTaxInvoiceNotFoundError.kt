package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서가 존재하지 않은 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_NOT_FOUND")
public data class B2bTaxInvoiceNotFoundError(
  override val message: String? = null,
): AttachB2bTaxInvoiceFileError,
  ): CancelB2bTaxInvoiceRequestError,
    ): DeleteB2bTaxInvoiceAttachmentError,
      ): DeleteB2bTaxInvoiceError,
        ): GetB2bTaxInvoiceAttachmentsError,
          ): GetB2bTaxInvoiceError,
            ): GetB2bTaxInvoicePdfDownloadUrlError,
              ): GetB2bTaxInvoicePopupUrlError,
                ): GetB2bTaxInvoicePrintUrlError,
                  ): IssueB2bTaxInvoiceError,
                    ): RefuseB2bTaxInvoiceRequestError,
                      ): requestB2bTaxInvoiceError,
