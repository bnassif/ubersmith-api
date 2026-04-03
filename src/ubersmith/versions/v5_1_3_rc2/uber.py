from typing import Dict
from ubersmith.client.section import *

class UberAPI(Section):
    """
    Auto-generated section for ``uber``.

    Contains all ``uber.*`` API methods.
    """

    def acl_admin_role_get(
            self,
            role_id,
        ) -> Dict:
        """Get admin role details

        API Method: uber.acl_admin_role_get

        Obtains information about a given Admin Role

        Args:
            role_id: Admin Role ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.acl_admin_role_get',
            role_id=role_id,
        )

    def acl_admin_role_list(
            self,
            acls=None,
        ) -> Dict:
        """List available admin roles

        API Method: uber.acl_admin_role_list

        This method is used to list admin roles that may be set for an admin user

        Args:
            acls: Role ACLs. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.acl_admin_role_list',
            **{'acls': acls} if acls else {},
        )

    def acl_client_role_get(
            self,
            client_role_id,
        ) -> Dict:
        """Get role details

        API Method: uber.acl_client_role_get

        Obtains information about a given Client Role

        Args:
            client_role_id: Client Role ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.acl_client_role_get',
            client_role_id=client_role_id,
        )

    def acl_client_role_list(
            self,
            acls=None,
            client_id=None,
            contact_id=None,
        ) -> Dict:
        """List available client roles

        API Method: uber.acl_client_role_list

        This method is used to list client roles that may be set for a client or contact

        Args:
            acls: Client ACLs. Defaults to None.
            client_id: Client ID. Defaults to None.
            contact_id: Contact ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.acl_client_role_list',
            **{'acls': acls} if acls else {},
            **{'client_id': client_id} if client_id else {},
            **{'contact_id': contact_id} if contact_id else {},
        )

    def acl_resource_add(
            self,
            label,
            parent_resource_name,
            resource_name,
            actions=None,
        ) -> Dict:
        """Add ACL resource

        API Method: uber.acl_resource_add

        This method is used to add an ACL resource

        Args:
            label: Resource Label,
            parent_resource_name: Parent Resource Name,
            resource_name: Resource Name,
            actions: Available Actions. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.acl_resource_add',
            label=label,
            parent_resource_name=parent_resource_name,
            resource_name=resource_name,
            **{'actions': actions} if actions else {},
        )

    def acl_resource_delete(
            self,
            resource_name,
        ) -> Dict:
        """Delete ACL resource

        API Method: uber.acl_resource_delete

        This method is used to delete ACL resources

        Args:
            resource_name: Resource Name,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.acl_resource_delete',
            resource_name=resource_name,
        )

    def acl_resource_list(
            self,
            resource_name=None,
        ) -> Dict:
        """List ACL resources

        API Method: uber.acl_resource_list

        This method is used to list ACL resources

        Args:
            resource_name: Resource Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.acl_resource_list',
            **{'resource_name': resource_name} if resource_name else {},
        )

    def acl_resource_update(
            self,
            resource_name,
            actions=None,
            label=None,
        ) -> Dict:
        """Update ACL resource

        API Method: uber.acl_resource_update

        This method is used to update ACL resources

        Args:
            resource_name: Resource Name,
            actions: Available Actions. Defaults to None.
            label: Resource Label. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.acl_resource_update',
            resource_name=resource_name,
            **{'actions': actions} if actions else {},
            **{'label': label} if label else {},
        )

    def admin_avatar_get(
            self,
            brand=None,
            size=None,
            user_id=None,
        ) -> Dict:
        """Retrieve an Admin Avatar

        API Method: uber.admin_avatar_get

        This method is used to retrieve an admin user avatar.

        Args:
            brand: Brand. Defaults to None.
            size: Size. Defaults to None.
            user_id: User ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_avatar_get',
            **{'brand': brand} if brand else {},
            **{'size': size} if size else {},
            **{'user_id': user_id} if user_id else {},
        )

    def admin_avatar_set(
            self,
            avatar=None,
            brand=None,
            user_id=None,
        ) -> Dict:
        """Set an Admin Avatar

        API Method: uber.admin_avatar_set

        This method is used to set an admin user avatar.

        Args:
            avatar: Attachment. Defaults to None.
            brand: Brand ID. Defaults to None.
            user_id: Client ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_avatar_set',
            **{'avatar': avatar} if avatar else {},
            **{'brand': brand} if brand else {},
            **{'user_id': user_id} if user_id else {},
        )

    def admin_client_relationship_add(
            self,
            client_id,
            people_client_type_id,
            person_id,
        ) -> Dict:
        """Add Admin-Client Relationship

        API Method: uber.admin_client_relationship_add

        This method adds an admin-client relationship such as a dedicated Account Manager or Salesperson.

        Args:
            client_id: Client ID,
            people_client_type_id: Relationship Type ID,
            person_id: Admin ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_client_relationship_add',
            client_id=client_id,
            people_client_type_id=people_client_type_id,
            person_id=person_id,
        )

    def admin_client_relationship_delete(
            self,
            people_client_id,
        ) -> Dict:
        """Remove Admin-Client Relationship

        API Method: uber.admin_client_relationship_delete

        This method removes an existing admin-client relationship.

        Args:
            people_client_id: Relationship ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_client_relationship_delete',
            people_client_id=people_client_id,
        )

    def admin_client_relationship_list(
            self,
            client_id=None,
            pct_status=None,
            people_client_id=None,
            people_client_type_id=None,
            person_id=None,
        ) -> Dict:
        """List Admin-Client Relationships

        API Method: uber.admin_client_relationship_list

        This method lists admin-client relationship filtered by the parameters specified.

        Args:
            client_id: Client ID. Defaults to None.
            pct_status: Relationship Type Status. Defaults to None.
            people_client_id: Relationship ID. Defaults to None.
            people_client_type_id: Relationship Type ID. Defaults to None.
            person_id: Admin ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_client_relationship_list',
            **{'client_id': client_id} if client_id else {},
            **{'pct_status': pct_status} if pct_status else {},
            **{'people_client_id': people_client_id} if people_client_id else {},
            **{'people_client_type_id': people_client_type_id} if people_client_type_id else {},
            **{'person_id': person_id} if person_id else {},
        )

    def admin_client_relationship_type_add(
            self,
            name=None,
            send_notifications=None,
            status=None,
        ) -> Dict:
        """Add Admin-Client Relationship Type

        API Method: uber.admin_client_relationship_type_add

        This method adds a admin-client relationship type to the system.

        Args:
            name: Relationship Type Name. Defaults to None.
            send_notifications: Send Notifications. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_client_relationship_type_add',
            **{'name': name} if name else {},
            **{'send_notifications': send_notifications} if send_notifications else {},
            **{'status': status} if status else {},
        )

    def admin_client_relationship_type_list(
            self,
            name=None,
            people_client_type_id=None,
            send_notifications=None,
            status=None,
        ) -> Dict:
        """List Admin-Client Relationship Types

        API Method: uber.admin_client_relationship_type_list

        This method lists existing admin-client relationship types.

        Args:
            name: Relationship Type Name. Defaults to None.
            people_client_type_id: Relationship Type ID. Defaults to None.
            send_notifications: Send Notifications. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_client_relationship_type_list',
            **{'name': name} if name else {},
            **{'people_client_type_id': people_client_type_id} if people_client_type_id else {},
            **{'send_notifications': send_notifications} if send_notifications else {},
            **{'status': status} if status else {},
        )

    def admin_client_relationship_type_update(
            self,
            people_client_type_id,
            name=None,
            send_notifications=None,
            status=None,
        ) -> Dict:
        """Edit Admin-Client Relationship Type

        API Method: uber.admin_client_relationship_type_update

        This method edits an existing admin-client relationship type.

        Args:
            people_client_type_id: Relationship Type ID,
            name: Relationship Type Name. Defaults to None.
            send_notifications: Send Notifications. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_client_relationship_type_update',
            people_client_type_id=people_client_type_id,
            **{'name': name} if name else {},
            **{'send_notifications': send_notifications} if send_notifications else {},
            **{'status': status} if status else {},
        )

    def admin_client_relationship_update(
            self,
            people_client_id,
            client_id=None,
            people_client_type_id=None,
            person_id=None,
        ) -> Dict:
        """Edit Admin-Client Relationship

        API Method: uber.admin_client_relationship_update

        This method edits an existing admin-client relationship.

        Args:
            people_client_id: Relationship ID,
            client_id: Client ID. Defaults to None.
            people_client_type_id: Relationship Type ID. Defaults to None.
            person_id: Admin ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_client_relationship_update',
            people_client_id=people_client_id,
            **{'client_id': client_id} if client_id else {},
            **{'people_client_type_id': people_client_type_id} if people_client_type_id else {},
            **{'person_id': person_id} if person_id else {},
        )

    def admin_deactivate(
            self,
            userid,
            reassign_person_id=None,
        ) -> Dict:
        """Deactivate an Admin

        API Method: uber.admin_deactivate

        This method is used to deactivate an admin.

        Args:
            userid: Admin ID,
            reassign_person_id: Reassign Person ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_deactivate',
            userid=userid,
            **{'reassign_person_id': reassign_person_id} if reassign_person_id else {},
        )

    def admin_get(
            self,
            userid=None,
            username=None,
        ) -> Dict:
        """User Information

        API Method: uber.admin_get

        This method is used to return a admin user information based on the user ID or username.

        Args:
            userid: User ID. Defaults to None.
            username: User Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_get',
            **{'userid': userid} if userid else {},
            **{'username': username} if username else {},
        )

    def admin_list(
            self,
            active=None,
            direction=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List User Logins

        API Method: uber.admin_list

        This method is used to returns a list of login names defined.

        Args:
            active: User Active. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_list',
            **{'active': active} if active else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def admin_permission_get(
            self,
            action,
            resource_name,
            userid=None,
            username=None,
        ) -> Dict:
        """Get User Permission

        API Method: uber.admin_permission_get

        This method is used to get admin user permission.

        Args:
            action: Action,
            resource_name: Resource Name,
            userid: User ID. Defaults to None.
            username: User Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_permission_get',
            action=action,
            resource_name=resource_name,
            **{'userid': userid} if userid else {},
            **{'username': username} if username else {},
        )

    def admin_permission_list(
            self,
            effective=None,
            format=None,
            resource=None,
            userid=None,
            username=None,
        ) -> Dict:
        """List User Permissions

        API Method: uber.admin_permission_list

        This method is used to return a tree/list of user permissions.

        Args:
            effective: Include Effective Actions. Defaults to None.
            format: Listing format. Defaults to None.
            resource: Resource Name. Defaults to None.
            userid: User ID. Defaults to None.
            username: User Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_permission_list',
            **{'effective': effective} if effective else {},
            **{'format': format} if format else {},
            **{'resource': resource} if resource else {},
            **{'userid': userid} if userid else {},
            **{'username': username} if username else {},
        )

    def admin_permission_set(
            self,
            permissions,
            userid=None,
            username=None,
        ) -> Dict:
        """Set User Permissions

        API Method: uber.admin_permission_set

        This method is used to set admin user permissions.

        Args:
            permissions: Permissions,
            userid: User ID. Defaults to None.
            username: User Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_permission_set',
            permissions=permissions,
            **{'userid': userid} if userid else {},
            **{'username': username} if username else {},
        )

    def admin_resource_list(
            self,
        ) -> Dict:
        """List available admin ACL resources

        API Method: uber.admin_resource_list

        This method is used to list ACL resources that may be set for an admin

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.admin_resource_list',
        )

    def api_export(
            self,
            table,
            gzip=None,
            order_by=None,
        ) -> Dict:
        """Export Data

        API Method: uber.api_export

        This method is used to export data from Ubersmith in CSV format.

        Args:
            table: Table to export,
            gzip: Gzip Flag. Defaults to None.
            order_by: Order By. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.api_export',
            table=table,
            **{'gzip': gzip} if gzip else {},
            **{'order_by': order_by} if order_by else {},
        )

    def appliance_list(
            self,
        ) -> Dict:
        """List Ubersmith Appliances

        API Method: uber.appliance_list

        This method lists Ubersmith Appliances.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.appliance_list',
        )

    def attachment_get(
            self,
            attach_id,
            attach_type,
        ) -> Dict:
        """Get an attachment

        API Method: uber.attachment_get

        This method is used to get a specified attachment.

        Args:
            attach_id: Attachment ID,
            attach_type: Attachment Type,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.attachment_get',
            attach_id=attach_id,
            attach_type=attach_type,
        )

    def attachment_list(
            self,
            attach_type,
            attach_id=None,
            comment_type=None,
            id=None,
        ) -> Dict:
        """List Attachments

        API Method: uber.attachment_list

        This method is used to output a list of attachments

        Args:
            attach_type: Attachment type,
            attach_id: Attachment ID. Defaults to None.
            comment_type: Comment type. Defaults to None.
            id: ID of ticket post, comment, etc.. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.attachment_list',
            attach_type=attach_type,
            **{'attach_id': attach_id} if attach_id else {},
            **{'comment_type': comment_type} if comment_type else {},
            **{'id': id} if id else {},
        )

    def billing_period_list(
            self,
            brand_id,
        ) -> Dict:
        """List Billing Periods

        API Method: uber.billing_period_list

        This method is used to get a list of billing periods.

        Args:
            brand_id: Brand ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.billing_period_list',
            brand_id=brand_id,
        )

    def brand_list(
            self,
        ) -> Dict:
        """List Brands

        API Method: uber.brand_list

        This method is used to returns a list of brands.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.brand_list',
        )

    def check_login(
            self,
            login,
            passwd,
        ) -> Dict:
        """Verify a login and password

        API Method: uber.check_login

        This method is used to check the specified login and password.

        Args:
            login: Login Name,
            passwd: Password,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.check_login',
            login=login,
            passwd=passwd,
        )

    def check_user_twofactor(
            self,
            user_id,
            user_type,
        ) -> Dict:
        """Verify if the user has Two-Factor Enabled

        API Method: uber.check_user_twofactor

        This method is used to verify if a user (Admin, Client or Contact) has a Two-Factor Module enabled

        Args:
            user_id: User ID,
            user_type: User Type,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.check_user_twofactor',
            user_id=user_id,
            user_type=user_type,
        )

    def client_permission_list(
            self,
        ) -> Dict:
        """List available permissions

        API Method: uber.client_permission_list

        This method is used to list permissions that may be set for a client or contact

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.client_permission_list',
        )

    def client_resource_list(
            self,
        ) -> Dict:
        """List available ACL resources

        API Method: uber.client_resource_list

        This method is used to list ACL resources that may be set for a client or contact

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.client_resource_list',
        )

    def client_role_get(
            self,
            client_role_id,
        ) -> Dict:
        """Get role details

        API Method: uber.client_role_get

        [Deprecated: Use uber.acl_client_role_get] Obtains information about a given Client Role

        Args:
            client_role_id: Client Role ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.client_role_get',
            client_role_id=client_role_id,
        )

    def client_role_list(
            self,
            acls=None,
            client_id=None,
            contact_id=None,
        ) -> Dict:
        """List available client roles

        API Method: uber.client_role_list

        [Deprecated: Use uber.acl_client_role_list] This method is used to list client roles that may be set for a client or contact

        Args:
            acls: Client ACLs. Defaults to None.
            client_id: Client ID. Defaults to None.
            contact_id: Contact ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.client_role_list',
            **{'acls': acls} if acls else {},
            **{'client_id': client_id} if client_id else {},
            **{'contact_id': contact_id} if contact_id else {},
        )

    def client_tag_add(
            self,
            tag,
            color=None,
            important=None,
        ) -> Dict:
        """Add a client tag

        API Method: uber.client_tag_add

        This method is used to create a client tag

        Args:
            tag: Tag Name,
            color: Color. Defaults to None.
            important: Important?. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.client_tag_add',
            tag=tag,
            **{'color': color} if color else {},
            **{'important': important} if important else {},
        )

    def client_tag_delete(
            self,
            tag_id,
        ) -> Dict:
        """Delete a client tag

        API Method: uber.client_tag_delete

        This method is used to delete a client tag -- warning: this removes the tag permanently from all clients

        Args:
            tag_id: Tag ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.client_tag_delete',
            tag_id=tag_id,
        )

    def client_tag_list(
            self,
            client_id=None,
            direction=None,
            has_clients=None,
            important=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List client tags

        API Method: uber.client_tag_list

        This method is used to list client tags

        Args:
            client_id: Client ID. Defaults to None.
            direction: Direction. Defaults to None.
            has_clients: Has Clients. Defaults to None.
            important: Important?. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.client_tag_list',
            **{'client_id': client_id} if client_id else {},
            **{'direction': direction} if direction else {},
            **{'has_clients': has_clients} if has_clients else {},
            **{'important': important} if important else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def client_tag_update(
            self,
            tag_id,
            color=None,
            important=None,
            tag=None,
        ) -> Dict:
        """Update a client tag

        API Method: uber.client_tag_update

        This method is used to update an existing client tag

        Args:
            tag_id: Tag ID,
            color: Color. Defaults to None.
            important: Important?. Defaults to None.
            tag: Tag Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.client_tag_update',
            tag_id=tag_id,
            **{'color': color} if color else {},
            **{'important': important} if important else {},
            **{'tag': tag} if tag else {},
        )

    def client_welcome_stats(
            self,
            client_id,
        ) -> Dict:
        """Display Client Statistics

        API Method: uber.client_welcome_stats

        This method is used to output the same statistics that are shown at the top of the client interface.

        Args:
            client_id: Client ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.client_welcome_stats',
            client_id=client_id,
        )

    def comment_add(
            self,
            comment,
            ref_id,
            type,
            user_id=None,
        ) -> Dict:
        """Add Comment

        API Method: uber.comment_add

        This method is used to add client, service, device, credit or opportunity comments.

        Args:
            comment: Comment,
            ref_id: Related ID,
            type: Comment Type,
            user_id: User ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.comment_add',
            comment=comment,
            ref_id=ref_id,
            type=type,
            **{'user_id': user_id} if user_id else {},
        )

    def comment_delete(
            self,
            comment_id,
            type,
        ) -> Dict:
        """Delete Comment

        API Method: uber.comment_delete

        This method is used to delete client, service, device, credit or opportunity comments.

        Args:
            comment_id: Comment ID,
            type: Comment Type,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.comment_delete',
            comment_id=comment_id,
            type=type,
        )

    def comment_get(
            self,
            comment_id,
            type,
        ) -> Dict:
        """Get Comments

        API Method: uber.comment_get

        This method is used to get client, service, device, credit or opportunity comments.

        Args:
            comment_id: Comment ID,
            type: Comment Type,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.comment_get',
            comment_id=comment_id,
            type=type,
        )

    def comment_list(
            self,
            ref_id,
            type,
            client_viewable=None,
            direction=None,
            filter_text=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List Comments

        API Method: uber.comment_list

        This method is used to list client, service, device, credit or opportunity comments.

        Args:
            ref_id: Related ID,
            type: Comment Type,
            client_viewable: Client Viewable. Defaults to None.
            direction: Direction. Defaults to None.
            filter_text: Filter Text. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.comment_list',
            ref_id=ref_id,
            type=type,
            **{'client_viewable': client_viewable} if client_viewable else {},
            **{'direction': direction} if direction else {},
            **{'filter_text': filter_text} if filter_text else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def comment_update(
            self,
            comment,
            comment_id,
            type,
            user_id=None,
        ) -> Dict:
        """Update Comment

        API Method: uber.comment_update

        This method is used to update client, service, device, credit or opportunity comments.

        Args:
            comment: Comment,
            comment_id: Comment ID,
            type: Comment Type,
            user_id: User ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.comment_update',
            comment=comment,
            comment_id=comment_id,
            type=type,
            **{'user_id': user_id} if user_id else {},
        )

    def config_list(
            self,
            brand_id,
            items=None,
        ) -> Dict:
        """List Configuration Values

        API Method: uber.config_list

        This method is used to list configuration values.

        Args:
            brand_id: Brand ID,
            items: Items. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.config_list',
            brand_id=brand_id,
            **{'items': items} if items else {},
        )

    def config_update(
            self,
            brand_id,
            items,
        ) -> Dict:
        """Update Configuration Value

        API Method: uber.config_update

        This method is used to update a configuration value.

        Args:
            brand_id: Brand ID,
            items: Items,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.config_update',
            brand_id=brand_id,
            items=items,
        )

    def contract_template_add(
            self,
            brand_id,
            name,
            template,
        ) -> Dict:
        """Add a New Contract Template

        API Method: uber.contract_template_add

        This method is used to add a new contract template to a brand.

        Args:
            brand_id: Brand ID,
            name: Name,
            template: Template,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.contract_template_add',
            brand_id=brand_id,
            name=name,
            template=template,
        )

    def contract_template_delete(
            self,
            id,
        ) -> Dict:
        """Delete Contract Template

        API Method: uber.contract_template_delete

        This method is used to delete a contract template.

        Args:
            id: Template ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.contract_template_delete',
            id=id,
        )

    def contract_template_get(
            self,
            id,
        ) -> Dict:
        """Get Contract Template

        API Method: uber.contract_template_get

        This method is used to return a contract template data.

        Args:
            id: Template ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.contract_template_get',
            id=id,
        )

    def contract_template_list(
            self,
            brand_id,
            created_after=None,
            created_before=None,
            direction=None,
            id=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List Contract Templates

        API Method: uber.contract_template_list

        This method is used to list contract templates.

        Args:
            brand_id: Brand ID,
            created_after: Created After. Defaults to None.
            created_before: Created Before. Defaults to None.
            direction: Direction. Defaults to None.
            id: Template IDs. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.contract_template_list',
            brand_id=brand_id,
            **{'created_after': created_after} if created_after else {},
            **{'created_before': created_before} if created_before else {},
            **{'direction': direction} if direction else {},
            **{'id': id} if id else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def contract_template_update(
            self,
            id,
            name=None,
            template=None,
        ) -> Dict:
        """Update a Contract Template

        API Method: uber.contract_template_update

        This method is used to update a contract template.

        Args:
            id: Template ID,
            name: Name. Defaults to None.
            template: Template. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.contract_template_update',
            id=id,
            **{'name': name} if name else {},
            **{'template': template} if template else {},
        )

    def contract_term_add(
            self,
            name,
            term,
            status=None,
        ) -> Dict:
        """Add a Contract Term

        API Method: uber.contract_term_add

        This method is used to add a contract term

        Args:
            name: Contract Term Name,
            term: Term Length,
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.contract_term_add',
            name=name,
            term=term,
            **{'status': status} if status else {},
        )

    def contract_term_get(
            self,
            contract_term_id,
        ) -> Dict:
        """Get Contract Term Details

        API Method: uber.contract_term_get

        This method is used to get the details of a specified contract term

        Args:
            contract_term_id: Contract Term ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.contract_term_get',
            contract_term_id=contract_term_id,
        )

    def contract_term_list(
            self,
            status=None,
        ) -> Dict:
        """List Contract Terms

        API Method: uber.contract_term_list

        This method is used to list contract terms

        Args:
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.contract_term_list',
            **{'status': status} if status else {},
        )

    def contract_term_update(
            self,
            contract_term_id,
            name=None,
            status=None,
            term=None,
        ) -> Dict:
        """Update a Contract Term

        API Method: uber.contract_term_update

        This method is used to update a contract term

        Args:
            contract_term_id: Contract Term ID,
            name: Contract Term Name. Defaults to None.
            status: Status. Defaults to None.
            term: Term Length. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.contract_term_update',
            contract_term_id=contract_term_id,
            **{'name': name} if name else {},
            **{'status': status} if status else {},
            **{'term': term} if term else {},
        )

    def custom_payment_type_add(
            self,
            brand_id,
            id,
            label,
            active=None,
            description=None,
            i18n=None,
        ) -> Dict:
        """Add Custom Payment Type

        API Method: uber.custom_payment_type_add

        This method is used to create a new custom payment type

        Args:
            brand_id: Brand ID,
            id: ID,
            label: Label,
            active: Status. Defaults to None.
            description: Description. Defaults to None.
            i18n: Internationalization. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.custom_payment_type_add',
            brand_id=brand_id,
            id=id,
            label=label,
            **{'active': active} if active else {},
            **{'description': description} if description else {},
            **{'i18n': i18n} if i18n else {},
        )

    def custom_payment_type_list(
            self,
            brand_id,
            is_active=None,
        ) -> Dict:
        """Get Custom Payment Types list

        API Method: uber.custom_payment_type_list

        This method is used to get a list of custom payment types

        Args:
            brand_id: Brand ID,
            is_active: Is Active. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.custom_payment_type_list',
            brand_id=brand_id,
            **{'is_active': is_active} if is_active else {},
        )

    def custom_payment_type_update(
            self,
            brand_id,
            id,
            active=None,
            description=None,
            label=None,
        ) -> Dict:
        """Update Custom Payment Type

        API Method: uber.custom_payment_type_update

        This method is used to update a custom payment type

        Args:
            brand_id: Brand ID,
            id: ID,
            active: Status. Defaults to None.
            description: Description. Defaults to None.
            label: Label. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.custom_payment_type_update',
            brand_id=brand_id,
            id=id,
            **{'active': active} if active else {},
            **{'description': description} if description else {},
            **{'label': label} if label else {},
        )

    def documentation(
            self,
        ) -> Dict:
        """Download API Documentation

        API Method: uber.documentation

        This method is used to get a document with details of all available API methods.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.documentation',
        )

    def event_alert_list(
            self,
            begin=None,
            direction=None,
            end=None,
            limit=None,
            offset=None,
            order_by=None,
            read=None,
        ) -> Dict:
        """List Event Alerts

        API Method: uber.event_alert_list

        This method is used to list the current user's event alerts.

        Args:
            begin: Begin Time. Defaults to None.
            direction: Direction. Defaults to None.
            end: End Time. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            read: Read. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.event_alert_list',
            **{'begin': begin} if begin else {},
            **{'direction': direction} if direction else {},
            **{'end': end} if end else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'read': read} if read else {},
        )

    def event_alert_mark_read(
            self,
        ) -> Dict:
        """Mark Event Alerts Read

        API Method: uber.event_alert_mark_read

        This method is used to mark event alerts as read.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.event_alert_mark_read',
        )

    def event_list(
            self,
            begin=None,
            direction=None,
            end=None,
            ledger=None,
            limit=None,
            offset=None,
            order_by=None,
            searchfor=None,
            user_login=None,
        ) -> Dict:
        """Access the Event Log

        API Method: uber.event_list

        This method is used to retrieve data from the event log.

        Args:
            begin: Begin Time. Defaults to None.
            direction: Direction. Defaults to None.
            end: End Time. Defaults to None.
            ledger: Ledger events only. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            searchfor: Search term. Defaults to None.
            user_login: Client Login. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.event_list',
            **{'begin': begin} if begin else {},
            **{'direction': direction} if direction else {},
            **{'end': end} if end else {},
            **{'ledger': ledger} if ledger else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'searchfor': searchfor} if searchfor else {},
            **{'user_login': user_login} if user_login else {},
        )

    def event_trigger_action_get(
            self,
            brand_id=None,
            ea_id=None,
            ea_name=None,
        ) -> Dict:
        """Get Event Trigger Action Details

        API Method: uber.event_trigger_action_get

        This method is used to get an event trigger action's details.

        Args:
            brand_id: Brand ID. Defaults to None.
            ea_id: Event Trigger Action ID. Defaults to None.
            ea_name: Event Trigger Action Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.event_trigger_action_get',
            **{'brand_id': brand_id} if brand_id else {},
            **{'ea_id': ea_id} if ea_id else {},
            **{'ea_name': ea_name} if ea_name else {},
        )

    def event_trigger_action_list(
            self,
            brand_id=None,
        ) -> Dict:
        """List Event Trigger Actions

        API Method: uber.event_trigger_action_list

        This method is used to list event trigger actions.

        Args:
            brand_id: Brand ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.event_trigger_action_list',
            **{'brand_id': brand_id} if brand_id else {},
        )

    def event_trigger_script_add(
            self,
            es_label,
            es_url,
            args=None,
            brand_id=None,
            ea_id=None,
            ea_name=None,
            es_no_response=None,
            es_rs_check=None,
            matches=None,
        ) -> Dict:
        """Add a New Event Trigger Script

        API Method: uber.event_trigger_script_add

        This method is used to add a new event trigger script.

        Args:
            es_label: Label,
            es_url: URL,
            args: Variables. Defaults to None.
            brand_id: Brand ID. Defaults to None.
            ea_id: Event Trigger Action ID. Defaults to None.
            ea_name: Event Trigger Action Name. Defaults to None.
            es_no_response: Script Timeout Action. Defaults to None.
            es_rs_check: Response Action. Defaults to None.
            matches: Response Matches. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.event_trigger_script_add',
            es_label=es_label,
            es_url=es_url,
            **{'args': args} if args else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'ea_id': ea_id} if ea_id else {},
            **{'ea_name': ea_name} if ea_name else {},
            **{'es_no_response': es_no_response} if es_no_response else {},
            **{'es_rs_check': es_rs_check} if es_rs_check else {},
            **{'matches': matches} if matches else {},
        )

    def event_trigger_script_delete(
            self,
            es_id,
        ) -> Dict:
        """Delete an Event Trigger Script

        API Method: uber.event_trigger_script_delete

        This method is used to delete an event trigger script.

        Args:
            es_id: Event Trigger Script ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.event_trigger_script_delete',
            es_id=es_id,
        )

    def event_trigger_script_get(
            self,
            es_id,
        ) -> Dict:
        """Get Event Trigger Script Details

        API Method: uber.event_trigger_script_get

        This method is used to get an event trigger script's details.

        Args:
            es_id: Event Trigger Script ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.event_trigger_script_get',
            es_id=es_id,
        )

    def event_trigger_script_list(
            self,
            brand_id=None,
            ea_id=None,
            ea_name=None,
        ) -> Dict:
        """List Event Trigger Scripts

        API Method: uber.event_trigger_script_list

        This method is used to list event trigger scripts.

        Args:
            brand_id: Brand ID. Defaults to None.
            ea_id: Event Trigger Action ID. Defaults to None.
            ea_name: Event Trigger Action Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.event_trigger_script_list',
            **{'brand_id': brand_id} if brand_id else {},
            **{'ea_id': ea_id} if ea_id else {},
            **{'ea_name': ea_name} if ea_name else {},
        )

    def event_trigger_script_update(
            self,
            es_id,
            args=None,
            brand_id=None,
            es_label=None,
            es_no_response=None,
            es_rs_check=None,
            es_url=None,
            matches=None,
        ) -> Dict:
        """Update an Event Trigger Script

        API Method: uber.event_trigger_script_update

        This method is used to update an event trigger script.

        Args:
            es_id: Event Trigger Script ID,
            args: Variables. Defaults to None.
            brand_id: Brand ID. Defaults to None.
            es_label: Label. Defaults to None.
            es_no_response: Script Timeout Action. Defaults to None.
            es_rs_check: Response Action. Defaults to None.
            es_url: URL. Defaults to None.
            matches: Response Matches. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.event_trigger_script_update',
            es_id=es_id,
            **{'args': args} if args else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'es_label': es_label} if es_label else {},
            **{'es_no_response': es_no_response} if es_no_response else {},
            **{'es_rs_check': es_rs_check} if es_rs_check else {},
            **{'es_url': es_url} if es_url else {},
            **{'matches': matches} if matches else {},
        )

    def file_add(
            self,
            client_id=None,
            contents=None,
            name=None,
            public=None,
            type=None,
        ) -> Dict:
        """Add a file

        API Method: uber.file_add

        This method is used to add a file.

        Args:
            client_id: Client ID. Defaults to None.
            contents: base64 encoded data. Defaults to None.
            name:  Defaults to None.
            public:  Defaults to None.
            type:  Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.file_add',
            **{'client_id': client_id} if client_id else {},
            **{'contents': contents} if contents else {},
            **{'name': name} if name else {},
            **{'public': public} if public else {},
            **{'type': type} if type else {},
        )

    def file_delete(
            self,
            hash=None,
            id=None,
        ) -> Dict:
        """Delete a file

        API Method: uber.file_delete

        This method is used to delete a file.

        Args:
            hash: File Hash. Defaults to None.
            id: File ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.file_delete',
            **{'hash': hash} if hash else {},
            **{'id': id} if id else {},
        )

    def file_get(
            self,
            hash=None,
            id=None,
        ) -> Dict:
        """Get a File

        API Method: uber.file_get

        This method is used to return a single file.

        Args:
            hash: File Hash. Defaults to None.
            id: File ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.file_get',
            **{'hash': hash} if hash else {},
            **{'id': id} if id else {},
        )

    def file_list(
            self,
            client_id=None,
            direction=None,
            hash=None,
            id=None,
            limit=None,
            name=None,
            offset=None,
            order_by=None,
            public=None,
            type=None,
        ) -> Dict:
        """Get a List of Files

        API Method: uber.file_list

        This method is used to return a list of files.

        Args:
            client_id: Client ID. Defaults to None.
            direction: Direction. Defaults to None.
            hash:  Defaults to None.
            id: File ID. Defaults to None.
            limit: Limit. Defaults to None.
            name:  Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            public:  Defaults to None.
            type:  Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.file_list',
            **{'client_id': client_id} if client_id else {},
            **{'direction': direction} if direction else {},
            **{'hash': hash} if hash else {},
            **{'id': id} if id else {},
            **{'limit': limit} if limit else {},
            **{'name': name} if name else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'public': public} if public else {},
            **{'type': type} if type else {},
        )

    def file_update(
            self,
            client_id=None,
            contents=None,
            hash=None,
            id=None,
            name=None,
            public=None,
            type=None,
        ) -> Dict:
        """Update a file

        API Method: uber.file_update

        This method is used to update a file.

        Args:
            client_id: Client ID. Defaults to None.
            contents: base64 encoded data. Defaults to None.
            hash:  Defaults to None.
            id: File ID. Defaults to None.
            name:  Defaults to None.
            public:  Defaults to None.
            type:  Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.file_update',
            **{'client_id': client_id} if client_id else {},
            **{'contents': contents} if contents else {},
            **{'hash': hash} if hash else {},
            **{'id': id} if id else {},
            **{'name': name} if name else {},
            **{'public': public} if public else {},
            **{'type': type} if type else {},
        )

    def forgot_pass(
            self,
            email=None,
            user_login=None,
        ) -> Dict:
        """Send a Password Reset

        API Method: uber.forgot_pass

        Sends a reset password link to the email address on file.

        Args:
            email: Email Address. Defaults to None.
            user_login: Client Login. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.forgot_pass',
            **{'email': email} if email else {},
            **{'user_login': user_login} if user_login else {},
        )

    def language_add(
            self,
            locale,
            date_format=None,
            default=None,
            description=None,
            name=None,
            name_convention=None,
            status=None,
        ) -> Dict:
        """Add a New Language

        API Method: uber.language_add

        This method is used to add a new language to Ubersmith.

        Args:
            locale: Locale,
            date_format: Date Format. Defaults to None.
            default: Default. Defaults to None.
            description: Description. Defaults to None.
            name: Name. Defaults to None.
            name_convention: Name Convention. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.language_add',
            locale=locale,
            **{'date_format': date_format} if date_format else {},
            **{'default': default} if default else {},
            **{'description': description} if description else {},
            **{'name': name} if name else {},
            **{'name_convention': name_convention} if name_convention else {},
            **{'status': status} if status else {},
        )

    def language_list(
            self,
            available=None,
            default=None,
            installed=None,
            lang_id=None,
            locale=None,
            name=None,
            status=None,
        ) -> Dict:
        """Language List

        API Method: uber.language_list

        This method is used to list the languages that Ubersmith is aware of.

        Args:
            available: Available. Defaults to None.
            default: Default. Defaults to None.
            installed: Installed. Defaults to None.
            lang_id: Language Id. Defaults to None.
            locale: Locale. Defaults to None.
            name: Name. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.language_list',
            **{'available': available} if available else {},
            **{'default': default} if default else {},
            **{'installed': installed} if installed else {},
            **{'lang_id': lang_id} if lang_id else {},
            **{'locale': locale} if locale else {},
            **{'name': name} if name else {},
            **{'status': status} if status else {},
        )

    def language_update(
            self,
            date_format=None,
            default=None,
            description=None,
            lang_id=None,
            locale=None,
            name=None,
            name_convention=None,
            status=None,
        ) -> Dict:
        """Update Language

        API Method: uber.language_update

        This method is used to update an existing language in Ubersmith.

        Args:
            date_format: Date Format. Defaults to None.
            default: Default. Defaults to None.
            description: Description. Defaults to None.
            lang_id: Language ID. Defaults to None.
            locale: Locale. Defaults to None.
            name: Name. Defaults to None.
            name_convention: Name Convention. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.language_update',
            **{'date_format': date_format} if date_format else {},
            **{'default': default} if default else {},
            **{'description': description} if description else {},
            **{'lang_id': lang_id} if lang_id else {},
            **{'locale': locale} if locale else {},
            **{'name': name} if name else {},
            **{'name_convention': name_convention} if name_convention else {},
            **{'status': status} if status else {},
        )

    def late_fee_schedule_list(
            self,
            active=None,
            amount=None,
            class_id=None,
            delay=None,
            direction=None,
            limit=None,
            offset=None,
            order_by=None,
            recur_amount=None,
            recur_interval=None,
            recur_method=None,
        ) -> Dict:
        """List Late Fee Schedules

        API Method: uber.late_fee_schedule_list

        This method is used to list late fee schedules.

        Args:
            active: Active. Defaults to None.
            amount: Amount. Defaults to None.
            class_id: Brand ID. Defaults to None.
            delay: Days Overdue. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            recur_amount: Recur Amount. Defaults to None.
            recur_interval: Recur Interval Days. Defaults to None.
            recur_method: Recur Method. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.late_fee_schedule_list',
            **{'active': active} if active else {},
            **{'amount': amount} if amount else {},
            **{'class_id': class_id} if class_id else {},
            **{'delay': delay} if delay else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'recur_amount': recur_amount} if recur_amount else {},
            **{'recur_interval': recur_interval} if recur_interval else {},
            **{'recur_method': recur_method} if recur_method else {},
        )

    def login_list(
            self,
            brand_id=None,
        ) -> Dict:
        """List User Logins

        API Method: uber.login_list

        This method is used to returns a list of login names defined.

        Args:
            brand_id: Brand ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.login_list',
            **{'brand_id': brand_id} if brand_id else {},
        )

    def mail_get(
            self,
            mail_id,
        ) -> Dict:
        """Get an Email From the Log

        API Method: uber.mail_get

        This method is used to retrieve data for a specific stored email from the mail log.

        Args:
            mail_id: Mail ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.mail_get',
            mail_id=mail_id,
        )

    def mail_list(
            self,
            all=None,
            begin=None,
            direction=None,
            end=None,
            limit=None,
            offset=None,
            order_by=None,
            searchfor=None,
            searchin=None,
            user_login=None,
        ) -> Dict:
        """Access the Mail Log

        API Method: uber.mail_list

        This method is used to retrieve data from the mail log.

        Args:
            all: Include Message Header and Body. Defaults to None.
            begin: Begin Time. Defaults to None.
            direction: Direction. Defaults to None.
            end: End Time. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            searchfor: Search Term. Defaults to None.
            searchin: Field that should be used by the 'searchfor' variable.. Defaults to None.
            user_login: Client's login name or id number. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.mail_list',
            **{'all': all} if all else {},
            **{'begin': begin} if begin else {},
            **{'direction': direction} if direction else {},
            **{'end': end} if end else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'searchfor': searchfor} if searchfor else {},
            **{'searchin': searchin} if searchin else {},
            **{'user_login': user_login} if user_login else {},
        )

    def message_list(
            self,
            brand_id,
            direction=None,
            order_by=None,
            public=None,
        ) -> Dict:
        """List Message Board Messages

        API Method: uber.message_list

        This method is used to retrieve the messages from Ubersmith's internal message board.

        Args:
            brand_id: Brand ID,
            direction: Direction. Defaults to None.
            order_by: Order By. Defaults to None.
            public: Public-only Flag. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.message_list',
            brand_id=brand_id,
            **{'direction': direction} if direction else {},
            **{'order_by': order_by} if order_by else {},
            **{'public': public} if public else {},
        )

    def metadata_bulk_get(
            self,
            meta_type,
            variable,
            brand_id=None,
        ) -> Dict:
        """Bulk Get Custom Field Values

        API Method: uber.metadata_bulk_get

        This method is used to bulk retrieve the value of a single custom field for every client, service, contact, ticket or device.

        Args:
            meta_type: Custom Field Object Type,
            variable: Custom Field Variable Name,
            brand_id: Brand ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.metadata_bulk_get',
            meta_type=meta_type,
            variable=variable,
            **{'brand_id': brand_id} if brand_id else {},
        )

    def metadata_field_add(
            self,
            label,
            meta_type,
            type,
            variable,
            class_id=None,
            client_access=None,
            default_value=None,
            editable=None,
            i18n=None,
            metagroup_id=None,
            regular_expression_help=None,
            regular_expression_match=None,
            required=None,
            show_in_list=None,
            unique=None,
        ) -> Dict:
        """Add Custom Field

        API Method: uber.metadata_field_add

        This method is used to add a new custom field.

        Args:
            label: Label,
            meta_type: Custom Field Config Type,
            type: Type,
            variable: Variable Name,
            class_id: Brand ID. Defaults to None.
            client_access: Client Access Level. Defaults to None.
            default_value: Default value. Defaults to None.
            editable: Editable Type. Defaults to None.
            i18n: Internationalization Options. Defaults to None.
            metagroup_id: Custom Field Group ID. Defaults to None.
            regular_expression_help: Regular Expression Help Text. Defaults to None.
            regular_expression_match: Regular Expression Match. Defaults to None.
            required: Required. Defaults to None.
            show_in_list: Show in Lists. Defaults to None.
            unique: Unique. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.metadata_field_add',
            label=label,
            meta_type=meta_type,
            type=type,
            variable=variable,
            **{'class_id': class_id} if class_id else {},
            **{'client_access': client_access} if client_access else {},
            **{'default_value': default_value} if default_value else {},
            **{'editable': editable} if editable else {},
            **{'i18n': i18n} if i18n else {},
            **{'metagroup_id': metagroup_id} if metagroup_id else {},
            **{'regular_expression_help': regular_expression_help} if regular_expression_help else {},
            **{'regular_expression_match': regular_expression_match} if regular_expression_match else {},
            **{'required': required} if required else {},
            **{'show_in_list': show_in_list} if show_in_list else {},
            **{'unique': unique} if unique else {},
        )

    def metadata_field_delete(
            self,
            metaconf_id,
        ) -> Dict:
        """Delete Custom Field

        API Method: uber.metadata_field_delete

        This method is used to delete an existing custom field.

        Args:
            metaconf_id: Custom Field Config ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.metadata_field_delete',
            metaconf_id=metaconf_id,
        )

    def metadata_field_list(
            self,
            class_id=None,
            meta_type=None,
            metaconf_id=None,
            variable=None,
        ) -> Dict:
        """Get Custom Field Definitions

        API Method: uber.metadata_field_list

        This method is used to retrieve a list of matching custom fields.

        Args:
            class_id: Brand ID. Defaults to None.
            meta_type: Custom Field Type. Defaults to None.
            metaconf_id: Custom Field Config ID. Defaults to None.
            variable: Custom Field Variable Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.metadata_field_list',
            **{'class_id': class_id} if class_id else {},
            **{'meta_type': meta_type} if meta_type else {},
            **{'metaconf_id': metaconf_id} if metaconf_id else {},
            **{'variable': variable} if variable else {},
        )

    def metadata_field_update(
            self,
            metaconf_id,
            client_access=None,
            default_value=None,
            editable=None,
            i18n=None,
            label=None,
            metagroup_id=None,
            regular_expression_help=None,
            regular_expression_match=None,
            required=None,
            show_in_list=None,
            type=None,
            unique=None,
            variable=None,
        ) -> Dict:
        """Update Custom Field

        API Method: uber.metadata_field_update

        This method is used to update an existing custom field.

        Args:
            metaconf_id: Custom Field Config ID,
            client_access: Client Access Level. Defaults to None.
            default_value: Default value. Defaults to None.
            editable: Editable Type. Defaults to None.
            i18n: Internationalization Options. Defaults to None.
            label: Label. Defaults to None.
            metagroup_id: Custom Field Group ID. Defaults to None.
            regular_expression_help: Regular Expression Help Text. Defaults to None.
            regular_expression_match: Regular Expression Match. Defaults to None.
            required: Required. Defaults to None.
            show_in_list: Show in Lists. Defaults to None.
            type: Type. Defaults to None.
            unique: Unique. Defaults to None.
            variable: Variable Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.metadata_field_update',
            metaconf_id=metaconf_id,
            **{'client_access': client_access} if client_access else {},
            **{'default_value': default_value} if default_value else {},
            **{'editable': editable} if editable else {},
            **{'i18n': i18n} if i18n else {},
            **{'label': label} if label else {},
            **{'metagroup_id': metagroup_id} if metagroup_id else {},
            **{'regular_expression_help': regular_expression_help} if regular_expression_help else {},
            **{'regular_expression_match': regular_expression_match} if regular_expression_match else {},
            **{'required': required} if required else {},
            **{'show_in_list': show_in_list} if show_in_list else {},
            **{'type': type} if type else {},
            **{'unique': unique} if unique else {},
            **{'variable': variable} if variable else {},
        )

    def metadata_field_update_applicable(
            self,
            metaconf_id,
            metadata_applicable,
        ) -> Dict:
        """Update Custom Field Applicable

        API Method: uber.metadata_field_update_applicable

        This method is used to update custom field applicable values.

        Args:
            metaconf_id: Custom Field Config ID,
            metadata_applicable: Applicable Custom Fields,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.metadata_field_update_applicable',
            metaconf_id=metaconf_id,
            metadata_applicable=metadata_applicable,
        )

    def metadata_get(
            self,
            id,
            brand_id=None,
            client_access=None,
            meta_type=None,
            metagroup_id=None,
        ) -> Dict:
        """Get Custom Field Values

        API Method: uber.metadata_get

        This method is used to retrieve custom field values.

        Args:
            id: Object ID,
            brand_id: Brand ID. Defaults to None.
            client_access: Client Access Level. Defaults to None.
            meta_type: Custom Field Object Type. Defaults to None.
            metagroup_id: Custom Field Group ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.metadata_get',
            id=id,
            **{'brand_id': brand_id} if brand_id else {},
            **{'client_access': client_access} if client_access else {},
            **{'meta_type': meta_type} if meta_type else {},
            **{'metagroup_id': metagroup_id} if metagroup_id else {},
        )

    def metadata_group_add(
            self,
            meta_type,
            name,
            variable,
            class_id=None,
            i18n=None,
            priority=None,
        ) -> Dict:
        """Add Custom Field Group

        API Method: uber.metadata_group_add

        This method is used to add a custom field group.

        Args:
            meta_type: Custom Field Group Type,
            name: Display Name,
            variable: Variable Name,
            class_id: Brand ID. Defaults to None.
            i18n: Internationalization Options. Defaults to None.
            priority: Priority. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.metadata_group_add',
            meta_type=meta_type,
            name=name,
            variable=variable,
            **{'class_id': class_id} if class_id else {},
            **{'i18n': i18n} if i18n else {},
            **{'priority': priority} if priority else {},
        )

    def metadata_group_delete(
            self,
            metagroup_id,
        ) -> Dict:
        """Delete Custom Field Group

        API Method: uber.metadata_group_delete

        This method is used to delete an existing custom field group.

        Args:
            metagroup_id: Custom Field Group ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.metadata_group_delete',
            metagroup_id=metagroup_id,
        )

    def metadata_group_list(
            self,
            class_id=None,
            meta_type=None,
            metagroup_id=None,
            variable=None,
        ) -> Dict:
        """List Custom Field Groups

        API Method: uber.metadata_group_list

        This method is used to list the existing custom field groups.

        Args:
            class_id: Brand ID. Defaults to None.
            meta_type: Custom Fields Config Type. Defaults to None.
            metagroup_id: Custom Field Group ID. Defaults to None.
            variable: The machine name of the custom field group. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.metadata_group_list',
            **{'class_id': class_id} if class_id else {},
            **{'meta_type': meta_type} if meta_type else {},
            **{'metagroup_id': metagroup_id} if metagroup_id else {},
            **{'variable': variable} if variable else {},
        )

    def metadata_group_update(
            self,
            metagroup_id,
            i18n=None,
            name=None,
            priority=None,
            variable=None,
        ) -> Dict:
        """Update Custom Field Group

        API Method: uber.metadata_group_update

        This method is used to update an existing custom field group.

        Args:
            metagroup_id: Custom Field Group ID,
            i18n: Internationalization Options. Defaults to None.
            name: Display Name. Defaults to None.
            priority: Priority. Defaults to None.
            variable: Variable Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.metadata_group_update',
            metagroup_id=metagroup_id,
            **{'i18n': i18n} if i18n else {},
            **{'name': name} if name else {},
            **{'priority': priority} if priority else {},
            **{'variable': variable} if variable else {},
        )

    def method_get(
            self,
            method_name,
        ) -> Dict:
        """Get API Method Details

        API Method: uber.method_get

        This method is used to get the details of an API method.

        Args:
            method_name: Method Name,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.method_get',
            method_name=method_name,
        )

    def method_list(
            self,
        ) -> Dict:
        """List Available API Methods

        API Method: uber.method_list

        This method is used to get a list of all available API methods.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.method_list',
        )

    def msa_get(
            self,
            brand_id=None,
            format=None,
            msa_id=None,
        ) -> Dict:
        """Get MSA Details

        API Method: uber.msa_get

        This method is used to get the details of a specified msa.

        Args:
            brand_id: Brand ID. Defaults to None.
            format: Format. Defaults to None.
            msa_id: MSA ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.msa_get',
            **{'brand_id': brand_id} if brand_id else {},
            **{'format': format} if format else {},
            **{'msa_id': msa_id} if msa_id else {},
        )

    def notification_add(
            self,
            name,
            notification_type_id,
            assignment=None,
            association=None,
            classification_id=None,
            email_from_default=None,
            impact=None,
            make_replies_links=None,
            notify_account_team=None,
            priority=None,
            q_id=None,
            status_id=None,
        ) -> Dict:
        """Add Notification

        API Method: uber.notification_add

        This method adds a notification.

        Args:
            name: Notification Name,
            notification_type_id: Notification Type ID,
            assignment: Ticket Assignment User ID. Defaults to None.
            association: Association. Defaults to None.
            classification_id: Ticket Classification ID. Defaults to None.
            email_from_default: Default From Address. Defaults to None.
            impact: Ticket Impact. Defaults to None.
            make_replies_links: Replies will open Linked Tickets. Defaults to None.
            notify_account_team: Notify Account Team. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            q_id: Ticket Department ID. Defaults to None.
            status_id: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_add',
            name=name,
            notification_type_id=notification_type_id,
            **{'assignment': assignment} if assignment else {},
            **{'association': association} if association else {},
            **{'classification_id': classification_id} if classification_id else {},
            **{'email_from_default': email_from_default} if email_from_default else {},
            **{'impact': impact} if impact else {},
            **{'make_replies_links': make_replies_links} if make_replies_links else {},
            **{'notify_account_team': notify_account_team} if notify_account_team else {},
            **{'priority': priority} if priority else {},
            **{'q_id': q_id} if q_id else {},
            **{'status_id': status_id} if status_id else {},
        )

    def notification_list(
            self,
            assignment=None,
            association=None,
            classification_id=None,
            created_by=None,
            created_ts=None,
            email_from_default=None,
            impact=None,
            make_replies_links=None,
            name=None,
            notification_id=None,
            notification_type_id=None,
            notify_account_team=None,
            priority=None,
            q_id=None,
            status_id=None,
            updated_by=None,
            updated_ts=None,
        ) -> Dict:
        """List Notifications

        API Method: uber.notification_list

        This method lists existing notifications filtered by the parameters specified.

        Args:
            assignment: Ticket Assignment User ID. Defaults to None.
            association: Association. Defaults to None.
            classification_id: Ticket Classification ID. Defaults to None.
            created_by: Created By. Defaults to None.
            created_ts: Created Timestamp. Defaults to None.
            email_from_default: Default From Address. Defaults to None.
            impact: Ticket Impact. Defaults to None.
            make_replies_links: Replies will open Linked Tickets. Defaults to None.
            name: Notification Name. Defaults to None.
            notification_id: Notification ID. Defaults to None.
            notification_type_id: Notification Type ID. Defaults to None.
            notify_account_team: Notify Account Team. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            q_id: Ticket Department ID. Defaults to None.
            status_id: Status. Defaults to None.
            updated_by: Updated By. Defaults to None.
            updated_ts: Updated Timestamp. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_list',
            **{'assignment': assignment} if assignment else {},
            **{'association': association} if association else {},
            **{'classification_id': classification_id} if classification_id else {},
            **{'created_by': created_by} if created_by else {},
            **{'created_ts': created_ts} if created_ts else {},
            **{'email_from_default': email_from_default} if email_from_default else {},
            **{'impact': impact} if impact else {},
            **{'make_replies_links': make_replies_links} if make_replies_links else {},
            **{'name': name} if name else {},
            **{'notification_id': notification_id} if notification_id else {},
            **{'notification_type_id': notification_type_id} if notification_type_id else {},
            **{'notify_account_team': notify_account_team} if notify_account_team else {},
            **{'priority': priority} if priority else {},
            **{'q_id': q_id} if q_id else {},
            **{'status_id': status_id} if status_id else {},
            **{'updated_by': updated_by} if updated_by else {},
            **{'updated_ts': updated_ts} if updated_ts else {},
        )

    def notification_message_add(
            self,
            notification_id,
            notification_message_type_id,
            email_body=None,
            email_from=None,
            email_subject=None,
            send_date=None,
        ) -> Dict:
        """Add Notification Message

        API Method: uber.notification_message_add

        This method adds a notification message and can allow a notification to be scheduled for delivery.

        Args:
            notification_id: Notification ID,
            notification_message_type_id: Notification Message Type ID,
            email_body: Email Body. Defaults to None.
            email_from: Email From. Defaults to None.
            email_subject: Email Subject. Defaults to None.
            send_date: Send Date. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_message_add',
            notification_id=notification_id,
            notification_message_type_id=notification_message_type_id,
            **{'email_body': email_body} if email_body else {},
            **{'email_from': email_from} if email_from else {},
            **{'email_subject': email_subject} if email_subject else {},
            **{'send_date': send_date} if send_date else {},
        )

    def notification_message_list(
            self,
            created_by=None,
            created_ts=None,
            email_body=None,
            email_from=None,
            email_subject=None,
            notification_id=None,
            notification_message_id=None,
            notification_message_type_id=None,
            send_date=None,
            send_date_max=None,
            send_date_min=None,
            status_id=None,
            updated_by=None,
            updated_ts=None,
        ) -> Dict:
        """List Notification Messages

        API Method: uber.notification_message_list

        This method lists notification messages filtered by the parameters specified.

        Args:
            created_by: Created By. Defaults to None.
            created_ts: Created Timestamp. Defaults to None.
            email_body: Email Body. Defaults to None.
            email_from: Email From. Defaults to None.
            email_subject: Email Subject. Defaults to None.
            notification_id: Notification ID. Defaults to None.
            notification_message_id: Notification Message ID. Defaults to None.
            notification_message_type_id: Notification Message Type ID. Defaults to None.
            send_date: Send Date. Defaults to None.
            send_date_max: Send Date Before. Defaults to None.
            send_date_min: Send Date After. Defaults to None.
            status_id: Status ID. Defaults to None.
            updated_by: Updated By. Defaults to None.
            updated_ts: Updated Timestamp. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_message_list',
            **{'created_by': created_by} if created_by else {},
            **{'created_ts': created_ts} if created_ts else {},
            **{'email_body': email_body} if email_body else {},
            **{'email_from': email_from} if email_from else {},
            **{'email_subject': email_subject} if email_subject else {},
            **{'notification_id': notification_id} if notification_id else {},
            **{'notification_message_id': notification_message_id} if notification_message_id else {},
            **{'notification_message_type_id': notification_message_type_id} if notification_message_type_id else {},
            **{'send_date': send_date} if send_date else {},
            **{'send_date_max': send_date_max} if send_date_max else {},
            **{'send_date_min': send_date_min} if send_date_min else {},
            **{'status_id': status_id} if status_id else {},
            **{'updated_by': updated_by} if updated_by else {},
            **{'updated_ts': updated_ts} if updated_ts else {},
        )

    def notification_message_update(
            self,
            notification_message_id,
            email_body=None,
            email_from=None,
            email_subject=None,
            notification_message_type_id=None,
            send_date=None,
        ) -> Dict:
        """Edit Notification Message

        API Method: uber.notification_message_update

        This method edits an existing notification message.

        Args:
            notification_message_id: Notification Message ID,
            email_body: Email Body. Defaults to None.
            email_from: Email From. Defaults to None.
            email_subject: Email Subject. Defaults to None.
            notification_message_type_id: Notification Message Type ID. Defaults to None.
            send_date: Send Date. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_message_update',
            notification_message_id=notification_message_id,
            **{'email_body': email_body} if email_body else {},
            **{'email_from': email_from} if email_from else {},
            **{'email_subject': email_subject} if email_subject else {},
            **{'notification_message_type_id': notification_message_type_id} if notification_message_type_id else {},
            **{'send_date': send_date} if send_date else {},
        )

    def notification_recipient_add(
            self,
            notification_id,
            contact_id=None,
            email=None,
            person_id=None,
            status=None,
        ) -> Dict:
        """Manually Add Notification Recipient

        API Method: uber.notification_recipient_add

        This method manually adds a unique recipient to a notification.

        Args:
            notification_id: Notification ID,
            contact_id: Contact ID. Defaults to None.
            email: Email. Defaults to None.
            person_id: Admin ID. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_recipient_add',
            notification_id=notification_id,
            **{'contact_id': contact_id} if contact_id else {},
            **{'email': email} if email else {},
            **{'person_id': person_id} if person_id else {},
            **{'status': status} if status else {},
        )

    def notification_recipient_list(
            self,
            contact_id=None,
            created_by=None,
            created_ts=None,
            created_ts_max=None,
            created_ts_min=None,
            email=None,
            manually_added=None,
            notification_id=None,
            notification_recipient_id=None,
            person_id=None,
            status=None,
            updated_by=None,
            updated_ts=None,
            updated_ts_max=None,
            updated_ts_min=None,
        ) -> Dict:
        """List Notification Recipients

        API Method: uber.notification_recipient_list

        This method lists notification recipients filtered by the specified parameters.

        Args:
            contact_id: Contact ID. Defaults to None.
            created_by: Created By. Defaults to None.
            created_ts: Created Timestamp. Defaults to None.
            created_ts_max: Created Timestamp Before. Defaults to None.
            created_ts_min: Created Timestamp After. Defaults to None.
            email: Email. Defaults to None.
            manually_added: Manually Added. Defaults to None.
            notification_id: Notification ID. Defaults to None.
            notification_recipient_id: Notification Recipient ID. Defaults to None.
            person_id: Admin ID. Defaults to None.
            status: Status. Defaults to None.
            updated_by: Updated By. Defaults to None.
            updated_ts: Updated Timestamp. Defaults to None.
            updated_ts_max: Updated Timestamp Before. Defaults to None.
            updated_ts_min: Updated Timestamp After. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_recipient_list',
            **{'contact_id': contact_id} if contact_id else {},
            **{'created_by': created_by} if created_by else {},
            **{'created_ts': created_ts} if created_ts else {},
            **{'created_ts_max': created_ts_max} if created_ts_max else {},
            **{'created_ts_min': created_ts_min} if created_ts_min else {},
            **{'email': email} if email else {},
            **{'manually_added': manually_added} if manually_added else {},
            **{'notification_id': notification_id} if notification_id else {},
            **{'notification_recipient_id': notification_recipient_id} if notification_recipient_id else {},
            **{'person_id': person_id} if person_id else {},
            **{'status': status} if status else {},
            **{'updated_by': updated_by} if updated_by else {},
            **{'updated_ts': updated_ts} if updated_ts else {},
            **{'updated_ts_max': updated_ts_max} if updated_ts_max else {},
            **{'updated_ts_min': updated_ts_min} if updated_ts_min else {},
        )

    def notification_recipient_log_list(
            self,
            notification_message_id=None,
            notification_recipient_id=None,
            notification_recipient_log_id=None,
            result=None,
            result_ts=None,
            result_ts_max=None,
            result_ts_min=None,
            sent_to=None,
            status_id=None,
        ) -> Dict:
        """List Notification Recipient Logs

        API Method: uber.notification_recipient_log_list

        This method lists notification recipient logs filtered by the specified parameters.

        Args:
            notification_message_id: Notification Message ID. Defaults to None.
            notification_recipient_id: Notification Recipient ID. Defaults to None.
            notification_recipient_log_id: Notification Recipient Log ID. Defaults to None.
            result: Result. Defaults to None.
            result_ts: Result Timestamp. Defaults to None.
            result_ts_max: Result Timestamp Before. Defaults to None.
            result_ts_min: Result Timestamp After. Defaults to None.
            sent_to: Sent To. Defaults to None.
            status_id: Status ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_recipient_log_list',
            **{'notification_message_id': notification_message_id} if notification_message_id else {},
            **{'notification_recipient_id': notification_recipient_id} if notification_recipient_id else {},
            **{'notification_recipient_log_id': notification_recipient_log_id} if notification_recipient_log_id else {},
            **{'result': result} if result else {},
            **{'result_ts': result_ts} if result_ts else {},
            **{'result_ts_max': result_ts_max} if result_ts_max else {},
            **{'result_ts_min': result_ts_min} if result_ts_min else {},
            **{'sent_to': sent_to} if sent_to else {},
            **{'status_id': status_id} if status_id else {},
        )

    def notification_recipient_populate(
            self,
            notification_id,
        ) -> Dict:
        """Notification Recipient Populate

        API Method: uber.notification_recipient_populate

        This method creates all recipient records for a notification based on existing subscriptions.

        Args:
            notification_id: Notification ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_recipient_populate',
            notification_id=notification_id,
        )

    def notification_recipient_update(
            self,
            notification_recipient_id,
            email=None,
            status=None,
        ) -> Dict:
        """Edit a Notification Recipient

        API Method: uber.notification_recipient_update

        This method edits a notification recipient.

        Args:
            notification_recipient_id: Notification Recipient ID,
            email: Email. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_recipient_update',
            notification_recipient_id=notification_recipient_id,
            **{'email': email} if email else {},
            **{'status': status} if status else {},
        )

    def notification_type_add(
            self,
            class_id,
            name,
            assignment=None,
            classification_id=None,
            email_from_default=None,
            impact=None,
            make_replies_links=None,
            notify_account_team=None,
            priority=None,
            q_id=None,
            status=None,
        ) -> Dict:
        """Add a Notification Type

        API Method: uber.notification_type_add

        This method adds a notification type.

        Args:
            class_id: Brand ID,
            name: Notification Type Name,
            assignment: Ticket Assignment User ID. Defaults to None.
            classification_id: Ticket Classification ID. Defaults to None.
            email_from_default: Default From Address. Defaults to None.
            impact: Ticket Impact. Defaults to None.
            make_replies_links: Replies will open Linked Tickets. Defaults to None.
            notify_account_team: Notify Account Team. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            q_id: Ticket Department ID. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_type_add',
            class_id=class_id,
            name=name,
            **{'assignment': assignment} if assignment else {},
            **{'classification_id': classification_id} if classification_id else {},
            **{'email_from_default': email_from_default} if email_from_default else {},
            **{'impact': impact} if impact else {},
            **{'make_replies_links': make_replies_links} if make_replies_links else {},
            **{'notify_account_team': notify_account_team} if notify_account_team else {},
            **{'priority': priority} if priority else {},
            **{'q_id': q_id} if q_id else {},
            **{'status': status} if status else {},
        )

    def notification_type_get(
            self,
            notification_type_id,
        ) -> Dict:
        """Get Notification Type Details

        API Method: uber.notification_type_get

        This method retrieves the details of a notification type.

        Args:
            notification_type_id: Notification Type ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_type_get',
            notification_type_id=notification_type_id,
        )

    def notification_type_list(
            self,
            assignment=None,
            class_id=None,
            classification_id=None,
            email_from_default=None,
            impact=None,
            make_replies_links=None,
            name=None,
            notify_account_team=None,
            priority=None,
            q_id=None,
            status=None,
        ) -> Dict:
        """List Notification Types

        API Method: uber.notification_type_list

        This method lists the notification types registered.

        Args:
            assignment: Ticket Assignment User ID. Defaults to None.
            class_id: Brand ID. Defaults to None.
            classification_id: Ticket Classification ID. Defaults to None.
            email_from_default: Default From Address. Defaults to None.
            impact: Ticket Impact. Defaults to None.
            make_replies_links: Replies will open Linked Tickets. Defaults to None.
            name: Notification Type Name. Defaults to None.
            notify_account_team: Notify Account Team. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            q_id: Ticket Department ID. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_type_list',
            **{'assignment': assignment} if assignment else {},
            **{'class_id': class_id} if class_id else {},
            **{'classification_id': classification_id} if classification_id else {},
            **{'email_from_default': email_from_default} if email_from_default else {},
            **{'impact': impact} if impact else {},
            **{'make_replies_links': make_replies_links} if make_replies_links else {},
            **{'name': name} if name else {},
            **{'notify_account_team': notify_account_team} if notify_account_team else {},
            **{'priority': priority} if priority else {},
            **{'q_id': q_id} if q_id else {},
            **{'status': status} if status else {},
        )

    def notification_type_subscriber_add(
            self,
            notification_type_id,
            contact_id=None,
            override_email=None,
            person_id=None,
        ) -> Dict:
        """Add Subscriber to a Notification Type

        API Method: uber.notification_type_subscriber_add

        This method adds a subscriber to notifications of a certain type.

        Args:
            notification_type_id: Notification Type ID,
            contact_id: Contact ID. Defaults to None.
            override_email: Override email. Defaults to None.
            person_id: Admin ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_type_subscriber_add',
            notification_type_id=notification_type_id,
            **{'contact_id': contact_id} if contact_id else {},
            **{'override_email': override_email} if override_email else {},
            **{'person_id': person_id} if person_id else {},
        )

    def notification_type_subscriber_delete(
            self,
            notification_type_subscriber_id=None,
        ) -> Dict:
        """Unsubscribe From a Notification Type

        API Method: uber.notification_type_subscriber_delete

        This method unsubscribes a contact or admin from notifications of a certain type.

        Args:
            notification_type_subscriber_id: Notification Type Subscriber ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_type_subscriber_delete',
            **{'notification_type_subscriber_id': notification_type_subscriber_id} if notification_type_subscriber_id else {},
        )

    def notification_type_subscriber_list(
            self,
            contact_id=None,
            created_by=None,
            created_ts=None,
            created_ts_max=None,
            created_ts_min=None,
            notification_type_id=None,
            override_email=None,
            person_id=None,
            updated_by=None,
            updated_ts=None,
            updated_ts_max=None,
            updated_ts_min=None,
        ) -> Dict:
        """List Notification Type Subscriptions

        API Method: uber.notification_type_subscriber_list

        This method lists notification subscriptions filtered by the parameters supplied.

        Args:
            contact_id: Contact ID. Defaults to None.
            created_by: Created By. Defaults to None.
            created_ts: Created Timestamp. Defaults to None.
            created_ts_max: Created Timestamp Before. Defaults to None.
            created_ts_min: Created Timestamp After. Defaults to None.
            notification_type_id: Notification Type ID. Defaults to None.
            override_email: Override email. Defaults to None.
            person_id: Admin ID. Defaults to None.
            updated_by: Updated By. Defaults to None.
            updated_ts: Updated Timestamp. Defaults to None.
            updated_ts_max: Updated Timestamp Before. Defaults to None.
            updated_ts_min: Updated Timestamp After. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_type_subscriber_list',
            **{'contact_id': contact_id} if contact_id else {},
            **{'created_by': created_by} if created_by else {},
            **{'created_ts': created_ts} if created_ts else {},
            **{'created_ts_max': created_ts_max} if created_ts_max else {},
            **{'created_ts_min': created_ts_min} if created_ts_min else {},
            **{'notification_type_id': notification_type_id} if notification_type_id else {},
            **{'override_email': override_email} if override_email else {},
            **{'person_id': person_id} if person_id else {},
            **{'updated_by': updated_by} if updated_by else {},
            **{'updated_ts': updated_ts} if updated_ts else {},
            **{'updated_ts_max': updated_ts_max} if updated_ts_max else {},
            **{'updated_ts_min': updated_ts_min} if updated_ts_min else {},
        )

    def notification_type_subscriber_update(
            self,
            notification_type_subscriber_id,
            override_email=None,
        ) -> Dict:
        """Edit a Notification Type Subscription

        API Method: uber.notification_type_subscriber_update

        This method edits a subscription for a notification type.

        Args:
            notification_type_subscriber_id: Notification Type Subscriber ID,
            override_email: Override email. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_type_subscriber_update',
            notification_type_subscriber_id=notification_type_subscriber_id,
            **{'override_email': override_email} if override_email else {},
        )

    def notification_type_update(
            self,
            notification_type_id,
            assignment=None,
            class_id=None,
            classification_id=None,
            email_from_default=None,
            impact=None,
            make_replies_links=None,
            name=None,
            notify_account_team=None,
            priority=None,
            q_id=None,
            status=None,
        ) -> Dict:
        """Edit Notification Type

        API Method: uber.notification_type_update

        This method edits an existing notification type.

        Args:
            notification_type_id: Notification Type ID,
            assignment: Ticket Assignment User ID. Defaults to None.
            class_id: Brand ID. Defaults to None.
            classification_id: Ticket Classification ID. Defaults to None.
            email_from_default: Default From Address. Defaults to None.
            impact: Ticket Impact. Defaults to None.
            make_replies_links: Replies will open Linked Tickets. Defaults to None.
            name: Notification Type Name. Defaults to None.
            notify_account_team: Notify Account Team. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            q_id: Ticket Department ID. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_type_update',
            notification_type_id=notification_type_id,
            **{'assignment': assignment} if assignment else {},
            **{'class_id': class_id} if class_id else {},
            **{'classification_id': classification_id} if classification_id else {},
            **{'email_from_default': email_from_default} if email_from_default else {},
            **{'impact': impact} if impact else {},
            **{'make_replies_links': make_replies_links} if make_replies_links else {},
            **{'name': name} if name else {},
            **{'notify_account_team': notify_account_team} if notify_account_team else {},
            **{'priority': priority} if priority else {},
            **{'q_id': q_id} if q_id else {},
            **{'status': status} if status else {},
        )

    def notification_update(
            self,
            notification_id,
            assignment=None,
            association=None,
            classification_id=None,
            email_from_default=None,
            impact=None,
            make_replies_links=None,
            name=None,
            notification_type_id=None,
            notify_account_team=None,
            priority=None,
            q_id=None,
            status_id=None,
        ) -> Dict:
        """Edit Notification

        API Method: uber.notification_update

        This method edits a notification.

        Args:
            notification_id: Notification ID,
            assignment: Ticket Assignment User ID. Defaults to None.
            association: Association. Defaults to None.
            classification_id: Ticket Classification ID. Defaults to None.
            email_from_default: Default From Address. Defaults to None.
            impact: Ticket Impact. Defaults to None.
            make_replies_links: Replies will open Linked Tickets. Defaults to None.
            name: Notification Name. Defaults to None.
            notification_type_id: Notification Type ID. Defaults to None.
            notify_account_team: Notify Account Team. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            q_id: Ticket Department ID. Defaults to None.
            status_id: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.notification_update',
            notification_id=notification_id,
            **{'assignment': assignment} if assignment else {},
            **{'association': association} if association else {},
            **{'classification_id': classification_id} if classification_id else {},
            **{'email_from_default': email_from_default} if email_from_default else {},
            **{'impact': impact} if impact else {},
            **{'make_replies_links': make_replies_links} if make_replies_links else {},
            **{'name': name} if name else {},
            **{'notification_type_id': notification_type_id} if notification_type_id else {},
            **{'notify_account_team': notify_account_team} if notify_account_team else {},
            **{'priority': priority} if priority else {},
            **{'q_id': q_id} if q_id else {},
            **{'status_id': status_id} if status_id else {},
        )

    def overdue_notice_schedules_activate(
            self,
            id,
        ) -> Dict:
        """Activate an Invoice Overdue Notice Schedules

        API Method: uber.overdue_notice_schedules_activate

        This method is used to activate an invoice overdue notice schedule.

        Args:
            id: Invoice Overdue Notice ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.overdue_notice_schedules_activate',
            id=id,
        )

    def overdue_notice_schedules_add(
            self,
            class_id,
            name,
            schedules,
            attach_pdf=None,
        ) -> Dict:
        """Add Invoice Overdue Notice Schedules

        API Method: uber.overdue_notice_schedules_add

        This method is used to create an invoice overdue notice schedules.

        Args:
            class_id: Brand ID,
            name: Notice Schedule Name,
            schedules: Schedules,
            attach_pdf: Attach PDF. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.overdue_notice_schedules_add',
            class_id=class_id,
            name=name,
            schedules=schedules,
            **{'attach_pdf': attach_pdf} if attach_pdf else {},
        )

    def overdue_notice_schedules_assign(
            self,
            id,
            brand_id=None,
            client_id=None,
        ) -> Dict:
        """Assign an Invoice Overdue Notice Schedules

        API Method: uber.overdue_notice_schedules_assign

        This method is used to set an active invoice overdue notice schedules as default for a client or for a brand.

        Args:
            id: Overdue Notice Schedules ID,
            brand_id: Brand ID. Defaults to None.
            client_id: Client ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.overdue_notice_schedules_assign',
            id=id,
            **{'brand_id': brand_id} if brand_id else {},
            **{'client_id': client_id} if client_id else {},
        )

    def overdue_notice_schedules_deactivate(
            self,
            id,
        ) -> Dict:
        """Deactivate an Invoice Overdue Notice Schedules

        API Method: uber.overdue_notice_schedules_deactivate

        This method is used to deactivate an invoice overdue notice schedules.

        Args:
            id: Invoice Overdue Notice Schedules ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.overdue_notice_schedules_deactivate',
            id=id,
        )

    def overdue_notice_schedules_delete(
            self,
            id,
        ) -> Dict:
        """Delete an Invoice Overdue Notice Schedules

        API Method: uber.overdue_notice_schedules_delete

        This method is used to delete an invoice overdue notice schedules.

        Args:
            id: Invoice Overdue Notice ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.overdue_notice_schedules_delete',
            id=id,
        )

    def overdue_notice_schedules_get(
            self,
            id,
        ) -> Dict:
        """Get Invoice Overdue Notice Schedules

        API Method: uber.overdue_notice_schedules_get

        This method is used to get an invoice overdue notice schedules.

        Args:
            id: Overdue Notice Schedules ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.overdue_notice_schedules_get',
            id=id,
        )

    def overdue_notice_schedules_list(
            self,
            class_id=None,
            direction=None,
            limit=None,
            offset=None,
            order_by=None,
            status=None,
        ) -> Dict:
        """List Invoice Overdue Notice Schedules

        API Method: uber.overdue_notice_schedules_list

        This method is used to list invoice overdue notice schedules.

        Args:
            class_id: Brand ID. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.overdue_notice_schedules_list',
            **{'class_id': class_id} if class_id else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'status': status} if status else {},
        )

    def overdue_notice_schedules_mute(
            self,
            mute,
            class_id=None,
            client_id=None,
        ) -> Dict:
        """Mute/Unmute Invoice Overdue Notices Schedules.

        API Method: uber.overdue_notice_schedules_mute

        This method is used to mute/unmute invoice overdue notice schedules for a specific client or for the whole barnd.

        Args:
            mute: Mute,
            class_id: Brand ID. Defaults to None.
            client_id: Client ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.overdue_notice_schedules_mute',
            mute=mute,
            **{'class_id': class_id} if class_id else {},
            **{'client_id': client_id} if client_id else {},
        )

    def overdue_notice_schedules_update(
            self,
            id,
            attach_pdf=None,
            name=None,
            schedules=None,
        ) -> Dict:
        """Update an Invoice Overdue Notice Schedules

        API Method: uber.overdue_notice_schedules_update

        This method is used to update an invoice overdue notice schedules.

        Args:
            id: Overdue Notice Schedules ID,
            attach_pdf: Attach PDF. Defaults to None.
            name: Notice Schedule Name. Defaults to None.
            schedules: Schedules. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.overdue_notice_schedules_update',
            id=id,
            **{'attach_pdf': attach_pdf} if attach_pdf else {},
            **{'name': name} if name else {},
            **{'schedules': schedules} if schedules else {},
        )

    def password_reset(
            self,
            new_pass,
            reset_code,
        ) -> Dict:
        """Reset Password

        API Method: uber.password_reset

        Reset a user password given a valid reset code and new password.

        Args:
            new_pass: New Password,
            reset_code: Reset Code,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.password_reset',
            new_pass=new_pass,
            reset_code=reset_code,
        )

    def plan_option_add(
            self,
            pu_id,
            i18n=None,
            po_data=None,
            po_desc=None,
            po_description=None,
            po_priority=None,
            pog_id=None,
            pricing=None,
        ) -> Dict:
        """Add Plan Option

        API Method: uber.plan_option_add

        This method is used to add an plan option to an existing upgrade.

        Args:
            pu_id: Plan Upgrade ID,
            i18n: Internationalization. Defaults to None.
            po_data: Extra Data. Defaults to None.
            po_desc: Description. Defaults to None.
            po_description: Name. Defaults to None.
            po_priority: Priority. Defaults to None.
            pog_id: Plan Option Group ID. Defaults to None.
            pricing: Pricing. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_option_add',
            pu_id=pu_id,
            **{'i18n': i18n} if i18n else {},
            **{'po_data': po_data} if po_data else {},
            **{'po_desc': po_desc} if po_desc else {},
            **{'po_description': po_description} if po_description else {},
            **{'po_priority': po_priority} if po_priority else {},
            **{'pog_id': pog_id} if pog_id else {},
            **{'pricing': pricing} if pricing else {},
        )

    def plan_option_assign(
            self,
            assign,
            plan_id,
            po_id,
            po_data=None,
            po_val=None,
            pricing=None,
        ) -> Dict:
        """Assign Plan Option

        API Method: uber.plan_option_assign

        This method is used to assign and unassign a plan option to a service plan.

        Args:
            assign: Assign,
            plan_id: Service Plan ID,
            po_id: Plan Option ID,
            po_data: Extra Data. Defaults to None.
            po_val: Value. Defaults to None.
            pricing: Pricing. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_option_assign',
            assign=assign,
            plan_id=plan_id,
            po_id=po_id,
            **{'po_data': po_data} if po_data else {},
            **{'po_val': po_val} if po_val else {},
            **{'pricing': pricing} if pricing else {},
        )

    def plan_option_assign_bulk(
            self,
            plan_id,
            plan_options,
        ) -> Dict:
        """Assign Plan Options in Bulk

        API Method: uber.plan_option_assign_bulk

        <p>This method is used to assign and/or unassign a list of plan options to a service plan.</p><p>If there is an error in the request format, the execution will stop immediately without performing any modifications to the plan options.</p><p>Otherwise, each option assignment will be executed in sequence. Each individual option assignments can be a failure or a success. See the <b>Example Output</b> bellow for response examples.</p><br />

        Args:
            plan_id: Service Plan ID,
            plan_options: Plan Options List,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_option_assign_bulk',
            plan_id=plan_id,
            plan_options=plan_options,
        )

    def plan_option_group_add(
            self,
            pog_name,
            pu_id,
            i18n=None,
            pog_data=None,
            pog_desc=None,
            pog_priority=None,
            pog_status=None,
        ) -> Dict:
        """Add Plan Option Group

        API Method: uber.plan_option_group_add

        This method is used to add an plan option group to an existing plan upgrade.

        Args:
            pog_name: Name,
            pu_id: Plan Upgrade ID,
            i18n: Internationalization. Defaults to None.
            pog_data: Extra Data. Defaults to None.
            pog_desc: Description. Defaults to None.
            pog_priority: Priority. Defaults to None.
            pog_status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_option_group_add',
            pog_name=pog_name,
            pu_id=pu_id,
            **{'i18n': i18n} if i18n else {},
            **{'pog_data': pog_data} if pog_data else {},
            **{'pog_desc': pog_desc} if pog_desc else {},
            **{'pog_priority': pog_priority} if pog_priority else {},
            **{'pog_status': pog_status} if pog_status else {},
        )

    def plan_option_group_assign(
            self,
            assign,
            plan_id,
            pog_id,
            pu_id=None,
        ) -> Dict:
        """Assign Plan Option Group

        API Method: uber.plan_option_group_assign

        This method is used to assign and unassign a plan option group to a service plan.

        Args:
            assign: Assign,
            plan_id: Service Plan ID,
            pog_id: Plan Option Group ID,
            pu_id: Plan Upgrade ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_option_group_assign',
            assign=assign,
            plan_id=plan_id,
            pog_id=pog_id,
            **{'pu_id': pu_id} if pu_id else {},
        )

    def plan_option_group_list(
            self,
            pu_id,
            all_options=None,
            exclude_empty=None,
            include_inactive=None,
            lang_id=None,
            plan_id=None,
            pog_id=None,
        ) -> Dict:
        """List Plan Option Groups

        API Method: uber.plan_option_group_list

        This method is used to list plan option groups.

        Args:
            pu_id: Plan Upgrade ID,
            all_options: Include Options. Defaults to None.
            exclude_empty: Exclude Empty Option Groups. Defaults to None.
            include_inactive: Include Inactive Items. Defaults to None.
            lang_id: Language ID. Defaults to None.
            plan_id: Service Plan ID. Defaults to None.
            pog_id: Plan Option Group ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_option_group_list',
            pu_id=pu_id,
            **{'all_options': all_options} if all_options else {},
            **{'exclude_empty': exclude_empty} if exclude_empty else {},
            **{'include_inactive': include_inactive} if include_inactive else {},
            **{'lang_id': lang_id} if lang_id else {},
            **{'plan_id': plan_id} if plan_id else {},
            **{'pog_id': pog_id} if pog_id else {},
        )

    def plan_option_group_update(
            self,
            pog_id,
            i18n=None,
            pog_data=None,
            pog_desc=None,
            pog_name=None,
            pog_priority=None,
            pog_status=None,
        ) -> Dict:
        """Update Service Plan Option Group

        API Method: uber.plan_option_group_update

        This method is used to update an option group for an existing service plan.

        Args:
            pog_id: Plan Option Group ID,
            i18n: Internationalization. Defaults to None.
            pog_data: Extra Data. Defaults to None.
            pog_desc: Description. Defaults to None.
            pog_name: Name. Defaults to None.
            pog_priority: Priority. Defaults to None.
            pog_status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_option_group_update',
            pog_id=pog_id,
            **{'i18n': i18n} if i18n else {},
            **{'pog_data': pog_data} if pog_data else {},
            **{'pog_desc': pog_desc} if pog_desc else {},
            **{'pog_name': pog_name} if pog_name else {},
            **{'pog_priority': pog_priority} if pog_priority else {},
            **{'pog_status': pog_status} if pog_status else {},
        )

    def plan_option_list(
            self,
            brand_id=None,
            include_inactive=None,
            lang_id=None,
            plan_id=None,
            po_id=None,
            pog_id=None,
            pu_id=None,
        ) -> Dict:
        """List Plan Options

        API Method: uber.plan_option_list

        This method is used to list plan options.

        Args:
            brand_id: Brand ID. Defaults to None.
            include_inactive: Include Inactive Items. Defaults to None.
            lang_id: Language ID. Defaults to None.
            plan_id: Service Plan ID. Defaults to None.
            po_id: Plan Option ID. Defaults to None.
            pog_id: Plan Option Group ID. Defaults to None.
            pu_id: Plan Upgrade ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_option_list',
            **{'brand_id': brand_id} if brand_id else {},
            **{'include_inactive': include_inactive} if include_inactive else {},
            **{'lang_id': lang_id} if lang_id else {},
            **{'plan_id': plan_id} if plan_id else {},
            **{'po_id': po_id} if po_id else {},
            **{'pog_id': pog_id} if pog_id else {},
            **{'pu_id': pu_id} if pu_id else {},
        )

    def plan_option_update(
            self,
            po_id,
            i18n=None,
            po_data=None,
            po_desc=None,
            po_description=None,
            po_priority=None,
            pog_id=None,
            pricing=None,
        ) -> Dict:
        """Update Plan Option

        API Method: uber.plan_option_update

        This method is used to update a plan option.

        Args:
            po_id: Plan Option ID,
            i18n: Internationalization. Defaults to None.
            po_data: Extra Data. Defaults to None.
            po_desc: Description. Defaults to None.
            po_description: Name. Defaults to None.
            po_priority: Priority. Defaults to None.
            pog_id: Plan Option Group ID. Defaults to None.
            pricing: Pricing. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_option_update',
            po_id=po_id,
            **{'i18n': i18n} if i18n else {},
            **{'po_data': po_data} if po_data else {},
            **{'po_desc': po_desc} if po_desc else {},
            **{'po_description': po_description} if po_description else {},
            **{'po_priority': po_priority} if po_priority else {},
            **{'pog_id': pog_id} if pog_id else {},
            **{'pricing': pricing} if pricing else {},
        )

    def plan_upgrade_add(
            self,
            pu_name,
            variable,
            i18n=None,
            invoice_hide=None,
            pu_data=None,
            pu_desc=None,
            pu_priority=None,
            pu_status=None,
            pug_id=None,
        ) -> Dict:
        """Add Plan Upgrade

        API Method: uber.plan_upgrade_add

        This method is used to add a plan upgrade.

        Args:
            pu_name: Name,
            variable: Variable,
            i18n: Internationalization. Defaults to None.
            invoice_hide: Client Visibility. Defaults to None.
            pu_data: Extra Data. Defaults to None.
            pu_desc: Description. Defaults to None.
            pu_priority: Priority. Defaults to None.
            pu_status: Status. Defaults to None.
            pug_id: Plan Upgrade Group ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_upgrade_add',
            pu_name=pu_name,
            variable=variable,
            **{'i18n': i18n} if i18n else {},
            **{'invoice_hide': invoice_hide} if invoice_hide else {},
            **{'pu_data': pu_data} if pu_data else {},
            **{'pu_desc': pu_desc} if pu_desc else {},
            **{'pu_priority': pu_priority} if pu_priority else {},
            **{'pu_status': pu_status} if pu_status else {},
            **{'pug_id': pug_id} if pug_id else {},
        )

    def plan_upgrade_assign(
            self,
            assign,
            plan_id,
            pu_id,
        ) -> Dict:
        """Assign Plan Upgrade

        API Method: uber.plan_upgrade_assign

        This method is used to assign and unassign a plan upgrade to a service plan.

        Args:
            assign: Assign,
            plan_id: Service Plan ID,
            pu_id: Plan Upgrade ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_upgrade_assign',
            assign=assign,
            plan_id=plan_id,
            pu_id=pu_id,
        )

    def plan_upgrade_group_add(
            self,
            pug_name,
            i18n=None,
            pug_data=None,
            pug_desc=None,
            pug_priority=None,
            pug_status=None,
        ) -> Dict:
        """Add Plan Upgrade Group

        API Method: uber.plan_upgrade_group_add

        This method is used to add a plan upgrade group.

        Args:
            pug_name: Name,
            i18n: Internationalization. Defaults to None.
            pug_data: Extra Data. Defaults to None.
            pug_desc: Description. Defaults to None.
            pug_priority: Priority. Defaults to None.
            pug_status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_upgrade_group_add',
            pug_name=pug_name,
            **{'i18n': i18n} if i18n else {},
            **{'pug_data': pug_data} if pug_data else {},
            **{'pug_desc': pug_desc} if pug_desc else {},
            **{'pug_priority': pug_priority} if pug_priority else {},
            **{'pug_status': pug_status} if pug_status else {},
        )

    def plan_upgrade_group_assign(
            self,
            assign,
            plan_id,
            pug_id,
        ) -> Dict:
        """Assign Plan Upgrade Group

        API Method: uber.plan_upgrade_group_assign

        This method is used to assign and unassign a plan upgrade group to a service plan.

        Args:
            assign: Assign,
            plan_id: Service Plan ID,
            pug_id: Plan Upgrade Group ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_upgrade_group_assign',
            assign=assign,
            plan_id=plan_id,
            pug_id=pug_id,
        )

    def plan_upgrade_group_list(
            self,
            all_options=None,
            exclude_empty=None,
            include_inactive=None,
            lang_id=None,
            plan_id=None,
            pug_id=None,
        ) -> Dict:
        """List Plan Upgrade Groups

        API Method: uber.plan_upgrade_group_list

        This method is used to list plan upgrade groups.

        Args:
            all_options: Include Options. Defaults to None.
            exclude_empty: Exclude Empty Upgrade Groups. Defaults to None.
            include_inactive: Include Inactive Items. Defaults to None.
            lang_id: Language ID. Defaults to None.
            plan_id: Service Plan ID. Defaults to None.
            pug_id: Plan Upgrade Group ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_upgrade_group_list',
            **{'all_options': all_options} if all_options else {},
            **{'exclude_empty': exclude_empty} if exclude_empty else {},
            **{'include_inactive': include_inactive} if include_inactive else {},
            **{'lang_id': lang_id} if lang_id else {},
            **{'plan_id': plan_id} if plan_id else {},
            **{'pug_id': pug_id} if pug_id else {},
        )

    def plan_upgrade_group_update(
            self,
            pug_id,
            i18n=None,
            pug_data=None,
            pug_desc=None,
            pug_name=None,
            pug_priority=None,
            pug_status=None,
        ) -> Dict:
        """Update Plan Upgrade Group

        API Method: uber.plan_upgrade_group_update

        This method is used to update a plan upgrade group.

        Args:
            pug_id: Plan Upgrade Group ID,
            i18n: Internationalization. Defaults to None.
            pug_data: Extra Data. Defaults to None.
            pug_desc: Description. Defaults to None.
            pug_name: Name. Defaults to None.
            pug_priority: Priority. Defaults to None.
            pug_status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_upgrade_group_update',
            pug_id=pug_id,
            **{'i18n': i18n} if i18n else {},
            **{'pug_data': pug_data} if pug_data else {},
            **{'pug_desc': pug_desc} if pug_desc else {},
            **{'pug_name': pug_name} if pug_name else {},
            **{'pug_priority': pug_priority} if pug_priority else {},
            **{'pug_status': pug_status} if pug_status else {},
        )

    def plan_upgrade_list(
            self,
            all_options=None,
            exclude_empty=None,
            include_inactive=None,
            lang_id=None,
            plan_id=None,
            pu_id=None,
            pug_id=None,
        ) -> Dict:
        """List Plan Upgrades

        API Method: uber.plan_upgrade_list

        This method is used to list plan upgrades.

        Args:
            all_options: Include Option Groups and Options. Defaults to None.
            exclude_empty: Exclude Empty Upgrades. Defaults to None.
            include_inactive: Include Inactive Items. Defaults to None.
            lang_id: Language ID. Defaults to None.
            plan_id: Service Plan ID. Defaults to None.
            pu_id: Plan Upgrade ID. Defaults to None.
            pug_id: Plan Upgrade Group ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_upgrade_list',
            **{'all_options': all_options} if all_options else {},
            **{'exclude_empty': exclude_empty} if exclude_empty else {},
            **{'include_inactive': include_inactive} if include_inactive else {},
            **{'lang_id': lang_id} if lang_id else {},
            **{'plan_id': plan_id} if plan_id else {},
            **{'pu_id': pu_id} if pu_id else {},
            **{'pug_id': pug_id} if pug_id else {},
        )

    def plan_upgrade_update(
            self,
            pu_id,
            i18n=None,
            invoice_hide=None,
            pu_data=None,
            pu_desc=None,
            pu_name=None,
            pu_priority=None,
            pu_status=None,
            pug_id=None,
            variable=None,
        ) -> Dict:
        """Update Service Plan Upgrade

        API Method: uber.plan_upgrade_update

        This method is used to update an existing upgrade on an existing service plan.

        Args:
            pu_id: Plan Upgrade ID,
            i18n: Internationalization. Defaults to None.
            invoice_hide: Client Visibility. Defaults to None.
            pu_data: Extra Data. Defaults to None.
            pu_desc: Description. Defaults to None.
            pu_name: Name. Defaults to None.
            pu_priority: Priority. Defaults to None.
            pu_status: Status. Defaults to None.
            pug_id: Plan Upgrade Group ID. Defaults to None.
            variable: Variable. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.plan_upgrade_update',
            pu_id=pu_id,
            **{'i18n': i18n} if i18n else {},
            **{'invoice_hide': invoice_hide} if invoice_hide else {},
            **{'pu_data': pu_data} if pu_data else {},
            **{'pu_desc': pu_desc} if pu_desc else {},
            **{'pu_name': pu_name} if pu_name else {},
            **{'pu_priority': pu_priority} if pu_priority else {},
            **{'pu_status': pu_status} if pu_status else {},
            **{'pug_id': pug_id} if pug_id else {},
            **{'variable': variable} if variable else {},
        )

    def quick_stats(
            self,
            when=None,
        ) -> Dict:
        """Get Quick System Stats

        API Method: uber.quick_stats

        This method is used to get a quick system overview, as seen in the top bar of the admin interface.

        Args:
            when: Timestamp. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.quick_stats',
            **{'when': when} if when else {},
        )

    def quick_stats_detail(
            self,
            stat_name,
            when=None,
        ) -> Dict:
        """Get Detailed System Stats

        API Method: uber.quick_stats_detail

        This method is used to provide more detailed information on various system stats.

        Args:
            stat_name: Statistic to Return,
            when: Timestamp. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.quick_stats_detail',
            stat_name=stat_name,
            **{'when': when} if when else {},
        )

    def rate_plan_add(
            self,
            name,
            brand_id=None,
            contract_terms=None,
            data=None,
            description=None,
            facilities=None,
            status=None,
        ) -> Dict:
        """Add a Rate Plan

        API Method: uber.rate_plan_add

        This method is used to add a rate plan

        Args:
            name: Rate Plan Name,
            brand_id: Brand ID. Defaults to None.
            contract_terms: Contract Terms. Defaults to None.
            data: Data. Defaults to None.
            description: Description. Defaults to None.
            facilities: Facilities. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.rate_plan_add',
            name=name,
            **{'brand_id': brand_id} if brand_id else {},
            **{'contract_terms': contract_terms} if contract_terms else {},
            **{'data': data} if data else {},
            **{'description': description} if description else {},
            **{'facilities': facilities} if facilities else {},
            **{'status': status} if status else {},
        )

    def rate_plan_get(
            self,
            rate_plan_id,
            include_inactive=None,
        ) -> Dict:
        """Get Rate Plan Details

        API Method: uber.rate_plan_get

        This method is used to get the details of a specified rate plan

        Args:
            rate_plan_id: Rate Plan ID,
            include_inactive: Include Inactive Items. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.rate_plan_get',
            rate_plan_id=rate_plan_id,
            **{'include_inactive': include_inactive} if include_inactive else {},
        )

    def rate_plan_list(
            self,
            brand_id=None,
            status=None,
        ) -> Dict:
        """List Rate Plans

        API Method: uber.rate_plan_list

        This method is used to list rate plans

        Args:
            brand_id: Brand ID. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.rate_plan_list',
            **{'brand_id': brand_id} if brand_id else {},
            **{'status': status} if status else {},
        )

    def rate_plan_option_add(
            self,
            po_id,
            rate_plan_id,
            data=None,
            pricing=None,
            status=None,
        ) -> Dict:
        """Add a Plan Option to a Rate Plan

        API Method: uber.rate_plan_option_add

        This method is used to add an plan option to a rate plan

        Args:
            po_id: Plan Option ID,
            rate_plan_id: Rate Plan ID,
            data: Data. Defaults to None.
            pricing: Pricing. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.rate_plan_option_add',
            po_id=po_id,
            rate_plan_id=rate_plan_id,
            **{'data': data} if data else {},
            **{'pricing': pricing} if pricing else {},
            **{'status': status} if status else {},
        )

    def rate_plan_option_get(
            self,
            rate_plan_option_id,
            include_option_info=None,
        ) -> Dict:
        """Get Rate Plan Option Details

        API Method: uber.rate_plan_option_get

        This method is used to get the details of a specified rate plan option

        Args:
            rate_plan_option_id: Rate Plan Option ID,
            include_option_info: Include Option Info Flag. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.rate_plan_option_get',
            rate_plan_option_id=rate_plan_option_id,
            **{'include_option_info': include_option_info} if include_option_info else {},
        )

    def rate_plan_option_update(
            self,
            rate_plan_option_id,
            data=None,
            delete_data=None,
            pricing=None,
            status=None,
        ) -> Dict:
        """Update a Plan Option in a Rate Plan

        API Method: uber.rate_plan_option_update

        This method is used to update a plan option in a rate plan

        Args:
            rate_plan_option_id: Rate Plan Option ID,
            data: Data. Defaults to None.
            delete_data: Delete Data. Defaults to None.
            pricing: Pricing. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.rate_plan_option_update',
            rate_plan_option_id=rate_plan_option_id,
            **{'data': data} if data else {},
            **{'delete_data': delete_data} if delete_data else {},
            **{'pricing': pricing} if pricing else {},
            **{'status': status} if status else {},
        )

    def rate_plan_service_plan_add(
            self,
            plan_id,
            rate_plan_id,
            pricing=None,
            status=None,
        ) -> Dict:
        """Add a Service Plan to a Rate Plan

        API Method: uber.rate_plan_service_plan_add

        This method is used to add a service plan to a rate plan

        Args:
            plan_id: Plan ID,
            rate_plan_id: Rate Plan ID,
            pricing: Pricing. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.rate_plan_service_plan_add',
            plan_id=plan_id,
            rate_plan_id=rate_plan_id,
            **{'pricing': pricing} if pricing else {},
            **{'status': status} if status else {},
        )

    def rate_plan_service_plan_get(
            self,
            plan_id,
            rate_plan_id,
        ) -> Dict:
        """Get a Service Plan Detail in a Rate Plan

        API Method: uber.rate_plan_service_plan_get

        This method is used to get a service plan detail in a rate plan

        Args:
            plan_id: Plan ID,
            rate_plan_id: Rate Plan ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.rate_plan_service_plan_get',
            plan_id=plan_id,
            rate_plan_id=rate_plan_id,
        )

    def rate_plan_service_plan_update(
            self,
            plan_id,
            rate_plan_id,
            pricing=None,
            status=None,
        ) -> Dict:
        """Update a Service Plan in a Rate Plan

        API Method: uber.rate_plan_service_plan_update

        This method is used to update a service plan in a rate plan

        Args:
            plan_id: Plan ID,
            rate_plan_id: Rate Plan ID,
            pricing: Pricing. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.rate_plan_service_plan_update',
            plan_id=plan_id,
            rate_plan_id=rate_plan_id,
            **{'pricing': pricing} if pricing else {},
            **{'status': status} if status else {},
        )

    def rate_plan_update(
            self,
            rate_plan_id,
            brand_id=None,
            contract_terms=None,
            data=None,
            delete_contract_terms=None,
            delete_data=None,
            delete_facilities=None,
            description=None,
            facilities=None,
            name=None,
            status=None,
        ) -> Dict:
        """Update a Rate Plan

        API Method: uber.rate_plan_update

        This method is used to update a rate plan

        Args:
            rate_plan_id: Rate Plan ID,
            brand_id: Brand ID. Defaults to None.
            contract_terms: Contract Terms. Defaults to None.
            data: Data. Defaults to None.
            delete_contract_terms: Delete Contract Terms. Defaults to None.
            delete_data: Delete Data. Defaults to None.
            delete_facilities: Delete Facilities. Defaults to None.
            description: Description. Defaults to None.
            facilities: Facilities. Defaults to None.
            name: Rate Plan Name. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.rate_plan_update',
            rate_plan_id=rate_plan_id,
            **{'brand_id': brand_id} if brand_id else {},
            **{'contract_terms': contract_terms} if contract_terms else {},
            **{'data': data} if data else {},
            **{'delete_contract_terms': delete_contract_terms} if delete_contract_terms else {},
            **{'delete_data': delete_data} if delete_data else {},
            **{'delete_facilities': delete_facilities} if delete_facilities else {},
            **{'description': description} if description else {},
            **{'facilities': facilities} if facilities else {},
            **{'name': name} if name else {},
            **{'status': status} if status else {},
        )

    def service_module_list(
            self,
            module=None,
        ) -> Dict:
        """List Service Modules

        API Method: uber.service_module_list

        This method is used to list all available service modules.

        Args:
            module: Service Module. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_module_list',
            **{'module': module} if module else {},
        )

    def service_plan_activate(
            self,
            plan_id,
        ) -> Dict:
        """Activate Service Plan

        API Method: uber.service_plan_activate

        This method is used to activate a service plan.

        Args:
            plan_id: Service Plan ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_activate',
            plan_id=plan_id,
        )

    def service_plan_add(
            self,
            code,
            title,
            allow_quotes=None,
            api_include=None,
            auto_cancel=None,
            auto_charge=None,
            auto_prorate=None,
            auto_suspend=None,
            bill_prior=None,
            bill_type=None,
            category=None,
            class_id=None,
            default_quantity=None,
            hide_upgrades=None,
            i18n=None,
            period=None,
            plan_data=None,
            post_renew=None,
            pricing=None,
            qbaccount=None,
            setup_qs=None,
            tax_situs_code=None,
            tax_situs_code_world=None,
            tax_trans_type_code=None,
            taxes=None,
            welcome_body=None,
            welcome_email_from=None,
            welcome_send=None,
            welcome_subject=None,
            zero_invoice=None,
        ) -> Dict:
        """Add Service Plan

        API Method: uber.service_plan_add

        This method is used to add a new service plan.

        Args:
            code: Service Plan Code,
            title: Service Plan Title,
            allow_quotes: Allow Quoting. Defaults to None.
            api_include: Include in API. Defaults to None.
            auto_cancel: Auto Cancel. Defaults to None.
            auto_charge: Automatically Charge. Defaults to None.
            auto_prorate: Automatically Prorate. Defaults to None.
            auto_suspend: Auto Suspend. Defaults to None.
            bill_prior: Bill in Advance. Defaults to None.
            bill_type: Default Billing Type. Defaults to None.
            category: Category. Defaults to None.
            class_id: Brand ID. Defaults to None.
            default_quantity: Default Quantity. Defaults to None.
            hide_upgrades: Hide Upgrades. Defaults to None.
            i18n: Internationalization. Defaults to None.
            period: Default Billing Period. Defaults to None.
            plan_data: Data. Defaults to None.
            post_renew: Post Renew. Defaults to None.
            pricing: Pricing. Defaults to None.
            qbaccount: Quickbooks Account. Defaults to None.
            setup_qs: Setup Quantity Sensitive. Defaults to None.
            tax_situs_code: Tax Situs Rule Code (US/Canada). Defaults to None.
            tax_situs_code_world: Tax Situs Rule Code (Non US/Canada). Defaults to None.
            tax_trans_type_code: Tax Transaction Type Code. Defaults to None.
            taxes: Taxes. Defaults to None.
            welcome_body: Welcome Letter Body. Defaults to None.
            welcome_email_from: Welcome Letter From. Defaults to None.
            welcome_send: Send Welcome Letter. Defaults to None.
            welcome_subject: Welcome Letter Subject. Defaults to None.
            zero_invoice: Invoice when Zero. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_add',
            code=code,
            title=title,
            **{'allow_quotes': allow_quotes} if allow_quotes else {},
            **{'api_include': api_include} if api_include else {},
            **{'auto_cancel': auto_cancel} if auto_cancel else {},
            **{'auto_charge': auto_charge} if auto_charge else {},
            **{'auto_prorate': auto_prorate} if auto_prorate else {},
            **{'auto_suspend': auto_suspend} if auto_suspend else {},
            **{'bill_prior': bill_prior} if bill_prior else {},
            **{'bill_type': bill_type} if bill_type else {},
            **{'category': category} if category else {},
            **{'class_id': class_id} if class_id else {},
            **{'default_quantity': default_quantity} if default_quantity else {},
            **{'hide_upgrades': hide_upgrades} if hide_upgrades else {},
            **{'i18n': i18n} if i18n else {},
            **{'period': period} if period else {},
            **{'plan_data': plan_data} if plan_data else {},
            **{'post_renew': post_renew} if post_renew else {},
            **{'pricing': pricing} if pricing else {},
            **{'qbaccount': qbaccount} if qbaccount else {},
            **{'setup_qs': setup_qs} if setup_qs else {},
            **{'tax_situs_code': tax_situs_code} if tax_situs_code else {},
            **{'tax_situs_code_world': tax_situs_code_world} if tax_situs_code_world else {},
            **{'tax_trans_type_code': tax_trans_type_code} if tax_trans_type_code else {},
            **{'taxes': taxes} if taxes else {},
            **{'welcome_body': welcome_body} if welcome_body else {},
            **{'welcome_email_from': welcome_email_from} if welcome_email_from else {},
            **{'welcome_send': welcome_send} if welcome_send else {},
            **{'welcome_subject': welcome_subject} if welcome_subject else {},
            **{'zero_invoice': zero_invoice} if zero_invoice else {},
        )

    def service_plan_copy(
            self,
            code,
            plan_id,
            title,
            class_id=None,
            i18n=None,
        ) -> Dict:
        """Copy Service Plan

        API Method: uber.service_plan_copy

        This method is used to copy a service plan to a new service plan.

        Args:
            code: Service Plan Code,
            plan_id: Service Plan ID,
            title: Service Plan Title,
            class_id: Brand ID. Defaults to None.
            i18n: Internationalization. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_copy',
            code=code,
            plan_id=plan_id,
            title=title,
            **{'class_id': class_id} if class_id else {},
            **{'i18n': i18n} if i18n else {},
        )

    def service_plan_deactivate(
            self,
            plan_id,
        ) -> Dict:
        """Deactivate Service Plan

        API Method: uber.service_plan_deactivate

        This method is used to deactivate a service plan.

        Args:
            plan_id: Service Plan ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_deactivate',
            plan_id=plan_id,
        )

    def service_plan_get(
            self,
            plan_id,
        ) -> Dict:
        """Get Service Plan Details

        API Method: uber.service_plan_get

        This method is used to get the details of a specified service plan.

        Args:
            plan_id: Service Plan ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_get',
            plan_id=plan_id,
        )

    def service_plan_list(
            self,
            active=None,
            brand_id=None,
            code=None,
            direction=None,
            limit=None,
            offset=None,
            order_by=None,
            qblistid=None,
        ) -> Dict:
        """List Service Plans

        API Method: uber.service_plan_list

        This method is used to get a list of service plans.

        Args:
            active: Active. Defaults to None.
            brand_id: Brand ID. Defaults to None.
            code: Service Plan Code. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            qblistid: Quick Book List ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_list',
            **{'active': active} if active else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'code': code} if code else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'qblistid': qblistid} if qblistid else {},
        )

    def service_plan_metadata_list(
            self,
            plan_id,
        ) -> Dict:
        """List Service Plan Default Custom Fields

        API Method: uber.service_plan_metadata_list

        This method is used to list an existing service plan's default custom fields.

        Args:
            plan_id: Service Plan ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_metadata_list',
            plan_id=plan_id,
        )

    def service_plan_metadata_update(
            self,
            plan_id,
            metadata=None,
            metadata_applicable=None,
        ) -> Dict:
        """Update Service Plan Custom Fields

        API Method: uber.service_plan_metadata_update

        This method is used to update an existing service plan's default custom fields.

        Args:
            plan_id: Service Plan ID,
            metadata: Custom Fields. Defaults to None.
            metadata_applicable: Applicable Custom Fields. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_metadata_update',
            plan_id=plan_id,
            **{'metadata': metadata} if metadata else {},
            **{'metadata_applicable': metadata_applicable} if metadata_applicable else {},
        )

    def service_plan_module_add(
            self,
            enabled,
            module,
            plan_id,
            client_access=None,
            config=None,
        ) -> Dict:
        """Add Service Plan Service Module

        API Method: uber.service_plan_module_add

        This method is used to add a service module to an existing service plan.

        Args:
            enabled: Enabled,
            module: Module,
            plan_id: Service Plan ID,
            client_access: Client Access. Defaults to None.
            config: Config. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_module_add',
            enabled=enabled,
            module=module,
            plan_id=plan_id,
            **{'client_access': client_access} if client_access else {},
            **{'config': config} if config else {},
        )

    def service_plan_module_delete(
            self,
            plan_id,
            service_module_id,
        ) -> Dict:
        """Delete Service Plan Service Module

        API Method: uber.service_plan_module_delete

        This method is used to delete a service module from an existing service plan.

        Args:
            plan_id: Service Plan ID,
            service_module_id: Service Module ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_module_delete',
            plan_id=plan_id,
            service_module_id=service_module_id,
        )

    def service_plan_module_list(
            self,
            plan_id,
        ) -> Dict:
        """List Service Plan Service Modules

        API Method: uber.service_plan_module_list

        This method is used to list an existing service plan's service modules.

        Args:
            plan_id: Service Plan ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_module_list',
            plan_id=plan_id,
        )

    def service_plan_module_update(
            self,
            plan_id,
            service_module_id,
            client_access=None,
            config=None,
            enabled=None,
            module=None,
        ) -> Dict:
        """Update Service Plan Service Module

        API Method: uber.service_plan_module_update

        This method is used to update a service module on an existing service plan.

        Args:
            plan_id: Service Plan ID,
            service_module_id: Service Module ID,
            client_access: Client Access. Defaults to None.
            config: Config. Defaults to None.
            enabled: Enabled. Defaults to None.
            module: Module. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_module_update',
            plan_id=plan_id,
            service_module_id=service_module_id,
            **{'client_access': client_access} if client_access else {},
            **{'config': config} if config else {},
            **{'enabled': enabled} if enabled else {},
            **{'module': module} if module else {},
        )

    def service_plan_note_add(
            self,
            note,
            plan_id,
        ) -> Dict:
        """Add a New Service Plan Note

        API Method: uber.service_plan_note_add

        This method is used to add a service plan note.

        Args:
            note: Note Text,
            plan_id: Service Plan ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_note_add',
            note=note,
            plan_id=plan_id,
        )

    def service_plan_note_delete(
            self,
            note_id,
        ) -> Dict:
        """Delete a Service Plan Note

        API Method: uber.service_plan_note_delete

        This method is used to delete a service plan note.

        Args:
            note_id: Note ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_note_delete',
            note_id=note_id,
        )

    def service_plan_note_list(
            self,
            plan_id,
        ) -> Dict:
        """List Service Plan Notes

        API Method: uber.service_plan_note_list

        This method is used to list a service plan's notes.

        Args:
            plan_id: Service Plan ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_note_list',
            plan_id=plan_id,
        )

    def service_plan_note_update(
            self,
            note,
            note_id,
        ) -> Dict:
        """Update a Service Plan Note

        API Method: uber.service_plan_note_update

        This method is used to update a service plan note.

        Args:
            note: Note Text,
            note_id: Note ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_note_update',
            note=note,
            note_id=note_id,
        )

    def service_plan_update(
            self,
            plan_id,
            allow_quotes=None,
            api_include=None,
            auto_cancel=None,
            auto_charge=None,
            auto_prorate=None,
            auto_suspend=None,
            bill_prior=None,
            bill_type=None,
            category=None,
            code=None,
            default_quantity=None,
            hide_upgrades=None,
            i18n=None,
            period=None,
            post_renew=None,
            pricing=None,
            qbaccount=None,
            setup_qs=None,
            tax_situs_code=None,
            tax_situs_code_world=None,
            tax_trans_type_code=None,
            taxes=None,
            title=None,
            welcome_body=None,
            welcome_email_from=None,
            welcome_send=None,
            welcome_subject=None,
            zero_invoice=None,
        ) -> Dict:
        """Edit Service Plan

        API Method: uber.service_plan_update

        This method is used to update an existing service plan.

        Args:
            plan_id: Service Plan ID,
            allow_quotes: Allow Quoting. Defaults to None.
            api_include: Include in API. Defaults to None.
            auto_cancel: Auto Cancel. Defaults to None.
            auto_charge: Automatically Charge. Defaults to None.
            auto_prorate: Automatically Prorate. Defaults to None.
            auto_suspend: Auto Suspend. Defaults to None.
            bill_prior: Bill in Advance. Defaults to None.
            bill_type: Default Billing Type. Defaults to None.
            category: Category. Defaults to None.
            code: Service Plan Code. Defaults to None.
            default_quantity: Default Quantity. Defaults to None.
            hide_upgrades: Hide Upgrades. Defaults to None.
            i18n: Internationalization. Defaults to None.
            period: Default Billing Period. Defaults to None.
            post_renew: Post Renew. Defaults to None.
            pricing: Pricing. Defaults to None.
            qbaccount: Quickbooks Account. Defaults to None.
            setup_qs: Setup Quantity Sensitive. Defaults to None.
            tax_situs_code: Tax Situs Rule Code (US/Canada). Defaults to None.
            tax_situs_code_world: Tax Situs Rule Code (Non US/Canada). Defaults to None.
            tax_trans_type_code: Tax Transaction Type Code. Defaults to None.
            taxes: Taxes. Defaults to None.
            title: Service Plan Title. Defaults to None.
            welcome_body: Welcome Letter Body. Defaults to None.
            welcome_email_from: Welcome Letter From. Defaults to None.
            welcome_send: Send Welcome Letter. Defaults to None.
            welcome_subject: Welcome Letter Subject. Defaults to None.
            zero_invoice: Invoice when Zero. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.service_plan_update',
            plan_id=plan_id,
            **{'allow_quotes': allow_quotes} if allow_quotes else {},
            **{'api_include': api_include} if api_include else {},
            **{'auto_cancel': auto_cancel} if auto_cancel else {},
            **{'auto_charge': auto_charge} if auto_charge else {},
            **{'auto_prorate': auto_prorate} if auto_prorate else {},
            **{'auto_suspend': auto_suspend} if auto_suspend else {},
            **{'bill_prior': bill_prior} if bill_prior else {},
            **{'bill_type': bill_type} if bill_type else {},
            **{'category': category} if category else {},
            **{'code': code} if code else {},
            **{'default_quantity': default_quantity} if default_quantity else {},
            **{'hide_upgrades': hide_upgrades} if hide_upgrades else {},
            **{'i18n': i18n} if i18n else {},
            **{'period': period} if period else {},
            **{'post_renew': post_renew} if post_renew else {},
            **{'pricing': pricing} if pricing else {},
            **{'qbaccount': qbaccount} if qbaccount else {},
            **{'setup_qs': setup_qs} if setup_qs else {},
            **{'tax_situs_code': tax_situs_code} if tax_situs_code else {},
            **{'tax_situs_code_world': tax_situs_code_world} if tax_situs_code_world else {},
            **{'tax_trans_type_code': tax_trans_type_code} if tax_trans_type_code else {},
            **{'taxes': taxes} if taxes else {},
            **{'title': title} if title else {},
            **{'welcome_body': welcome_body} if welcome_body else {},
            **{'welcome_email_from': welcome_email_from} if welcome_email_from else {},
            **{'welcome_send': welcome_send} if welcome_send else {},
            **{'welcome_subject': welcome_subject} if welcome_subject else {},
            **{'zero_invoice': zero_invoice} if zero_invoice else {},
        )

    def system_info(
            self,
        ) -> Dict:
        """System Information

        API Method: uber.system_info

        This method is used to list system information.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.system_info',
        )

    def tax_authority_number_add(
            self,
            brand_id,
            tax_number,
            tax_number_label,
            show_on_invoice=None,
        ) -> Dict:
        """Add Tax Authority Number 

        API Method: uber.tax_authority_number_add

        This method is used to add a tax authority number

        Args:
            brand_id: Brand ID,
            tax_number: Tax Authority Number,
            tax_number_label: Label,
            show_on_invoice: Show on Invoices. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.tax_authority_number_add',
            brand_id=brand_id,
            tax_number=tax_number,
            tax_number_label=tax_number_label,
            **{'show_on_invoice': show_on_invoice} if show_on_invoice else {},
        )

    def tax_authority_number_delete(
            self,
            tax_number_id,
        ) -> Dict:
        """Delete Tax Authority Number 

        API Method: uber.tax_authority_number_delete

        This method is used to delete a tax authority number. The association related to any tax rate will also be removed

        Args:
            tax_number_id: Tax Authority Number ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.tax_authority_number_delete',
            tax_number_id=tax_number_id,
        )

    def tax_authority_number_list(
            self,
            brand_id,
        ) -> Dict:
        """List all Tax Authority Numbers associated with a brand

        API Method: uber.tax_authority_number_list

        This method is used to list all tax authority numbers for a given brand.

        Args:
            brand_id: Brand ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.tax_authority_number_list',
            brand_id=brand_id,
        )

    def tax_authority_number_update(
            self,
            tax_number_id,
            show_on_invoice=None,
            tax_number=None,
            tax_number_label=None,
        ) -> Dict:
        """Update Tax Authority Number 

        API Method: uber.tax_authority_number_update

        This method is used to update a tax authority number

        Args:
            tax_number_id: Tax Authority Number ID,
            show_on_invoice: Show on Invoices. Defaults to None.
            tax_number: Tax Authority Number. Defaults to None.
            tax_number_label: Label. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.tax_authority_number_update',
            tax_number_id=tax_number_id,
            **{'show_on_invoice': show_on_invoice} if show_on_invoice else {},
            **{'tax_number': tax_number} if tax_number else {},
            **{'tax_number_label': tax_number_label} if tax_number_label else {},
        )

    def tax_engine_list(
            self,
            description=None,
            direction=None,
            limit=None,
            offset=None,
            order_by=None,
            status=None,
            type=None,
        ) -> Dict:
        """List Tax Engines

        API Method: uber.tax_engine_list

        This method is used to list the configured tax engines.

        Args:
            description: Description. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            status: Status. Defaults to None.
            type: Type. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.tax_engine_list',
            **{'description': description} if description else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'status': status} if status else {},
            **{'type': type} if type else {},
        )

    def tax_exemption_type_get(
            self,
            tax_exemption_type_id,
        ) -> Dict:
        """Get a Tax Exemption Type

        API Method: uber.tax_exemption_type_get

        This method is used to get a tax exemption type.

        Args:
            tax_exemption_type_id: Tax Exemption Type ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.tax_exemption_type_get',
            tax_exemption_type_id=tax_exemption_type_id,
        )

    def tax_exemption_type_list(
            self,
            code=None,
            code_engine=None,
            direction=None,
            limit=None,
            name=None,
            offset=None,
            order_by=None,
            status=None,
        ) -> Dict:
        """List Tax Exemption Types

        API Method: uber.tax_exemption_type_list

        This method is used to list tax exemption types.

        Args:
            code: Ubersmith Code. Defaults to None.
            code_engine: Tax Engine Code. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            name: Name. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.tax_exemption_type_list',
            **{'code': code} if code else {},
            **{'code_engine': code_engine} if code_engine else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'name': name} if name else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'status': status} if status else {},
        )

    def tax_rate_add(
            self,
            brand_id,
            name,
            rate,
            code_engine=None,
            i18n=None,
            include_other=None,
            tax_number_ids=None,
        ) -> Dict:
        """Add Tax Rate

        API Method: uber.tax_rate_add

        This method is used to add a tax rate

        Args:
            brand_id: Brand ID,
            name: Name,
            rate: Tax Rate,
            code_engine: Tax Engine Code. Defaults to None.
            i18n: Internationalization. Defaults to None.
            include_other: Include other taxes. Defaults to None.
            tax_number_ids: Tax Numbers IDs. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.tax_rate_add',
            brand_id=brand_id,
            name=name,
            rate=rate,
            **{'code_engine': code_engine} if code_engine else {},
            **{'i18n': i18n} if i18n else {},
            **{'include_other': include_other} if include_other else {},
            **{'tax_number_ids': tax_number_ids} if tax_number_ids else {},
        )

    def tax_rate_get(
            self,
            tax_id,
        ) -> Dict:
        """Get Tax Rate Details

        API Method: uber.tax_rate_get

        This method is used to get a tax rate's details

        Args:
            tax_id: Tax id,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.tax_rate_get',
            tax_id=tax_id,
        )

    def tax_rate_list(
            self,
            active=None,
            brand_id=None,
            direction=None,
            ids=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List Tax Rates

        API Method: uber.tax_rate_list

        This method is used to list the tax rates in the system.

        Args:
            active: Active Flag. Defaults to None.
            brand_id: Brand id. Defaults to None.
            direction: Direction. Defaults to None.
            ids: list of id, eg: &ids[]=1&ids[]=5. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order by. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.tax_rate_list',
            **{'active': active} if active else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'direction': direction} if direction else {},
            **{'ids': ids} if ids else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def tax_rate_update(
            self,
            tax_id,
            active=None,
            code_engine=None,
            i18n=None,
            include_other=None,
            name=None,
            rate=None,
            tax_number_ids=None,
        ) -> Dict:
        """Edit Tax Rate Details

        API Method: uber.tax_rate_update

        This method is used to edit a tax rate's details

        Args:
            tax_id: Tax ID,
            active: Active. Defaults to None.
            code_engine: Tax Engine Code. Defaults to None.
            i18n: Internationalization. Defaults to None.
            include_other: Include other taxes. Defaults to None.
            name: Name. Defaults to None.
            rate: Tax Rate. Defaults to None.
            tax_number_ids: Tax Numbers IDs. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.tax_rate_update',
            tax_id=tax_id,
            **{'active': active} if active else {},
            **{'code_engine': code_engine} if code_engine else {},
            **{'i18n': i18n} if i18n else {},
            **{'include_other': include_other} if include_other else {},
            **{'name': name} if name else {},
            **{'rate': rate} if rate else {},
            **{'tax_number_ids': tax_number_ids} if tax_number_ids else {},
        )

    def user_exists(
            self,
            user_login=None,
        ) -> Dict:
        """Check whether a Client Exists

        API Method: uber.user_exists

        This method is used to check if a given login name or client id corresponds to an existing client.

        Args:
            user_login: Client Login. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.user_exists',
            **{'user_login': user_login} if user_login else {},
        )

    def username_exists(
            self,
            username,
        ) -> Dict:
        """Check Whether a Username Exists

        API Method: uber.username_exists

        This method is used to check whether the specified username exists in the system.

        Args:
            username: Username,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'uber.username_exists',
            username=username,
        )
