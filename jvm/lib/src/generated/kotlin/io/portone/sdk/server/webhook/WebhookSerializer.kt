package io.portone.sdk.server.webhook
import kotlinx.serialization.DeserializationStrategy
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

internal object WebhookSerializer : JsonContentPolymorphicSerializer<Webhook>(Webhook::class) {
  override fun selectDeserializer(element: JsonElement): DeserializationStrategy<Webhook> = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "Transaction.Ready" -> WebhookTransactionReady.serializer()
    "Transaction.Paid" -> WebhookTransactionPaid.serializer()
    "Transaction.VirtualAccountIssued" -> WebhookTransactionVirtualAccountIssued.serializer()
    "Transaction.PartialCancelled" -> WebhookTransactionCancelledPartialCancelled.serializer()
    "Transaction.Cancelled" -> WebhookTransactionCancelledCancelled.serializer()
    "Transaction.Failed" -> WebhookTransactionFailed.serializer()
    "Transaction.PayPending" -> WebhookTransactionPayPending.serializer()
    "Transaction.CancelPending" -> WebhookTransactionCancelledCancelPending.serializer()
    "BillingKey.Ready" -> WebhookBillingKeyReady.serializer()
    "BillingKey.Issued" -> WebhookBillingKeyIssued.serializer()
    "BillingKey.Failed" -> WebhookBillingKeyFailed.serializer()
    "BillingKey.Deleted" -> WebhookBillingKeyDeleted.serializer()
    "BillingKey.Updated" -> WebhookBillingKeyUpdated.serializer()
    else -> Webhook.Unrecognized.serializer()
  }
}
