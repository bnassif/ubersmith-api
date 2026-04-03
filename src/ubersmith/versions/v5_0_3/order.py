from typing import Dict
from ubersmith.client.section import *

class OrderAPI(Section):
    """
    Auto-generated section for ``order``.

    Contains all ``order.*`` API methods.
    """

    def cancel(
            self,
            hash=None,
            order_id=None,
        ) -> Dict:
        """Cancel an Order

        API Method: order.cancel

        This method is used to cancel a specified order.

        Args:
            hash: Order Hash. Defaults to None.
            order_id: Order ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.cancel',
            **{'hash': hash} if hash else {},
            **{'order_id': order_id} if order_id else {},
        )

    def client_respond(
            self,
            attach=None,
            author=None,
            body=None,
            cc=None,
            contact_id=None,
            hash=None,
            order_id=None,
            subject=None,
        ) -> Dict:
        """Post a Client/Lead Order Response

        API Method: order.client_respond

        This method is used to post a response on the specified order as a client or lead.

        Args:
            attach: Attachments. Defaults to None.
            author: Author Email. Defaults to None.
            body: Response. Defaults to None.
            cc: Cc. Defaults to None.
            contact_id: Contact ID. Defaults to None.
            hash: Order Hash. Defaults to None.
            order_id: Order ID. Defaults to None.
            subject: Subject. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.client_respond',
            **{'attach': attach} if attach else {},
            **{'author': author} if author else {},
            **{'body': body} if body else {},
            **{'cc': cc} if cc else {},
            **{'contact_id': contact_id} if contact_id else {},
            **{'hash': hash} if hash else {},
            **{'order_id': order_id} if order_id else {},
            **{'subject': subject} if subject else {},
        )

    def coupon_add(
            self,
            coupon_code,
            active=None,
            class_id=None,
            description=None,
            discount_value=None,
            dollar=None,
            expire=None,
            max_uses=None,
            opts=None,
            plan_id=None,
            recurring=None,
            setup_discount_value=None,
            setup_dollar=None,
            start=None,
            vip=None,
        ) -> Dict:
        """Add Coupon

        API Method: order.coupon_add

        This method is used to add a new coupon.

        Args:
            coupon_code: Coupon Code,
            active: Active. Defaults to None.
            class_id: Brand ID. Defaults to None.
            description: Description. Defaults to None.
            discount_value: Discount Value. Defaults to None.
            dollar: Dollar. Defaults to None.
            expire: Expire. Defaults to None.
            max_uses: Max Uses. Defaults to None.
            opts: Service Plan Options. Defaults to None.
            plan_id: Plan ID. Defaults to None.
            recurring: Recurring. Defaults to None.
            setup_discount_value: Setup Discount Value. Defaults to None.
            setup_dollar: Setup Dollar. Defaults to None.
            start: Start. Defaults to None.
            vip: VIP. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.coupon_add',
            coupon_code=coupon_code,
            **{'active': active} if active else {},
            **{'class_id': class_id} if class_id else {},
            **{'description': description} if description else {},
            **{'discount_value': discount_value} if discount_value else {},
            **{'dollar': dollar} if dollar else {},
            **{'expire': expire} if expire else {},
            **{'max_uses': max_uses} if max_uses else {},
            **{'opts': opts} if opts else {},
            **{'plan_id': plan_id} if plan_id else {},
            **{'recurring': recurring} if recurring else {},
            **{'setup_discount_value': setup_discount_value} if setup_discount_value else {},
            **{'setup_dollar': setup_dollar} if setup_dollar else {},
            **{'start': start} if start else {},
            **{'vip': vip} if vip else {},
        )

    def coupon_client_add(
            self,
            coupon_id,
            client_id=None,
        ) -> Dict:
        """Add Coupon Client

        API Method: order.coupon_client_add

        This method is used to add client(s) to a coupon.

        Args:
            coupon_id: Coupon ID,
            client_id: Client ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.coupon_client_add',
            coupon_id=coupon_id,
            **{'client_id': client_id} if client_id else {},
        )

    def coupon_client_delete(
            self,
            coupon_id,
            client_id=None,
        ) -> Dict:
        """Delete Coupon Client

        API Method: order.coupon_client_delete

        This method is used to delete client(s) from a coupon.

        Args:
            coupon_id: Coupon ID,
            client_id: Client ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.coupon_client_delete',
            coupon_id=coupon_id,
            **{'client_id': client_id} if client_id else {},
        )

    def coupon_get(
            self,
            brand_id=None,
            coupon_code=None,
            coupon_id=None,
        ) -> Dict:
        """Get Order Coupon Details

        API Method: order.coupon_get

        This method is used to get the details of a specified order coupon.

        Args:
            brand_id: Brand ID. Defaults to None.
            coupon_code: Coupon Code. Defaults to None.
            coupon_id: Coupon ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.coupon_get',
            **{'brand_id': brand_id} if brand_id else {},
            **{'coupon_code': coupon_code} if coupon_code else {},
            **{'coupon_id': coupon_id} if coupon_id else {},
        )

    def coupon_list(
            self,
            active=None,
            class_id=None,
            direction=None,
            expire=None,
            include_clients=None,
            include_options=None,
            limit=None,
            offset=None,
            order_by=None,
            plan_id=None,
            start=None,
        ) -> Dict:
        """Coupon List

        API Method: order.coupon_list

        This method is used to retrieve list of coupons.

        Args:
            active: Active. Defaults to None.
            class_id: Brand ID. Defaults to None.
            direction: Direction. Defaults to None.
            expire: Coupon Expiration Date. Defaults to None.
            include_clients: Include Clients. Defaults to None.
            include_options: Include Options. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            plan_id: Service Plan ID. Defaults to None.
            start: Coupon Start Date. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.coupon_list',
            **{'active': active} if active else {},
            **{'class_id': class_id} if class_id else {},
            **{'direction': direction} if direction else {},
            **{'expire': expire} if expire else {},
            **{'include_clients': include_clients} if include_clients else {},
            **{'include_options': include_options} if include_options else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'plan_id': plan_id} if plan_id else {},
            **{'start': start} if start else {},
        )

    def coupon_update(
            self,
            coupon_id,
            active=None,
            class_id=None,
            coupon_code=None,
            description=None,
            discount_value=None,
            dollar=None,
            expire=None,
            max_uses=None,
            opts=None,
            plan_id=None,
            recurring=None,
            setup_discount_value=None,
            setup_dollar=None,
            start=None,
            vip=None,
        ) -> Dict:
        """Update Coupon Details

        API Method: order.coupon_update

        This method is used to update the details for a coupon.

        Args:
            coupon_id: Coupon ID,
            active: Active. Defaults to None.
            class_id: Brand ID. Defaults to None.
            coupon_code: Coupon Code. Defaults to None.
            description: Description. Defaults to None.
            discount_value: Discount Value. Defaults to None.
            dollar: Dollar. Defaults to None.
            expire: Expire. Defaults to None.
            max_uses: Max Uses. Defaults to None.
            opts: Service Plan Options. Defaults to None.
            plan_id: Plan ID. Defaults to None.
            recurring: Recurring. Defaults to None.
            setup_discount_value: Setup Discount Value. Defaults to None.
            setup_dollar: Setup Dollar. Defaults to None.
            start: Start. Defaults to None.
            vip: VIP. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.coupon_update',
            coupon_id=coupon_id,
            **{'active': active} if active else {},
            **{'class_id': class_id} if class_id else {},
            **{'coupon_code': coupon_code} if coupon_code else {},
            **{'description': description} if description else {},
            **{'discount_value': discount_value} if discount_value else {},
            **{'dollar': dollar} if dollar else {},
            **{'expire': expire} if expire else {},
            **{'max_uses': max_uses} if max_uses else {},
            **{'opts': opts} if opts else {},
            **{'plan_id': plan_id} if plan_id else {},
            **{'recurring': recurring} if recurring else {},
            **{'setup_discount_value': setup_discount_value} if setup_discount_value else {},
            **{'setup_dollar': setup_dollar} if setup_dollar else {},
            **{'start': start} if start else {},
            **{'vip': vip} if vip else {},
        )

    def create(
            self,
            order_queue_id,
            activity=None,
            add_default_pack_upgrades=None,
            client_id=None,
            hash=None,
            info=None,
            listed_company=None,
            order_form_id=None,
            order_status=None,
            owner=None,
            planned_completion=None,
            priority=None,
            progress=None,
            requested_completion=None,
            signature=None,
            total=None,
            ts=None,
        ) -> Dict:
        """Create a New Order

        API Method: order.create

        This method is used to create a new order.

        Args:
            order_queue_id: Order Queue ID,
            activity: Activity Timestamp. Defaults to None.
            add_default_pack_upgrades: Add Default Service Upgrades. Defaults to None.
            client_id: Client ID. Defaults to None.
            hash: Order Hash. Defaults to None.
            info: Order Information. Defaults to None.
            listed_company: Listed Company. Defaults to None.
            order_form_id: Order Form ID. Defaults to None.
            order_status: Step ID. Defaults to None.
            owner: Admin ID. Defaults to None.
            planned_completion: Planned Completion. Defaults to None.
            priority: Order Priority. Defaults to None.
            progress: Progress. Defaults to None.
            requested_completion: Requested Completion. Defaults to None.
            signature: Signature Data. Defaults to None.
            total: Order Total. Defaults to None.
            ts: Timestamp. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.create',
            order_queue_id=order_queue_id,
            **{'activity': activity} if activity else {},
            **{'add_default_pack_upgrades': add_default_pack_upgrades} if add_default_pack_upgrades else {},
            **{'client_id': client_id} if client_id else {},
            **{'hash': hash} if hash else {},
            **{'info': info} if info else {},
            **{'listed_company': listed_company} if listed_company else {},
            **{'order_form_id': order_form_id} if order_form_id else {},
            **{'order_status': order_status} if order_status else {},
            **{'owner': owner} if owner else {},
            **{'planned_completion': planned_completion} if planned_completion else {},
            **{'priority': priority} if priority else {},
            **{'progress': progress} if progress else {},
            **{'requested_completion': requested_completion} if requested_completion else {},
            **{'signature': signature} if signature else {},
            **{'total': total} if total else {},
            **{'ts': ts} if ts else {},
        )

    def get(
            self,
            hash=None,
            order_id=None,
        ) -> Dict:
        """Get Order Details

        API Method: order.get

        This method is used to get the details of a specified order.

        Args:
            hash: Order Hash. Defaults to None.
            order_id: Order ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.get',
            **{'hash': hash} if hash else {},
            **{'order_id': order_id} if order_id else {},
        )

    def list(
            self,
            brand_id=None,
            client_id=None,
            direction=None,
            limit=None,
            max_ts=None,
            min_ts=None,
            offset=None,
            opportunity_id=None,
            order_by=None,
            order_queue_id=None,
            order_step_id=None,
            step_name=None,
            step_status=None,
        ) -> Dict:
        """List Orders

        API Method: order.list

        This method is used to get a list of orders.

        Args:
            brand_id: Brand ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            max_ts: Maximum Timestamp. Defaults to None.
            min_ts: Minimum Timestamp. Defaults to None.
            offset: Offset. Defaults to None.
            opportunity_id: Opportunity ID. Defaults to None.
            order_by: Order By. Defaults to None.
            order_queue_id: Order Queue ID. Defaults to None.
            order_step_id: Order Step ID. Defaults to None.
            step_name: Order Step Name. Defaults to None.
            step_status: Order Step Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.list',
            **{'brand_id': brand_id} if brand_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'max_ts': max_ts} if max_ts else {},
            **{'min_ts': min_ts} if min_ts else {},
            **{'offset': offset} if offset else {},
            **{'opportunity_id': opportunity_id} if opportunity_id else {},
            **{'order_by': order_by} if order_by else {},
            **{'order_queue_id': order_queue_id} if order_queue_id else {},
            **{'order_step_id': order_step_id} if order_step_id else {},
            **{'step_name': step_name} if step_name else {},
            **{'step_status': step_status} if step_status else {},
        )

    def module_get(
            self,
            order_module_name,
        ) -> Dict:
        """Order Module Details

        API Method: order.module_get

        This method is used to retrieve details for a single order module.

        Args:
            order_module_name: Order Module Name,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.module_get',
            order_module_name=order_module_name,
        )

    def module_list(
            self,
        ) -> Dict:
        """Order Modules

        API Method: order.module_list

        This method is used to retrieve a list of available order modules.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.module_list',
        )

    def post_list(
            self,
            order_id,
            direction=None,
            limit=None,
            offset=None,
            private=None,
        ) -> Dict:
        """Get all posts for an Order

        API Method: order.post_list

        This method is used to return all the posts for the specified order.

        Args:
            order_id: Order ID,
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            private: Show only client-viewable posts. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.post_list',
            order_id=order_id,
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'private': private} if private else {},
        )

    def process(
            self,
            order_action_id,
            hash=None,
            order_id=None,
            skip=None,
            undo_skip=None,
        ) -> Dict:
        """Process an Order

        API Method: order.process

        This method is used to process an order.

        Args:
            order_action_id: Order Action ID,
            hash: Order Hash. Defaults to None.
            order_id: Order ID. Defaults to None.
            skip: Skip Action. Defaults to None.
            undo_skip: Undo Skip. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.process',
            order_action_id=order_action_id,
            **{'hash': hash} if hash else {},
            **{'order_id': order_id} if order_id else {},
            **{'skip': skip} if skip else {},
            **{'undo_skip': undo_skip} if undo_skip else {},
        )

    def queue_action_add(
            self,
            module,
            order_step_id,
            automatic=None,
            client_viewable=None,
            config=None,
            i18n=None,
            name=None,
            optional=None,
            prereqs=None,
            priority=None,
        ) -> Dict:
        """Add Order Action

        API Method: order.queue_action_add

        This method is used to add a new order action.

        Args:
            module: Module Name,
            order_step_id: Order Step ID,
            automatic: Automatic. Defaults to None.
            client_viewable: Client Viewable. Defaults to None.
            config: Config. Defaults to None.
            i18n: Internationalization Options. Defaults to None.
            name: Name. Defaults to None.
            optional: Optional. Defaults to None.
            prereqs: Prerequisite Order Actions. Defaults to None.
            priority: Priority. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_action_add',
            module=module,
            order_step_id=order_step_id,
            **{'automatic': automatic} if automatic else {},
            **{'client_viewable': client_viewable} if client_viewable else {},
            **{'config': config} if config else {},
            **{'i18n': i18n} if i18n else {},
            **{'name': name} if name else {},
            **{'optional': optional} if optional else {},
            **{'prereqs': prereqs} if prereqs else {},
            **{'priority': priority} if priority else {},
        )

    def queue_action_delete(
            self,
            order_action_id,
        ) -> Dict:
        """Delete an order action

        API Method: order.queue_action_delete

        This method is used to delete the given order action ID.

        Args:
            order_action_id: Order Action ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_action_delete',
            order_action_id=order_action_id,
        )

    def queue_action_get(
            self,
            order_action_id,
        ) -> Dict:
        """Order Queue Action Details

        API Method: order.queue_action_get

        This method is used to retrieve details for a single order queue action.

        Args:
            order_action_id: Order Action ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_action_get',
            order_action_id=order_action_id,
        )

    def queue_action_list(
            self,
            order_step_id,
        ) -> Dict:
        """Order Queue Actions

        API Method: order.queue_action_list

        This method is used to retrieve the order actions for an order step ID.

        Args:
            order_step_id: Order Step ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_action_list',
            order_step_id=order_step_id,
        )

    def queue_action_update(
            self,
            order_action_id,
            automatic=None,
            client_viewable=None,
            config=None,
            i18n=None,
            module=None,
            name=None,
            optional=None,
            prereqs=None,
            priority=None,
        ) -> Dict:
        """Update Order Action Details

        API Method: order.queue_action_update

        This method is used to update the details for an order action ID.

        Args:
            order_action_id: Order Action ID,
            automatic: Automatic. Defaults to None.
            client_viewable: Client Viewable. Defaults to None.
            config: Config. Defaults to None.
            i18n: Internationalization Options. Defaults to None.
            module: Module Name. Defaults to None.
            name: Name. Defaults to None.
            optional: Optional. Defaults to None.
            prereqs: Prerequisite Order Actions. Defaults to None.
            priority: Priority. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_action_update',
            order_action_id=order_action_id,
            **{'automatic': automatic} if automatic else {},
            **{'client_viewable': client_viewable} if client_viewable else {},
            **{'config': config} if config else {},
            **{'i18n': i18n} if i18n else {},
            **{'module': module} if module else {},
            **{'name': name} if name else {},
            **{'optional': optional} if optional else {},
            **{'prereqs': prereqs} if prereqs else {},
            **{'priority': priority} if priority else {},
        )

    def queue_add(
            self,
            allow_quotes=None,
            brand_id=None,
            i18n=None,
            name=None,
            sendlink_body=None,
            sendlink_from=None,
            sendlink_sub=None,
        ) -> Dict:
        """Add Order Queue

        API Method: order.queue_add

        This method is used to add an order queue.

        Args:
            allow_quotes: Allow Quotes. Defaults to None.
            brand_id: Brand ID. Defaults to None.
            i18n: Internationalization Options. Defaults to None.
            name: Name. Defaults to None.
            sendlink_body: Send Link Body. Defaults to None.
            sendlink_from: Send Link From. Defaults to None.
            sendlink_sub: Send Link Subject. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_add',
            **{'allow_quotes': allow_quotes} if allow_quotes else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'i18n': i18n} if i18n else {},
            **{'name': name} if name else {},
            **{'sendlink_body': sendlink_body} if sendlink_body else {},
            **{'sendlink_from': sendlink_from} if sendlink_from else {},
            **{'sendlink_sub': sendlink_sub} if sendlink_sub else {},
        )

    def queue_get(
            self,
            order_queue_id,
        ) -> Dict:
        """Order Queue Details

        API Method: order.queue_get

        This method is used to retrieve details for a single order queue.

        Args:
            order_queue_id: Order Queue ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_get',
            order_queue_id=order_queue_id,
        )

    def queue_list(
            self,
            brand_id,
        ) -> Dict:
        """List Order Queues

        API Method: order.queue_list

        This method is used to get a list of order queues.

        Args:
            brand_id: Brand ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_list',
            brand_id=brand_id,
        )

    def queue_step_add(
            self,
            order_queue_id,
            i18n=None,
            name=None,
            priority=None,
        ) -> Dict:
        """Add Order Step

        API Method: order.queue_step_add

        This method is used to add an order step to the given order queue ID.

        Args:
            order_queue_id: Order Queue ID,
            i18n: Internationalization Options. Defaults to None.
            name: Name. Defaults to None.
            priority: Priority. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_step_add',
            order_queue_id=order_queue_id,
            **{'i18n': i18n} if i18n else {},
            **{'name': name} if name else {},
            **{'priority': priority} if priority else {},
        )

    def queue_step_delete(
            self,
            order_step_id,
        ) -> Dict:
        """Delete an order step

        API Method: order.queue_step_delete

        This method is used to delete the given order step ID.

        Args:
            order_step_id: Order Step ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_step_delete',
            order_step_id=order_step_id,
        )

    def queue_step_get(
            self,
            order_step_id,
        ) -> Dict:
        """Order Queue Step Details

        API Method: order.queue_step_get

        This method is used to retrieve details for a single order queue step.

        Args:
            order_step_id: Order Step ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_step_get',
            order_step_id=order_step_id,
        )

    def queue_step_list(
            self,
            order_queue_id,
        ) -> Dict:
        """Order Queue Steps

        API Method: order.queue_step_list

        This method is used to retrieve the order steps for an order queue ID.

        Args:
            order_queue_id: Order Queue ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_step_list',
            order_queue_id=order_queue_id,
        )

    def queue_step_update(
            self,
            order_step_id,
            i18n=None,
            name=None,
            priority=None,
        ) -> Dict:
        """Update Order Step Details

        API Method: order.queue_step_update

        This method is used to update the details for an order step ID.

        Args:
            order_step_id: Order Step ID,
            i18n: Internationalization Options. Defaults to None.
            name: Name. Defaults to None.
            priority: Priority. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_step_update',
            order_step_id=order_step_id,
            **{'i18n': i18n} if i18n else {},
            **{'name': name} if name else {},
            **{'priority': priority} if priority else {},
        )

    def queue_update(
            self,
            order_queue_id,
            active=None,
            allow_quotes=None,
            i18n=None,
            name=None,
            sendlink_body=None,
            sendlink_from=None,
            sendlink_sub=None,
        ) -> Dict:
        """Update Order Queue

        API Method: order.queue_update

        This method is used to update an order queue.

        Args:
            order_queue_id: Order Queue ID,
            active: Active. Defaults to None.
            allow_quotes: Allow Quotes. Defaults to None.
            i18n: Internationalization Options. Defaults to None.
            name: Name. Defaults to None.
            sendlink_body: Send Link Body. Defaults to None.
            sendlink_from: Send Link From. Defaults to None.
            sendlink_sub: Send Link Subject. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.queue_update',
            order_queue_id=order_queue_id,
            **{'active': active} if active else {},
            **{'allow_quotes': allow_quotes} if allow_quotes else {},
            **{'i18n': i18n} if i18n else {},
            **{'name': name} if name else {},
            **{'sendlink_body': sendlink_body} if sendlink_body else {},
            **{'sendlink_from': sendlink_from} if sendlink_from else {},
            **{'sendlink_sub': sendlink_sub} if sendlink_sub else {},
        )

    def respond(
            self,
            bcc=None,
            cc=None,
            comment=None,
            followup=None,
            from_address=None,
            hash=None,
            order_id=None,
            recipient=None,
            subject=None,
            user_id=None,
        ) -> Dict:
        """Post an Order Response

        API Method: order.respond

        This method is used to post a response on the specified order.

        Args:
            bcc: Bcc. Defaults to None.
            cc: Cc. Defaults to None.
            comment: Comment. Defaults to None.
            followup: Response. Defaults to None.
            from_address: From. Defaults to None.
            hash: Order Hash. Defaults to None.
            order_id: Order ID. Defaults to None.
            recipient: Recipient. Defaults to None.
            subject: Subject. Defaults to None.
            user_id: User ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.respond',
            **{'bcc': bcc} if bcc else {},
            **{'cc': cc} if cc else {},
            **{'comment': comment} if comment else {},
            **{'followup': followup} if followup else {},
            **{'from_address': from_address} if from_address else {},
            **{'hash': hash} if hash else {},
            **{'order_id': order_id} if order_id else {},
            **{'recipient': recipient} if recipient else {},
            **{'subject': subject} if subject else {},
            **{'user_id': user_id} if user_id else {},
        )

    def submit(
            self,
            hash=None,
            order_id=None,
        ) -> Dict:
        """Submit An Order

        API Method: order.submit

        This method is used to submit the specified order.

        Args:
            hash: Order Hash. Defaults to None.
            order_id: Order ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.submit',
            **{'hash': hash} if hash else {},
            **{'order_id': order_id} if order_id else {},
        )

    def threedsecure2_payment(
            self,
            threedsecure,
            hash=None,
            order_id=None,
        ) -> Dict:
        """Retry an order payment

        API Method: order.threedsecure2_payment

        This method is used to retry an order payment

        Args:
            threedsecure: Provider specific 3D Secure 2 parameters (array),
            hash: Order Hash. Defaults to None.
            order_id: Order ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.threedsecure2_payment',
            threedsecure=threedsecure,
            **{'hash': hash} if hash else {},
            **{'order_id': order_id} if order_id else {},
        )

    def threedsecure2_process(
            self,
            action,
            threedsecure,
            hash=None,
            order_id=None,
        ) -> Dict:
        """Execute a provider specific 3D secure action

        API Method: order.threedsecure2_process

        This method is used to execute a provider specific 3D Secure action.

        Args:
            action: Action,
            threedsecure: Provider specific 3D Secure 2 parameters (array),
            hash: Order Hash. Defaults to None.
            order_id: Order ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.threedsecure2_process',
            action=action,
            threedsecure=threedsecure,
            **{'hash': hash} if hash else {},
            **{'order_id': order_id} if order_id else {},
        )

    def update(
            self,
            client_id=None,
            hash=None,
            info=None,
            listed_company=None,
            order_id=None,
            owner=None,
            planned_completion=None,
            priority=None,
            requested_completion=None,
            signature=None,
            step_id=None,
            step_name=None,
            total=None,
        ) -> Dict:
        """Update an Order

        API Method: order.update

        This method is used to update the details of an existing order.

        Args:
            client_id: Client ID. Defaults to None.
            hash: Order Hash. Defaults to None.
            info: Order Information. Defaults to None.
            listed_company: Listed Company. Defaults to None.
            order_id: Order ID. Defaults to None.
            owner: Admin ID. Defaults to None.
            planned_completion: Planned Completion. Defaults to None.
            priority: Order Priority. Defaults to None.
            requested_completion: Requested Completion. Defaults to None.
            signature: Signature Data. Defaults to None.
            step_id: Order Step ID. Defaults to None.
            step_name: Order Step Name. Defaults to None.
            total: Order Total. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'order.update',
            **{'client_id': client_id} if client_id else {},
            **{'hash': hash} if hash else {},
            **{'info': info} if info else {},
            **{'listed_company': listed_company} if listed_company else {},
            **{'order_id': order_id} if order_id else {},
            **{'owner': owner} if owner else {},
            **{'planned_completion': planned_completion} if planned_completion else {},
            **{'priority': priority} if priority else {},
            **{'requested_completion': requested_completion} if requested_completion else {},
            **{'signature': signature} if signature else {},
            **{'step_id': step_id} if step_id else {},
            **{'step_name': step_name} if step_name else {},
            **{'total': total} if total else {},
        )
