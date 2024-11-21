package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface CancelCashReceiptError {
  public sealed interface Recognized : CancelCashReceiptError {
    public val message: String?
  }
  public data object Unrecognized : CancelCashReceiptError
}
