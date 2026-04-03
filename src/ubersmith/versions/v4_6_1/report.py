from typing import Dict
from ubersmith.client.section import *

class ReportAPI(Section):
    """
    Auto-generated section for ``report``.

    Contains all ``report.*`` API methods.
    """

    def device_event_log(
            self,
            begin=None,
            device=None,
            direction=None,
            end=None,
            event_group=None,
            event_type=None,
            eventuser=None,
            limit=None,
            next_cursor=None,
            order_by=None,
            searchfor=None,
            uri_prepend=None,
        ) -> Dict:
        """List of Device Event Log

        API Method: report.device_event_log

        This method is used to retrieve the device event logs.

        Args:
            begin: Begin Time. Defaults to None.
            device: Device. Defaults to None.
            direction: Order. Defaults to None.
            end: End Time. Defaults to None.
            event_group: Event Group. Defaults to None.
            event_type: Event Type. Defaults to None.
            eventuser: User. Defaults to None.
            limit: Limit. Defaults to None.
            next_cursor: Next Cursor. Defaults to None.
            order_by: Order By. Defaults to None.
            searchfor: Search term. Defaults to None.
            uri_prepend: Prepend to URI. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'report.device_event_log',
            **{'begin': begin} if begin else {},
            **{'device': device} if device else {},
            **{'direction': direction} if direction else {},
            **{'end': end} if end else {},
            **{'event_group': event_group} if event_group else {},
            **{'event_type': event_type} if event_type else {},
            **{'eventuser': eventuser} if eventuser else {},
            **{'limit': limit} if limit else {},
            **{'next_cursor': next_cursor} if next_cursor else {},
            **{'order_by': order_by} if order_by else {},
            **{'searchfor': searchfor} if searchfor else {},
            **{'uri_prepend': uri_prepend} if uri_prepend else {},
        )

    def global_event_log(
            self,
            begin=None,
            clientid=None,
            direction=None,
            end=None,
            event_group=None,
            eventuser=None,
            limit=None,
            next_cursor=None,
            order_by=None,
            reference_id=None,
            reference_type=None,
            searchfor=None,
            uri_prepend=None,
        ) -> Dict:
        """List of Global Event Log

        API Method: report.global_event_log

        This method is used to retrieve the global event logs.

        Args:
            begin: Begin Time. Defaults to None.
            clientid: Client. Defaults to None.
            direction: Order. Defaults to None.
            end: End Time. Defaults to None.
            event_group: Event Group. Defaults to None.
            eventuser: User. Defaults to None.
            limit: Limit. Defaults to None.
            next_cursor: Next Cursor. Defaults to None.
            order_by: Order By. Defaults to None.
            reference_id: Reference Id. Defaults to None.
            reference_type: Reference Type. Defaults to None.
            searchfor: Search term. Defaults to None.
            uri_prepend: Prepend to URI. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'report.global_event_log',
            **{'begin': begin} if begin else {},
            **{'clientid': clientid} if clientid else {},
            **{'direction': direction} if direction else {},
            **{'end': end} if end else {},
            **{'event_group': event_group} if event_group else {},
            **{'eventuser': eventuser} if eventuser else {},
            **{'limit': limit} if limit else {},
            **{'next_cursor': next_cursor} if next_cursor else {},
            **{'order_by': order_by} if order_by else {},
            **{'reference_id': reference_id} if reference_id else {},
            **{'reference_type': reference_type} if reference_type else {},
            **{'searchfor': searchfor} if searchfor else {},
            **{'uri_prepend': uri_prepend} if uri_prepend else {},
        )

    def ticket_event_log(
            self,
            begin=None,
            direction=None,
            end=None,
            event_group=None,
            limit=None,
            next_cursor=None,
            order_by=None,
            searchfor=None,
            ticket=None,
            uri_prepend=None,
            user=None,
        ) -> Dict:
        """List of Ticket Event Log

        API Method: report.ticket_event_log

        This method is used to retrieve the ticket event logs.

        Args:
            begin: Begin Time. Defaults to None.
            direction: Order. Defaults to None.
            end: End Time. Defaults to None.
            event_group: Event Group. Defaults to None.
            limit: Limit. Defaults to None.
            next_cursor: Next Cursor. Defaults to None.
            order_by: Order By. Defaults to None.
            searchfor: Search term. Defaults to None.
            ticket: Ticket. Defaults to None.
            uri_prepend: Prepend to URI. Defaults to None.
            user: User. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'report.ticket_event_log',
            **{'begin': begin} if begin else {},
            **{'direction': direction} if direction else {},
            **{'end': end} if end else {},
            **{'event_group': event_group} if event_group else {},
            **{'limit': limit} if limit else {},
            **{'next_cursor': next_cursor} if next_cursor else {},
            **{'order_by': order_by} if order_by else {},
            **{'searchfor': searchfor} if searchfor else {},
            **{'ticket': ticket} if ticket else {},
            **{'uri_prepend': uri_prepend} if uri_prepend else {},
            **{'user': user} if user else {},
        )
