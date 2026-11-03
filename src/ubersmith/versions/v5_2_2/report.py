from typing import Dict
from ubersmith.client.section import *

class ReportAPI(Section):
    """
    Auto-generated section for ``report``.

    Contains all ``report.*`` API methods.
    """

    def customer_revenue(
            self,
            class_id,
            begin=None,
            billing_period_type=None,
            client_ids=None,
            end=None,
            group_by=None,
            inv_type_select=None,
            invoice_ids=None,
            service_ids=None,
            service_plan_ids=None,
        ) -> Dict:
        """Customer Revenue

        API Method: report.customer_revenue

        This method is used to retrieve customer(s) revenue.

        Args:
            class_id: Brand ID,
            begin: Beginning Timestamp. Defaults to None.
            billing_period_type: Billing Period Type. Defaults to None.
            client_ids: Client Ids. Defaults to None.
            end: End Timestamp. Defaults to None.
            group_by: Group By. Defaults to None.
            inv_type_select: Invoice Status. Defaults to None.
            invoice_ids: Invoice IDs. Defaults to None.
            service_ids: Service IDs. Defaults to None.
            service_plan_ids: Service plan IDs. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'report.customer_revenue',
            class_id=class_id,
            **{'begin': begin} if begin else {},
            **{'billing_period_type': billing_period_type} if billing_period_type else {},
            **{'client_ids': client_ids} if client_ids else {},
            **{'end': end} if end else {},
            **{'group_by': group_by} if group_by else {},
            **{'inv_type_select': inv_type_select} if inv_type_select else {},
            **{'invoice_ids': invoice_ids} if invoice_ids else {},
            **{'service_ids': service_ids} if service_ids else {},
            **{'service_plan_ids': service_plan_ids} if service_plan_ids else {},
        )

    def customers_time_tracking(
            self,
            begin=None,
            class_id=None,
            classification=None,
            classification_ids=None,
            client_ids=None,
            department_ids=None,
            details=None,
            end=None,
            internal_ticket=None,
            service_ids=None,
            ticket_ids=None,
            ticket_type_ids=None,
            user_ids=None,
        ) -> Dict:
        """Customers Time Tracking

        API Method: report.customers_time_tracking

        This method is used to retrieve customer(s) time tracking.

        Args:
            begin: Beginning Timestamp. Defaults to None.
            class_id: Brand ID. Defaults to None.
            classification: Classification. Defaults to None.
            classification_ids: Classification (Exact). Defaults to None.
            client_ids: Customer Ids. Defaults to None.
            department_ids: Departments IDs. Defaults to None.
            details: Details. Defaults to None.
            end: End Timestamp. Defaults to None.
            internal_ticket: Internal Ticket. Defaults to None.
            service_ids: Service IDs (packid). Defaults to None.
            ticket_ids: Ticket IDs. Defaults to None.
            ticket_type_ids: Ticket Type IDs. Defaults to None.
            user_ids: User Ids. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'report.customers_time_tracking',
            **{'begin': begin} if begin else {},
            **{'class_id': class_id} if class_id else {},
            **{'classification': classification} if classification else {},
            **{'classification_ids': classification_ids} if classification_ids else {},
            **{'client_ids': client_ids} if client_ids else {},
            **{'department_ids': department_ids} if department_ids else {},
            **{'details': details} if details else {},
            **{'end': end} if end else {},
            **{'internal_ticket': internal_ticket} if internal_ticket else {},
            **{'service_ids': service_ids} if service_ids else {},
            **{'ticket_ids': ticket_ids} if ticket_ids else {},
            **{'ticket_type_ids': ticket_type_ids} if ticket_type_ids else {},
            **{'user_ids': user_ids} if user_ids else {},
        )

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

    def staff_time_tracking(
            self,
            begin=None,
            classification=None,
            classification_ids=None,
            client_ids=None,
            department_ids=None,
            details=None,
            end=None,
            internal_ticket=None,
            service_ids=None,
            ticket_ids=None,
            ticket_type_ids=None,
            user_ids=None,
            user_status=None,
        ) -> Dict:
        """Staff Time Tracking

        API Method: report.staff_time_tracking

        This method is used to retrieve the admin users time tracking.

        Args:
            begin: Beginning Timestamp. Defaults to None.
            classification: Classification. Defaults to None.
            classification_ids: Classification (Exact). Defaults to None.
            client_ids: Client Ids. Defaults to None.
            department_ids: Departments IDs. Defaults to None.
            details: Details. Defaults to None.
            end: End Timestamp. Defaults to None.
            internal_ticket: Internal Ticket. Defaults to None.
            service_ids: Service IDs. Defaults to None.
            ticket_ids: Ticket IDs. Defaults to None.
            ticket_type_ids: Ticket Type IDs. Defaults to None.
            user_ids: User Ids. Defaults to None.
            user_status: User Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'report.staff_time_tracking',
            **{'begin': begin} if begin else {},
            **{'classification': classification} if classification else {},
            **{'classification_ids': classification_ids} if classification_ids else {},
            **{'client_ids': client_ids} if client_ids else {},
            **{'department_ids': department_ids} if department_ids else {},
            **{'details': details} if details else {},
            **{'end': end} if end else {},
            **{'internal_ticket': internal_ticket} if internal_ticket else {},
            **{'service_ids': service_ids} if service_ids else {},
            **{'ticket_ids': ticket_ids} if ticket_ids else {},
            **{'ticket_type_ids': ticket_type_ids} if ticket_type_ids else {},
            **{'user_ids': user_ids} if user_ids else {},
            **{'user_status': user_status} if user_status else {},
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
