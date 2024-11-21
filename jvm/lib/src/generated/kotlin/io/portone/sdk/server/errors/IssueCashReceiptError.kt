package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface IssueCashReceiptError {
  public sealed interface Recognized : IssueCashReceiptError {
    public val message: String?
  }
  public data object Unrecognized : IssueCashReceiptError
}
