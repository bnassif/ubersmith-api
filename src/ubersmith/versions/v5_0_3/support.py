from typing import Dict
from ubersmith.client.section import *

class SupportAPI(Section):
    """
    Auto-generated section for ``support``.

    Contains all ``support.*`` API methods.
    """

    def classification_list(
            self,
            applicable=None,
            client_selectable=None,
            direction=None,
            limit=None,
            offset=None,
            order_by=None,
            q_id=None,
        ) -> Dict:
        """List Classifications

        API Method: support.classification_list

        This method is used to return a list of the classifications in the system.

        Args:
            applicable: Applicable. Defaults to None.
            client_selectable: Client Selectable. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            q_id: Department ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.classification_list',
            **{'applicable': applicable} if applicable else {},
            **{'client_selectable': client_selectable} if client_selectable else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'q_id': q_id} if q_id else {},
        )

    def department_get(
            self,
            queue,
        ) -> Dict:
        """Get Ticket Departments

        API Method: support.department_get

        This method is used to return the details for a specific department.

        Args:
            queue: Department ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.department_get',
            queue=queue,
        )

    def department_list(
            self,
        ) -> Dict:
        """List Ticket Departments

        API Method: support.department_list

        This method is used to return a list of the ticket departments in the system.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.department_list',
        )

    def resolution_list(
            self,
            applicable=None,
            direction=None,
            limit=None,
            offset=None,
            order_by=None,
            q_id=None,
        ) -> Dict:
        """List Resolutions

        API Method: support.resolution_list

        This method is used to return a list of the resolutions in the system.

        Args:
            applicable: Applicable. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            q_id: Department ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.resolution_list',
            **{'applicable': applicable} if applicable else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'q_id': q_id} if q_id else {},
        )

    def ticket_add_link(
            self,
            link_type_id,
            ticket2_id,
            ticket_id,
            comment=None,
            public_comment=None,
        ) -> Dict:
        """Link Support Tickets

        API Method: support.ticket_add_link

        This method is used to link two support tickets.

        Args:
            link_type_id: Link Type ID,
            ticket2_id: Ticket ID (Sub),
            ticket_id: Ticket ID (Main),
            comment: Comment. Defaults to None.
            public_comment: Public Comment. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_add_link',
            link_type_id=link_type_id,
            ticket2_id=ticket2_id,
            ticket_id=ticket_id,
            **{'comment': comment} if comment else {},
            **{'public_comment': public_comment} if public_comment else {},
        )

    def ticket_count(
            self,
            activity_begin=None,
            activity_end=None,
            assignment=None,
            begin=None,
            classification=None,
            classification_id=None,
            client_activity_begin=None,
            client_activity_end=None,
            client_id=None,
            contact_id=None,
            device_id=None,
            end=None,
            impact=None,
            internal_ticket=None,
            metadata=None,
            opportunity_id=None,
            order_id=None,
            priority=None,
            queue=None,
            service_id=None,
            ticket_post_begin=None,
            ticket_post_end=None,
            type=None,
        ) -> Dict:
        """Count Support Tickets

        API Method: support.ticket_count

        This method is used to count the number of support tickets in the system.

        Args:
            activity_begin: Activity Begin Timestamp. Defaults to None.
            activity_end: Activity End Timestamp. Defaults to None.
            assignment: Assigned admin ID. Defaults to None.
            begin: Beginning Timestamp. Defaults to None.
            classification: Classification. Defaults to None.
            classification_id: Classification (Exact). Defaults to None.
            client_activity_begin: Client Activity Begin Timestamp. Defaults to None.
            client_activity_end: Client Activity End Timestamp. Defaults to None.
            client_id: Client Login. Defaults to None.
            contact_id: Contact ID. Defaults to None.
            device_id: Device ID. Defaults to None.
            end: End Timestamp. Defaults to None.
            impact: Ticket Impact. Defaults to None.
            internal_ticket: Internal Ticket. Defaults to None.
            metadata: Apply custom field filters. Defaults to None.
            opportunity_id: Opportunity ID. Defaults to None.
            order_id: Order ID. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            queue: Ticket Department ID. Defaults to None.
            service_id: Service ID. Defaults to None.
            ticket_post_begin: Ticket Post Begin Timestamp. Defaults to None.
            ticket_post_end: Ticket Post End Timestamp. Defaults to None.
            type: Ticket Type. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_count',
            **{'activity_begin': activity_begin} if activity_begin else {},
            **{'activity_end': activity_end} if activity_end else {},
            **{'assignment': assignment} if assignment else {},
            **{'begin': begin} if begin else {},
            **{'classification': classification} if classification else {},
            **{'classification_id': classification_id} if classification_id else {},
            **{'client_activity_begin': client_activity_begin} if client_activity_begin else {},
            **{'client_activity_end': client_activity_end} if client_activity_end else {},
            **{'client_id': client_id} if client_id else {},
            **{'contact_id': contact_id} if contact_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'end': end} if end else {},
            **{'impact': impact} if impact else {},
            **{'internal_ticket': internal_ticket} if internal_ticket else {},
            **{'metadata': metadata} if metadata else {},
            **{'opportunity_id': opportunity_id} if opportunity_id else {},
            **{'order_id': order_id} if order_id else {},
            **{'priority': priority} if priority else {},
            **{'queue': queue} if queue else {},
            **{'service_id': service_id} if service_id else {},
            **{'ticket_post_begin': ticket_post_begin} if ticket_post_begin else {},
            **{'ticket_post_end': ticket_post_end} if ticket_post_end else {},
            **{'type': type} if type else {},
        )

    def ticket_delete_link(
            self,
            ticket2_id,
            ticket_id,
        ) -> Dict:
        """Delete Link Between Support Tickets

        API Method: support.ticket_delete_link

        This method is used to delete the link between two support tickets.

        Args:
            ticket2_id: Ticket ID (Sub),
            ticket_id: Ticket ID (Main),
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_delete_link',
            ticket2_id=ticket2_id,
            ticket_id=ticket_id,
        )

    def ticket_get(
            self,
            ticket_id,
        ) -> Dict:
        """Get Support Ticket Details

        API Method: support.ticket_get

        This method is used to get the details of a specified support ticket.

        Args:
            ticket_id: Ticket ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_get',
            ticket_id=ticket_id,
        )

    def ticket_list(
            self,
            meta=None,
            activity_begin=None,
            activity_end=None,
            assignment=None,
            begin=None,
            classification=None,
            classification_id=None,
            client_activity_begin=None,
            client_activity_end=None,
            client_id=None,
            contact_id=None,
            device_id=None,
            direction=None,
            end=None,
            impact=None,
            internal_ticket=None,
            limit=None,
            metadata=None,
            offset=None,
            opportunity_id=None,
            order_by=None,
            order_id=None,
            priority=None,
            queue=None,
            service_id=None,
            ticket_post_begin=None,
            ticket_post_end=None,
            type=None,
        ) -> Dict:
        """Get a List of Tickets

        API Method: support.ticket_list

        This method is used to return a list of tickets.

        Args:
            meta: Custom Field Filters. Defaults to None.
            activity_begin: Activity Begin Timestamp. Defaults to None.
            activity_end: Activity End Timestamp. Defaults to None.
            assignment: Assigned admin ID. Defaults to None.
            begin: Beginning Timestamp. Defaults to None.
            classification: Classification. Defaults to None.
            classification_id: Classification (Exact). Defaults to None.
            client_activity_begin: Client Activity Begin Timestamp. Defaults to None.
            client_activity_end: Client Activity End Timestamp. Defaults to None.
            client_id: Client Login. Defaults to None.
            contact_id: Contact ID. Defaults to None.
            device_id: Device ID. Defaults to None.
            direction: Direction. Defaults to None.
            end: End Timestamp. Defaults to None.
            impact: Ticket Impact. Defaults to None.
            internal_ticket: Internal Ticket. Defaults to None.
            limit: Limit. Defaults to None.
            metadata: Include Custom Fields. Defaults to None.
            offset: Offset. Defaults to None.
            opportunity_id: Opportunity ID. Defaults to None.
            order_by: Order By. Defaults to None.
            order_id: Order ID. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            queue: Ticket Department ID. Defaults to None.
            service_id: Service ID. Defaults to None.
            ticket_post_begin: Ticket Post Begin Timestamp. Defaults to None.
            ticket_post_end: Ticket Post End Timestamp. Defaults to None.
            type: Ticket Type. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_list',
            **{'meta': meta} if meta else {},
            **{'activity_begin': activity_begin} if activity_begin else {},
            **{'activity_end': activity_end} if activity_end else {},
            **{'assignment': assignment} if assignment else {},
            **{'begin': begin} if begin else {},
            **{'classification': classification} if classification else {},
            **{'classification_id': classification_id} if classification_id else {},
            **{'client_activity_begin': client_activity_begin} if client_activity_begin else {},
            **{'client_activity_end': client_activity_end} if client_activity_end else {},
            **{'client_id': client_id} if client_id else {},
            **{'contact_id': contact_id} if contact_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'direction': direction} if direction else {},
            **{'end': end} if end else {},
            **{'impact': impact} if impact else {},
            **{'internal_ticket': internal_ticket} if internal_ticket else {},
            **{'limit': limit} if limit else {},
            **{'metadata': metadata} if metadata else {},
            **{'offset': offset} if offset else {},
            **{'opportunity_id': opportunity_id} if opportunity_id else {},
            **{'order_by': order_by} if order_by else {},
            **{'order_id': order_id} if order_id else {},
            **{'priority': priority} if priority else {},
            **{'queue': queue} if queue else {},
            **{'service_id': service_id} if service_id else {},
            **{'ticket_post_begin': ticket_post_begin} if ticket_post_begin else {},
            **{'ticket_post_end': ticket_post_end} if ticket_post_end else {},
            **{'type': type} if type else {},
        )

    def ticket_merge(
            self,
            merge_ticket_id,
            ticket_id,
        ) -> Dict:
        """Merge Tickets

        API Method: support.ticket_merge

        This method is used to merge two tickets.

        Args:
            merge_ticket_id: Ticket ID (Sub),
            ticket_id: Ticket ID (Main),
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_merge',
            merge_ticket_id=merge_ticket_id,
            ticket_id=ticket_id,
        )

    def ticket_post_client_response(
            self,
            ticket_id,
            author=None,
            body=None,
            cc=None,
            contact_id=None,
            no_notification=None,
            subject=None,
            timestamp=None,
        ) -> Dict:
        """Post a Client Response to a Ticket

        API Method: support.ticket_post_client_response

        This method is used to post a client response to a ticket, in the same way as if the client had responded via the client interface.

        Args:
            ticket_id: Ticket ID,
            author: Client Email Address. Defaults to None.
            body: Response Body. Defaults to None.
            cc: CC Address(es). Defaults to None.
            contact_id: Contact ID. Defaults to None.
            no_notification: Do Not Send Notification. Defaults to None.
            subject: Response Subject. Defaults to None.
            timestamp: Timestamp. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_post_client_response',
            ticket_id=ticket_id,
            **{'author': author} if author else {},
            **{'body': body} if body else {},
            **{'cc': cc} if cc else {},
            **{'contact_id': contact_id} if contact_id else {},
            **{'no_notification': no_notification} if no_notification else {},
            **{'subject': subject} if subject else {},
            **{'timestamp': timestamp} if timestamp else {},
        )

    def ticket_post_list(
            self,
            begin=None,
            direction=None,
            end=None,
            limit=None,
            offset=None,
            order_by=None,
            private=None,
            ticket_id=None,
            ticket_post_id=None,
        ) -> Dict:
        """Get all Posts for a Ticket

        API Method: support.ticket_post_list

        This method is used to return all the posts for the specified ticket.

        Args:
            begin: Ticket Post Begin Timestamp. Defaults to None.
            direction: Direction. Defaults to None.
            end: Ticket Post End Timestamp. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            private: Show only client-viewable posts. Defaults to None.
            ticket_id: Ticket ID. Defaults to None.
            ticket_post_id: Ticket Post ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_post_list',
            **{'begin': begin} if begin else {},
            **{'direction': direction} if direction else {},
            **{'end': end} if end else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'private': private} if private else {},
            **{'ticket_id': ticket_id} if ticket_id else {},
            **{'ticket_post_id': ticket_post_id} if ticket_post_id else {},
        )

    def ticket_post_staff_response(
            self,
            ticket_id,
            bcc=None,
            body=None,
            cc=None,
            comment=None,
            from_address=None,
            no_notification=None,
            recipient=None,
            subject=None,
            time_spent=None,
            timestamp=None,
            user_id=None,
        ) -> Dict:
        """Post a Staff Response to a Ticket

        API Method: support.ticket_post_staff_response

        This method is used to post a staff response to a ticket.

        Args:
            ticket_id: Ticket ID,
            bcc: BCC Address(es). Defaults to None.
            body: Response Body. Defaults to None.
            cc: CC Address(es). Defaults to None.
            comment: Comment Only. Defaults to None.
            from_address: Author's Name and/or Email. Defaults to None.
            no_notification: Do Not Send Notification. Defaults to None.
            recipient: Recipient Email. Defaults to None.
            subject: Response Subject. Defaults to None.
            time_spent: Time Spent. Defaults to None.
            timestamp: Timestamp. Defaults to None.
            user_id: Admin ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_post_staff_response',
            ticket_id=ticket_id,
            **{'bcc': bcc} if bcc else {},
            **{'body': body} if body else {},
            **{'cc': cc} if cc else {},
            **{'comment': comment} if comment else {},
            **{'from_address': from_address} if from_address else {},
            **{'no_notification': no_notification} if no_notification else {},
            **{'recipient': recipient} if recipient else {},
            **{'subject': subject} if subject else {},
            **{'time_spent': time_spent} if time_spent else {},
            **{'timestamp': timestamp} if timestamp else {},
            **{'user_id': user_id} if user_id else {},
        )

    def ticket_submit(
            self,
            body,
            subject,
            author=None,
            bcc=None,
            brand_id=None,
            cc=None,
            classification_id=None,
            client_id=None,
            contact_id=None,
            device_id=None,
            impact=None,
            internal_ticket=None,
            meta=None,
            name=None,
            no_notification=None,
            opportunity_id=None,
            order_id=None,
            priority=None,
            queue=None,
            quote_id=None,
            service_id=None,
            ticket_resolution_id=None,
            timestamp=None,
        ) -> Dict:
        """Submit a New Ticket

        API Method: support.ticket_submit

        This method is used to create a new support ticket.

        Args:
            body: Ticket Body,
            subject: Ticket Subject,
            author: Author Email Address. Defaults to None.
            bcc: Bcc Address(es). Defaults to None.
            brand_id: Brand ID. Defaults to None.
            cc: Cc Address(es). Defaults to None.
            classification_id: Classification ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            contact_id: Contact ID. Defaults to None.
            device_id: Associate Device. Defaults to None.
            impact: Ticket Impact. Defaults to None.
            internal_ticket: Internal Ticket. Defaults to None.
            meta: Custom Fields. Defaults to None.
            name: Author Name. Defaults to None.
            no_notification: Do Not Send Notification. Defaults to None.
            opportunity_id: Opportunity ID. Defaults to None.
            order_id: Order ID. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            queue: Ticket Department ID. Defaults to None.
            quote_id: Quote ID. Defaults to None.
            service_id: Associate Service. Defaults to None.
            ticket_resolution_id: Resolution ID. Defaults to None.
            timestamp: Timestamp. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_submit',
            body=body,
            subject=subject,
            **{'author': author} if author else {},
            **{'bcc': bcc} if bcc else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'cc': cc} if cc else {},
            **{'classification_id': classification_id} if classification_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'contact_id': contact_id} if contact_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'impact': impact} if impact else {},
            **{'internal_ticket': internal_ticket} if internal_ticket else {},
            **{'meta': meta} if meta else {},
            **{'name': name} if name else {},
            **{'no_notification': no_notification} if no_notification else {},
            **{'opportunity_id': opportunity_id} if opportunity_id else {},
            **{'order_id': order_id} if order_id else {},
            **{'priority': priority} if priority else {},
            **{'queue': queue} if queue else {},
            **{'quote_id': quote_id} if quote_id else {},
            **{'service_id': service_id} if service_id else {},
            **{'ticket_resolution_id': ticket_resolution_id} if ticket_resolution_id else {},
            **{'timestamp': timestamp} if timestamp else {},
        )

    def ticket_submit_outgoing(
            self,
            body,
            author=None,
            bcc=None,
            brand_id=None,
            cc=None,
            classification_id=None,
            client_id=None,
            contact_id=None,
            device_id=None,
            impact=None,
            internal_ticket=None,
            meta=None,
            no_notification=None,
            opportunity_id=None,
            order_id=None,
            priority=None,
            queue=None,
            quote_id=None,
            recipient=None,
            service_id=None,
            subject=None,
            timestamp=None,
            user_id=None,
        ) -> Dict:
        """Create a New Outgoing Ticket

        API Method: support.ticket_submit_outgoing

        This method is used to create a new outgoing support ticket.

        Args:
            body: Ticket Body,
            author: Author Email Address. Defaults to None.
            bcc: Bcc Address(es). Defaults to None.
            brand_id: Brand ID. Defaults to None.
            cc: Cc Address(es). Defaults to None.
            classification_id: Classification ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            contact_id: Contact ID. Defaults to None.
            device_id: Associate Device. Defaults to None.
            impact: Ticket Impact. Defaults to None.
            internal_ticket: Internal Ticket. Defaults to None.
            meta: Custom Fields. Defaults to None.
            no_notification: Do Not Send Notification. Defaults to None.
            opportunity_id: Opportunity ID. Defaults to None.
            order_id: Order ID. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            queue: Ticket Department ID. Defaults to None.
            quote_id: Quote ID. Defaults to None.
            recipient: Recipient Email. Defaults to None.
            service_id: Associate Service. Defaults to None.
            subject: Ticket Subject. Defaults to None.
            timestamp: Timestamp. Defaults to None.
            user_id: Admin ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_submit_outgoing',
            body=body,
            **{'author': author} if author else {},
            **{'bcc': bcc} if bcc else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'cc': cc} if cc else {},
            **{'classification_id': classification_id} if classification_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'contact_id': contact_id} if contact_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'impact': impact} if impact else {},
            **{'internal_ticket': internal_ticket} if internal_ticket else {},
            **{'meta': meta} if meta else {},
            **{'no_notification': no_notification} if no_notification else {},
            **{'opportunity_id': opportunity_id} if opportunity_id else {},
            **{'order_id': order_id} if order_id else {},
            **{'priority': priority} if priority else {},
            **{'queue': queue} if queue else {},
            **{'quote_id': quote_id} if quote_id else {},
            **{'recipient': recipient} if recipient else {},
            **{'service_id': service_id} if service_id else {},
            **{'subject': subject} if subject else {},
            **{'timestamp': timestamp} if timestamp else {},
            **{'user_id': user_id} if user_id else {},
        )

    def ticket_time_update(
            self,
            ticket_post_id,
            time_spent,
            billable=None,
            user_id=None,
        ) -> Dict:
        """Update Time Spent on a Ticket

        API Method: support.ticket_time_update

        This method is used to update time spent on a ticket.

        Args:
            ticket_post_id: Ticket Post ID,
            time_spent: Time Spent,
            billable: Billable. Defaults to None.
            user_id: User ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_time_update',
            ticket_post_id=ticket_post_id,
            time_spent=time_spent,
            **{'billable': billable} if billable else {},
            **{'user_id': user_id} if user_id else {},
        )

    def ticket_timer_add(
            self,
            ticket_id,
            ts,
            assignment=None,
            auto_remove=None,
            notify_body=None,
            notify_email=None,
            notify_subject=None,
            priority=None,
            q_id=None,
            respond=None,
            respond_body=None,
            respond_from=None,
            respond_subject=None,
            type=None,
        ) -> Dict:
        """Add a New Ticket Timer

        API Method: support.ticket_timer_add

        This method is used to add a new ticket timer to a ticket.

        Args:
            ticket_id: Ticket ID,
            ts: Timestamp,
            assignment: Assign to Admin. Defaults to None.
            auto_remove: Auto Remove on Reply. Defaults to None.
            notify_body: Notification Body. Defaults to None.
            notify_email: Notification To. Defaults to None.
            notify_subject: Notification Subject. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            q_id: Ticket Department ID. Defaults to None.
            respond: Update Type. Defaults to None.
            respond_body: Update Body. Defaults to None.
            respond_from: Update From. Defaults to None.
            respond_subject: Update Subject. Defaults to None.
            type: Ticket Type. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_timer_add',
            ticket_id=ticket_id,
            ts=ts,
            **{'assignment': assignment} if assignment else {},
            **{'auto_remove': auto_remove} if auto_remove else {},
            **{'notify_body': notify_body} if notify_body else {},
            **{'notify_email': notify_email} if notify_email else {},
            **{'notify_subject': notify_subject} if notify_subject else {},
            **{'priority': priority} if priority else {},
            **{'q_id': q_id} if q_id else {},
            **{'respond': respond} if respond else {},
            **{'respond_body': respond_body} if respond_body else {},
            **{'respond_from': respond_from} if respond_from else {},
            **{'respond_subject': respond_subject} if respond_subject else {},
            **{'type': type} if type else {},
        )

    def ticket_timer_delete(
            self,
            ticket_timer_id,
        ) -> Dict:
        """Delete a Ticket Timer

        API Method: support.ticket_timer_delete

        This method is used to delete a ticket timer.

        Args:
            ticket_timer_id: Ticket Timer ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_timer_delete',
            ticket_timer_id=ticket_timer_id,
        )

    def ticket_timer_list(
            self,
            ticket_id,
            assignment=None,
            auto_remove=None,
            direction=None,
            limit=None,
            offset=None,
            order_by=None,
            priority=None,
            q_id=None,
            type=None,
        ) -> Dict:
        """Get a List of Ticket Timers

        API Method: support.ticket_timer_list

        This method is used to return a list of ticket timers.

        Args:
            ticket_id: Ticket ID,
            assignment: Assign to Admin. Defaults to None.
            auto_remove: Auto Remove on Reply. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            q_id: Ticket Department ID. Defaults to None.
            type: Ticket Type. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_timer_list',
            ticket_id=ticket_id,
            **{'assignment': assignment} if assignment else {},
            **{'auto_remove': auto_remove} if auto_remove else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'priority': priority} if priority else {},
            **{'q_id': q_id} if q_id else {},
            **{'type': type} if type else {},
        )

    def ticket_timer_update(
            self,
            ticket_timer_id,
            assignment=None,
            auto_remove=None,
            notify_body=None,
            notify_email=None,
            notify_subject=None,
            priority=None,
            q_id=None,
            respond=None,
            respond_body=None,
            respond_from=None,
            respond_subject=None,
            ts=None,
            type=None,
        ) -> Dict:
        """Update a Ticket Timer

        API Method: support.ticket_timer_update

        This method is used to update a ticket timer.

        Args:
            ticket_timer_id: Ticket Timer ID,
            assignment: Assign to Admin. Defaults to None.
            auto_remove: Auto Remove on Reply. Defaults to None.
            notify_body: Notification Body. Defaults to None.
            notify_email: Notification To. Defaults to None.
            notify_subject: Notification Subject. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            q_id: Ticket Department ID. Defaults to None.
            respond: Update Type. Defaults to None.
            respond_body: Update Body. Defaults to None.
            respond_from: Update From. Defaults to None.
            respond_subject: Update Subject. Defaults to None.
            ts: Timestamp. Defaults to None.
            type: Ticket Type. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_timer_update',
            ticket_timer_id=ticket_timer_id,
            **{'assignment': assignment} if assignment else {},
            **{'auto_remove': auto_remove} if auto_remove else {},
            **{'notify_body': notify_body} if notify_body else {},
            **{'notify_email': notify_email} if notify_email else {},
            **{'notify_subject': notify_subject} if notify_subject else {},
            **{'priority': priority} if priority else {},
            **{'q_id': q_id} if q_id else {},
            **{'respond': respond} if respond else {},
            **{'respond_body': respond_body} if respond_body else {},
            **{'respond_from': respond_from} if respond_from else {},
            **{'respond_subject': respond_subject} if respond_subject else {},
            **{'ts': ts} if ts else {},
            **{'type': type} if type else {},
        )

    def ticket_type_list(
            self,
            direction=None,
            limit=None,
            offset=None,
            order_by=None,
            queue=None,
        ) -> Dict:
        """Get a List of Ticket Types

        API Method: support.ticket_type_list

        This method is used to return a list of ticket types.  If the q_id parameter is specified the output will include a client_selectable element indicating whether clients are allowed to select each type in the specific department.

        Args:
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            queue: Ticket Department ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_type_list',
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'queue': queue} if queue else {},
        )

    def ticket_update(
            self,
            ticket_id,
            assignment=None,
            author=None,
            bcc=None,
            cc=None,
            classification_id=None,
            client_id=None,
            contact_id=None,
            device_id=None,
            impact=None,
            internal_ticket=None,
            meta=None,
            opportunity_id=None,
            order_id=None,
            priority=None,
            queue=None,
            quote_id=None,
            service_id=None,
            subject=None,
            ticket_resolution_id=None,
            type=None,
            weight=None,
        ) -> Dict:
        """Update a Ticket

        API Method: support.ticket_update

        This method is used to update the details of a ticket.

        Args:
            ticket_id: Ticket ID,
            assignment: Assigned User ID. Defaults to None.
            author: Ticket Author Email Address. Defaults to None.
            bcc: Bcc Address(es). Defaults to None.
            cc: Cc Address(es). Defaults to None.
            classification_id: Classification ID. Defaults to None.
            client_id: Associate Client. Defaults to None.
            contact_id: Associate Contact. Defaults to None.
            device_id: Associate Device. Defaults to None.
            impact: Ticket Impact. Defaults to None.
            internal_ticket: Internal Ticket. Defaults to None.
            meta: Custom Fields. Defaults to None.
            opportunity_id: Opportunity ID. Defaults to None.
            order_id: Order ID. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            queue: Ticket Department ID. Defaults to None.
            quote_id: Quote ID. Defaults to None.
            service_id: Associate Service. Defaults to None.
            subject: Ticket Subject. Defaults to None.
            ticket_resolution_id: Resolution ID. Defaults to None.
            type: Ticket Type. Defaults to None.
            weight: Ticket Rating. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'support.ticket_update',
            ticket_id=ticket_id,
            **{'assignment': assignment} if assignment else {},
            **{'author': author} if author else {},
            **{'bcc': bcc} if bcc else {},
            **{'cc': cc} if cc else {},
            **{'classification_id': classification_id} if classification_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'contact_id': contact_id} if contact_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'impact': impact} if impact else {},
            **{'internal_ticket': internal_ticket} if internal_ticket else {},
            **{'meta': meta} if meta else {},
            **{'opportunity_id': opportunity_id} if opportunity_id else {},
            **{'order_id': order_id} if order_id else {},
            **{'priority': priority} if priority else {},
            **{'queue': queue} if queue else {},
            **{'quote_id': quote_id} if quote_id else {},
            **{'service_id': service_id} if service_id else {},
            **{'subject': subject} if subject else {},
            **{'ticket_resolution_id': ticket_resolution_id} if ticket_resolution_id else {},
            **{'type': type} if type else {},
            **{'weight': weight} if weight else {},
        )
