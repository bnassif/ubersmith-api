from typing import Dict
from ubersmith.client.section import *

class SalesAPI(Section):
    """
    Auto-generated section for ``sales``.

    Contains all ``sales.*`` API methods.
    """

    def opportunity_add(
            self,
            opportunity_stage_id,
            opportunity_type_id,
            client_id=None,
            closure_pct=None,
            closure_ts=None,
            contact_id=None,
            description=None,
            last_action=None,
            name=None,
            next_step=None,
            owner=None,
            price_max=None,
            price_min=None,
            status=None,
            user_login=None,
        ) -> Dict:
        """Add an Opportunity

        API Method: sales.opportunity_add

        This method is used to add a new opportunity to the Sales Manager.

        Args:
            opportunity_stage_id: Opportunity Stage,
            opportunity_type_id: Opportunity Type,
            client_id: Client/Lead ID. Defaults to None.
            closure_pct: Closure Percentage. Defaults to None.
            closure_ts: Closure Timestamp. Defaults to None.
            contact_id: Contact ID. Defaults to None.
            description: Description. Defaults to None.
            last_action: Last Action. Defaults to None.
            name: Opportunity Name. Defaults to None.
            next_step: Next Step. Defaults to None.
            owner: Owner ID. Defaults to None.
            price_max: Maximum Price. Defaults to None.
            price_min: Minimum Price. Defaults to None.
            status: Opportunity Status. Defaults to None.
            user_login: Client/Lead Login Name or ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'sales.opportunity_add',
            opportunity_stage_id=opportunity_stage_id,
            opportunity_type_id=opportunity_type_id,
            **{'client_id': client_id} if client_id else {},
            **{'closure_pct': closure_pct} if closure_pct else {},
            **{'closure_ts': closure_ts} if closure_ts else {},
            **{'contact_id': contact_id} if contact_id else {},
            **{'description': description} if description else {},
            **{'last_action': last_action} if last_action else {},
            **{'name': name} if name else {},
            **{'next_step': next_step} if next_step else {},
            **{'owner': owner} if owner else {},
            **{'price_max': price_max} if price_max else {},
            **{'price_min': price_min} if price_min else {},
            **{'status': status} if status else {},
            **{'user_login': user_login} if user_login else {},
        )

    def opportunity_list(
            self,
            opportunity_stage_id,
            opportunity_type_id,
            begin=None,
            brand_id=None,
            client_id=None,
            contact_id=None,
            direction=None,
            end=None,
            limit=None,
            max_value=None,
            min_activity=None,
            min_value=None,
            offset=None,
            opportunity_id=None,
            order_by=None,
            owner=None,
            price_max=None,
            price_min=None,
            status=None,
            user_login=None,
        ) -> Dict:
        """List Opportunities

        API Method: sales.opportunity_list

        This method is used to retrieve a list of opportunities from the Sales Manager.

        Args:
            opportunity_stage_id: Opportunity Stage,
            opportunity_type_id: Opportunity Type,
            begin: Begin Timestamp. Defaults to None.
            brand_id: Brand ID. Defaults to None.
            client_id: Client/Lead ID. Defaults to None.
            contact_id: Contact ID. Defaults to None.
            direction: Direction. Defaults to None.
            end: End Timestamp. Defaults to None.
            limit: Limit. Defaults to None.
            max_value: Maximum Value. Defaults to None.
            min_activity: Minimum Activity Timestamp. Defaults to None.
            min_value: Minimum Value. Defaults to None.
            offset: Offset. Defaults to None.
            opportunity_id: Opportunity ID. Defaults to None.
            order_by: Order By. Defaults to None.
            owner: Owner ID. Defaults to None.
            price_max: Maximum Price. Defaults to None.
            price_min: Minimum Price. Defaults to None.
            status: Opportunity Status. Defaults to None.
            user_login: Client/Lead Login Name or ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'sales.opportunity_list',
            opportunity_stage_id=opportunity_stage_id,
            opportunity_type_id=opportunity_type_id,
            **{'begin': begin} if begin else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'contact_id': contact_id} if contact_id else {},
            **{'direction': direction} if direction else {},
            **{'end': end} if end else {},
            **{'limit': limit} if limit else {},
            **{'max_value': max_value} if max_value else {},
            **{'min_activity': min_activity} if min_activity else {},
            **{'min_value': min_value} if min_value else {},
            **{'offset': offset} if offset else {},
            **{'opportunity_id': opportunity_id} if opportunity_id else {},
            **{'order_by': order_by} if order_by else {},
            **{'owner': owner} if owner else {},
            **{'price_max': price_max} if price_max else {},
            **{'price_min': price_min} if price_min else {},
            **{'status': status} if status else {},
            **{'user_login': user_login} if user_login else {},
        )

    def opportunity_stage_list(
            self,
        ) -> Dict:
        """List Opportunity Stages

        API Method: sales.opportunity_stage_list

        This method is used to retrieve a list of opportunity stages from the Sales Manager.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'sales.opportunity_stage_list',
        )

    def opportunity_status_list(
            self,
        ) -> Dict:
        """List Opportunity Statuses

        API Method: sales.opportunity_status_list

        This method is used to retrieve a list of opportunity statuses from the Sales Manager.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'sales.opportunity_status_list',
        )

    def opportunity_type_list(
            self,
        ) -> Dict:
        """List Opportunity Types

        API Method: sales.opportunity_type_list

        This method is used to retrieve a list of opportunity types from the Sales Manager.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'sales.opportunity_type_list',
        )

    def opportunity_update(
            self,
            opportunity_id,
            opportunity_stage_id,
            opportunity_type_id,
            closure_pct=None,
            closure_ts=None,
            contact_id=None,
            description=None,
            last_action=None,
            name=None,
            next_step=None,
            owner=None,
            price_max=None,
            price_min=None,
            status=None,
        ) -> Dict:
        """Update an Opportunity

        API Method: sales.opportunity_update

        This method is used to update an opportunity in the Sales Manager.

        Args:
            opportunity_id: Opportunity ID,
            opportunity_stage_id: Opportunity Stage,
            opportunity_type_id: Opportunity Type,
            closure_pct: Closure Percentage. Defaults to None.
            closure_ts: Closure Timestamp. Defaults to None.
            contact_id: Contact ID. Defaults to None.
            description: Description. Defaults to None.
            last_action: Last Action. Defaults to None.
            name: Opportunity Name. Defaults to None.
            next_step: Next Step. Defaults to None.
            owner: Owner ID. Defaults to None.
            price_max: Maximum Price. Defaults to None.
            price_min: Minimum Price. Defaults to None.
            status: Opportunity Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'sales.opportunity_update',
            opportunity_id=opportunity_id,
            opportunity_stage_id=opportunity_stage_id,
            opportunity_type_id=opportunity_type_id,
            **{'closure_pct': closure_pct} if closure_pct else {},
            **{'closure_ts': closure_ts} if closure_ts else {},
            **{'contact_id': contact_id} if contact_id else {},
            **{'description': description} if description else {},
            **{'last_action': last_action} if last_action else {},
            **{'name': name} if name else {},
            **{'next_step': next_step} if next_step else {},
            **{'owner': owner} if owner else {},
            **{'price_max': price_max} if price_max else {},
            **{'price_min': price_min} if price_min else {},
            **{'status': status} if status else {},
        )
