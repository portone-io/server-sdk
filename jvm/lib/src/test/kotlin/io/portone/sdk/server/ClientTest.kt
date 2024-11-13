import io.portone.sdk.server.PortOneClient
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.errors.PaymentAlreadyCancelledException
import io.portone.sdk.server.errors.PaymentNotFoundException
import io.portone.sdk.server.payment.CancelledPayment
import io.portone.sdk.server.payment.GetPaymentsResponse
import kotlinx.coroutines.test.runTest
import org.junit.jupiter.api.assertThrows
import kotlin.test.Test
import kotlin.test.assertContentEquals
import kotlin.test.assertIs

class ClientTest {
    private val apiSecret = System.getenv("PORTONE_API_SECRET")
    private val client = PortOneClient(apiSecret)

    @Test
    fun testGetPaymentsWithoutParams() =
        runTest {
            val payments = client.payment.getPayments()
            assertIs<GetPaymentsResponse>(payments)
        }

    @Test
    fun testGetPaymentsWithParams() =
        runTest {
            val payments = client.payment.getPayments(PageInput(3000))
            assertContentEquals(emptyList(), payments.items)
        }

    @Test
    fun testGetPaymentWithParams() =
        runTest {
            val payment = client.payment.getPayment("test-server-sdk")
            assertIs<CancelledPayment>(payment)
        }

    @Test
    fun testGetPaymentWithInvalidPaymentId() =
        runTest {
            assertThrows<PaymentNotFoundException> {
                client.payment.getPayment(" ")
            }
        }

    @Test
    fun testCancelPaymentWithAlreadyCancelledPaymentId() =
        runTest {
            assertThrows<PaymentAlreadyCancelledException> {
                client.payment.cancelPayment(paymentId = "test-server-sdk", reason = "test", amount = 1)
            }
        }
}