from django.test import TestCase
from unittest.mock import patch, Mock
from .utils import send_email_async  # Import your send_email_async function
import unittest

class EmailSendingTestCase(TestCase):

    @patch('CAT.utils.send_mail')  # Mock the send_mail function
    def test_send_email_async(self, mock_send_mail):
        # Mock the email_sent_signal function to capture signal emission
        mock_signal = Mock()
        mock_signal.connect.return_value = None
        with patch('CAT.signals.email_sent_signal', mock_signal):
            subject = "Test Subject"
            message = "Test Message"
            from_email = "test@example.com"
            recipient_list = ["recipient@example.com"]

            # Call your send_email_async function
            send_email_async(subject, message, from_email, recipient_list)

            # Assert that send_mail was called with the correct arguments
            mock_send_mail.assert_called_once_with(subject, message, from_email, recipient_list)

            # Assert that the email_sent_signal was sent
            mock_signal.return_value.send.assert_called_once_with(sender=None)

if __name__ == '__main__':
    unittest.main()
