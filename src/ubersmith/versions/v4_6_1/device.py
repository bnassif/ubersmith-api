from typing import Dict
from ubersmith.client.section import *

class DeviceAPI(Section):
    """
    Auto-generated section for ``device``.

    Contains all ``device.*`` API methods.
    """

    def add(
            self,
            dev_desc,
            type_id,
            back_image=None,
            back_image_file_id=None,
            client_id=None,
            client_owned=None,
            connection_node_type_id=None,
            front_image=None,
            front_image_file_id=None,
            height=None,
            label=None,
            meta=None,
            parent=None,
            rack_id=None,
            rack_pos=None,
            service_id=None,
        ) -> Dict:
        """Add a New Device

        API Method: device.add

        This method is used to create a new device.

        Args:
            dev_desc: Device Description,
            type_id: Device Type ID,
            back_image: Attachment. Defaults to None.
            back_image_file_id: Back Image File ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            client_owned: Client Owns Physical Device. Defaults to None.
            connection_node_type_id: Connection Node Type ID. Defaults to None.
            front_image: Attachment. Defaults to None.
            front_image_file_id: Front Image File ID. Defaults to None.
            height: Device Height. Defaults to None.
            label: Device Label. Defaults to None.
            meta: Custom Fields. Defaults to None.
            parent: Parent Device ID. Defaults to None.
            rack_id: Rack ID. Defaults to None.
            rack_pos: Position Within Rack. Defaults to None.
            service_id: Service ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.add',
            dev_desc=dev_desc,
            type_id=type_id,
            **{'back_image': back_image} if back_image else {},
            **{'back_image_file_id': back_image_file_id} if back_image_file_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'client_owned': client_owned} if client_owned else {},
            **{'connection_node_type_id': connection_node_type_id} if connection_node_type_id else {},
            **{'front_image': front_image} if front_image else {},
            **{'front_image_file_id': front_image_file_id} if front_image_file_id else {},
            **{'height': height} if height else {},
            **{'label': label} if label else {},
            **{'meta': meta} if meta else {},
            **{'parent': parent} if parent else {},
            **{'rack_id': rack_id} if rack_id else {},
            **{'rack_pos': rack_pos} if rack_pos else {},
            **{'service_id': service_id} if service_id else {},
        )

    def cage_add(
            self,
            zone_id,
            ac_power_capacity=None,
            area_display_value=None,
            assigned_date=None,
            cage_code=None,
            cage_name=None,
            cage_type=None,
            client_id=None,
            dc_power_capacity=None,
            depth_display_unit=None,
            depth_display_value=None,
            meta_=None,
            rofr_expiration_date=None,
            status=None,
            width_display_unit=None,
            width_display_value=None,
        ) -> Dict:
        """Add a cage

        API Method: device.cage_add

        This method is used to add a cage in the system.

        Args:
            zone_id: Zone ID,
            ac_power_capacity: AC Power Capacity. Defaults to None.
            area_display_value: Area Size Value. Defaults to None.
            assigned_date: Assigned Date. Defaults to None.
            cage_code: Cage Code. Defaults to None.
            cage_name: Cage Name. Defaults to None.
            cage_type: Cage Type. Defaults to None.
            client_id: Client ID. Defaults to None.
            dc_power_capacity: DC Power Capacity. Defaults to None.
            depth_display_unit: Depth Unit. Defaults to None.
            depth_display_value: Depth Value. Defaults to None.
            meta_: Custom Fields. Defaults to None.
            rofr_expiration_date: ROFR Expiration Date. Defaults to None.
            status: Status. Defaults to None.
            width_display_unit: Width Unit. Defaults to None.
            width_display_value: Width Value. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.cage_add',
            zone_id=zone_id,
            **{'ac_power_capacity': ac_power_capacity} if ac_power_capacity else {},
            **{'area_display_value': area_display_value} if area_display_value else {},
            **{'assigned_date': assigned_date} if assigned_date else {},
            **{'cage_code': cage_code} if cage_code else {},
            **{'cage_name': cage_name} if cage_name else {},
            **{'cage_type': cage_type} if cage_type else {},
            **{'client_id': client_id} if client_id else {},
            **{'dc_power_capacity': dc_power_capacity} if dc_power_capacity else {},
            **{'depth_display_unit': depth_display_unit} if depth_display_unit else {},
            **{'depth_display_value': depth_display_value} if depth_display_value else {},
            **{'meta_': meta_} if meta_ else {},
            **{'rofr_expiration_date': rofr_expiration_date} if rofr_expiration_date else {},
            **{'status': status} if status else {},
            **{'width_display_unit': width_display_unit} if width_display_unit else {},
            **{'width_display_value': width_display_value} if width_display_value else {},
        )

    def cage_list(
            self,
            cage_code=None,
            cage_id=None,
            client_id=None,
            exclude_downstream=None,
            fac_code=None,
            fac_id=None,
            metadata=None,
            rack_code=None,
            rack_id=None,
            row_code=None,
            row_id=None,
            zone_code=None,
            zone_id=None,
        ) -> Dict:
        """List Device Cages

        API Method: device.cage_list

        This method is used to list device cages.

        Args:
            cage_code: Cage Code. Defaults to None.
            cage_id: Cage ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            exclude_downstream: Exclude downstream. Defaults to None.
            fac_code: Facility Code. Defaults to None.
            fac_id: Facility ID. Defaults to None.
            metadata: Include Custom Fields. Defaults to None.
            rack_code: Rack Code. Defaults to None.
            rack_id: Rack ID. Defaults to None.
            row_code: Row Code. Defaults to None.
            row_id: Row ID. Defaults to None.
            zone_code: Zone Code. Defaults to None.
            zone_id: Zone ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.cage_list',
            **{'cage_code': cage_code} if cage_code else {},
            **{'cage_id': cage_id} if cage_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'exclude_downstream': exclude_downstream} if exclude_downstream else {},
            **{'fac_code': fac_code} if fac_code else {},
            **{'fac_id': fac_id} if fac_id else {},
            **{'metadata': metadata} if metadata else {},
            **{'rack_code': rack_code} if rack_code else {},
            **{'rack_id': rack_id} if rack_id else {},
            **{'row_code': row_code} if row_code else {},
            **{'row_id': row_id} if row_id else {},
            **{'zone_code': zone_code} if zone_code else {},
            **{'zone_id': zone_id} if zone_id else {},
        )

    def cage_update(
            self,
            cage_id,
            ac_power_capacity=None,
            area_display_value=None,
            assigned_date=None,
            cage_code=None,
            cage_name=None,
            cage_type=None,
            client_id=None,
            dc_power_capacity=None,
            depth_display_unit=None,
            depth_display_value=None,
            meta_=None,
            rofr_expiration_date=None,
            status=None,
            width_display_unit=None,
            width_display_value=None,
            zone_id=None,
        ) -> Dict:
        """Update a cage

        API Method: device.cage_update

        This method is used to update a cage in the system.

        Args:
            cage_id: Cage ID,
            ac_power_capacity: AC Power Capacity. Defaults to None.
            area_display_value: Area Size Value. Defaults to None.
            assigned_date: Assigned Date. Defaults to None.
            cage_code: Cage Code. Defaults to None.
            cage_name: Cage Name. Defaults to None.
            cage_type: Cage Type. Defaults to None.
            client_id: Client ID. Defaults to None.
            dc_power_capacity: DC Power Capacity. Defaults to None.
            depth_display_unit: Depth Unit. Defaults to None.
            depth_display_value: Depth Value. Defaults to None.
            meta_: Custom Fields. Defaults to None.
            rofr_expiration_date: ROFR Expiration Date. Defaults to None.
            status: Status. Defaults to None.
            width_display_unit: Width Unit. Defaults to None.
            width_display_value: Width Value. Defaults to None.
            zone_id: Zone ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.cage_update',
            cage_id=cage_id,
            **{'ac_power_capacity': ac_power_capacity} if ac_power_capacity else {},
            **{'area_display_value': area_display_value} if area_display_value else {},
            **{'assigned_date': assigned_date} if assigned_date else {},
            **{'cage_code': cage_code} if cage_code else {},
            **{'cage_name': cage_name} if cage_name else {},
            **{'cage_type': cage_type} if cage_type else {},
            **{'client_id': client_id} if client_id else {},
            **{'dc_power_capacity': dc_power_capacity} if dc_power_capacity else {},
            **{'depth_display_unit': depth_display_unit} if depth_display_unit else {},
            **{'depth_display_value': depth_display_value} if depth_display_value else {},
            **{'meta_': meta_} if meta_ else {},
            **{'rofr_expiration_date': rofr_expiration_date} if rofr_expiration_date else {},
            **{'status': status} if status else {},
            **{'width_display_unit': width_display_unit} if width_display_unit else {},
            **{'width_display_value': width_display_value} if width_display_value else {},
            **{'zone_id': zone_id} if zone_id else {},
        )

    def comment_list(
            self,
            device_id,
            client_viewable=None,
            direction=None,
            filter_text=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List a Device's Comments

        API Method: device.comment_list

        This method is used to list a device's comments.

        Args:
            device_id: Device ID,
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
            'device.comment_list',
            device_id=device_id,
            **{'client_viewable': client_viewable} if client_viewable else {},
            **{'direction': direction} if direction else {},
            **{'filter_text': filter_text} if filter_text else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def connection_add(
            self,
            links,
            name,
            connection_type_id=None,
            status=None,
        ) -> Dict:
        """Add a Device Connection

        API Method: device.connection_add

        This method is used to add a new Connection between Devices.

        Args:
            links: Links,
            name: Name,
            connection_type_id: Connection Type ID. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.connection_add',
            links=links,
            name=name,
            **{'connection_type_id': connection_type_id} if connection_type_id else {},
            **{'status': status} if status else {},
        )

    def connection_delete(
            self,
            connection_class_id=None,
            connection_id=None,
            device_id=None,
        ) -> Dict:
        """Delete a Device Connection

        API Method: device.connection_delete

        This method is used to remove Connections between Devices.

        Args:
            connection_class_id: Connection Class ID. Defaults to None.
            connection_id: Connection ID. Defaults to None.
            device_id: Device ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.connection_delete',
            **{'connection_class_id': connection_class_id} if connection_class_id else {},
            **{'connection_id': connection_id} if connection_id else {},
            **{'device_id': device_id} if device_id else {},
        )

    def connection_link_add(
            self,
            connection_id,
            name,
            segments,
        ) -> Dict:
        """Add a Connection Link

        API Method: device.connection_link_add

        This method is used to add a new Link within a Connection.

        Args:
            connection_id: Connection ID,
            name: Name,
            segments: Segments,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.connection_link_add',
            connection_id=connection_id,
            name=name,
            segments=segments,
        )

    def connection_link_list(
            self,
            connection_class_id=None,
            connection_id=None,
            device_id=None,
            dst_interface_id=None,
            src_interface_id=None,
            status=None,
            status_bit=None,
        ) -> Dict:
        """List Connection Links

        API Method: device.connection_link_list

        This method is used to list Connection Links.

        Args:
            connection_class_id: Connection Class ID. Defaults to None.
            connection_id: Connection ID. Defaults to None.
            device_id: Device ID. Defaults to None.
            dst_interface_id: Destination Interface. Defaults to None.
            src_interface_id: Source Interface. Defaults to None.
            status: Status. Defaults to None.
            status_bit: Status Bit. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.connection_link_list',
            **{'connection_class_id': connection_class_id} if connection_class_id else {},
            **{'connection_id': connection_id} if connection_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'dst_interface_id': dst_interface_id} if dst_interface_id else {},
            **{'src_interface_id': src_interface_id} if src_interface_id else {},
            **{'status': status} if status else {},
            **{'status_bit': status_bit} if status_bit else {},
        )

    def connection_link_update(
            self,
            connection_link_id,
            name=None,
            segments=None,
        ) -> Dict:
        """Update a Connection Link

        API Method: device.connection_link_update

        This method is used to update a Link within a Connection.

        Args:
            connection_link_id: Connection Link ID,
            name: Name. Defaults to None.
            segments: Segments. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.connection_link_update',
            connection_link_id=connection_link_id,
            **{'name': name} if name else {},
            **{'segments': segments} if segments else {},
        )

    def connection_list(
            self,
            connection_class_id=None,
            connection_id=None,
            device_id=None,
            dst_interface_id=None,
            src_interface_id=None,
            status=None,
            status_bit=None,
        ) -> Dict:
        """List Device Connections

        API Method: device.connection_list

        This method is used to list a device's Connections.

        Args:
            connection_class_id: Connection Class ID. Defaults to None.
            connection_id: Connection ID. Defaults to None.
            device_id: Device ID. Defaults to None.
            dst_interface_id: Destination Interface. Defaults to None.
            src_interface_id: Source Interface. Defaults to None.
            status: Status. Defaults to None.
            status_bit: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.connection_list',
            **{'connection_class_id': connection_class_id} if connection_class_id else {},
            **{'connection_id': connection_id} if connection_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'dst_interface_id': dst_interface_id} if dst_interface_id else {},
            **{'src_interface_id': src_interface_id} if src_interface_id else {},
            **{'status': status} if status else {},
            **{'status_bit': status_bit} if status_bit else {},
        )

    def connection_node_type_list(
            self,
        ) -> Dict:
        """List Connection Node Types

        API Method: device.connection_node_type_list

        This method is used to list available connection node types.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.connection_node_type_list',
        )

    def connection_type_add(
            self,
            code,
            connection_class_id,
            name,
            description=None,
            status=None,
        ) -> Dict:
        """Add a Connection Type

        API Method: device.connection_type_add

        Adds a new connection type

        Args:
            code: Code,
            connection_class_id: Connection Class ID,
            name: Name,
            description: Description. Defaults to None.
            status: Status ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.connection_type_add',
            code=code,
            connection_class_id=connection_class_id,
            name=name,
            **{'description': description} if description else {},
            **{'status': status} if status else {},
        )

    def connection_type_list(
            self,
            connection_class_id=None,
        ) -> Dict:
        """List Connection Types

        API Method: device.connection_type_list

        This method is used to list available connection types.

        Args:
            connection_class_id: Connection Class ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.connection_type_list',
            **{'connection_class_id': connection_class_id} if connection_class_id else {},
        )

    def connection_update(
            self,
            connection_id,
            name=None,
            status=None,
        ) -> Dict:
        """Update a Device Connection

        API Method: device.connection_update

        This method is used to update a Connection between Devices.

        Args:
            connection_id: Connection ID,
            name: Name. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.connection_update',
            connection_id=connection_id,
            **{'name': name} if name else {},
            **{'status': status} if status else {},
        )

    def cpanel_add(
            self,
            service_id,
            cpanel_plan=None,
            create=None,
        ) -> Dict:
        """Add a cPanel Account

        API Method: device.cpanel_add

        This method is used to add a cPanel account.

        Args:
            service_id: Service ID,
            cpanel_plan: cPanel Plan Code. Defaults to None.
            create: Create Flag. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.cpanel_add',
            service_id=service_id,
            **{'cpanel_plan': cpanel_plan} if cpanel_plan else {},
            **{'create': create} if create else {},
        )

    def delete(
            self,
            device_id,
            force_delete_connections=None,
        ) -> Dict:
        """Delete a Device

        API Method: device.delete

        This method is used to delete a device.

        Args:
            device_id: Device ID,
            force_delete_connections: Allow deleting a device that has connections. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.delete',
            device_id=device_id,
            **{'force_delete_connections': force_delete_connections} if force_delete_connections else {},
        )

    def dns_record_add(
            self,
            content,
            name,
            type,
            zone_id,
            disabled=None,
            prio=None,
            ttl=None,
        ) -> Dict:
        """Add a DNS record

        API Method: device.dns_record_add

        This method is used to add a new DNS record to a DNS Zone.

        Args:
            content: Record Content,
            name: Record Name,
            type: Record Type,
            zone_id: Zone ID,
            disabled: Record Status. Defaults to None.
            prio: Priority. Defaults to None.
            ttl: TTL. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.dns_record_add',
            content=content,
            name=name,
            type=type,
            zone_id=zone_id,
            **{'disabled': disabled} if disabled else {},
            **{'prio': prio} if prio else {},
            **{'ttl': ttl} if ttl else {},
        )

    def dns_record_delete(
            self,
            record_id,
        ) -> Dict:
        """Delete a DNS Record

        API Method: device.dns_record_delete

        This method is used to delete a DNS Record.

        Args:
            record_id: Record ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.dns_record_delete',
            record_id=record_id,
        )

    def dns_record_list(
            self,
            client_id=None,
            content=None,
            direction=None,
            disabled=None,
            exclude_special=None,
            limit=None,
            name=None,
            offset=None,
            order_by=None,
            record_id=None,
            service_id=None,
            type=None,
            zone_id=None,
            zone_name=None,
        ) -> Dict:
        """List DNS records

        API Method: device.dns_record_list

        This method is used to list DNS records.

        Args:
            client_id: Client ID. Defaults to None.
            content: Record Content. Defaults to None.
            direction: Direction. Defaults to None.
            disabled: Record Status. Defaults to None.
            exclude_special: Exclude Special Records. Defaults to None.
            limit: Limit. Defaults to None.
            name: Record Name. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            record_id: Record ID. Defaults to None.
            service_id: Service ID. Defaults to None.
            type: Record Type. Defaults to None.
            zone_id: Zone ID. Defaults to None.
            zone_name: Zone Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.dns_record_list',
            **{'client_id': client_id} if client_id else {},
            **{'content': content} if content else {},
            **{'direction': direction} if direction else {},
            **{'disabled': disabled} if disabled else {},
            **{'exclude_special': exclude_special} if exclude_special else {},
            **{'limit': limit} if limit else {},
            **{'name': name} if name else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'record_id': record_id} if record_id else {},
            **{'service_id': service_id} if service_id else {},
            **{'type': type} if type else {},
            **{'zone_id': zone_id} if zone_id else {},
            **{'zone_name': zone_name} if zone_name else {},
        )

    def dns_record_update(
            self,
            record_id,
            content=None,
            disabled=None,
            name=None,
            prio=None,
            ttl=None,
            type=None,
        ) -> Dict:
        """Update a DNS record

        API Method: device.dns_record_update

        This method is used to update a DNS record.

        Args:
            record_id: Record ID,
            content: Record Content. Defaults to None.
            disabled: Record Status. Defaults to None.
            name: Record Name. Defaults to None.
            prio: Priority. Defaults to None.
            ttl: TTL. Defaults to None.
            type: Record Type. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.dns_record_update',
            record_id=record_id,
            **{'content': content} if content else {},
            **{'disabled': disabled} if disabled else {},
            **{'name': name} if name else {},
            **{'prio': prio} if prio else {},
            **{'ttl': ttl} if ttl else {},
            **{'type': type} if type else {},
        )

    def dns_zone_add(
            self,
            name,
            client_id=None,
            default_ttl=None,
            expire=None,
            hostmaster=None,
            ns1=None,
            ns2=None,
            ns3=None,
            ns4=None,
            refresh=None,
            retry=None,
            service_id=None,
        ) -> Dict:
        """Add a DNS Zone

        API Method: device.dns_zone_add

        This method is used to add a new DNS Zone

        Args:
            name: Domain Name,
            client_id: Client ID. Defaults to None.
            default_ttl: Default TTL. Defaults to None.
            expire: Expire Interval. Defaults to None.
            hostmaster: Hostmaster. Defaults to None.
            ns1: Primary Nameserver. Defaults to None.
            ns2: Secondary Nameserver. Defaults to None.
            ns3: Tertiary Nameserver. Defaults to None.
            ns4: Quaternary Nameserver. Defaults to None.
            refresh: Refresh Interval. Defaults to None.
            retry: Retry Interval. Defaults to None.
            service_id: Service ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.dns_zone_add',
            name=name,
            **{'client_id': client_id} if client_id else {},
            **{'default_ttl': default_ttl} if default_ttl else {},
            **{'expire': expire} if expire else {},
            **{'hostmaster': hostmaster} if hostmaster else {},
            **{'ns1': ns1} if ns1 else {},
            **{'ns2': ns2} if ns2 else {},
            **{'ns3': ns3} if ns3 else {},
            **{'ns4': ns4} if ns4 else {},
            **{'refresh': refresh} if refresh else {},
            **{'retry': retry} if retry else {},
            **{'service_id': service_id} if service_id else {},
        )

    def dns_zone_delete(
            self,
            zone_id,
        ) -> Dict:
        """Delete a DNS Zone

        API Method: device.dns_zone_delete

        This method is used to delete a DNS Zone.

        Args:
            zone_id: Zone ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.dns_zone_delete',
            zone_id=zone_id,
        )

    def dns_zone_list(
            self,
            client_id=None,
            direction=None,
            limit=None,
            name=None,
            offset=None,
            order_by=None,
            service_id=None,
            zone_id=None,
        ) -> Dict:
        """List DNS Zones

        API Method: device.dns_zone_list

        This method is used to list DNS Zones.

        Args:
            client_id: Client ID. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            name: Zone Name. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            service_id: Service ID. Defaults to None.
            zone_id: Zone ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.dns_zone_list',
            **{'client_id': client_id} if client_id else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'name': name} if name else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'service_id': service_id} if service_id else {},
            **{'zone_id': zone_id} if zone_id else {},
        )

    def dns_zone_update(
            self,
            zone_id,
            client_id=None,
            default_ttl=None,
            expire=None,
            hostmaster=None,
            name=None,
            refresh=None,
            retry=None,
            service_id=None,
        ) -> Dict:
        """Update a DNS Zone

        API Method: device.dns_zone_update

        This method is used to update a DNS Zone.

        Args:
            zone_id: Zone ID,
            client_id: Client ID. Defaults to None.
            default_ttl: Default TTL. Defaults to None.
            expire: Expire Interval. Defaults to None.
            hostmaster: Hostmaster. Defaults to None.
            name: Domain Name. Defaults to None.
            refresh: Refresh Interval. Defaults to None.
            retry: Retry Interval. Defaults to None.
            service_id: Service ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.dns_zone_update',
            zone_id=zone_id,
            **{'client_id': client_id} if client_id else {},
            **{'default_ttl': default_ttl} if default_ttl else {},
            **{'expire': expire} if expire else {},
            **{'hostmaster': hostmaster} if hostmaster else {},
            **{'name': name} if name else {},
            **{'refresh': refresh} if refresh else {},
            **{'retry': retry} if retry else {},
            **{'service_id': service_id} if service_id else {},
        )

    def event_list(
            self,
            device_id,
            begin=None,
            direction=None,
            end=None,
            eventuser=None,
            limit=None,
            offset=None,
            order_by=None,
            searchfor=None,
        ) -> Dict:
        """List Device Events

        API Method: device.event_list

        This method is used to list device events.

        Args:
            device_id: Device ID,
            begin: Start Date. Defaults to None.
            direction: Direction. Defaults to None.
            end: End Date. Defaults to None.
            eventuser: User. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            searchfor: Search String. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.event_list',
            device_id=device_id,
            **{'begin': begin} if begin else {},
            **{'direction': direction} if direction else {},
            **{'end': end} if end else {},
            **{'eventuser': eventuser} if eventuser else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'searchfor': searchfor} if searchfor else {},
        )

    def facility_add(
            self,
            ac_power_capacity=None,
            area_display_value=None,
            assigned_date=None,
            client_id=None,
            dc_power_capacity=None,
            fac_address=None,
            fac_address2=None,
            fac_city=None,
            fac_code=None,
            fac_country=None,
            fac_description=None,
            fac_name=None,
            fac_state=None,
            fac_zip=None,
            meta_=None,
            phone=None,
            provider_client_id=None,
            rofr_expiration_date=None,
            status=None,
        ) -> Dict:
        """Add a facility

        API Method: device.facility_add

        This method is used to add a facility in the system.

        Args:
            ac_power_capacity: AC Power Capacity. Defaults to None.
            area_display_value: Area Size Value. Defaults to None.
            assigned_date: Assigned Date. Defaults to None.
            client_id: Client ID. Defaults to None.
            dc_power_capacity: DC Power Capacity. Defaults to None.
            fac_address: Address. Defaults to None.
            fac_address2: Address 2. Defaults to None.
            fac_city: City. Defaults to None.
            fac_code: Facility Code. Defaults to None.
            fac_country: Country. Defaults to None.
            fac_description: Facility Description. Defaults to None.
            fac_name: Facility Name. Defaults to None.
            fac_state: State. Defaults to None.
            fac_zip: Postal code. Defaults to None.
            meta_: Custom Fields. Defaults to None.
            phone: Telephone. Defaults to None.
            provider_client_id: Provide Client Id. Defaults to None.
            rofr_expiration_date: ROFR Expiration Date. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.facility_add',
            **{'ac_power_capacity': ac_power_capacity} if ac_power_capacity else {},
            **{'area_display_value': area_display_value} if area_display_value else {},
            **{'assigned_date': assigned_date} if assigned_date else {},
            **{'client_id': client_id} if client_id else {},
            **{'dc_power_capacity': dc_power_capacity} if dc_power_capacity else {},
            **{'fac_address': fac_address} if fac_address else {},
            **{'fac_address2': fac_address2} if fac_address2 else {},
            **{'fac_city': fac_city} if fac_city else {},
            **{'fac_code': fac_code} if fac_code else {},
            **{'fac_country': fac_country} if fac_country else {},
            **{'fac_description': fac_description} if fac_description else {},
            **{'fac_name': fac_name} if fac_name else {},
            **{'fac_state': fac_state} if fac_state else {},
            **{'fac_zip': fac_zip} if fac_zip else {},
            **{'meta_': meta_} if meta_ else {},
            **{'phone': phone} if phone else {},
            **{'provider_client_id': provider_client_id} if provider_client_id else {},
            **{'rofr_expiration_date': rofr_expiration_date} if rofr_expiration_date else {},
            **{'status': status} if status else {},
        )

    def facility_list(
            self,
            cage_code=None,
            cage_id=None,
            client_id=None,
            exclude_downstream=None,
            fac_code=None,
            fac_id=None,
            metadata=None,
            rack_code=None,
            rack_id=None,
            row_code=None,
            row_id=None,
            zone_code=None,
            zone_id=None,
        ) -> Dict:
        """List Device Facilities

        API Method: device.facility_list

        This method is used to list device facilities.

        Args:
            cage_code: Cage Code. Defaults to None.
            cage_id: Cage ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            exclude_downstream: Exclude downstream. Defaults to None.
            fac_code: Facility Code. Defaults to None.
            fac_id: Facility ID. Defaults to None.
            metadata: Include Custom Fields. Defaults to None.
            rack_code: Rack Code. Defaults to None.
            rack_id: Rack ID. Defaults to None.
            row_code: Row Code. Defaults to None.
            row_id: Row ID. Defaults to None.
            zone_code: Zone Code. Defaults to None.
            zone_id: Zone ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.facility_list',
            **{'cage_code': cage_code} if cage_code else {},
            **{'cage_id': cage_id} if cage_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'exclude_downstream': exclude_downstream} if exclude_downstream else {},
            **{'fac_code': fac_code} if fac_code else {},
            **{'fac_id': fac_id} if fac_id else {},
            **{'metadata': metadata} if metadata else {},
            **{'rack_code': rack_code} if rack_code else {},
            **{'rack_id': rack_id} if rack_id else {},
            **{'row_code': row_code} if row_code else {},
            **{'row_id': row_id} if row_id else {},
            **{'zone_code': zone_code} if zone_code else {},
            **{'zone_id': zone_id} if zone_id else {},
        )

    def facility_update(
            self,
            fac_id,
            ac_power_capacity=None,
            area_display_value=None,
            assigned_date=None,
            client_id=None,
            dc_power_capacity=None,
            fac_address=None,
            fac_address2=None,
            fac_city=None,
            fac_code=None,
            fac_country=None,
            fac_description=None,
            fac_name=None,
            fac_state=None,
            fac_zip=None,
            meta_=None,
            phone=None,
            provider_client_id=None,
            rofr_expiration_date=None,
            status=None,
        ) -> Dict:
        """Update a facility

        API Method: device.facility_update

        This method is used to update a facility in the system.

        Args:
            fac_id: Facility ID,
            ac_power_capacity: AC Power Capacity. Defaults to None.
            area_display_value: Area Size Value. Defaults to None.
            assigned_date: Assigned Date. Defaults to None.
            client_id: Client ID. Defaults to None.
            dc_power_capacity: DC Power Capacity. Defaults to None.
            fac_address: Address. Defaults to None.
            fac_address2: Address 2. Defaults to None.
            fac_city: City. Defaults to None.
            fac_code: Facility Code. Defaults to None.
            fac_country: Country. Defaults to None.
            fac_description: Facility Description. Defaults to None.
            fac_name: Facility Name. Defaults to None.
            fac_state: State. Defaults to None.
            fac_zip: Postal code. Defaults to None.
            meta_: Custom Fields. Defaults to None.
            phone: Telephone. Defaults to None.
            provider_client_id: Provide Client Id. Defaults to None.
            rofr_expiration_date: ROFR Expiration Date. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.facility_update',
            fac_id=fac_id,
            **{'ac_power_capacity': ac_power_capacity} if ac_power_capacity else {},
            **{'area_display_value': area_display_value} if area_display_value else {},
            **{'assigned_date': assigned_date} if assigned_date else {},
            **{'client_id': client_id} if client_id else {},
            **{'dc_power_capacity': dc_power_capacity} if dc_power_capacity else {},
            **{'fac_address': fac_address} if fac_address else {},
            **{'fac_address2': fac_address2} if fac_address2 else {},
            **{'fac_city': fac_city} if fac_city else {},
            **{'fac_code': fac_code} if fac_code else {},
            **{'fac_country': fac_country} if fac_country else {},
            **{'fac_description': fac_description} if fac_description else {},
            **{'fac_name': fac_name} if fac_name else {},
            **{'fac_state': fac_state} if fac_state else {},
            **{'fac_zip': fac_zip} if fac_zip else {},
            **{'meta_': meta_} if meta_ else {},
            **{'phone': phone} if phone else {},
            **{'provider_client_id': provider_client_id} if provider_client_id else {},
            **{'rofr_expiration_date': rofr_expiration_date} if rofr_expiration_date else {},
            **{'status': status} if status else {},
        )

    def get(
            self,
            device_id,
            locations=None,
            metadata=None,
            modules=None,
            service=None,
            tags=None,
        ) -> Dict:
        """Get a Device

        API Method: device.get

        This method is used to get a device's details.

        Args:
            device_id: Device ID,
            locations: Device Locations. Defaults to None.
            metadata: Device Custom Fields. Defaults to None.
            modules: Device Modules. Defaults to None.
            service: Service ID. Defaults to None.
            tags: Device Tags. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.get',
            device_id=device_id,
            **{'locations': locations} if locations else {},
            **{'metadata': metadata} if metadata else {},
            **{'modules': modules} if modules else {},
            **{'service': service} if service else {},
            **{'tags': tags} if tags else {},
        )

    def hostname_get(
            self,
            plan_id=None,
            service_id=None,
        ) -> Dict:
        """Get Control Panel Host Device information

        API Method: device.hostname_get

        This method is used to get control panel host information. Returns all active system hosts if no params are provided

        Args:
            plan_id: Service Plan ID. Defaults to None.
            service_id: Service ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.hostname_get',
            **{'plan_id': plan_id} if plan_id else {},
            **{'service_id': service_id} if service_id else {},
        )

    def interface_add(
            self,
            device_id,
            name,
            description=None,
            interface_type_id=None,
            mac=None,
            status=None,
        ) -> Dict:
        """Add a Device Interface

        API Method: device.interface_add

        This method is used to add a new Interface to a Device.

        Args:
            device_id: Device ID,
            name: Interface Name,
            description: Description. Defaults to None.
            interface_type_id: Interface Type ID. Defaults to None.
            mac: MAC Address. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.interface_add',
            device_id=device_id,
            name=name,
            **{'description': description} if description else {},
            **{'interface_type_id': interface_type_id} if interface_type_id else {},
            **{'mac': mac} if mac else {},
            **{'status': status} if status else {},
        )

    def interface_list(
            self,
            connection_class_id=None,
            device_id=None,
            device_interface_id=None,
            interface_type_id=None,
            mac=None,
            name=None,
            status=None,
        ) -> Dict:
        """List Device Interfaces

        API Method: device.interface_list

        This method is used to list a device's Interfaces.

        Args:
            connection_class_id: Connection Class ID. Defaults to None.
            device_id: Device ID. Defaults to None.
            device_interface_id: Device Interface ID. Defaults to None.
            interface_type_id: Interface Type ID. Defaults to None.
            mac: MAC Address. Defaults to None.
            name: Name. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.interface_list',
            **{'connection_class_id': connection_class_id} if connection_class_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'device_interface_id': device_interface_id} if device_interface_id else {},
            **{'interface_type_id': interface_type_id} if interface_type_id else {},
            **{'mac': mac} if mac else {},
            **{'name': name} if name else {},
            **{'status': status} if status else {},
        )

    def interface_type_add(
            self,
            code,
            connection_class_id,
            name,
            description=None,
            status=None,
        ) -> Dict:
        """Add an Interface Type

        API Method: device.interface_type_add

        Adds a new interface type

        Args:
            code: Code,
            connection_class_id: Connection Class ID,
            name: Name,
            description: Description. Defaults to None.
            status: Status ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.interface_type_add',
            code=code,
            connection_class_id=connection_class_id,
            name=name,
            **{'description': description} if description else {},
            **{'status': status} if status else {},
        )

    def interface_type_list(
            self,
            connection_class_id=None,
        ) -> Dict:
        """List Device Interface Types

        API Method: device.interface_type_list

        This method is used to list available device interface types.

        Args:
            connection_class_id: Connection Class ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.interface_type_list',
            **{'connection_class_id': connection_class_id} if connection_class_id else {},
        )

    def interface_update(
            self,
            device_interface_id,
            description=None,
            interface_type_id=None,
            mac=None,
            name=None,
            status=None,
        ) -> Dict:
        """Update a Device Interface

        API Method: device.interface_update

        This method is used to update an Interface on a Device.

        Args:
            device_interface_id: Device Interface ID,
            description: Description. Defaults to None.
            interface_type_id: Interface Type ID. Defaults to None.
            mac: MAC Address. Defaults to None.
            name: Interface Name. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.interface_update',
            device_interface_id=device_interface_id,
            **{'description': description} if description else {},
            **{'interface_type_id': interface_type_id} if interface_type_id else {},
            **{'mac': mac} if mac else {},
            **{'name': name} if name else {},
            **{'status': status} if status else {},
        )

    def ip_assign(
            self,
            device_id,
            addr=None,
            cidr=None,
            client_id=None,
            force=None,
            group_id=None,
            vlan_num=None,
        ) -> Dict:
        """Assign an IP to a Device

        API Method: device.ip_assign

        This method is used to assign an IP address to a device.

        Args:
            device_id: Device ID,
            addr: IP Assignment. Defaults to None.
            cidr: CIDR Assignment Size. Defaults to None.
            client_id: Client ID. Defaults to None.
            force: Force Flag. Defaults to None.
            group_id: IP Group ID. Defaults to None.
            vlan_num: VLAN Number. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_assign',
            device_id=device_id,
            **{'addr': addr} if addr else {},
            **{'cidr': cidr} if cidr else {},
            **{'client_id': client_id} if client_id else {},
            **{'force': force} if force else {},
            **{'group_id': group_id} if group_id else {},
            **{'vlan_num': vlan_num} if vlan_num else {},
        )

    def ip_assignment_add(
            self,
            device_id,
            addr=None,
            addr_type=None,
            assign_description=None,
            block_id=None,
            cidr=None,
            client_id=None,
            fac_id=None,
            group_id=None,
            pool_id=None,
            service_id=None,
        ) -> Dict:
        """Create a New IP Assignment

        API Method: device.ip_assignment_add

        This method is used to create a new IP address assignment.

        Args:
            device_id: Device ID,
            addr: Address(es) to Assign. Defaults to None.
            addr_type: Address Type. Defaults to None.
            assign_description: Description. Defaults to None.
            block_id: Block ID. Defaults to None.
            cidr: CIDR Assignment Size. Defaults to None.
            client_id: Client ID. Defaults to None.
            fac_id: Facility ID. Defaults to None.
            group_id: Group ID. Defaults to None.
            pool_id: Pool ID. Defaults to None.
            service_id: Service ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_assignment_add',
            device_id=device_id,
            **{'addr': addr} if addr else {},
            **{'addr_type': addr_type} if addr_type else {},
            **{'assign_description': assign_description} if assign_description else {},
            **{'block_id': block_id} if block_id else {},
            **{'cidr': cidr} if cidr else {},
            **{'client_id': client_id} if client_id else {},
            **{'fac_id': fac_id} if fac_id else {},
            **{'group_id': group_id} if group_id else {},
            **{'pool_id': pool_id} if pool_id else {},
            **{'service_id': service_id} if service_id else {},
        )

    def ip_assignment_delete(
            self,
            assign_id,
        ) -> Dict:
        """Delete a Device IP Assignment

        API Method: device.ip_assignment_delete

        This method is used to delete an IP assignment from a device.

        Args:
            assign_id: IP Assignment ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_assignment_delete',
            assign_id=assign_id,
        )

    def ip_assignment_list(
            self,
            client_id=None,
            device_id=None,
            group_id=None,
            limit=None,
            offset=None,
            service_id=None,
        ) -> Dict:
        """List Device IP Assignments

        API Method: device.ip_assignment_list

        This method is used to list a device's IP assignments.

        Args:
            client_id: Client ID. Defaults to None.
            device_id: Device ID. Defaults to None.
            group_id: IP Group ID. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            service_id: Service ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_assignment_list',
            **{'client_id': client_id} if client_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'group_id': group_id} if group_id else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'service_id': service_id} if service_id else {},
        )

    def ip_assignment_update(
            self,
            assign_id,
            addr=None,
            addr_type=None,
            assign_description=None,
            client_id=None,
            device_id=None,
            group_id=None,
            service_id=None,
        ) -> Dict:
        """Update a Device IP Assignment

        API Method: device.ip_assignment_update

        This method is used to update a device's IP assignment.

        Args:
            assign_id: IP Assignment ID,
            addr: IP Address. Defaults to None.
            addr_type: Address Type. Defaults to None.
            assign_description: Description. Defaults to None.
            client_id: Client ID. Defaults to None.
            device_id: Device ID. Defaults to None.
            group_id: Group ID. Defaults to None.
            service_id: Service ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_assignment_update',
            assign_id=assign_id,
            **{'addr': addr} if addr else {},
            **{'addr_type': addr_type} if addr_type else {},
            **{'assign_description': assign_description} if assign_description else {},
            **{'client_id': client_id} if client_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'group_id': group_id} if group_id else {},
            **{'service_id': service_id} if service_id else {},
        )

    def ip_block_add(
            self,
            addr,
            pool_id,
            block_assign=None,
            block_description=None,
            priority=None,
        ) -> Dict:
        """Add a Block

        API Method: device.ip_block_add

        This method is used to add a Block in the system.

        Args:
            addr: Network (CIDR),
            pool_id: Pool ID,
            block_assign: Auto Assignment. Defaults to None.
            block_description: Block Description. Defaults to None.
            priority: Priority. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_block_add',
            addr=addr,
            pool_id=pool_id,
            **{'block_assign': block_assign} if block_assign else {},
            **{'block_description': block_description} if block_description else {},
            **{'priority': priority} if priority else {},
        )

    def ip_block_delete(
            self,
            block_id,
        ) -> Dict:
        """Delete a Block

        API Method: device.ip_block_delete

        This method is used to delete a Block.

        Args:
            block_id: Block ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_block_delete',
            block_id=block_id,
        )

    def ip_block_list(
            self,
            block_assign=None,
            block_id=None,
            fac_id=None,
            ipver=None,
            limit=None,
            offset=None,
            pool_id=None,
        ) -> Dict:
        """List IP Blocks

        API Method: device.ip_block_list

        This method is used to list IP blocks.

        Args:
            block_assign: Auto-assignment. Defaults to None.
            block_id: Block ID. Defaults to None.
            fac_id: Facility ID. Defaults to None.
            ipver: IP Version. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            pool_id: Pool ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_block_list',
            **{'block_assign': block_assign} if block_assign else {},
            **{'block_id': block_id} if block_id else {},
            **{'fac_id': fac_id} if fac_id else {},
            **{'ipver': ipver} if ipver else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'pool_id': pool_id} if pool_id else {},
        )

    def ip_block_update(
            self,
            block_id,
            addr=None,
            block_assign=None,
            block_description=None,
            priority=None,
        ) -> Dict:
        """Update a Block

        API Method: device.ip_block_update

        This method is used to update a Block in the system.

        Args:
            block_id: Block ID,
            addr: Network (CIDR). Defaults to None.
            block_assign: Auto Assignment. Defaults to None.
            block_description: Block Description. Defaults to None.
            priority: Priority. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_block_update',
            block_id=block_id,
            **{'addr': addr} if addr else {},
            **{'block_assign': block_assign} if block_assign else {},
            **{'block_description': block_description} if block_description else {},
            **{'priority': priority} if priority else {},
        )

    def ip_get_available(
            self,
            cidr=None,
            client_id=None,
            device_id=None,
            group_id=None,
            vlan_num=None,
        ) -> Dict:
        """List Available IP Addresses

        API Method: device.ip_get_available

        This method is used to list existing IP Assignments which are not currently associated with a device.

        Args:
            cidr: CIDR Assignment Size. Defaults to None.
            client_id: Client ID. Defaults to None.
            device_id: Device ID. Defaults to None.
            group_id: IP Group ID. Defaults to None.
            vlan_num: VLAN Number. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_get_available',
            **{'cidr': cidr} if cidr else {},
            **{'client_id': client_id} if client_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'group_id': group_id} if group_id else {},
            **{'vlan_num': vlan_num} if vlan_num else {},
        )

    def ip_get_unassigned(
            self,
            block_id=None,
            cidr=None,
            fac_id=None,
            limit=None,
            pool_id=None,
        ) -> Dict:
        """Get Unassigned IP Addresses

        API Method: device.ip_get_unassigned

        This method is used to get a list of unassigned IP Addresses.

        Args:
            block_id: IP Address Block ID. Defaults to None.
            cidr: CIDR Assignment Size. Defaults to None.
            fac_id: Facility ID. Defaults to None.
            limit: Limit. Defaults to None.
            pool_id: IP Address Pool ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_get_unassigned',
            **{'block_id': block_id} if block_id else {},
            **{'cidr': cidr} if cidr else {},
            **{'fac_id': fac_id} if fac_id else {},
            **{'limit': limit} if limit else {},
            **{'pool_id': pool_id} if pool_id else {},
        )

    def ip_group_add(
            self,
            group_description,
            client_id=None,
            hsrp=None,
            vlan_num=None,
            vlan_range_id=None,
        ) -> Dict:
        """Add a Device IP Group

        API Method: device.ip_group_add

        This method is used to add an IP group to a device.

        Args:
            group_description: Group Description,
            client_id: Client ID. Defaults to None.
            hsrp: HSRP. Defaults to None.
            vlan_num: VLAN Number. Defaults to None.
            vlan_range_id: VLAN Range ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_group_add',
            group_description=group_description,
            **{'client_id': client_id} if client_id else {},
            **{'hsrp': hsrp} if hsrp else {},
            **{'vlan_num': vlan_num} if vlan_num else {},
            **{'vlan_range_id': vlan_range_id} if vlan_range_id else {},
        )

    def ip_group_delete(
            self,
            group_id,
        ) -> Dict:
        """Delete a Device IP Group

        API Method: device.ip_group_delete

        This method is used to delete an IP group from a device.

        Args:
            group_id: Group ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_group_delete',
            group_id=group_id,
        )

    def ip_group_list(
            self,
            client_id=None,
            device_id=None,
            direction=None,
            empty=None,
            fac_id=None,
            is_hsrp=None,
            is_vlan=None,
            limit=None,
            offset=None,
            order_by=None,
            vlan_num=None,
            vlan_range_id=None,
            with_ips=None,
        ) -> Dict:
        """List a Device IP Group

        API Method: device.ip_group_list

        This method is used to list a device's IP groups.

        Args:
            client_id: Client ID. Defaults to None.
            device_id: Device ID. Defaults to None.
            direction: Direction. Defaults to None.
            empty: Empty VLANs. Defaults to None.
            fac_id: Facility ID. Defaults to None.
            is_hsrp: HSRP Flag. Defaults to None.
            is_vlan: VLAN Flag. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            vlan_num: VLAN Number. Defaults to None.
            vlan_range_id: VLAN Range ID. Defaults to None.
            with_ips: With IPs. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_group_list',
            **{'client_id': client_id} if client_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'direction': direction} if direction else {},
            **{'empty': empty} if empty else {},
            **{'fac_id': fac_id} if fac_id else {},
            **{'is_hsrp': is_hsrp} if is_hsrp else {},
            **{'is_vlan': is_vlan} if is_vlan else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'vlan_num': vlan_num} if vlan_num else {},
            **{'vlan_range_id': vlan_range_id} if vlan_range_id else {},
            **{'with_ips': with_ips} if with_ips else {},
        )

    def ip_group_update(
            self,
            group_id,
            client_id=None,
            group_description=None,
            hsrp=None,
            vlan_num=None,
            vlan_range_id=None,
        ) -> Dict:
        """Update a Device IP Group

        API Method: device.ip_group_update

        This method is used to update a device's IP group.

        Args:
            group_id: Group ID,
            client_id: Client ID. Defaults to None.
            group_description: Group Description. Defaults to None.
            hsrp: HSRP. Defaults to None.
            vlan_num: VLAN Number. Defaults to None.
            vlan_range_id: VLAN Range ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_group_update',
            group_id=group_id,
            **{'client_id': client_id} if client_id else {},
            **{'group_description': group_description} if group_description else {},
            **{'hsrp': hsrp} if hsrp else {},
            **{'vlan_num': vlan_num} if vlan_num else {},
            **{'vlan_range_id': vlan_range_id} if vlan_range_id else {},
        )

    def ip_lookup(
            self,
            ip,
            addr_type=None,
            client_id=None,
            metadata=None,
        ) -> Dict:
        """Look Up a Device IP

        API Method: device.ip_lookup

        This method is used to look up the details of the assignment which contains the specified IP address.

        Args:
            ip: IP Address,
            addr_type: IP Assignment Type. Defaults to None.
            client_id: Client ID. Defaults to None.
            metadata: Custom Fields Flag. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_lookup',
            ip=ip,
            **{'addr_type': addr_type} if addr_type else {},
            **{'client_id': client_id} if client_id else {},
            **{'metadata': metadata} if metadata else {},
        )

    def ip_pool_add(
            self,
            pool_name,
            fac_id=None,
            max_util=None,
            min_subnet=None,
            min_subnet_size=None,
            notify_address=None,
            pool_assign=None,
            pool_description=None,
        ) -> Dict:
        """Add a Pool

        API Method: device.ip_pool_add

        This method is used to add a Pool in the system.

        Args:
            pool_name: Name,
            fac_id: Facility ID. Defaults to None.
            max_util: Maximum Utilization. Defaults to None.
            min_subnet: Minimum Subnets. Defaults to None.
            min_subnet_size: Minimum Subnet Size. Defaults to None.
            notify_address: Notify Address. Defaults to None.
            pool_assign: Auto Assignment. Defaults to None.
            pool_description: Pool Description. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_pool_add',
            pool_name=pool_name,
            **{'fac_id': fac_id} if fac_id else {},
            **{'max_util': max_util} if max_util else {},
            **{'min_subnet': min_subnet} if min_subnet else {},
            **{'min_subnet_size': min_subnet_size} if min_subnet_size else {},
            **{'notify_address': notify_address} if notify_address else {},
            **{'pool_assign': pool_assign} if pool_assign else {},
            **{'pool_description': pool_description} if pool_description else {},
        )

    def ip_pool_delete(
            self,
            pool_id,
        ) -> Dict:
        """Delete a Pool

        API Method: device.ip_pool_delete

        This method is used to delete a Pool.

        Args:
            pool_id: Pool ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_pool_delete',
            pool_id=pool_id,
        )

    def ip_pool_list(
            self,
            direction=None,
            fac_id=None,
            limit=None,
            offset=None,
            order_by=None,
            pool_assign=None,
            pool_id=None,
            show_blocks=None,
        ) -> Dict:
        """List IP Pools

        API Method: device.ip_pool_list

        This method is used to list IP pools.

        Args:
            direction: Direction. Defaults to None.
            fac_id: Facility ID. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            pool_assign: Auto-assignment. Defaults to None.
            pool_id: Pool ID. Defaults to None.
            show_blocks: Show IP blocks. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_pool_list',
            **{'direction': direction} if direction else {},
            **{'fac_id': fac_id} if fac_id else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'pool_assign': pool_assign} if pool_assign else {},
            **{'pool_id': pool_id} if pool_id else {},
            **{'show_blocks': show_blocks} if show_blocks else {},
        )

    def ip_pool_update(
            self,
            pool_id,
            fac_id=None,
            max_util=None,
            min_subnet=None,
            min_subnet_size=None,
            notify_address=None,
            pool_assign=None,
            pool_description=None,
            pool_name=None,
        ) -> Dict:
        """Update a Pool

        API Method: device.ip_pool_update

        This method is used to update a Pool in the system.

        Args:
            pool_id: Pool ID,
            fac_id: Facility ID. Defaults to None.
            max_util: Maximum Utilization. Defaults to None.
            min_subnet: Minimum Subnets. Defaults to None.
            min_subnet_size: Minimum Subnet Size. Defaults to None.
            notify_address: Notify Address. Defaults to None.
            pool_assign: Auto Assignment. Defaults to None.
            pool_description: Pool Description. Defaults to None.
            pool_name: Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_pool_update',
            pool_id=pool_id,
            **{'fac_id': fac_id} if fac_id else {},
            **{'max_util': max_util} if max_util else {},
            **{'min_subnet': min_subnet} if min_subnet else {},
            **{'min_subnet_size': min_subnet_size} if min_subnet_size else {},
            **{'notify_address': notify_address} if notify_address else {},
            **{'pool_assign': pool_assign} if pool_assign else {},
            **{'pool_description': pool_description} if pool_description else {},
            **{'pool_name': pool_name} if pool_name else {},
        )

    def ip_unassign(
            self,
            device_id,
            addr=None,
            assign_id=None,
        ) -> Dict:
        """Unassign a Device IP

        API Method: device.ip_unassign

        This method is used to unassign a device's IP.

        Args:
            device_id: Device ID,
            addr: IP Address. Defaults to None.
            assign_id: IP Assignment ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.ip_unassign',
            device_id=device_id,
            **{'addr': addr} if addr else {},
            **{'assign_id': assign_id} if assign_id else {},
        )

    def list(
            self,
            cage_id=None,
            client_id=None,
            dev_desc=None,
            device=None,
            devtype_group_id=None,
            direction=None,
            fac_id=None,
            label=None,
            limit=None,
            metadata=None,
            modules=None,
            offset=None,
            order_by=None,
            parent=None,
            rack_id=None,
            require_ip=None,
            row_id=None,
            service_id=None,
            status=None,
            tag_id=None,
            tag_ids=None,
            tags=None,
            type_id=None,
            zone_id=None,
        ) -> Dict:
        """List Devices

        API Method: device.list

        This method is used to list devices in the system.

        Args:
            cage_id: Cage ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            dev_desc: Device Description. Defaults to None.
            device: Device ID(s). Defaults to None.
            devtype_group_id: Device Type Group ID. Defaults to None.
            direction: Direction. Defaults to None.
            fac_id: Facility ID. Defaults to None.
            label: Device Label. Defaults to None.
            limit: Limit. Defaults to None.
            metadata: Include Custom Fields. Defaults to None.
            modules: Device Modules. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            parent: Parent Device ID. Defaults to None.
            rack_id: Rack ID. Defaults to None.
            require_ip: Include IP Addresses. Defaults to None.
            row_id: Row ID. Defaults to None.
            service_id: Service ID. Defaults to None.
            status: Device Status. Defaults to None.
            tag_id: Tag ID. Defaults to None.
            tag_ids: Tag IDs. Defaults to None.
            tags: Include Tags. Defaults to None.
            type_id: Device Type ID. Defaults to None.
            zone_id: Zone ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.list',
            **{'cage_id': cage_id} if cage_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'dev_desc': dev_desc} if dev_desc else {},
            **{'device': device} if device else {},
            **{'devtype_group_id': devtype_group_id} if devtype_group_id else {},
            **{'direction': direction} if direction else {},
            **{'fac_id': fac_id} if fac_id else {},
            **{'label': label} if label else {},
            **{'limit': limit} if limit else {},
            **{'metadata': metadata} if metadata else {},
            **{'modules': modules} if modules else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'parent': parent} if parent else {},
            **{'rack_id': rack_id} if rack_id else {},
            **{'require_ip': require_ip} if require_ip else {},
            **{'row_id': row_id} if row_id else {},
            **{'service_id': service_id} if service_id else {},
            **{'status': status} if status else {},
            **{'tag_id': tag_id} if tag_id else {},
            **{'tag_ids': tag_ids} if tag_ids else {},
            **{'tags': tags} if tags else {},
            **{'type_id': type_id} if type_id else {},
            **{'zone_id': zone_id} if zone_id else {},
        )

    def module_call(
            self,
            device_id,
            function,
            module_id,
            module_params=None,
        ) -> Dict:
        """Call a Device Module Function

        API Method: device.module_call

        This method is used to execute a device module function.

        Args:
            device_id: Device ID,
            function: Function Name,
            module_id: Module Name,
            module_params: Parameters. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.module_call',
            device_id=device_id,
            function=function,
            module_id=module_id,
            **{'module_params': module_params} if module_params else {},
        )

    def module_call_aggregate(
            self,
            device_ids,
            function,
            module_id,
            module_params=None,
        ) -> Dict:
        """Call an Aggregate Device Module Function

        API Method: device.module_call_aggregate

        This method is used to execute an aggregate device module function.

        Args:
            device_ids: Device ID Array,
            function: Function Name,
            module_id: Device Module Name,
            module_params: Parameters. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.module_call_aggregate',
            device_ids=device_ids,
            function=function,
            module_id=module_id,
            **{'module_params': module_params} if module_params else {},
        )

    def module_graph(
            self,
            device_id,
            module_id,
            module_params=None,
        ) -> Dict:
        """Generate Device Module Graph

        API Method: device.module_graph

        This method is used to generate a device module graph.

        Args:
            device_id: Device ID,
            module_id: Device Module Name,
            module_params: Module Parameters. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.module_graph',
            device_id=device_id,
            module_id=module_id,
            **{'module_params': module_params} if module_params else {},
        )

    def monitor_add(
            self,
            device_id,
            protocol,
            address=None,
            extra=None,
            label=None,
            loss=None,
            notify=None,
            notify_delay=None,
            notify_interval=None,
            port=None,
            script_id=None,
        ) -> Dict:
        """Add a New Device Monitor

        API Method: device.monitor_add

        This method is used to add a new device monitor.

        Args:
            device_id: Device ID,
            protocol: Protocol,
            address: Monitored IP Address. Defaults to None.
            extra: Extra Parameters. Defaults to None.
            label: Monitor Label. Defaults to None.
            loss: Packet Loss. Defaults to None.
            notify: Notification Email Address. Defaults to None.
            notify_delay: Notification Delay. Defaults to None.
            notify_interval: Notification Interval. Defaults to None.
            port: Port. Defaults to None.
            script_id: Script ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.monitor_add',
            device_id=device_id,
            protocol=protocol,
            **{'address': address} if address else {},
            **{'extra': extra} if extra else {},
            **{'label': label} if label else {},
            **{'loss': loss} if loss else {},
            **{'notify': notify} if notify else {},
            **{'notify_delay': notify_delay} if notify_delay else {},
            **{'notify_interval': notify_interval} if notify_interval else {},
            **{'port': port} if port else {},
            **{'script_id': script_id} if script_id else {},
        )

    def monitor_delete(
            self,
            device_id=None,
            module=None,
            mon_id=None,
            protocol=None,
            script_id=None,
        ) -> Dict:
        """Delete a Device Monitor

        API Method: device.monitor_delete

        This method is used to delete a device monitor.

        Args:
            device_id: Device ID. Defaults to None.
            module: Module Name. Defaults to None.
            mon_id: Monitor ID. Defaults to None.
            protocol: Protocol. Defaults to None.
            script_id: Script ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.monitor_delete',
            **{'device_id': device_id} if device_id else {},
            **{'module': module} if module else {},
            **{'mon_id': mon_id} if mon_id else {},
            **{'protocol': protocol} if protocol else {},
            **{'script_id': script_id} if script_id else {},
        )

    def monitor_disable(
            self,
            client_id=None,
            device_id=None,
            devtype_group_id=None,
            module=None,
            mon_id=None,
            script_id=None,
            zone_id=None,
        ) -> Dict:
        """Disable a Device Monitor

        API Method: device.monitor_disable

        This method is used to disable a device monitor.

        Args:
            client_id: Client ID. Defaults to None.
            device_id: Device ID. Defaults to None.
            devtype_group_id: Device Type Group ID. Defaults to None.
            module: Module Name. Defaults to None.
            mon_id: Monitor ID. Defaults to None.
            script_id: Script ID. Defaults to None.
            zone_id: Monitor ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.monitor_disable',
            **{'client_id': client_id} if client_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'devtype_group_id': devtype_group_id} if devtype_group_id else {},
            **{'module': module} if module else {},
            **{'mon_id': mon_id} if mon_id else {},
            **{'script_id': script_id} if script_id else {},
            **{'zone_id': zone_id} if zone_id else {},
        )

    def monitor_enable(
            self,
            client_id=None,
            device_id=None,
            devtype_group_id=None,
            module=None,
            mon_id=None,
            script_id=None,
            zone_id=None,
        ) -> Dict:
        """Enable a Device Monitor

        API Method: device.monitor_enable

        This method is used to enable a device monitor.

        Args:
            client_id: Client ID. Defaults to None.
            device_id: Device ID. Defaults to None.
            devtype_group_id: Device Type Group ID. Defaults to None.
            module: Module Name. Defaults to None.
            mon_id: Monitor ID. Defaults to None.
            script_id: Script ID. Defaults to None.
            zone_id: Monitor ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.monitor_enable',
            **{'client_id': client_id} if client_id else {},
            **{'device_id': device_id} if device_id else {},
            **{'devtype_group_id': devtype_group_id} if devtype_group_id else {},
            **{'module': module} if module else {},
            **{'mon_id': mon_id} if mon_id else {},
            **{'script_id': script_id} if script_id else {},
            **{'zone_id': zone_id} if zone_id else {},
        )

    def monitor_get(
            self,
            mon_id,
            direction=None,
            limit=None,
            logs=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """Get a Device Monitor

        API Method: device.monitor_get

        This method is used to get a device monitor's details.

        Args:
            mon_id: Monitor ID,
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            logs: Monitor Logs. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.monitor_get',
            mon_id=mon_id,
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'logs': logs} if logs else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def monitor_list(
            self,
            device_id=None,
            direction=None,
            limit=None,
            module=None,
            mon_id=None,
            not_state=None,
            offset=None,
            order_by=None,
            protocol=None,
            script_id=None,
            state=None,
        ) -> Dict:
        """List Device Monitors

        API Method: device.monitor_list

        This method is used to list device monitors.

        Args:
            device_id: Device ID. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            module: Device Module. Defaults to None.
            mon_id: Monitor ID. Defaults to None.
            not_state: Monitor State. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            protocol: Monitoring Protocol. Defaults to None.
            script_id: Script ID. Defaults to None.
            state: Monitor State. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.monitor_list',
            **{'device_id': device_id} if device_id else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'module': module} if module else {},
            **{'mon_id': mon_id} if mon_id else {},
            **{'not_state': not_state} if not_state else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'protocol': protocol} if protocol else {},
            **{'script_id': script_id} if script_id else {},
            **{'state': state} if state else {},
        )

    def monitor_update(
            self,
            mon_id,
            protocol,
            address=None,
            extra=None,
            label=None,
            loss=None,
            notify=None,
            notify_delay=None,
            notify_interval=None,
            port=None,
            script_id=None,
        ) -> Dict:
        """Update a Device Monitor

        API Method: device.monitor_update

        This method is used to update a device monitor.

        Args:
            mon_id: Monitor ID,
            protocol: Protocol,
            address: Monitored IP Address. Defaults to None.
            extra: Extra Parameters. Defaults to None.
            label: Monitor Label. Defaults to None.
            loss: Packet Loss. Defaults to None.
            notify: Notification Email Address. Defaults to None.
            notify_delay: Notification Delay. Defaults to None.
            notify_interval: Notification Interval. Defaults to None.
            port: Port. Defaults to None.
            script_id: Script ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.monitor_update',
            mon_id=mon_id,
            protocol=protocol,
            **{'address': address} if address else {},
            **{'extra': extra} if extra else {},
            **{'label': label} if label else {},
            **{'loss': loss} if loss else {},
            **{'notify': notify} if notify else {},
            **{'notify_delay': notify_delay} if notify_delay else {},
            **{'notify_interval': notify_interval} if notify_interval else {},
            **{'port': port} if port else {},
            **{'script_id': script_id} if script_id else {},
        )

    def rack_add(
            self,
            row_id,
            ac_power_capacity=None,
            area_display_value=None,
            assigned_date=None,
            client_id=None,
            dc_power_capacity=None,
            depth_display_unit=None,
            depth_display_value=None,
            height_display_unit=None,
            height_display_value=None,
            meta_=None,
            rack_code=None,
            rack_direction=None,
            rack_name=None,
            rack_unit=None,
            rofr_expiration_date=None,
            shelves=None,
            slots=None,
            status=None,
            width_display_unit=None,
            width_display_value=None,
        ) -> Dict:
        """Add a rack

        API Method: device.rack_add

        This method is used to add a rack in the system.

        Args:
            row_id: Row ID,
            ac_power_capacity: AC Power Capacity. Defaults to None.
            area_display_value: Area Size Value. Defaults to None.
            assigned_date: Assigned Date. Defaults to None.
            client_id: Client ID. Defaults to None.
            dc_power_capacity: DC Power Capacity. Defaults to None.
            depth_display_unit: Depth Unit. Defaults to None.
            depth_display_value: Depth Value. Defaults to None.
            height_display_unit: Height Unit. Defaults to None.
            height_display_value: Height Value. Defaults to None.
            meta_: Custom Fields. Defaults to None.
            rack_code: Rack Code. Defaults to None.
            rack_direction: Rack Direction And Type. Defaults to None.
            rack_name: Rack Name. Defaults to None.
            rack_unit: Rack Unit. Defaults to None.
            rofr_expiration_date: ROFR Expiration Date. Defaults to None.
            shelves: Rack Shelves. Defaults to None.
            slots: Rack Slots. Defaults to None.
            status: Status. Defaults to None.
            width_display_unit: Width Unit. Defaults to None.
            width_display_value: Width Value. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.rack_add',
            row_id=row_id,
            **{'ac_power_capacity': ac_power_capacity} if ac_power_capacity else {},
            **{'area_display_value': area_display_value} if area_display_value else {},
            **{'assigned_date': assigned_date} if assigned_date else {},
            **{'client_id': client_id} if client_id else {},
            **{'dc_power_capacity': dc_power_capacity} if dc_power_capacity else {},
            **{'depth_display_unit': depth_display_unit} if depth_display_unit else {},
            **{'depth_display_value': depth_display_value} if depth_display_value else {},
            **{'height_display_unit': height_display_unit} if height_display_unit else {},
            **{'height_display_value': height_display_value} if height_display_value else {},
            **{'meta_': meta_} if meta_ else {},
            **{'rack_code': rack_code} if rack_code else {},
            **{'rack_direction': rack_direction} if rack_direction else {},
            **{'rack_name': rack_name} if rack_name else {},
            **{'rack_unit': rack_unit} if rack_unit else {},
            **{'rofr_expiration_date': rofr_expiration_date} if rofr_expiration_date else {},
            **{'shelves': shelves} if shelves else {},
            **{'slots': slots} if slots else {},
            **{'status': status} if status else {},
            **{'width_display_unit': width_display_unit} if width_display_unit else {},
            **{'width_display_value': width_display_value} if width_display_value else {},
        )

    def rack_list(
            self,
            cage_code=None,
            cage_id=None,
            client_id=None,
            fac_code=None,
            fac_id=None,
            rack_code=None,
            rack_id=None,
            row_code=None,
            row_id=None,
            status=None,
            zone_code=None,
            zone_id=None,
        ) -> Dict:
        """List Racks

        API Method: device.rack_list

        This method is used to list racks, including devices by position.

        Args:
            cage_code: Cage Code. Defaults to None.
            cage_id: Cage ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            fac_code: Facility Code. Defaults to None.
            fac_id: Facility ID. Defaults to None.
            rack_code: Rack Code. Defaults to None.
            rack_id: Rack ID. Defaults to None.
            row_code: Row Code. Defaults to None.
            row_id: Row ID. Defaults to None.
            status: Status. Defaults to None.
            zone_code: Zone Code. Defaults to None.
            zone_id: Zone ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.rack_list',
            **{'cage_code': cage_code} if cage_code else {},
            **{'cage_id': cage_id} if cage_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'fac_code': fac_code} if fac_code else {},
            **{'fac_id': fac_id} if fac_id else {},
            **{'rack_code': rack_code} if rack_code else {},
            **{'rack_id': rack_id} if rack_id else {},
            **{'row_code': row_code} if row_code else {},
            **{'row_id': row_id} if row_id else {},
            **{'status': status} if status else {},
            **{'zone_code': zone_code} if zone_code else {},
            **{'zone_id': zone_id} if zone_id else {},
        )

    def rack_update(
            self,
            rack_id,
            ac_power_capacity=None,
            area_display_value=None,
            assigned_date=None,
            client_id=None,
            dc_power_capacity=None,
            depth_display_unit=None,
            depth_display_value=None,
            height_display_unit=None,
            height_display_value=None,
            meta_=None,
            rack_code=None,
            rack_direction=None,
            rack_name=None,
            rack_unit=None,
            rofr_expiration_date=None,
            row_id=None,
            shelves=None,
            slots=None,
            status=None,
            width_display_unit=None,
            width_display_value=None,
        ) -> Dict:
        """Update a rack

        API Method: device.rack_update

        This method is used to update a rack in the system.

        Args:
            rack_id: Rack ID,
            ac_power_capacity: AC Power Capacity. Defaults to None.
            area_display_value: Area Size Value. Defaults to None.
            assigned_date: Assigned Date. Defaults to None.
            client_id: Client ID. Defaults to None.
            dc_power_capacity: DC Power Capacity. Defaults to None.
            depth_display_unit: Depth Unit. Defaults to None.
            depth_display_value: Depth Value. Defaults to None.
            height_display_unit: Height Unit. Defaults to None.
            height_display_value: Height Value. Defaults to None.
            meta_: Custom Fields. Defaults to None.
            rack_code: Rack Code. Defaults to None.
            rack_direction: Rack Direction And Type. Defaults to None.
            rack_name: Rack Name. Defaults to None.
            rack_unit: Rack Unit. Defaults to None.
            rofr_expiration_date: ROFR Expiration Date. Defaults to None.
            row_id: Row ID. Defaults to None.
            shelves: Rack Shelves. Defaults to None.
            slots: Rack Slots. Defaults to None.
            status: Status. Defaults to None.
            width_display_unit: Width Unit. Defaults to None.
            width_display_value: Width Value. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.rack_update',
            rack_id=rack_id,
            **{'ac_power_capacity': ac_power_capacity} if ac_power_capacity else {},
            **{'area_display_value': area_display_value} if area_display_value else {},
            **{'assigned_date': assigned_date} if assigned_date else {},
            **{'client_id': client_id} if client_id else {},
            **{'dc_power_capacity': dc_power_capacity} if dc_power_capacity else {},
            **{'depth_display_unit': depth_display_unit} if depth_display_unit else {},
            **{'depth_display_value': depth_display_value} if depth_display_value else {},
            **{'height_display_unit': height_display_unit} if height_display_unit else {},
            **{'height_display_value': height_display_value} if height_display_value else {},
            **{'meta_': meta_} if meta_ else {},
            **{'rack_code': rack_code} if rack_code else {},
            **{'rack_direction': rack_direction} if rack_direction else {},
            **{'rack_name': rack_name} if rack_name else {},
            **{'rack_unit': rack_unit} if rack_unit else {},
            **{'rofr_expiration_date': rofr_expiration_date} if rofr_expiration_date else {},
            **{'row_id': row_id} if row_id else {},
            **{'shelves': shelves} if shelves else {},
            **{'slots': slots} if slots else {},
            **{'status': status} if status else {},
            **{'width_display_unit': width_display_unit} if width_display_unit else {},
            **{'width_display_value': width_display_value} if width_display_value else {},
        )

    def raw_module_list(
            self,
        ) -> Dict:
        """List Available Device Modules

        API Method: device.raw_module_list

        This method returns a list of device modules.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.raw_module_list',
        )

    def reboot(
            self,
            device_id,
            power_action,
            outlet=None,
        ) -> Dict:
        """Set a Device's Power State

        API Method: device.reboot

        This method is used to control the power state of a device.

        Args:
            device_id: Device ID,
            power_action: Power Action,
            outlet: Outlet Number. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.reboot',
            device_id=device_id,
            power_action=power_action,
            **{'outlet': outlet} if outlet else {},
        )

    def reboot_graph(
            self,
            device_id,
            module_id,
            end_time=None,
            height=None,
            period=None,
            start_time=None,
            title=None,
            width=None,
        ) -> Dict:
        """Get a Reboot Graph

        API Method: device.reboot_graph

        This method is used to generate a graph of the power usage for a specified device.

        Args:
            device_id: Device ID,
            module_id: Device Module Name,
            end_time: End Date. Defaults to None.
            height: Graph Height. Defaults to None.
            period: Graph Period. Defaults to None.
            start_time: Start Date. Defaults to None.
            title: Graph Title. Defaults to None.
            width: Graph Width. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.reboot_graph',
            device_id=device_id,
            module_id=module_id,
            **{'end_time': end_time} if end_time else {},
            **{'height': height} if height else {},
            **{'period': period} if period else {},
            **{'start_time': start_time} if start_time else {},
            **{'title': title} if title else {},
            **{'width': width} if width else {},
        )

    def row_add(
            self,
            cage_id,
            meta_=None,
            row_code=None,
            row_name=None,
            status=None,
        ) -> Dict:
        """Add a row

        API Method: device.row_add

        This method is used to add a row in the system.

        Args:
            cage_id: Cage ID,
            meta_: Custom Fields. Defaults to None.
            row_code: Row Code. Defaults to None.
            row_name: Row Name. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.row_add',
            cage_id=cage_id,
            **{'meta_': meta_} if meta_ else {},
            **{'row_code': row_code} if row_code else {},
            **{'row_name': row_name} if row_name else {},
            **{'status': status} if status else {},
        )

    def row_list(
            self,
            cage_code=None,
            cage_id=None,
            client_id=None,
            exclude_downstream=None,
            fac_code=None,
            fac_id=None,
            metadata=None,
            rack_code=None,
            rack_id=None,
            row_code=None,
            row_id=None,
            zone_code=None,
            zone_id=None,
        ) -> Dict:
        """List Device Rows

        API Method: device.row_list

        This method is used to list device rows.

        Args:
            cage_code: Cage Code. Defaults to None.
            cage_id: Cage ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            exclude_downstream: Exclude downstream. Defaults to None.
            fac_code: Facility Code. Defaults to None.
            fac_id: Facility ID. Defaults to None.
            metadata: Include Custom Fields. Defaults to None.
            rack_code: Rack Code. Defaults to None.
            rack_id: Rack ID. Defaults to None.
            row_code: Row Code. Defaults to None.
            row_id: Row ID. Defaults to None.
            zone_code: Zone Code. Defaults to None.
            zone_id: Zone ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.row_list',
            **{'cage_code': cage_code} if cage_code else {},
            **{'cage_id': cage_id} if cage_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'exclude_downstream': exclude_downstream} if exclude_downstream else {},
            **{'fac_code': fac_code} if fac_code else {},
            **{'fac_id': fac_id} if fac_id else {},
            **{'metadata': metadata} if metadata else {},
            **{'rack_code': rack_code} if rack_code else {},
            **{'rack_id': rack_id} if rack_id else {},
            **{'row_code': row_code} if row_code else {},
            **{'row_id': row_id} if row_id else {},
            **{'zone_code': zone_code} if zone_code else {},
            **{'zone_id': zone_id} if zone_id else {},
        )

    def row_update(
            self,
            row_id,
            cage_id=None,
            meta_=None,
            row_code=None,
            row_name=None,
            status=None,
        ) -> Dict:
        """Update a row

        API Method: device.row_update

        This method is used to update a row in the system.

        Args:
            row_id: Row ID,
            cage_id: Cage ID. Defaults to None.
            meta_: Custom Fields. Defaults to None.
            row_code: Row Code. Defaults to None.
            row_name: Row Name. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.row_update',
            row_id=row_id,
            **{'cage_id': cage_id} if cage_id else {},
            **{'meta_': meta_} if meta_ else {},
            **{'row_code': row_code} if row_code else {},
            **{'row_name': row_name} if row_name else {},
            **{'status': status} if status else {},
        )

    def storage_delete(
            self,
            device_id,
            item,
        ) -> Dict:
        """Delete a Device's Storage

        API Method: device.storage_delete

        This method is used to delete a device's storage.

        Args:
            device_id: Device ID,
            item: Item,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.storage_delete',
            device_id=device_id,
            item=item,
        )

    def storage_get(
            self,
            device_id,
            item,
        ) -> Dict:
        """Get a Device's Storage

        API Method: device.storage_get

        This method is used to get a device's storage.

        Args:
            device_id: Device ID,
            item: Item,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.storage_get',
            device_id=device_id,
            item=item,
        )

    def storage_list(
            self,
            device_id=None,
            items=None,
        ) -> Dict:
        """List a Device's Storage

        API Method: device.storage_list

        This method is used to list a device's storage.

        Args:
            device_id: Device ID(s). Defaults to None.
            items: Item(s). Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.storage_list',
            **{'device_id': device_id} if device_id else {},
            **{'items': items} if items else {},
        )

    def storage_set(
            self,
            device_id,
            item,
            value,
            encrypt=None,
        ) -> Dict:
        """Set a Device's Storage

        API Method: device.storage_set

        This method is used to set a device's storage.

        Args:
            device_id: Device ID,
            item: Item,
            value: Value,
            encrypt: Encrypt. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.storage_set',
            device_id=device_id,
            item=item,
            value=value,
            **{'encrypt': encrypt} if encrypt else {},
        )

    def tag(
            self,
            device_id,
            tag,
        ) -> Dict:
        """Tag a Device

        API Method: device.tag

        This method is used to tag a device.

        Args:
            device_id: Device ID,
            tag: Tag(s) to set,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.tag',
            device_id=device_id,
            tag=tag,
        )

    def tag_list(
            self,
            device_id=None,
            direction=None,
            has_devices=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List Device Tags

        API Method: device.tag_list

        This method is used to list all device tags.

        Args:
            device_id: Device ID. Defaults to None.
            direction: Direction. Defaults to None.
            has_devices: Devices. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.tag_list',
            **{'device_id': device_id} if device_id else {},
            **{'direction': direction} if direction else {},
            **{'has_devices': has_devices} if has_devices else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def type_add(
            self,
            type,
            back_image_file_id=None,
            block_delete_if_connected=None,
            client_access=None,
            depth=None,
            depth_display_unit=None,
            depth_display_value=None,
            devtype_group_id=None,
            editable_dimensions=None,
            front_image_file_id=None,
            height=None,
            height_display_unit=None,
            height_display_value=None,
            rack_units=None,
            rackable_device=None,
            width=None,
            width_display_unit=None,
            width_display_value=None,
        ) -> Dict:
        """Add a new Device Type

        API Method: device.type_add

        This method is used to add a device type to the system. Device type id is returned on success.

        Args:
            type: Device Type Name,
            back_image_file_id: Back Image File ID. Defaults to None.
            block_delete_if_connected: Block Delete if Connected. Defaults to None.
            client_access: Client Visible. Defaults to None.
            depth: Depth in mm. Defaults to None.
            depth_display_unit: Depth Units. Defaults to None.
            depth_display_value: Depth. Defaults to None.
            devtype_group_id: Device Type Group ID. Defaults to None.
            editable_dimensions: Editable Dimensions. Defaults to None.
            front_image_file_id: Front Image File ID. Defaults to None.
            height: Height in mm. Defaults to None.
            height_display_unit: Height Units. Defaults to None.
            height_display_value: Height. Defaults to None.
            rack_units: Rack Units. Defaults to None.
            rackable_device: Rackable Device. Defaults to None.
            width: Width in mm. Defaults to None.
            width_display_unit: Width Units. Defaults to None.
            width_display_value: Width. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_add',
            type=type,
            **{'back_image_file_id': back_image_file_id} if back_image_file_id else {},
            **{'block_delete_if_connected': block_delete_if_connected} if block_delete_if_connected else {},
            **{'client_access': client_access} if client_access else {},
            **{'depth': depth} if depth else {},
            **{'depth_display_unit': depth_display_unit} if depth_display_unit else {},
            **{'depth_display_value': depth_display_value} if depth_display_value else {},
            **{'devtype_group_id': devtype_group_id} if devtype_group_id else {},
            **{'editable_dimensions': editable_dimensions} if editable_dimensions else {},
            **{'front_image_file_id': front_image_file_id} if front_image_file_id else {},
            **{'height': height} if height else {},
            **{'height_display_unit': height_display_unit} if height_display_unit else {},
            **{'height_display_value': height_display_value} if height_display_value else {},
            **{'rack_units': rack_units} if rack_units else {},
            **{'rackable_device': rackable_device} if rackable_device else {},
            **{'width': width} if width else {},
            **{'width_display_unit': width_display_unit} if width_display_unit else {},
            **{'width_display_value': width_display_value} if width_display_value else {},
        )

    def type_delete(
            self,
            new_type_id,
            type_id,
        ) -> Dict:
        """Delete a Device Type

        API Method: device.type_delete

        This method is used to delete a device type in the system. Child devices must be migrated to a new type

        Args:
            new_type_id: New Type ID,
            type_id: Device Type ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_delete',
            new_type_id=new_type_id,
            type_id=type_id,
        )

    def type_group_add(
            self,
            name,
        ) -> Dict:
        """Add Device Type Group

        API Method: device.type_group_add

        This method is used to add a device type group in the system. Device type group id is returned on success.

        Args:
            name: Device Type Group Name,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_group_add',
            name=name,
        )

    def type_group_delete(
            self,
            devtype_group_id,
        ) -> Dict:
        """Delete Device Type Group

        API Method: device.type_group_delete

        This method is used to delete a device type group in the system.

        Args:
            devtype_group_id: Device Type Group ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_group_delete',
            devtype_group_id=devtype_group_id,
        )

    def type_group_list(
            self,
            devtype_group_id=None,
            metadata=None,
            modules=None,
        ) -> Dict:
        """List Device Type Groups

        API Method: device.type_group_list

        This method is used to list device type groups in the system.

        Args:
            devtype_group_id: Device Type Group ID. Defaults to None.
            metadata: Include Custom Fields. Defaults to None.
            modules: Device Modules. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_group_list',
            **{'devtype_group_id': devtype_group_id} if devtype_group_id else {},
            **{'metadata': metadata} if metadata else {},
            **{'modules': modules} if modules else {},
        )

    def type_group_module_add(
            self,
            devtype_group_id,
            module,
            client_access=None,
            enabled=None,
            priority=None,
        ) -> Dict:
        """Add a Device Module to Device Type Group

        API Method: device.type_group_module_add

        This method is used to add a device module to a device type group.

        Args:
            devtype_group_id: Device Type Group ID,
            module: Device Module Name,
            client_access: Client Access. Defaults to None.
            enabled: Enabled. Defaults to None.
            priority: Module Priority. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_group_module_add',
            devtype_group_id=devtype_group_id,
            module=module,
            **{'client_access': client_access} if client_access else {},
            **{'enabled': enabled} if enabled else {},
            **{'priority': priority} if priority else {},
        )

    def type_group_module_delete(
            self,
            module_id,
        ) -> Dict:
        """Remove a Device Module from a Device Type Group

        API Method: device.type_group_module_delete

        This method is used to delete a device module from a device type group.

        Args:
            module_id: Device Module ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_group_module_delete',
            module_id=module_id,
        )

    def type_group_module_update(
            self,
            module_id,
            client_access=None,
            enabled=None,
            priority=None,
        ) -> Dict:
        """Configure a Device Module in a Device Type Group

        API Method: device.type_group_module_update

        This method is used to configure a device module in a device type group.

        Args:
            module_id: Device Module ID,
            client_access: Client Access. Defaults to None.
            enabled: Enabled. Defaults to None.
            priority: Module Priority. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_group_module_update',
            module_id=module_id,
            **{'client_access': client_access} if client_access else {},
            **{'enabled': enabled} if enabled else {},
            **{'priority': priority} if priority else {},
        )

    def type_group_update(
            self,
            devtype_group_id,
            name=None,
        ) -> Dict:
        """Update a Device Type Group

        API Method: device.type_group_update

        This method is used to update a device type group.

        Args:
            devtype_group_id: Device Type Group ID,
            name: Device Type Group Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_group_update',
            devtype_group_id=devtype_group_id,
            **{'name': name} if name else {},
        )

    def type_list(
            self,
            devtype_group_id=None,
            metadata=None,
            modules=None,
            type_id=None,
        ) -> Dict:
        """List Device Types

        API Method: device.type_list

        This method is used to list device types.

        Args:
            devtype_group_id: Type Group ID. Defaults to None.
            metadata: Custom Fields. Defaults to None.
            modules: Device Modules. Defaults to None.
            type_id: Type ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_list',
            **{'devtype_group_id': devtype_group_id} if devtype_group_id else {},
            **{'metadata': metadata} if metadata else {},
            **{'modules': modules} if modules else {},
            **{'type_id': type_id} if type_id else {},
        )

    def type_module_add(
            self,
            devtype_id,
            module,
            client_access=None,
            enabled=None,
            priority=None,
        ) -> Dict:
        """Add a Device Module to Device Type

        API Method: device.type_module_add

        This method is used to add a device module to a device type.

        Args:
            devtype_id: Device Type ID,
            module: Device Module Name,
            client_access: Client Access. Defaults to None.
            enabled: Enabled. Defaults to None.
            priority: Module Priority. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_module_add',
            devtype_id=devtype_id,
            module=module,
            **{'client_access': client_access} if client_access else {},
            **{'enabled': enabled} if enabled else {},
            **{'priority': priority} if priority else {},
        )

    def type_module_delete(
            self,
            module_id,
        ) -> Dict:
        """Remove a Device Module from a Device Type

        API Method: device.type_module_delete

        This method is used to delete a device module from a device type.

        Args:
            module_id: Device Module ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_module_delete',
            module_id=module_id,
        )

    def type_module_update(
            self,
            module_id,
            client_access=None,
            enabled=None,
            priority=None,
        ) -> Dict:
        """Configure a Device Module in a Device Type

        API Method: device.type_module_update

        This method is used to configure a device module in a device type.

        Args:
            module_id: Device Module ID,
            client_access: Client Access. Defaults to None.
            enabled: Enabled. Defaults to None.
            priority: Module Priority. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_module_update',
            module_id=module_id,
            **{'client_access': client_access} if client_access else {},
            **{'enabled': enabled} if enabled else {},
            **{'priority': priority} if priority else {},
        )

    def type_update(
            self,
            type_id,
            back_image_file_id=None,
            block_delete_if_connected=None,
            client_access=None,
            depth=None,
            depth_display_unit=None,
            depth_display_value=None,
            devtype_group_id=None,
            editable_dimensions=None,
            front_image_file_id=None,
            height=None,
            height_display_unit=None,
            height_display_value=None,
            rack_units=None,
            rackable_device=None,
            remove_back_image=None,
            remove_front_image=None,
            type=None,
            width=None,
            width_display_unit=None,
            width_display_value=None,
        ) -> Dict:
        """Edit a Device Type

        API Method: device.type_update

        This method is used to edit a device type in the system.

        Args:
            type_id: Device Type ID,
            back_image_file_id: Back Image File ID. Defaults to None.
            block_delete_if_connected: Block Delete if Connected. Defaults to None.
            client_access: Client Visible. Defaults to None.
            depth: Depth in mm. Defaults to None.
            depth_display_unit: Depth Units. Defaults to None.
            depth_display_value: Depth. Defaults to None.
            devtype_group_id: Device Type Group ID. Defaults to None.
            editable_dimensions: Editable Dimensions. Defaults to None.
            front_image_file_id: Front Image File ID. Defaults to None.
            height: Height in mm. Defaults to None.
            height_display_unit: Height Units. Defaults to None.
            height_display_value: Height. Defaults to None.
            rack_units: Rack Units. Defaults to None.
            rackable_device: Rackable Device. Defaults to None.
            remove_back_image: Remove Back Image. Defaults to None.
            remove_front_image: Remove Front Image. Defaults to None.
            type: Device Type Name. Defaults to None.
            width: Width in mm. Defaults to None.
            width_display_unit: Width Units. Defaults to None.
            width_display_value: Width. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.type_update',
            type_id=type_id,
            **{'back_image_file_id': back_image_file_id} if back_image_file_id else {},
            **{'block_delete_if_connected': block_delete_if_connected} if block_delete_if_connected else {},
            **{'client_access': client_access} if client_access else {},
            **{'depth': depth} if depth else {},
            **{'depth_display_unit': depth_display_unit} if depth_display_unit else {},
            **{'depth_display_value': depth_display_value} if depth_display_value else {},
            **{'devtype_group_id': devtype_group_id} if devtype_group_id else {},
            **{'editable_dimensions': editable_dimensions} if editable_dimensions else {},
            **{'front_image_file_id': front_image_file_id} if front_image_file_id else {},
            **{'height': height} if height else {},
            **{'height_display_unit': height_display_unit} if height_display_unit else {},
            **{'height_display_value': height_display_value} if height_display_value else {},
            **{'rack_units': rack_units} if rack_units else {},
            **{'rackable_device': rackable_device} if rackable_device else {},
            **{'remove_back_image': remove_back_image} if remove_back_image else {},
            **{'remove_front_image': remove_front_image} if remove_front_image else {},
            **{'type': type} if type else {},
            **{'width': width} if width else {},
            **{'width_display_unit': width_display_unit} if width_display_unit else {},
            **{'width_display_value': width_display_value} if width_display_value else {},
        )

    def untag(
            self,
            device_id,
            tag,
        ) -> Dict:
        """Untag a Device

        API Method: device.untag

        This method is used to untag a device.

        Args:
            device_id: Device ID,
            tag: Tag(s) to remove,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.untag',
            device_id=device_id,
            tag=tag,
        )

    def update(
            self,
            device_id,
            back_image=None,
            back_image_file_id=None,
            client_id=None,
            client_owned=None,
            connection_node_type_id=None,
            dev_desc=None,
            front_image=None,
            front_image_file_id=None,
            height=None,
            label=None,
            meta=None,
            parent=None,
            rack_id=None,
            rack_pos=None,
            remove_back_image=None,
            remove_front_image=None,
            service_id=None,
            type_id=None,
        ) -> Dict:
        """Update a Device

        API Method: device.update

        This method is used to update a device.

        Args:
            device_id: Device ID,
            back_image: Attachment. Defaults to None.
            back_image_file_id: Back Image File ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            client_owned: Client Owns Physical Device. Defaults to None.
            connection_node_type_id: Connection Node Type ID. Defaults to None.
            dev_desc: Device Description. Defaults to None.
            front_image: Attachment. Defaults to None.
            front_image_file_id: Front Image File ID. Defaults to None.
            height: Device Height. Defaults to None.
            label: Device Label. Defaults to None.
            meta: Custom Fields. Defaults to None.
            parent: Parent Device ID. Defaults to None.
            rack_id: Rack ID. Defaults to None.
            rack_pos: Position Within Rack. Defaults to None.
            remove_back_image: Remove Back Image. Defaults to None.
            remove_front_image: Remove Front Image. Defaults to None.
            service_id: Service ID. Defaults to None.
            type_id: Device Type ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.update',
            device_id=device_id,
            **{'back_image': back_image} if back_image else {},
            **{'back_image_file_id': back_image_file_id} if back_image_file_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'client_owned': client_owned} if client_owned else {},
            **{'connection_node_type_id': connection_node_type_id} if connection_node_type_id else {},
            **{'dev_desc': dev_desc} if dev_desc else {},
            **{'front_image': front_image} if front_image else {},
            **{'front_image_file_id': front_image_file_id} if front_image_file_id else {},
            **{'height': height} if height else {},
            **{'label': label} if label else {},
            **{'meta': meta} if meta else {},
            **{'parent': parent} if parent else {},
            **{'rack_id': rack_id} if rack_id else {},
            **{'rack_pos': rack_pos} if rack_pos else {},
            **{'remove_back_image': remove_back_image} if remove_back_image else {},
            **{'remove_front_image': remove_front_image} if remove_front_image else {},
            **{'service_id': service_id} if service_id else {},
            **{'type_id': type_id} if type_id else {},
        )

    def vlan_add(
            self,
            name,
            add_facilities=None,
            add_ranges=None,
            desc=None,
            hsrp=None,
            min_available=None,
            notify_address=None,
            shared=None,
            vlan_assignable=None,
            vlan_type_id=None,
        ) -> Dict:
        """Add a VLAN range

        API Method: device.vlan_add

        This method is used to add a VLAN range in the system.

        Args:
            name: Name,
            add_facilities: Add Facilities. Defaults to None.
            add_ranges: Add VLAN Ranges. Defaults to None.
            desc: Description. Defaults to None.
            hsrp: HSRP. Defaults to None.
            min_available: Alert threshold. Defaults to None.
            notify_address: Notify Address. Defaults to None.
            shared: Shared. Defaults to None.
            vlan_assignable: VLAN Assignable. Defaults to None.
            vlan_type_id: VLAN Type Id. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.vlan_add',
            name=name,
            **{'add_facilities': add_facilities} if add_facilities else {},
            **{'add_ranges': add_ranges} if add_ranges else {},
            **{'desc': desc} if desc else {},
            **{'hsrp': hsrp} if hsrp else {},
            **{'min_available': min_available} if min_available else {},
            **{'notify_address': notify_address} if notify_address else {},
            **{'shared': shared} if shared else {},
            **{'vlan_assignable': vlan_assignable} if vlan_assignable else {},
            **{'vlan_type_id': vlan_type_id} if vlan_type_id else {},
        )

    def vlan_delete(
            self,
            vlan_range_id,
        ) -> Dict:
        """Delete a Vlan Range

        API Method: device.vlan_delete

        This method is used to delete a Vlan Range.

        Args:
            vlan_range_id: Vlan Range ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.vlan_delete',
            vlan_range_id=vlan_range_id,
        )

    def vlan_get_available(
            self,
            fac_id=None,
            is_hsrp=None,
            limit=None,
            vlan_range_id=None,
        ) -> Dict:
        """List Available VLANs

        API Method: device.vlan_get_available

        This method is used to list available VLAN numbers, optionally filtered by:
