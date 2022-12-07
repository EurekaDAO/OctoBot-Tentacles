import octobot_services.notification as notification
import octobot_services.notifier as notifier
import tentacles.Services.Services_bases as Services_bases

class OutboundWebServiceNotifier(notifier.AbstractNotifier):
    REQUIRED_SERVICES = [Services_bases.TwitterService]
    NOTIFICATION_TYPE_KEY = "web"

    async def _handle_notification(self, notification: notification.Notification):
        self.logger.debug(f"sending notification: {notification}")
        if notification.linked_notification is None:
            result = await self._send_data(notification)
        else:
            result = await self._send_data(notification)
        if result is None:
            self.logger.error(f"Data is not sent, notification: {notification}")
        else:
            self.logger.info("Data sent")

    async def _send_data(self, notification):
        result = await self.services[0].send_to_backend(self._get_notification_text(notification), True)
        notification.metadata[self.NOTIFICATION_TYPE_KEY] = result
        return result


    @staticmethod
    def _get_notification_text(notification):
        return f"{notification.title}\n{notification.text}" if notification.title else notification.text