- VLAN range id (vlan_range_id)
- facility id (fac_id)
- HSRP (is_hsrp)
optionally limited by:
- limit (limit).
Returns an array of all available VLAN numbers with VLAN range ID and title.

        Args:
            fac_id: Facility ID. Defaults to None.
            is_hsrp: HSRP Flag. Defaults to None.
            limit: Results Limit. Defaults to None.
            vlan_range_id: VLAN Range ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.vlan_get_available',
            **{'fac_id': fac_id} if fac_id else {},
            **{'is_hsrp': is_hsrp} if is_hsrp else {},
            **{'limit': limit} if limit else {},
            **{'vlan_range_id': vlan_range_id} if vlan_range_id else {},
        )

    def vlan_update(
            self,
            vlan_range_id,
            add_facilities=None,
            add_ranges=None,
            desc=None,
            hsrp=None,
            min_available=None,
            name=None,
            notify_address=None,
            remove_facilities=None,
            shared=None,
            update_ranges=None,
            vlan_assignable=None,
            vlan_type_id=None,
        ) -> Dict:
        """Update a VLAN range

        API Method: device.vlan_update

        This method is used to update a VLAN range in the system.

        Args:
            vlan_range_id: VLAN range Id,
            add_facilities: Add Facilities. Defaults to None.
            add_ranges: Add VLAN Ranges. Defaults to None.
            desc: Description. Defaults to None.
            hsrp: HSRP. Defaults to None.
            min_available: Alert threshold. Defaults to None.
            name: Name. Defaults to None.
            notify_address: Notify Address. Defaults to None.
            remove_facilities: Add Facilities. Defaults to None.
            shared: Shared. Defaults to None.
            update_ranges: Update VLAN Ranges. Defaults to None.
            vlan_assignable: VLAN Assignable. Defaults to None.
            vlan_type_id: VLAN Type Id. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.vlan_update',
            vlan_range_id=vlan_range_id,
            **{'add_facilities': add_facilities} if add_facilities else {},
            **{'add_ranges': add_ranges} if add_ranges else {},
            **{'desc': desc} if desc else {},
            **{'hsrp': hsrp} if hsrp else {},
            **{'min_available': min_available} if min_available else {},
            **{'name': name} if name else {},
            **{'notify_address': notify_address} if notify_address else {},
            **{'remove_facilities': remove_facilities} if remove_facilities else {},
            **{'shared': shared} if shared else {},
            **{'update_ranges': update_ranges} if update_ranges else {},
            **{'vlan_assignable': vlan_assignable} if vlan_assignable else {},
            **{'vlan_type_id': vlan_type_id} if vlan_type_id else {},
        )

    def zone_add(
            self,
            fac_id,
            ac_power_capacity=None,
            area_display_value=None,
            assigned_date=None,
            client_id=None,
            dc_power_capacity=None,
            meta_=None,
            rofr_expiration_date=None,
            status=None,
            zone_code=None,
            zone_name=None,
        ) -> Dict:
        """Add a zone

        API Method: device.zone_add

        This method is used to add a zone in the system.

        Args:
            fac_id: Facility ID,
            ac_power_capacity: AC Power Capacity. Defaults to None.
            area_display_value: Area Size Value. Defaults to None.
            assigned_date: Assigned Date. Defaults to None.
            client_id: Client ID. Defaults to None.
            dc_power_capacity: DC Power Capacity. Defaults to None.
            meta_: Custom Fields. Defaults to None.
            rofr_expiration_date: ROFR Expiration Date. Defaults to None.
            status: Status. Defaults to None.
            zone_code: Zone Code. Defaults to None.
            zone_name: Zone Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.zone_add',
            fac_id=fac_id,
            **{'ac_power_capacity': ac_power_capacity} if ac_power_capacity else {},
            **{'area_display_value': area_display_value} if area_display_value else {},
            **{'assigned_date': assigned_date} if assigned_date else {},
            **{'client_id': client_id} if client_id else {},
            **{'dc_power_capacity': dc_power_capacity} if dc_power_capacity else {},
            **{'meta_': meta_} if meta_ else {},
            **{'rofr_expiration_date': rofr_expiration_date} if rofr_expiration_date else {},
            **{'status': status} if status else {},
            **{'zone_code': zone_code} if zone_code else {},
            **{'zone_name': zone_name} if zone_name else {},
        )

    def zone_list(
            self,
            cage_code=None,
            cage_id=None,
            client_id=None,
            exclude_downstream=None,
            fac_code=None,
            fac_id=None,
            metadata=None,
            rack_code=None,
            rack_id=None,
            row_code=None,
            row_id=None,
            zone_code=None,
            zone_id=None,
        ) -> Dict:
        """List Device Zones

        API Method: device.zone_list

        This method is used to list device zones.

        Args:
            cage_code: Cage Code. Defaults to None.
            cage_id: Cage ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            exclude_downstream: Exclude downstream. Defaults to None.
            fac_code: Facility Code. Defaults to None.
            fac_id: Facility ID. Defaults to None.
            metadata: Include Custom Fields. Defaults to None.
            rack_code: Rack Code. Defaults to None.
            rack_id: Rack ID. Defaults to None.
            row_code: Row Code. Defaults to None.
            row_id: Row ID. Defaults to None.
            zone_code: Zone Code. Defaults to None.
            zone_id: Zone ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.zone_list',
            **{'cage_code': cage_code} if cage_code else {},
            **{'cage_id': cage_id} if cage_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'exclude_downstream': exclude_downstream} if exclude_downstream else {},
            **{'fac_code': fac_code} if fac_code else {},
            **{'fac_id': fac_id} if fac_id else {},
            **{'metadata': metadata} if metadata else {},
            **{'rack_code': rack_code} if rack_code else {},
            **{'rack_id': rack_id} if rack_id else {},
            **{'row_code': row_code} if row_code else {},
            **{'row_id': row_id} if row_id else {},
            **{'zone_code': zone_code} if zone_code else {},
            **{'zone_id': zone_id} if zone_id else {},
        )

    def zone_update(
            self,
            zone_id,
            ac_power_capacity=None,
            area_display_value=None,
            assigned_date=None,
            client_id=None,
            dc_power_capacity=None,
            fac_id=None,
            meta_=None,
            rofr_expiration_date=None,
            status=None,
            zone_code=None,
            zone_name=None,
        ) -> Dict:
        """Update a zone

        API Method: device.zone_update

        This method is used to update a zone in the system.

        Args:
            zone_id: Zone ID,
            ac_power_capacity: AC Power Capacity. Defaults to None.
            area_display_value: Area Size Value. Defaults to None.
            assigned_date: Assigned Date. Defaults to None.
            client_id: Client ID. Defaults to None.
            dc_power_capacity: DC Power Capacity. Defaults to None.
            fac_id: Facility ID. Defaults to None.
            meta_: Custom Fields. Defaults to None.
            rofr_expiration_date: ROFR Expiration Date. Defaults to None.
            status: Status. Defaults to None.
            zone_code: Zone Code. Defaults to None.
            zone_name: Zone Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'device.zone_update',
            zone_id=zone_id,
            **{'ac_power_capacity': ac_power_capacity} if ac_power_capacity else {},
            **{'area_display_value': area_display_value} if area_display_value else {},
            **{'assigned_date': assigned_date} if assigned_date else {},
            **{'client_id': client_id} if client_id else {},
            **{'dc_power_capacity': dc_power_capacity} if dc_power_capacity else {},
            **{'fac_id': fac_id} if fac_id else {},
            **{'meta_': meta_} if meta_ else {},
            **{'rofr_expiration_date': rofr_expiration_date} if rofr_expiration_date else {},
            **{'status': status} if status else {},
            **{'zone_code': zone_code} if zone_code else {},
            **{'zone_name': zone_name} if zone_name else {},
        )
