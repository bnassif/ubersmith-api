from typing import Dict
from ubersmith.client.section import *

class ClientAPI(Section):
    """
    Auto-generated section for ``client``.

    Contains all ``client.*`` API methods.
    """

    def ach_add(
            self,
            ach_acct,
            user_login,
            ach_aba=None,
            ach_bank=None,
            ach_type=None,
            address=None,
            city=None,
            company=None,
            country=None,
            email=None,
            fname=None,
            lname=None,
            phone=None,
            set_default=None,
            state=None,
            zip=None,
        ) -> Dict:
        """Add a New Bank Account

        API Method: client.ach_add

        This method is used to add a new bank account to a client's account.

        Args:
            ach_acct: Account Number,
            user_login: Client Login,
            ach_aba: Routing Number. Defaults to None.
            ach_bank: Bank Name. Defaults to None.
            ach_type: Account Type. Defaults to None.
            address: Street Address. Defaults to None.
            city: City. Defaults to None.
            company: Company Name. Defaults to None.
            country: Country. Defaults to None.
            email: Email Address. Defaults to None.
            fname: First Name. Defaults to None.
            lname: Last Name. Defaults to None.
            phone: Telephone Number. Defaults to None.
            set_default: Set as default. Defaults to None.
            state: State. Defaults to None.
            zip: ZIP or Postal Code. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.ach_add',
            ach_acct=ach_acct,
            user_login=user_login,
            **{'ach_aba': ach_aba} if ach_aba else {},
            **{'ach_bank': ach_bank} if ach_bank else {},
            **{'ach_type': ach_type} if ach_type else {},
            **{'address': address} if address else {},
            **{'city': city} if city else {},
            **{'company': company} if company else {},
            **{'country': country} if country else {},
            **{'email': email} if email else {},
            **{'fname': fname} if fname else {},
            **{'lname': lname} if lname else {},
            **{'phone': phone} if phone else {},
            **{'set_default': set_default} if set_default else {},
            **{'state': state} if state else {},
            **{'zip': zip} if zip else {},
        )

    def ach_delete(
            self,
            billing_info_id,
            source=None,
        ) -> Dict:
        """Delete a Bank Account

        API Method: client.ach_delete

        This method is used to delete a bank account already on file.

        Args:
            billing_info_id: Bank Account ID,
            source: Source. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.ach_delete',
            billing_info_id=billing_info_id,
            **{'source': source} if source else {},
        )

    def ach_update(
            self,
            billing_info_id,
            ach_aba=None,
            ach_acct=None,
            ach_bank=None,
            ach_type=None,
            address=None,
            city=None,
            company=None,
            country=None,
            email=None,
            fname=None,
            lname=None,
            phone=None,
            set_default=None,
            state=None,
            zip=None,
        ) -> Dict:
        """Update a Bank Account

        API Method: client.ach_update

        This method is used to update a bank account already on file.

        Args:
            billing_info_id: Bank Account ID,
            ach_aba: Routing Number. Defaults to None.
            ach_acct: Account Number. Defaults to None.
            ach_bank: Bank Name. Defaults to None.
            ach_type: Account Type. Defaults to None.
            address: Street Address. Defaults to None.
            city: City. Defaults to None.
            company: Company Name. Defaults to None.
            country: Country. Defaults to None.
            email: Email Address. Defaults to None.
            fname: First Name. Defaults to None.
            lname: Last Name. Defaults to None.
            phone: Telephone Number. Defaults to None.
            set_default: Set as default. Defaults to None.
            state: State. Defaults to None.
            zip: ZIP or Postal Code. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.ach_update',
            billing_info_id=billing_info_id,
            **{'ach_aba': ach_aba} if ach_aba else {},
            **{'ach_acct': ach_acct} if ach_acct else {},
            **{'ach_bank': ach_bank} if ach_bank else {},
            **{'ach_type': ach_type} if ach_type else {},
            **{'address': address} if address else {},
            **{'city': city} if city else {},
            **{'company': company} if company else {},
            **{'country': country} if country else {},
            **{'email': email} if email else {},
            **{'fname': fname} if fname else {},
            **{'lname': lname} if lname else {},
            **{'phone': phone} if phone else {},
            **{'set_default': set_default} if set_default else {},
            **{'state': state} if state else {},
            **{'zip': zip} if zip else {},
        )

    def add(
            self,
            access=None,
            active=None,
            address=None,
            auto_apply_credit=None,
            brand_id=None,
            charge_days=None,
            city=None,
            company=None,
            country=None,
            datedue=None,
            datepay=None,
            datesend=None,
            default_renew=None,
            discount=None,
            discount_type=None,
            email=None,
            fax=None,
            first=None,
            grace_due=None,
            last=None,
            late_fee_scheme_id=None,
            login_enabled=None,
            meta=None,
            phone=None,
            prebill_days=None,
            prebill_method=None,
            priority=None,
            prorate_min_days=None,
            referred=None,
            referred_by=None,
            retry_every=None,
            state=None,
            strict=None,
            uber_login=None,
            uber_pass=None,
            vat_id=None,
            zip=None,
        ) -> Dict:
        """Add a New Client

        API Method: client.add

        This method is used to add a new client to the system.

        Args:
            access: Access Settings. Defaults to None.
            active: Client Status. Defaults to None.
            address: Street Address. Defaults to None.
            auto_apply_credit: Auto Apply Credit. Defaults to None.
            brand_id: Brand ID. Defaults to None.
            charge_days: Charge Delay. Defaults to None.
            city: City. Defaults to None.
            company: Company. Defaults to None.
            country: Country. Defaults to None.
            datedue: Invoice Due Date. Defaults to None.
            datepay: Grace Period. Defaults to None.
            datesend: Invoice Send Date. Defaults to None.
            default_renew: Default Renew Date. Defaults to None.
            discount: Discount Level. Defaults to None.
            discount_type: Discount Type. Defaults to None.
            email: Email Address. Defaults to None.
            fax: Fax Number. Defaults to None.
            first: First Name. Defaults to None.
            grace_due: Due Date Method. Defaults to None.
            last: Last Name. Defaults to None.
            late_fee_scheme_id: Late Fee Schedule. Defaults to None.
            login_enabled: Enable Login. Defaults to None.
            meta: Custom Fields. Defaults to None.
            phone: Telephone Number. Defaults to None.
            prebill_days: Pre Bill Days. Defaults to None.
            prebill_method: Pre Bill Method. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            prorate_min_days: Prorate Min. Days. Defaults to None.
            referred: Referred By. Defaults to None.
            referred_by: Referred By. Defaults to None.
            retry_every: Retry Interval. Defaults to None.
            state: State/Province. Defaults to None.
            strict: Strict Mode. Defaults to None.
            uber_login: Username. Defaults to None.
            uber_pass: Password. Defaults to None.
            vat_id: VAT ID. Defaults to None.
            zip: Zip/Postcode. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.add',
            **{'access': access} if access else {},
            **{'active': active} if active else {},
            **{'address': address} if address else {},
            **{'auto_apply_credit': auto_apply_credit} if auto_apply_credit else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'charge_days': charge_days} if charge_days else {},
            **{'city': city} if city else {},
            **{'company': company} if company else {},
            **{'country': country} if country else {},
            **{'datedue': datedue} if datedue else {},
            **{'datepay': datepay} if datepay else {},
            **{'datesend': datesend} if datesend else {},
            **{'default_renew': default_renew} if default_renew else {},
            **{'discount': discount} if discount else {},
            **{'discount_type': discount_type} if discount_type else {},
            **{'email': email} if email else {},
            **{'fax': fax} if fax else {},
            **{'first': first} if first else {},
            **{'grace_due': grace_due} if grace_due else {},
            **{'last': last} if last else {},
            **{'late_fee_scheme_id': late_fee_scheme_id} if late_fee_scheme_id else {},
            **{'login_enabled': login_enabled} if login_enabled else {},
            **{'meta': meta} if meta else {},
            **{'phone': phone} if phone else {},
            **{'prebill_days': prebill_days} if prebill_days else {},
            **{'prebill_method': prebill_method} if prebill_method else {},
            **{'priority': priority} if priority else {},
            **{'prorate_min_days': prorate_min_days} if prorate_min_days else {},
            **{'referred': referred} if referred else {},
            **{'referred_by': referred_by} if referred_by else {},
            **{'retry_every': retry_every} if retry_every else {},
            **{'state': state} if state else {},
            **{'strict': strict} if strict else {},
            **{'uber_login': uber_login} if uber_login else {},
            **{'uber_pass': uber_pass} if uber_pass else {},
            **{'vat_id': vat_id} if vat_id else {},
            **{'zip': zip} if zip else {},
        )

    def avatar_get(
            self,
            client_id=None,
            contact_id=None,
            email=None,
            gravatar_fallback=None,
            size=None,
        ) -> Dict:
        """Retrieve a Client Avatar

        API Method: client.avatar_get

        This method is used to retrieve a client or contact avatar.

        Args:
            client_id: Client ID. Defaults to None.
            contact_id: Contact ID. Defaults to None.
            email: Email. Defaults to None.
            gravatar_fallback: Gravatar Fallback. Defaults to None.
            size: Size. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.avatar_get',
            **{'client_id': client_id} if client_id else {},
            **{'contact_id': contact_id} if contact_id else {},
            **{'email': email} if email else {},
            **{'gravatar_fallback': gravatar_fallback} if gravatar_fallback else {},
            **{'size': size} if size else {},
        )

    def avatar_set(
            self,
            avatar=None,
            client_id=None,
            contact_id=None,
        ) -> Dict:
        """Set a Client Avatar

        API Method: client.avatar_set

        This method is used to set a client or contact avatar.

        Args:
            avatar: Attachment. Defaults to None.
            client_id: Client ID. Defaults to None.
            contact_id: Contact ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.avatar_set',
            **{'avatar': avatar} if avatar else {},
            **{'client_id': client_id} if client_id else {},
            **{'contact_id': contact_id} if contact_id else {},
        )

    def ba_add(
            self,
            cancel_url,
            client_id,
            gateway,
            return_url,
        ) -> Dict:
        """Add a New Billing agreement

        API Method: client.ba_add

        This method is used to start a new Billing agreement creation process

        Args:
            cancel_url: Cancel URL,
            client_id: Client id,
            gateway: Gateway,
            return_url: Return URL,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.ba_add',
            cancel_url=cancel_url,
            client_id=client_id,
            gateway=gateway,
            return_url=return_url,
        )

    def ba_approve(
            self,
            billing_info_id,
        ) -> Dict:
        """Approve a new Billing agreement

        API Method: client.ba_approve

        This method is used to finish a new Billing agreement creation process

        Args:
            billing_info_id: Id of the billing agreement,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.ba_approve',
            billing_info_id=billing_info_id,
        )

    def ba_delete(
            self,
            billing_info_id,
        ) -> Dict:
        """Delete a Billing agreement

        API Method: client.ba_delete

        This method is used to delete a Billing Agreement

        Args:
            billing_info_id: Id of the billing agreement,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.ba_delete',
            billing_info_id=billing_info_id,
        )

    def ba_get(
            self,
            billing_info_id,
        ) -> Dict:
        """Get a Billing agreement's information

        API Method: client.ba_get

        This method is used to fetch a Billing Agreement's information

        Args:
            billing_info_id: Id of the billing agreement,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.ba_get',
            billing_info_id=billing_info_id,
        )

    def ba_import(
            self,
            agreement_id,
            client_id,
            gateway,
            end_date=None,
            overall_limit=None,
            payment_limit=None,
            start_date=None,
        ) -> Dict:
        """Import an existing Billing agreement

        API Method: client.ba_import

        This method is used to import a Billing agreement

        Args:
            agreement_id: Agreement id,
            client_id: Client id,
            gateway: Gateway,
            end_date: End date. Defaults to None.
            overall_limit: Overall limit. Defaults to None.
            payment_limit: Payment limit. Defaults to None.
            start_date: Start date. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.ba_import',
            agreement_id=agreement_id,
            client_id=client_id,
            gateway=gateway,
            **{'end_date': end_date} if end_date else {},
            **{'overall_limit': overall_limit} if overall_limit else {},
            **{'payment_limit': payment_limit} if payment_limit else {},
            **{'start_date': start_date} if start_date else {},
        )

    def ba_list(
            self,
            client_id,
        ) -> Dict:
        """List available Billing agreements

        API Method: client.ba_list

        This method is used to list all available Billing Agreements

        Args:
            client_id: Client id,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.ba_list',
            client_id=client_id,
        )

    def billing_dispute_add(
            self,
            description,
            invoice_id,
            user_opened=None,
        ) -> Dict:
        """Add a new Billing Dispute

        API Method: client.billing_dispute_add

        This method is used to add a billing dispute for an invoice.

        Args:
            description: Description,
            invoice_id: Invoice ID,
            user_opened: User ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.billing_dispute_add',
            description=description,
            invoice_id=invoice_id,
            **{'user_opened': user_opened} if user_opened else {},
        )

    def billing_dispute_get(
            self,
            billing_dispute_id,
        ) -> Dict:
        """Get a Billing Dispute

        API Method: client.billing_dispute_get

        This method is used to get a billing dispute.

        Args:
            billing_dispute_id: Billing Dispute ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.billing_dispute_get',
            billing_dispute_id=billing_dispute_id,
        )

    def billing_dispute_list(
            self,
            invoice_id,
            direction=None,
            limit=None,
            offset=None,
            open=None,
            order_by=None,
        ) -> Dict:
        """List billing disputes associated with each invoice

        API Method: client.billing_dispute_list

        This method is used to list an invoice's billing disputes.

        Args:
            invoice_id: Invoice ID,
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            open: Open Dispute Flag. Defaults to None.
            order_by: Order By. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.billing_dispute_list',
            invoice_id=invoice_id,
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'open': open} if open else {},
            **{'order_by': order_by} if order_by else {},
        )

    def billing_dispute_update(
            self,
            billing_dispute_id,
            close_dispute=None,
            description=None,
            user_closed=None,
        ) -> Dict:
        """Update a Billing Dispute

        API Method: client.billing_dispute_update

        This method is used to update a billing dispute.

        Args:
            billing_dispute_id: Billing Dispute ID,
            close_dispute: Close Dispute Flag. Defaults to None.
            description: Description. Defaults to None.
            user_closed: User ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.billing_dispute_update',
            billing_dispute_id=billing_dispute_id,
            **{'close_dispute': close_dispute} if close_dispute else {},
            **{'description': description} if description else {},
            **{'user_closed': user_closed} if user_closed else {},
        )

    def cc_add(
            self,
            cc_num,
            client_id,
            country,
            address=None,
            cc_cvv2=None,
            cc_expire=None,
            cc_token=None,
            cc_type=None,
            city=None,
            company=None,
            email=None,
            fname=None,
            lname=None,
            phone=None,
            set_default=None,
            state=None,
            zip=None,
        ) -> Dict:
        """Add a New Credit Card

        API Method: client.cc_add

        This method is used to add a new credit card to a client's account.

        Args:
            cc_num: Credit Card Number,
            client_id: Client Login,
            country: Country,
            address: Street Address. Defaults to None.
            cc_cvv2: CVV/CVC Code. Defaults to None.
            cc_expire: Expiration Date. Defaults to None.
            cc_token: Tokenized Card. Defaults to None.
            cc_type: Card Type. Defaults to None.
            city: City. Defaults to None.
            company: Company Name. Defaults to None.
            email: Email Address. Defaults to None.
            fname: First Name. Defaults to None.
            lname: Last Name. Defaults to None.
            phone: Telephone Number. Defaults to None.
            set_default: Set as default. Defaults to None.
            state: State. Defaults to None.
            zip: ZIP or Postal Code. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.cc_add',
            cc_num=cc_num,
            client_id=client_id,
            country=country,
            **{'address': address} if address else {},
            **{'cc_cvv2': cc_cvv2} if cc_cvv2 else {},
            **{'cc_expire': cc_expire} if cc_expire else {},
            **{'cc_token': cc_token} if cc_token else {},
            **{'cc_type': cc_type} if cc_type else {},
            **{'city': city} if city else {},
            **{'company': company} if company else {},
            **{'email': email} if email else {},
            **{'fname': fname} if fname else {},
            **{'lname': lname} if lname else {},
            **{'phone': phone} if phone else {},
            **{'set_default': set_default} if set_default else {},
            **{'state': state} if state else {},
            **{'zip': zip} if zip else {},
        )

    def cc_delete(
            self,
            billing_info_id,
            source=None,
        ) -> Dict:
        """Delete a Credit Card

        API Method: client.cc_delete

        This method is used to delete a credit card already on file.

        Args:
            billing_info_id: Bank Account ID,
            source: Source. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.cc_delete',
            billing_info_id=billing_info_id,
            **{'source': source} if source else {},
        )

    def cc_info(
            self,
            billing_info_id=None,
            client_id=None,
        ) -> Dict:
        """List a Client's Credit Card Details

        API Method: client.cc_info

        This method is used to get a client's credit card information.

        Args:
            billing_info_id: Credit Card ID. Defaults to None.
            client_id: Client ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.cc_info',
            **{'billing_info_id': billing_info_id} if billing_info_id else {},
            **{'client_id': client_id} if client_id else {},
        )

    def cc_update(
            self,
            billing_info_id,
            address=None,
            cc_cvv2=None,
            cc_expire=None,
            cc_num=None,
            city=None,
            company=None,
            country=None,
            email=None,
            fname=None,
            lname=None,
            phone=None,
            set_default=None,
            state=None,
            zip=None,
        ) -> Dict:
        """Update a Credit Card

        API Method: client.cc_update

        This method is used to update a credit card already on file.

        Args:
            billing_info_id: Credit Card ID,
            address: Street Address. Defaults to None.
            cc_cvv2: CVV/CVC Code. Defaults to None.
            cc_expire: Expiration Date. Defaults to None.
            cc_num: Credit Card Number. Defaults to None.
            city: City. Defaults to None.
            company: Company Name. Defaults to None.
            country: Country. Defaults to None.
            email: Email Address. Defaults to None.
            fname: First Name. Defaults to None.
            lname: Last Name. Defaults to None.
            phone: Telephone Number. Defaults to None.
            set_default: Set as default. Defaults to None.
            state: State. Defaults to None.
            zip: ZIP or Postal Code. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.cc_update',
            billing_info_id=billing_info_id,
            **{'address': address} if address else {},
            **{'cc_cvv2': cc_cvv2} if cc_cvv2 else {},
            **{'cc_expire': cc_expire} if cc_expire else {},
            **{'cc_num': cc_num} if cc_num else {},
            **{'city': city} if city else {},
            **{'company': company} if company else {},
            **{'country': country} if country else {},
            **{'email': email} if email else {},
            **{'fname': fname} if fname else {},
            **{'lname': lname} if lname else {},
            **{'phone': phone} if phone else {},
            **{'set_default': set_default} if set_default else {},
            **{'state': state} if state else {},
            **{'zip': zip} if zip else {},
        )

    def charge_log_list(
            self,
            begin=None,
            brand_id=None,
            card_type=None,
            charge_id=None,
            client_id=None,
            direction=None,
            end=None,
            gateway=None,
            invoice_id=None,
            limit=None,
            offset=None,
            order_by=None,
            success=None,
        ) -> Dict:
        """List Charge Logs

        API Method: client.charge_log_list

        This method is used to list charge logs in the system.

        Args:
            begin: Begin Time. Defaults to None.
            brand_id: Brand ID. Defaults to None.
            card_type: Credit Card Type. Defaults to None.
            charge_id: Charge Log ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            direction: Direction. Defaults to None.
            end: End Time. Defaults to None.
            gateway: Payment Gateway. Defaults to None.
            invoice_id: Invoice ID. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            success: Successful Charge. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.charge_log_list',
            **{'begin': begin} if begin else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'card_type': card_type} if card_type else {},
            **{'charge_id': charge_id} if charge_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'direction': direction} if direction else {},
            **{'end': end} if end else {},
            **{'gateway': gateway} if gateway else {},
            **{'invoice_id': invoice_id} if invoice_id else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'success': success} if success else {},
        )

    def comment_list(
            self,
            client_id,
            client_viewable=None,
            direction=None,
            filter_text=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List a Client's Comments

        API Method: client.comment_list

        This method is used to list a client's comments.

        Args:
            client_id: Client ID,
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
            'client.comment_list',
            client_id=client_id,
            **{'client_viewable': client_viewable} if client_viewable else {},
            **{'direction': direction} if direction else {},
            **{'filter_text': filter_text} if filter_text else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def contact_add(
            self,
            client_id,
            access=None,
            description=None,
            email=None,
            login=None,
            login_enabled=None,
            meta=None,
            password=None,
            phone=None,
            prefer_lang=None,
            real_name=None,
            roles=None,
            rwhois_contact=None,
        ) -> Dict:
        """Add a New Contact

        API Method: client.contact_add

        This method is used to add a new contact to a client's account.

        Args:
            client_id: Client ID,
            access: Access Settings. Defaults to None.
            description: Description. Defaults to None.
            email: Email Address. Defaults to None.
            login: Login Username. Defaults to None.
            login_enabled: Enable Login. Defaults to None.
            meta: Custom Fields. Defaults to None.
            password: Password. Defaults to None.
            phone: Telephone Number. Defaults to None.
            prefer_lang: Preferred Interface Language. Defaults to None.
            real_name: Contact's Name. Defaults to None.
            roles: Contact Roles. Defaults to None.
            rwhois_contact: RWhois Role. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_add',
            client_id=client_id,
            **{'access': access} if access else {},
            **{'description': description} if description else {},
            **{'email': email} if email else {},
            **{'login': login} if login else {},
            **{'login_enabled': login_enabled} if login_enabled else {},
            **{'meta': meta} if meta else {},
            **{'password': password} if password else {},
            **{'phone': phone} if phone else {},
            **{'prefer_lang': prefer_lang} if prefer_lang else {},
            **{'real_name': real_name} if real_name else {},
            **{'roles': roles} if roles else {},
            **{'rwhois_contact': rwhois_contact} if rwhois_contact else {},
        )

    def contact_delete(
            self,
            contact_id,
            client_id=None,
        ) -> Dict:
        """Deactivate a Contact

        API Method: client.contact_delete

        This method is used to deactivate a contact from a client's account. To reactivate a contact, set active=1 on client.contact_update.

        Args:
            contact_id: Contact ID,
            client_id: Client Login. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_delete',
            contact_id=contact_id,
            **{'client_id': client_id} if client_id else {},
        )

    def contact_facility_add(
            self,
            contact_id,
            fac_id,
            active=None,
            admin=None,
            escalation_priority=None,
            notes=None,
            notification=None,
            physical_entry=None,
            remote_hands=None,
            tech_support=None,
            thirdparty_entry=None,
        ) -> Dict:
        """Add Facility Contact

        API Method: client.contact_facility_add

        This method adds a new facility-contact and returns the newly created object. A feature of this method allows for updating facility contacts whose permissions had previously been revoked, their 'active' flag having been set to false. In such cases, the archived ID for the object record will be conserved to ease reconciliation efforts.

        Args:
            contact_id: Contact ID,
            fac_id: Facility ID,
            active: Access active. Defaults to None.
            admin: Contact Admin. Defaults to None.
            escalation_priority: Escalation Priority. Defaults to None.
            notes: Notes. Defaults to None.
            notification: Notification. Defaults to None.
            physical_entry: Entry. Defaults to None.
            remote_hands: Remote Hands. Defaults to None.
            tech_support: Technical Support. Defaults to None.
            thirdparty_entry: Third-Party Entry. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_facility_add',
            contact_id=contact_id,
            fac_id=fac_id,
            **{'active': active} if active else {},
            **{'admin': admin} if admin else {},
            **{'escalation_priority': escalation_priority} if escalation_priority else {},
            **{'notes': notes} if notes else {},
            **{'notification': notification} if notification else {},
            **{'physical_entry': physical_entry} if physical_entry else {},
            **{'remote_hands': remote_hands} if remote_hands else {},
            **{'tech_support': tech_support} if tech_support else {},
            **{'thirdparty_entry': thirdparty_entry} if thirdparty_entry else {},
        )

    def contact_facility_escalation(
            self,
            client_id,
            fac_id,
            priorities,
        ) -> Dict:
        """Facility Contact Escalation

        API Method: client.contact_facility_escalation

        This method updates a facility-contacts list with new escalation priorities.

        Args:
            client_id: Client ID,
            fac_id: Facility ID,
            priorities: Facility priorities,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_facility_escalation',
            client_id=client_id,
            fac_id=fac_id,
            priorities=priorities,
        )

    def contact_facility_list(
            self,
            active=None,
            admin=None,
            client_id=None,
            contact_id=None,
            direction=None,
            escalation_priority=None,
            fac_id=None,
            format=None,
            id=None,
            limit=None,
            notification=None,
            offset=None,
            order_by=None,
            physical_entry=None,
            remote_hands=None,
            tech_support=None,
            thirdparty_entry=None,
        ) -> Dict:
        """List Facility Contacts

        API Method: client.contact_facility_list

        This method returns a list of contacts with their escalation and access permissions per facility. If no valid argument is given, a list of all active facility contacts is taken as the default query.

        Args:
            active: Access active. Defaults to None.
            admin: Contact Admin. Defaults to None.
            client_id: Client ID. Defaults to None.
            contact_id: Contact ID. Defaults to None.
            direction: Direction. Defaults to None.
            escalation_priority: Escalation Priority. Defaults to None.
            fac_id: Facility ID. Defaults to None.
            format: Format. Defaults to None.
            id: Facility Contact ID. Defaults to None.
            limit: Limit. Defaults to None.
            notification: Notification. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            physical_entry: Entry. Defaults to None.
            remote_hands: Remote Hands. Defaults to None.
            tech_support: Technical Support. Defaults to None.
            thirdparty_entry: Third-Party Entry. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_facility_list',
            **{'active': active} if active else {},
            **{'admin': admin} if admin else {},
            **{'client_id': client_id} if client_id else {},
            **{'contact_id': contact_id} if contact_id else {},
            **{'direction': direction} if direction else {},
            **{'escalation_priority': escalation_priority} if escalation_priority else {},
            **{'fac_id': fac_id} if fac_id else {},
            **{'format': format} if format else {},
            **{'id': id} if id else {},
            **{'limit': limit} if limit else {},
            **{'notification': notification} if notification else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'physical_entry': physical_entry} if physical_entry else {},
            **{'remote_hands': remote_hands} if remote_hands else {},
            **{'tech_support': tech_support} if tech_support else {},
            **{'thirdparty_entry': thirdparty_entry} if thirdparty_entry else {},
        )

    def contact_facility_revoke(
            self,
            id,
        ) -> Dict:
        """Revoke Facility Contact Access

        API Method: client.contact_facility_revoke

        This method revokes all access for a contact at a facility by setting the facility-contact 'active' flag to false. Facility-contact ID's can be obtained through the contact_facility_list API method.

        Args:
            id: Facility Contact ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_facility_revoke',
            id=id,
        )

    def contact_facility_update(
            self,
            id,
            active=None,
            admin=None,
            escalation_priority=None,
            notes=None,
            notification=None,
            physical_entry=None,
            remote_hands=None,
            tech_support=None,
            thirdparty_entry=None,
        ) -> Dict:
        """Facility Contact Update

        API Method: client.contact_facility_update

        This method updates a facility-contact and returns the updated record.

        Args:
            id: Facility Contact ID,
            active: Access active. Defaults to None.
            admin: Contact Admin. Defaults to None.
            escalation_priority: Escalation Priority. Defaults to None.
            notes: Notes. Defaults to None.
            notification: Notification. Defaults to None.
            physical_entry: Entry. Defaults to None.
            remote_hands: Remote Hands. Defaults to None.
            tech_support: Technical Support. Defaults to None.
            thirdparty_entry: Third-Party Entry. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_facility_update',
            id=id,
            **{'active': active} if active else {},
            **{'admin': admin} if admin else {},
            **{'escalation_priority': escalation_priority} if escalation_priority else {},
            **{'notes': notes} if notes else {},
            **{'notification': notification} if notification else {},
            **{'physical_entry': physical_entry} if physical_entry else {},
            **{'remote_hands': remote_hands} if remote_hands else {},
            **{'tech_support': tech_support} if tech_support else {},
            **{'thirdparty_entry': thirdparty_entry} if thirdparty_entry else {},
        )

    def contact_get(
            self,
            acls=None,
            contact_id=None,
            user_login=None,
        ) -> Dict:
        """Get Contact Details

        API Method: client.contact_get

        This method is used to get a contact's details.

        Args:
            acls: Client ACLs. Defaults to None.
            contact_id: Contact ID. Defaults to None.
            user_login: Contact Login Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_get',
            **{'acls': acls} if acls else {},
            **{'contact_id': contact_id} if contact_id else {},
            **{'user_login': user_login} if user_login else {},
        )

    def contact_list(
            self,
            active=None,
            class_id=None,
            client_id=None,
            contact_active=None,
            direction=None,
            email=None,
            limit=None,
            metadata=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List a Client's Contacts

        API Method: client.contact_list

        This method is used to list a client's contacts.

        Args:
            active: Client Status. Defaults to None.
            class_id: Class ID. Defaults to None.
            client_id: Client Login. Defaults to None.
            contact_active: Contact Status. Defaults to None.
            direction: Direction. Defaults to None.
            email: Contact Email. Defaults to None.
            limit: Limit. Defaults to None.
            metadata: Include Custom Fields. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_list',
            **{'active': active} if active else {},
            **{'class_id': class_id} if class_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'contact_active': contact_active} if contact_active else {},
            **{'direction': direction} if direction else {},
            **{'email': email} if email else {},
            **{'limit': limit} if limit else {},
            **{'metadata': metadata} if metadata else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def contact_metadata_get(
            self,
            contact_id,
        ) -> Dict:
        """Get a Contact's Custom Fields

        API Method: client.contact_metadata_get

        This method is used to get a contact's custom fields.

        Args:
            contact_id: Contact ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_metadata_get',
            contact_id=contact_id,
        )

    def contact_metadata_single(
            self,
            contact_id,
            metaconf_id=None,
            variable=None,
        ) -> Dict:
        """Get a Contact's Custom Field Value

        API Method: client.contact_metadata_single

        This method is used to get a single custom field value from a contact.

        Args:
            contact_id: Contact ID,
            metaconf_id: Custom Field Item ID. Defaults to None.
            variable: Custom Field Variable Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_metadata_single',
            contact_id=contact_id,
            **{'metaconf_id': metaconf_id} if metaconf_id else {},
            **{'variable': variable} if variable else {},
        )

    def contact_permission_list(
            self,
            contact_id,
            effective=None,
            resource_name=None,
        ) -> Dict:
        """List Client Contact Permissions

        API Method: client.contact_permission_list

        This method is used to return a tree/list of client contact permissions.

        Args:
            contact_id: Contact ID,
            effective: Include Effective Actions. Defaults to None.
            resource_name: Resource Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_permission_list',
            contact_id=contact_id,
            **{'effective': effective} if effective else {},
            **{'resource_name': resource_name} if resource_name else {},
        )

    def contact_permission_set(
            self,
            action,
            contact_id,
            resource_name,
            type,
        ) -> Dict:
        """Set Client Contact Permissions

        API Method: client.contact_permission_set

        This method is used to set client contact permissions.

        Args:
            action: Action,
            contact_id: Contact ID,
            resource_name: Resource Name,
            type: Permission Type,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_permission_set',
            action=action,
            contact_id=contact_id,
            resource_name=resource_name,
            type=type,
        )

    def contact_update(
            self,
            contact_id,
            access=None,
            active=None,
            description=None,
            email=None,
            login=None,
            login_enabled=None,
            password=None,
            phone=None,
            prefer_lang=None,
            real_name=None,
            roles=None,
            rwhois_contact=None,
        ) -> Dict:
        """Update a Contact

        API Method: client.contact_update

        This method is used to update a client's contact.

        Args:
            contact_id: Contact ID,
            access: Access Settings. Defaults to None.
            active: Contact active. Defaults to None.
            description: Description. Defaults to None.
            email: Email Address. Defaults to None.
            login: Login Username. Defaults to None.
            login_enabled: Enable Login. Defaults to None.
            password: Password. Defaults to None.
            phone: Telephone Number. Defaults to None.
            prefer_lang: Preferred Interface Language. Defaults to None.
            real_name: Contact's Name. Defaults to None.
            roles: Contact Roles. Defaults to None.
            rwhois_contact: RWhois Role. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.contact_update',
            contact_id=contact_id,
            **{'access': access} if access else {},
            **{'active': active} if active else {},
            **{'description': description} if description else {},
            **{'email': email} if email else {},
            **{'login': login} if login else {},
            **{'login_enabled': login_enabled} if login_enabled else {},
            **{'password': password} if password else {},
            **{'phone': phone} if phone else {},
            **{'prefer_lang': prefer_lang} if prefer_lang else {},
            **{'real_name': real_name} if real_name else {},
            **{'roles': roles} if roles else {},
            **{'rwhois_contact': rwhois_contact} if rwhois_contact else {},
        )

    def count(
            self,
            active=None,
            brand_id=None,
            inactive=None,
        ) -> Dict:
        """Count Active Clients

        API Method: client.count

        This method is used to count the number of clients in the system.

        Args:
            active: Status. Defaults to None.
            brand_id: Brand ID. Defaults to None.
            inactive: Active Flag. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.count',
            **{'active': active} if active else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'inactive': inactive} if inactive else {},
        )

    def credit_add(
            self,
            client_id,
            payment_type,
            auto_apply=None,
            comment=None,
            line_items=None,
            pack_ids=None,
            payment_number=None,
            reason=None,
            send_note=None,
            start_date=None,
            value=None,
        ) -> Dict:
        """Add an Account Credit

        API Method: client.credit_add

        This method is used to add a new credit to a client's account.

        Args:
            client_id: Client ID,
            payment_type: Type of Account Credit,
            auto_apply: Automatic Application Flag. Defaults to None.
            comment: Additional Information. Defaults to None.
            line_items: Invoice Line Item IDs. Defaults to None.
            pack_ids: Package IDs. Defaults to None.
            payment_number: Number to be Associated with Credit. Defaults to None.
            reason: Description. Defaults to None.
            send_note: Send Credit Note. Defaults to None.
            start_date: Start Date. Defaults to None.
            value: Credit Amount. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.credit_add',
            client_id=client_id,
            payment_type=payment_type,
            **{'auto_apply': auto_apply} if auto_apply else {},
            **{'comment': comment} if comment else {},
            **{'line_items': line_items} if line_items else {},
            **{'pack_ids': pack_ids} if pack_ids else {},
            **{'payment_number': payment_number} if payment_number else {},
            **{'reason': reason} if reason else {},
            **{'send_note': send_note} if send_note else {},
            **{'start_date': start_date} if start_date else {},
            **{'value': value} if value else {},
        )

    def credit_apply(
            self,
            credit_id,
            inv_id,
            packages=None,
            taxes=None,
            total=None,
        ) -> Dict:
        """Apply a Credit to an Invoice

        API Method: client.credit_apply

        This method is used to apply a credit to a client's invoice.

        Args:
            credit_id: Credit ID,
            inv_id: Invoice ID,
            packages: Packages. Defaults to None.
            taxes: Taxes. Defaults to None.
            total: Total. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.credit_apply',
            credit_id=credit_id,
            inv_id=inv_id,
            **{'packages': packages} if packages else {},
            **{'taxes': taxes} if taxes else {},
            **{'total': total} if total else {},
        )

    def credit_comment_list(
            self,
            credit_id,
            client_viewable=None,
            direction=None,
            filter_text=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List a Credit's Comments

        API Method: client.credit_comment_list

        This method is used to list a credit's comments.

        Args:
            credit_id: Credit ID,
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
            'client.credit_comment_list',
            credit_id=credit_id,
            **{'client_viewable': client_viewable} if client_viewable else {},
            **{'direction': direction} if direction else {},
            **{'filter_text': filter_text} if filter_text else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def credit_deactivate(
            self,
            credit_id,
            user_login,
        ) -> Dict:
        """Deactivate an Account Credit

        API Method: client.credit_deactivate

        This method is used to deactivate a credit in a client's account.

        Args:
            credit_id: Credit ID,
            user_login: Client Login,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.credit_deactivate',
            credit_id=credit_id,
            user_login=user_login,
        )

    def credit_get(
            self,
            credit_id,
        ) -> Dict:
        """Get details of an Account Credit

        API Method: client.credit_get

        This method is used to get full details of an account credit.

        Args:
            credit_id: Credit ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.credit_get',
            credit_id=credit_id,
        )

    def credit_list(
            self,
            active,
            client_id,
            auto_apply=None,
        ) -> Dict:
        """List a Client's Credits

        API Method: client.credit_list

        This method is used to list a client's credits.

        Args:
            active: Credit Active Status,
            client_id: Client ID,
            auto_apply: Automatic Application Flag. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.credit_list',
            active=active,
            client_id=client_id,
            **{'auto_apply': auto_apply} if auto_apply else {},
        )

    def credit_update(
            self,
            credit_id,
            amount=None,
            auto_apply=None,
            balance=None,
            line_items=None,
            pack_ids=None,
            payment_number=None,
            reason=None,
            send_note=None,
        ) -> Dict:
        """Update an Account Credit

        API Method: client.credit_update

        This method is used to update a credit on a client's account.

        Args:
            credit_id: Credit ID,
            amount: Credit Amount. Defaults to None.
            auto_apply: Automatic Application Flag. Defaults to None.
            balance: Credit Balance. Defaults to None.
            line_items: Invoice Line Item IDs. Defaults to None.
            pack_ids: Package IDs. Defaults to None.
            payment_number: Number to be Associated with Credit. Defaults to None.
            reason: Description. Defaults to None.
            send_note: Send Credit Note. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.credit_update',
            credit_id=credit_id,
            **{'amount': amount} if amount else {},
            **{'auto_apply': auto_apply} if auto_apply else {},
            **{'balance': balance} if balance else {},
            **{'line_items': line_items} if line_items else {},
            **{'pack_ids': pack_ids} if pack_ids else {},
            **{'payment_number': payment_number} if payment_number else {},
            **{'reason': reason} if reason else {},
            **{'send_note': send_note} if send_note else {},
        )

    def deactivate(
            self,
            client_id,
        ) -> Dict:
        """Deactivate a Client

        API Method: client.deactivate

        This method is used to deactivate a client.

        Args:
            client_id: Client ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.deactivate',
            client_id=client_id,
        )

    def domain_add(
            self,
            client_id,
            expires,
            name,
            registered,
            orderid=None,
            password=None,
            registrar_id=None,
            service_id=None,
            tld=None,
            username=None,
        ) -> Dict:
        """Add a Domain

        API Method: client.domain_add

        This method is used to add a new domain to a client's account.

        Args:
            client_id: Client ID,
            expires: Expiration Date,
            name: Domain Name,
            registered: Registration Date,
            orderid: Order ID. Defaults to None.
            password: Password. Defaults to None.
            registrar_id: Domain Registrar. Defaults to None.
            service_id: Service ID. Defaults to None.
            tld: Top-Level Domain. Defaults to None.
            username: User Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.domain_add',
            client_id=client_id,
            expires=expires,
            name=name,
            registered=registered,
            **{'orderid': orderid} if orderid else {},
            **{'password': password} if password else {},
            **{'registrar_id': registrar_id} if registrar_id else {},
            **{'service_id': service_id} if service_id else {},
            **{'tld': tld} if tld else {},
            **{'username': username} if username else {},
        )

    def domain_external_attributes_get(
            self,
            tld,
        ) -> Dict:
        """Get Registrar/TLD external attributes.

        API Method: client.domain_external_attributes_get

        Return Registrar/TLD specific external attributes.

        Args:
            tld: TLD,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.domain_external_attributes_get',
            tld=tld,
        )

    def domain_list(
            self,
            user_login,
            direction=None,
            domain_type=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List a Client's Domains

        API Method: client.domain_list

        This method is used to list a client's domains.

        Args:
            user_login: Client Login,
            direction: Direction. Defaults to None.
            domain_type: Domain Type. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.domain_list',
            user_login=user_login,
            **{'direction': direction} if direction else {},
            **{'domain_type': domain_type} if domain_type else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def domain_lookup(
            self,
            domain,
        ) -> Dict:
        """Look Up a Domain

        API Method: client.domain_lookup

        This method is used to look up a client's domain using WHOIS.

        Args:
            domain: Domain Name,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.domain_lookup',
            domain=domain,
        )

    def domain_register(
            self,
            client_id,
            name,
            password,
            years,
            admin_address1=None,
            admin_address2=None,
            admin_city=None,
            admin_company=None,
            admin_country=None,
            admin_email=None,
            admin_fax=None,
            admin_fname=None,
            admin_info=None,
            admin_lname=None,
            admin_phone=None,
            admin_state=None,
            admin_zip=None,
            autorenew=None,
            billing_address1=None,
            billing_address2=None,
            billing_city=None,
            billing_company=None,
            billing_country=None,
            billing_email=None,
            billing_fax=None,
            billing_fname=None,
            billing_info=None,
            billing_lname=None,
            billing_phone=None,
            billing_state=None,
            billing_zip=None,
            external_attributes=None,
            force_premium=None,
            lockdomain=None,
            owner_address1=None,
            owner_address2=None,
            owner_city=None,
            owner_company=None,
            owner_country=None,
            owner_email=None,
            owner_fax=None,
            owner_fname=None,
            owner_lname=None,
            owner_phone=None,
            owner_state=None,
            owner_zip=None,
            premium_price_to_confirm=None,
            privacy=None,
            service_id=None,
            technical_address1=None,
            technical_address2=None,
            technical_city=None,
            technical_company=None,
            technical_country=None,
            technical_email=None,
            technical_fax=None,
            technical_fname=None,
            technical_info=None,
            technical_lname=None,
            technical_phone=None,
            technical_state=None,
            technical_zip=None,
            tld=None,
            username=None,
        ) -> Dict:
        """Register a Domain

        API Method: client.domain_register

        This method is used to register a client's domain.

        Args:
            client_id: Client ID,
            name: Domain Name,
            password: Password,
            years: Registration Period,
            admin_address1: Administrator's Address 1. Defaults to None.
            admin_address2: Administrator's Address 2. Defaults to None.
            admin_city: Administrator's City. Defaults to None.
            admin_company: Administrator's Company. Defaults to None.
            admin_country: Administrator's Country. Defaults to None.
            admin_email: Administrator's Email. Defaults to None.
            admin_fax: Administrator's Fax Number. Defaults to None.
            admin_fname: Administrator's First Name. Defaults to None.
            admin_info: Administrator's Information. Defaults to None.
            admin_lname: Administrator's Last Name. Defaults to None.
            admin_phone: Administrator's Telephone Number. Defaults to None.
            admin_state: Administrator's State. Defaults to None.
            admin_zip: Administrator's ZIP or Postal Code. Defaults to None.
            autorenew: Auto-Renew. Defaults to None.
            billing_address1: Billing Address 1. Defaults to None.
            billing_address2: Billing Address 2. Defaults to None.
            billing_city: Billing City. Defaults to None.
            billing_company: Billing Company. Defaults to None.
            billing_country: Billing Country. Defaults to None.
            billing_email: Billing Email. Defaults to None.
            billing_fax: Billing Fax Number. Defaults to None.
            billing_fname: Billing First Name. Defaults to None.
            billing_info: Billing Information. Defaults to None.
            billing_lname: Billing Last Name. Defaults to None.
            billing_phone: Billing Telephone Number. Defaults to None.
            billing_state: Billing State. Defaults to None.
            billing_zip: Billing ZIP or Postal Code. Defaults to None.
            external_attributes: An array of Registrar/TLD specific information. Defaults to None.
            force_premium: Force registration of premium domains. Defaults to None.
            lockdomain: Lock Domain. Defaults to None.
            owner_address1: Owner's Address 1. Defaults to None.
            owner_address2: Owner's Address 2. Defaults to None.
            owner_city: Owner's City. Defaults to None.
            owner_company: Owner's Company. Defaults to None.
            owner_country: Owner's Country. Defaults to None.
            owner_email: Owner's Email. Defaults to None.
            owner_fax: Owner's Fax Number. Defaults to None.
            owner_fname: Owner's First Name. Defaults to None.
            owner_lname: Owner's Last Name. Defaults to None.
            owner_phone: Owner's Telephone Number. Defaults to None.
            owner_state: Owner's State. Defaults to None.
            owner_zip: Owner's ZIP or Postal Code. Defaults to None.
            premium_price_to_confirm: Price confirmation for premium domains. Defaults to None.
            privacy: Add WHOIS Privacy Protection Service. Defaults to None.
            service_id: Service ID. Defaults to None.
            technical_address1: Technical Address 1. Defaults to None.
            technical_address2: Technical Address 2. Defaults to None.
            technical_city: Technical City. Defaults to None.
            technical_company: Technical Company. Defaults to None.
            technical_country: Technical Country. Defaults to None.
            technical_email: Technical Email. Defaults to None.
            technical_fax: Technical Fax Number. Defaults to None.
            technical_fname: Technical First Name. Defaults to None.
            technical_info: Technical Information. Defaults to None.
            technical_lname: Technical Last Name. Defaults to None.
            technical_phone: Technical Telephone Number. Defaults to None.
            technical_state: Technical State. Defaults to None.
            technical_zip: Technical ZIP or Postal Code. Defaults to None.
            tld: Top-Level Domain. Defaults to None.
            username: Username. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.domain_register',
            client_id=client_id,
            name=name,
            password=password,
            years=years,
            **{'admin_address1': admin_address1} if admin_address1 else {},
            **{'admin_address2': admin_address2} if admin_address2 else {},
            **{'admin_city': admin_city} if admin_city else {},
            **{'admin_company': admin_company} if admin_company else {},
            **{'admin_country': admin_country} if admin_country else {},
            **{'admin_email': admin_email} if admin_email else {},
            **{'admin_fax': admin_fax} if admin_fax else {},
            **{'admin_fname': admin_fname} if admin_fname else {},
            **{'admin_info': admin_info} if admin_info else {},
            **{'admin_lname': admin_lname} if admin_lname else {},
            **{'admin_phone': admin_phone} if admin_phone else {},
            **{'admin_state': admin_state} if admin_state else {},
            **{'admin_zip': admin_zip} if admin_zip else {},
            **{'autorenew': autorenew} if autorenew else {},
            **{'billing_address1': billing_address1} if billing_address1 else {},
            **{'billing_address2': billing_address2} if billing_address2 else {},
            **{'billing_city': billing_city} if billing_city else {},
            **{'billing_company': billing_company} if billing_company else {},
            **{'billing_country': billing_country} if billing_country else {},
            **{'billing_email': billing_email} if billing_email else {},
            **{'billing_fax': billing_fax} if billing_fax else {},
            **{'billing_fname': billing_fname} if billing_fname else {},
            **{'billing_info': billing_info} if billing_info else {},
            **{'billing_lname': billing_lname} if billing_lname else {},
            **{'billing_phone': billing_phone} if billing_phone else {},
            **{'billing_state': billing_state} if billing_state else {},
            **{'billing_zip': billing_zip} if billing_zip else {},
            **{'external_attributes': external_attributes} if external_attributes else {},
            **{'force_premium': force_premium} if force_premium else {},
            **{'lockdomain': lockdomain} if lockdomain else {},
            **{'owner_address1': owner_address1} if owner_address1 else {},
            **{'owner_address2': owner_address2} if owner_address2 else {},
            **{'owner_city': owner_city} if owner_city else {},
            **{'owner_company': owner_company} if owner_company else {},
            **{'owner_country': owner_country} if owner_country else {},
            **{'owner_email': owner_email} if owner_email else {},
            **{'owner_fax': owner_fax} if owner_fax else {},
            **{'owner_fname': owner_fname} if owner_fname else {},
            **{'owner_lname': owner_lname} if owner_lname else {},
            **{'owner_phone': owner_phone} if owner_phone else {},
            **{'owner_state': owner_state} if owner_state else {},
            **{'owner_zip': owner_zip} if owner_zip else {},
            **{'premium_price_to_confirm': premium_price_to_confirm} if premium_price_to_confirm else {},
            **{'privacy': privacy} if privacy else {},
            **{'service_id': service_id} if service_id else {},
            **{'technical_address1': technical_address1} if technical_address1 else {},
            **{'technical_address2': technical_address2} if technical_address2 else {},
            **{'technical_city': technical_city} if technical_city else {},
            **{'technical_company': technical_company} if technical_company else {},
            **{'technical_country': technical_country} if technical_country else {},
            **{'technical_email': technical_email} if technical_email else {},
            **{'technical_fax': technical_fax} if technical_fax else {},
            **{'technical_fname': technical_fname} if technical_fname else {},
            **{'technical_info': technical_info} if technical_info else {},
            **{'technical_lname': technical_lname} if technical_lname else {},
            **{'technical_phone': technical_phone} if technical_phone else {},
            **{'technical_state': technical_state} if technical_state else {},
            **{'technical_zip': technical_zip} if technical_zip else {},
            **{'tld': tld} if tld else {},
            **{'username': username} if username else {},
        )

    def domain_transfer(
            self,
            client_id,
            name,
            password,
            years,
            admin_address1=None,
            admin_address2=None,
            admin_city=None,
            admin_company=None,
            admin_country=None,
            admin_email=None,
            admin_fax=None,
            admin_fname=None,
            admin_info=None,
            admin_lname=None,
            admin_phone=None,
            admin_state=None,
            admin_zip=None,
            autorenew=None,
            billing_address1=None,
            billing_address2=None,
            billing_city=None,
            billing_company=None,
            billing_country=None,
            billing_email=None,
            billing_fax=None,
            billing_fname=None,
            billing_info=None,
            billing_lname=None,
            billing_phone=None,
            billing_state=None,
            billing_zip=None,
            external_attributes=None,
            force_premium=None,
            lockdomain=None,
            owner_address1=None,
            owner_address2=None,
            owner_city=None,
            owner_company=None,
            owner_country=None,
            owner_email=None,
            owner_fax=None,
            owner_fname=None,
            owner_lname=None,
            owner_phone=None,
            owner_state=None,
            owner_zip=None,
            premium_price_to_confirm=None,
            privacy=None,
            service_id=None,
            technical_address1=None,
            technical_address2=None,
            technical_city=None,
            technical_company=None,
            technical_country=None,
            technical_email=None,
            technical_fax=None,
            technical_fname=None,
            technical_info=None,
            technical_lname=None,
            technical_phone=None,
            technical_state=None,
            technical_zip=None,
            tld=None,
            username=None,
        ) -> Dict:
        """Transfer a Domain

        API Method: client.domain_transfer

        This method is used to transfer a client's domain.

        Args:
            client_id: Client ID,
            name: Domain Name,
            password: Password,
            years: Registration Period,
            admin_address1: Administrator's Address 1. Defaults to None.
            admin_address2: Administrator's Address 2. Defaults to None.
            admin_city: Administrator's City. Defaults to None.
            admin_company: Administrator's Company. Defaults to None.
            admin_country: Administrator's Country. Defaults to None.
            admin_email: Administrator's Email. Defaults to None.
            admin_fax: Administrator's Fax Number. Defaults to None.
            admin_fname: Administrator's First Name. Defaults to None.
            admin_info: Administrator's Information. Defaults to None.
            admin_lname: Administrator's Last Name. Defaults to None.
            admin_phone: Administrator's Telephone Number. Defaults to None.
            admin_state: Administrator's State. Defaults to None.
            admin_zip: Administrator's ZIP or Postal Code. Defaults to None.
            autorenew: Auto-Renew. Defaults to None.
            billing_address1: Billing Address 1. Defaults to None.
            billing_address2: Billing Address 2. Defaults to None.
            billing_city: Billing City. Defaults to None.
            billing_company: Billing Company. Defaults to None.
            billing_country: Billing Country. Defaults to None.
            billing_email: Billing Email. Defaults to None.
            billing_fax: Billing Fax Number. Defaults to None.
            billing_fname: Billing First Name. Defaults to None.
            billing_info: Billing Information. Defaults to None.
            billing_lname: Billing Last Name. Defaults to None.
            billing_phone: Billing Telephone Number. Defaults to None.
            billing_state: Billing State. Defaults to None.
            billing_zip: Billing ZIP or Postal Code. Defaults to None.
            external_attributes: An array of Registrar/TLD specific information. Defaults to None.
            force_premium: Force registration of premium domains. Defaults to None.
            lockdomain: Lock Domain. Defaults to None.
            owner_address1: Owner's Address 1. Defaults to None.
            owner_address2: Owner's Address 2. Defaults to None.
            owner_city: Owner's City. Defaults to None.
            owner_company: Owner's Company. Defaults to None.
            owner_country: Owner's Country. Defaults to None.
            owner_email: Owner's Email. Defaults to None.
            owner_fax: Owner's Fax Number. Defaults to None.
            owner_fname: Owner's First Name. Defaults to None.
            owner_lname: Owner's Last Name. Defaults to None.
            owner_phone: Owner's Telephone Number. Defaults to None.
            owner_state: Owner's State. Defaults to None.
            owner_zip: Owner's ZIP or Postal Code. Defaults to None.
            premium_price_to_confirm: Price confirmation for premium domains. Defaults to None.
            privacy: Add WHOIS Privacy Protection Service. Defaults to None.
            service_id: Service ID. Defaults to None.
            technical_address1: Technical Address 1. Defaults to None.
            technical_address2: Technical Address 2. Defaults to None.
            technical_city: Technical City. Defaults to None.
            technical_company: Technical Company. Defaults to None.
            technical_country: Technical Country. Defaults to None.
            technical_email: Technical Email. Defaults to None.
            technical_fax: Technical Fax Number. Defaults to None.
            technical_fname: Technical First Name. Defaults to None.
            technical_info: Technical Information. Defaults to None.
            technical_lname: Technical Last Name. Defaults to None.
            technical_phone: Technical Telephone Number. Defaults to None.
            technical_state: Technical State. Defaults to None.
            technical_zip: Technical ZIP or Postal Code. Defaults to None.
            tld: Top-Level Domain. Defaults to None.
            username: Username. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.domain_transfer',
            client_id=client_id,
            name=name,
            password=password,
            years=years,
            **{'admin_address1': admin_address1} if admin_address1 else {},
            **{'admin_address2': admin_address2} if admin_address2 else {},
            **{'admin_city': admin_city} if admin_city else {},
            **{'admin_company': admin_company} if admin_company else {},
            **{'admin_country': admin_country} if admin_country else {},
            **{'admin_email': admin_email} if admin_email else {},
            **{'admin_fax': admin_fax} if admin_fax else {},
            **{'admin_fname': admin_fname} if admin_fname else {},
            **{'admin_info': admin_info} if admin_info else {},
            **{'admin_lname': admin_lname} if admin_lname else {},
            **{'admin_phone': admin_phone} if admin_phone else {},
            **{'admin_state': admin_state} if admin_state else {},
            **{'admin_zip': admin_zip} if admin_zip else {},
            **{'autorenew': autorenew} if autorenew else {},
            **{'billing_address1': billing_address1} if billing_address1 else {},
            **{'billing_address2': billing_address2} if billing_address2 else {},
            **{'billing_city': billing_city} if billing_city else {},
            **{'billing_company': billing_company} if billing_company else {},
            **{'billing_country': billing_country} if billing_country else {},
            **{'billing_email': billing_email} if billing_email else {},
            **{'billing_fax': billing_fax} if billing_fax else {},
            **{'billing_fname': billing_fname} if billing_fname else {},
            **{'billing_info': billing_info} if billing_info else {},
            **{'billing_lname': billing_lname} if billing_lname else {},
            **{'billing_phone': billing_phone} if billing_phone else {},
            **{'billing_state': billing_state} if billing_state else {},
            **{'billing_zip': billing_zip} if billing_zip else {},
            **{'external_attributes': external_attributes} if external_attributes else {},
            **{'force_premium': force_premium} if force_premium else {},
            **{'lockdomain': lockdomain} if lockdomain else {},
            **{'owner_address1': owner_address1} if owner_address1 else {},
            **{'owner_address2': owner_address2} if owner_address2 else {},
            **{'owner_city': owner_city} if owner_city else {},
            **{'owner_company': owner_company} if owner_company else {},
            **{'owner_country': owner_country} if owner_country else {},
            **{'owner_email': owner_email} if owner_email else {},
            **{'owner_fax': owner_fax} if owner_fax else {},
            **{'owner_fname': owner_fname} if owner_fname else {},
            **{'owner_lname': owner_lname} if owner_lname else {},
            **{'owner_phone': owner_phone} if owner_phone else {},
            **{'owner_state': owner_state} if owner_state else {},
            **{'owner_zip': owner_zip} if owner_zip else {},
            **{'premium_price_to_confirm': premium_price_to_confirm} if premium_price_to_confirm else {},
            **{'privacy': privacy} if privacy else {},
            **{'service_id': service_id} if service_id else {},
            **{'technical_address1': technical_address1} if technical_address1 else {},
            **{'technical_address2': technical_address2} if technical_address2 else {},
            **{'technical_city': technical_city} if technical_city else {},
            **{'technical_company': technical_company} if technical_company else {},
            **{'technical_country': technical_country} if technical_country else {},
            **{'technical_email': technical_email} if technical_email else {},
            **{'technical_fax': technical_fax} if technical_fax else {},
            **{'technical_fname': technical_fname} if technical_fname else {},
            **{'technical_info': technical_info} if technical_info else {},
            **{'technical_lname': technical_lname} if technical_lname else {},
            **{'technical_phone': technical_phone} if technical_phone else {},
            **{'technical_state': technical_state} if technical_state else {},
            **{'technical_zip': technical_zip} if technical_zip else {},
            **{'tld': tld} if tld else {},
            **{'username': username} if username else {},
        )

    def domain_update(
            self,
            domain_id,
            active=None,
            client_id=None,
            expires=None,
            name=None,
            orderid=None,
            password=None,
            registered=None,
            registrar_id=None,
            service_id=None,
            tld=None,
            username=None,
        ) -> Dict:
        """Update a Domain

        API Method: client.domain_update

        This method is used to add a new domain to a client's account.

        Args:
            domain_id: Domain ID,
            active: Active. Defaults to None.
            client_id: Client ID. Defaults to None.
            expires: Expiration Date. Defaults to None.
            name: Domain Name. Defaults to None.
            orderid: Order ID. Defaults to None.
            password: Password. Defaults to None.
            registered: Registration Date. Defaults to None.
            registrar_id: Domain Registrar. Defaults to None.
            service_id: Service ID. Defaults to None.
            tld: Top-Level Domain. Defaults to None.
            username: User Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.domain_update',
            domain_id=domain_id,
            **{'active': active} if active else {},
            **{'client_id': client_id} if client_id else {},
            **{'expires': expires} if expires else {},
            **{'name': name} if name else {},
            **{'orderid': orderid} if orderid else {},
            **{'password': password} if password else {},
            **{'registered': registered} if registered else {},
            **{'registrar_id': registrar_id} if registrar_id else {},
            **{'service_id': service_id} if service_id else {},
            **{'tld': tld} if tld else {},
            **{'username': username} if username else {},
        )

    def find_similar(
            self,
            client=None,
            client_id=None,
        ) -> Dict:
        """Get a List of Similar Clients

        API Method: client.find_similar

        This method is used to return a list of similar clients.

        Args:
            client: Client Details. Defaults to None.
            client_id: Client ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.find_similar',
            **{'client': client} if client else {},
            **{'client_id': client_id} if client_id else {},
        )

    def get(
            self,
            acls=None,
            allclients=None,
            client_id=None,
            email=None,
            metadata=None,
            tags=None,
            user_login=None,
        ) -> Dict:
        """Get Client Details

        API Method: client.get

        This method is used to get a client's details.

        Args:
            acls: Client ACLs. Defaults to None.
            allclients: All Clients Flag. Defaults to None.
            client_id: Client ID. Defaults to None.
            email: Client Email Address. Defaults to None.
            metadata: Include Client Custom Fields. Defaults to None.
            tags: Client Tags. Defaults to None.
            user_login: Client Login Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.get',
            **{'acls': acls} if acls else {},
            **{'allclients': allclients} if allclients else {},
            **{'client_id': client_id} if client_id else {},
            **{'email': email} if email else {},
            **{'metadata': metadata} if metadata else {},
            **{'tags': tags} if tags else {},
            **{'user_login': user_login} if user_login else {},
        )

    def invoice_charge(
            self,
            inv_id,
            billing_info_id=None,
            package=None,
            paid_in_full=None,
            payment_type=None,
            tax=None,
            threedsecure=None,
        ) -> Dict:
        """Charge an Invoice

        API Method: client.invoice_charge

        This method is used to charge a client's invoice.

        Args:
            inv_id: Invoice ID,
            billing_info_id: Payment Method ID. Defaults to None.
            package: Packages. Defaults to None.
            paid_in_full: Paid In Full. Defaults to None.
            payment_type: Payment Type. Defaults to None.
            tax: Taxes. Defaults to None.
            threedsecure: Provider specific 3D Secure parameters (array). Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.invoice_charge',
            inv_id=inv_id,
            **{'billing_info_id': billing_info_id} if billing_info_id else {},
            **{'package': package} if package else {},
            **{'paid_in_full': paid_in_full} if paid_in_full else {},
            **{'payment_type': payment_type} if payment_type else {},
            **{'tax': tax} if tax else {},
            **{'threedsecure': threedsecure} if threedsecure else {},
        )

    def invoice_count(
            self,
            client_id,
            inv_type_select=None,
        ) -> Dict:
        """Count Invoices

        API Method: client.invoice_count

        This method is used to count the number of invoices associated with a client.

        Args:
            client_id: Client ID,
            inv_type_select: Invoice Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.invoice_count',
            client_id=client_id,
            **{'inv_type_select': inv_type_select} if inv_type_select else {},
        )

    def invoice_disregard(
            self,
            client_id,
            invoice_id,
        ) -> Dict:
        """Disregard an Invoice

        API Method: client.invoice_disregard

        This method is used to disregard a client's invoice.

        Args:
            client_id: Client ID,
            invoice_id: Invoice ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.invoice_disregard',
            client_id=client_id,
            invoice_id=invoice_id,
        )

    def invoice_generate(
            self,
            client_id,
            command=None,
            duedate=None,
            include_credits=None,
            include_packs=None,
            include_prebills=None,
            pre_bill=None,
            trans_id=None,
        ) -> Dict:
        """Generate an Invoice

        API Method: client.invoice_generate

        This method is used to generate an invoice for a client.

        Args:
            client_id: Client ID,
            command: Charge Command. Defaults to None.
            duedate: Due Date. Defaults to None.
            include_credits: Included Credits. Defaults to None.
            include_packs: Included Services. Defaults to None.
            include_prebills: Included Prebills. Defaults to None.
            pre_bill: Pre-Bill Date. Defaults to None.
            trans_id: Transaction ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.invoice_generate',
            client_id=client_id,
            **{'command': command} if command else {},
            **{'duedate': duedate} if duedate else {},
            **{'include_credits': include_credits} if include_credits else {},
            **{'include_packs': include_packs} if include_packs else {},
            **{'include_prebills': include_prebills} if include_prebills else {},
            **{'pre_bill': pre_bill} if pre_bill else {},
            **{'trans_id': trans_id} if trans_id else {},
        )

    def invoice_get(
            self,
            invoice_id,
            format=None,
        ) -> Dict:
        """Get an Invoice

        API Method: client.invoice_get

        This method is used to get a client's invoice.

        Args:
            invoice_id: Invoice ID,
            format: Format. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.invoice_get',
            invoice_id=invoice_id,
            **{'format': format} if format else {},
        )

    def invoice_list(
            self,
            brand_id=None,
            client_id=None,
            direction=None,
            limit=None,
            offset=None,
            order_by=None,
            paid=None,
            since=None,
        ) -> Dict:
        """List a Client's Invoices

        API Method: client.invoice_list

        This method is used to list a client's invoices.

        Args:
            brand_id: Brand ID. Defaults to None.
            client_id: Client Login. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            paid: Paid Status. Defaults to None.
            since: Start Date. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.invoice_list',
            **{'brand_id': brand_id} if brand_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'paid': paid} if paid else {},
            **{'since': since} if since else {},
        )

    def invoice_payments(
            self,
            invoice_id,
        ) -> Dict:
        """List an Invoice's Payments

        API Method: client.invoice_payments

        This method is used to list an invoice's payments.

        Args:
            invoice_id: Invoice ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.invoice_payments',
            invoice_id=invoice_id,
        )

    def invoice_post_gw_payment(
            self,
            amount,
            client_id,
            gateway,
            inv_id,
            transaction_id,
        ) -> Dict:
        """Record a Payment

        API Method: client.invoice_post_gw_payment

        This method is used to record a payment received outside Ubersmith through Paypal, WorldPay, 2Checkout or an ACH provider.

        Args:
            amount: Amount,
            client_id: Client ID,
            gateway: Gateway,
            inv_id: Invoice ID,
            transaction_id: Transaction ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.invoice_post_gw_payment',
            amount=amount,
            client_id=client_id,
            gateway=gateway,
            inv_id=inv_id,
            transaction_id=transaction_id,
        )

    def invoice_threedsecure2_process(
            self,
            action,
            amount,
            inv_id,
            threedsecure,
            billing_info_id=None,
        ) -> Dict:
        """Execute a provider specific 3D secure action

        API Method: client.invoice_threedsecure2_process

        This method is used to execute a provider specific 3D Secure action.

        Args:
            action: Action,
            amount: The amount being paid for the invoice,
            inv_id: Invoice ID,
            threedsecure: Provider specific 3D Secure 2 parameters (array),
            billing_info_id: Payment Method ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.invoice_threedsecure2_process',
            action=action,
            amount=amount,
            inv_id=inv_id,
            threedsecure=threedsecure,
            **{'billing_info_id': billing_info_id} if billing_info_id else {},
        )

    def ip_assignment_add(
            self,
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

        API Method: client.ip_assignment_add

        This method is used to create a new IP address assignment.

        Args:
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
            'client.ip_assignment_add',
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

    def ip_assignment_list(
            self,
            client_id,
            limit=None,
            offset=None,
        ) -> Dict:
        """List client IP Assignments

        API Method: client.ip_assignment_list

        This method is used to list a client's IP assignments. It will list ips assigned to a client as well as a client's services and devices

        Args:
            client_id: Client ID,
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.ip_assignment_list',
            client_id=client_id,
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
        )

    def latest_client(
            self,
        ) -> Dict:
        """Get the Latest Client

        API Method: client.latest_client

        This method is used to get the latest client in the system.

        Args:
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.latest_client',
        )

    def list(
            self,
            active=None,
            brand_id=None,
            client_id=None,
            direction=None,
            inactive=None,
            limit=None,
            metadata=None,
            offset=None,
            order_by=None,
            qblistid=None,
            short=None,
            tag_id=None,
            tag_ids=None,
        ) -> Dict:
        """List Clients

        API Method: client.list

        This method is used to list clients in the system.

        Args:
            active: Status. Defaults to None.
            brand_id: Brand ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            direction: Direction. Defaults to None.
            inactive: Active Flag. Defaults to None.
            limit: Limit. Defaults to None.
            metadata: Include Custom Fields. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            qblistid: QuickBooks ID. Defaults to None.
            short: Short Output Mode. Defaults to None.
            tag_id: Tag ID. Defaults to None.
            tag_ids: Tag IDs. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.list',
            **{'active': active} if active else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'direction': direction} if direction else {},
            **{'inactive': inactive} if inactive else {},
            **{'limit': limit} if limit else {},
            **{'metadata': metadata} if metadata else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'qblistid': qblistid} if qblistid else {},
            **{'short': short} if short else {},
            **{'tag_id': tag_id} if tag_id else {},
            **{'tag_ids': tag_ids} if tag_ids else {},
        )

    def lookup(
            self,
            active=None,
            address=None,
            brand_id=None,
            city=None,
            client_id=None,
            company=None,
            country=None,
            email=None,
            fax=None,
            first=None,
            full_name=None,
            last=None,
            listed_company=None,
            login=None,
            phone=None,
            state=None,
            zip=None,
        ) -> Dict:
        """Look Up a Client

        API Method: client.lookup

        This method is used to look up a client.

        Args:
            active: Client Status. Defaults to None.
            address: Address. Defaults to None.
            brand_id: Brand ID. Defaults to None.
            city: City. Defaults to None.
            client_id: Client ID. Defaults to None.
            company: Company. Defaults to None.
            country: Country. Defaults to None.
            email: Email. Defaults to None.
            fax: Fax. Defaults to None.
            first: First Name. Defaults to None.
            full_name: Full Name. Defaults to None.
            last: Last Name. Defaults to None.
            listed_company: Listed Company. Defaults to None.
            login: Login. Defaults to None.
            phone: Phone. Defaults to None.
            state: State. Defaults to None.
            zip: Zip. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.lookup',
            **{'active': active} if active else {},
            **{'address': address} if address else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'city': city} if city else {},
            **{'client_id': client_id} if client_id else {},
            **{'company': company} if company else {},
            **{'country': country} if country else {},
            **{'email': email} if email else {},
            **{'fax': fax} if fax else {},
            **{'first': first} if first else {},
            **{'full_name': full_name} if full_name else {},
            **{'last': last} if last else {},
            **{'listed_company': listed_company} if listed_company else {},
            **{'login': login} if login else {},
            **{'phone': phone} if phone else {},
            **{'state': state} if state else {},
            **{'zip': zip} if zip else {},
        )

    def metadata_get(
            self,
            client_id,
        ) -> Dict:
        """Get a Client's Custom Fields

        API Method: client.metadata_get

        This method is used to get a client's custom fields.

        Args:
            client_id: Client ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.metadata_get',
            client_id=client_id,
        )

    def metadata_single(
            self,
            client_id,
            metaconf_id=None,
            variable=None,
        ) -> Dict:
        """Get a Client's Custom Field Value

        API Method: client.metadata_single

        This method is used to get a single custom field value from a client.

        Args:
            client_id: Client ID,
            metaconf_id: Custom Field Item ID. Defaults to None.
            variable: Custom Field Variable Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.metadata_single',
            client_id=client_id,
            **{'metaconf_id': metaconf_id} if metaconf_id else {},
            **{'variable': variable} if variable else {},
        )

    def msa_assign(
            self,
            client_id,
            auto_renew=None,
            expires=None,
            expires_after_cancel=None,
            expires_term_type=None,
            ip_address=None,
            msa_id=None,
            pdf=None,
            pdf_bound=None,
            renew_term=None,
            signed=None,
            signer=None,
            term=None,
            term_renew_type=None,
            term_type=None,
        ) -> Dict:
        """Assign an MSA to a client

        API Method: client.msa_assign

        This method is used to assign an msa to a client

        Args:
            client_id: Client ID,
            auto_renew: Auto Renew. Defaults to None.
            expires: Expires. Defaults to None.
            expires_after_cancel: Expires after service cancellation. Defaults to None.
            expires_term_type: Expires after service cancellation Type. Defaults to None.
            ip_address: IP Address. Defaults to None.
            msa_id: MSA ID. Defaults to None.
            pdf: PDF. Defaults to None.
            pdf_bound: Add overlay. Defaults to None.
            renew_term: Renewal Term. Defaults to None.
            signed: Signed. Defaults to None.
            signer: Signer. Defaults to None.
            term: Term. Defaults to None.
            term_renew_type: Renewal Term Type. Defaults to None.
            term_type: Term type. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.msa_assign',
            client_id=client_id,
            **{'auto_renew': auto_renew} if auto_renew else {},
            **{'expires': expires} if expires else {},
            **{'expires_after_cancel': expires_after_cancel} if expires_after_cancel else {},
            **{'expires_term_type': expires_term_type} if expires_term_type else {},
            **{'ip_address': ip_address} if ip_address else {},
            **{'msa_id': msa_id} if msa_id else {},
            **{'pdf': pdf} if pdf else {},
            **{'pdf_bound': pdf_bound} if pdf_bound else {},
            **{'renew_term': renew_term} if renew_term else {},
            **{'signed': signed} if signed else {},
            **{'signer': signer} if signer else {},
            **{'term': term} if term else {},
            **{'term_renew_type': term_renew_type} if term_renew_type else {},
            **{'term_type': term_type} if term_type else {},
        )

    def msa_get(
            self,
            client_id=None,
            client_msa_id=None,
            format=None,
        ) -> Dict:
        """Get Client MSA Details

        API Method: client.msa_get

        This method is used to get the details of a specified client msa.

        Args:
            client_id: Client ID. Defaults to None.
            client_msa_id: Client MSA ID. Defaults to None.
            format: Format. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.msa_get',
            **{'client_id': client_id} if client_id else {},
            **{'client_msa_id': client_msa_id} if client_msa_id else {},
            **{'format': format} if format else {},
        )

    def payment_list(
            self,
            client_id,
            begin=None,
            direction=None,
            end=None,
            invoice_id=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List a Client's Payments

        API Method: client.payment_list

        This method is used to list a client's payments.

        Args:
            client_id: Client ID,
            begin: Begin Time. Defaults to None.
            direction: Direction. Defaults to None.
            end: End Time. Defaults to None.
            invoice_id: Invoice ID. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.payment_list',
            client_id=client_id,
            **{'begin': begin} if begin else {},
            **{'direction': direction} if direction else {},
            **{'end': end} if end else {},
            **{'invoice_id': invoice_id} if invoice_id else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def payment_method_list(
            self,
            client_id,
            direction=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List a Client's Payment Methods

        API Method: client.payment_method_list

        This method is used to list a client's payment methods.

        Args:
            client_id: Client ID,
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.payment_method_list',
            client_id=client_id,
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def payment_refund(
            self,
            pay_record_id,
            full_refund=None,
            note=None,
            refund_items=None,
            refund_type=None,
            tax_items=None,
        ) -> Dict:
        """Refund a payment.

        API Method: client.payment_refund

        This method is used to refund a payment, either in full or to specific payment items and/or tax payments.

        Args:
            pay_record_id: Payment Record ID,
            full_refund: Full Refund. Defaults to None.
            note: Notes. Defaults to None.
            refund_items: Refund Services. Defaults to None.
            refund_type: Refund Type. Defaults to None.
            tax_items: Refund Taxes. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.payment_refund',
            pay_record_id=pay_record_id,
            **{'full_refund': full_refund} if full_refund else {},
            **{'note': note} if note else {},
            **{'refund_items': refund_items} if refund_items else {},
            **{'refund_type': refund_type} if refund_type else {},
            **{'tax_items': tax_items} if tax_items else {},
        )

    def paypal_subscription_add(
            self,
            client_id,
            format=None,
            period=None,
            services=None,
        ) -> Dict:
        """Create a new Paypal Subscription

        API Method: client.paypal_subscription_add

        Generate an HTML form to make a new Paypal subscription; Add the necessary information to the DB

        Args:
            client_id: Client ID,
            format: Format. Defaults to None.
            period: Specify a period of services. Defaults to None.
            services: A list of services, eg: &services[]=1234&services[]=2345. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.paypal_subscription_add',
            client_id=client_id,
            **{'format': format} if format else {},
            **{'period': period} if period else {},
            **{'services': services} if services else {},
        )

    def paypal_subscription_list(
            self,
            brand_id=None,
            client_id=None,
            status=None,
        ) -> Dict:
        """List Paypal Subscriptions

        API Method: client.paypal_subscription_list

        List Paypal subscriptions for every client or optionally for a specific client.

        Args:
            brand_id: Brand ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.paypal_subscription_list',
            **{'brand_id': brand_id} if brand_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'status': status} if status else {},
        )

    def paypal_transaction_details_get(
            self,
            transaction_id,
            config=None,
        ) -> Dict:
        """Get a PayPal Transaction Information

        API Method: client.paypal_transaction_details_get

        Fetch a PayPal transaction information

        Args:
            transaction_id: Transaction ID,
            config: PayPal configuration. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.paypal_transaction_details_get',
            transaction_id=transaction_id,
            **{'config': config} if config else {},
        )

    def permission_get(
            self,
            action,
            client_id,
            resource_name,
        ) -> Dict:
        """Get Client Permission

        API Method: client.permission_get

        This method is used to get a client permission.

        Args:
            action: Action,
            client_id: Client ID,
            resource_name: Resource Name,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.permission_get',
            action=action,
            client_id=client_id,
            resource_name=resource_name,
        )

    def permission_list(
            self,
            client_id,
            effective=None,
            resource_name=None,
        ) -> Dict:
        """List Client Permissions

        API Method: client.permission_list

        This method is used to return a tree/list of client permissions.

        Args:
            client_id: Client ID,
            effective: Include Effective Actions. Defaults to None.
            resource_name: Resource Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.permission_list',
            client_id=client_id,
            **{'effective': effective} if effective else {},
            **{'resource_name': resource_name} if resource_name else {},
        )

    def permission_set(
            self,
            action,
            client_id,
            resource_name,
            type,
        ) -> Dict:
        """Set Client Permissions

        API Method: client.permission_set

        This method is used to set client permissions.

        Args:
            action: Action,
            client_id: Client ID,
            resource_name: Resource Name,
            type: Permission Type,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.permission_set',
            action=action,
            client_id=client_id,
            resource_name=resource_name,
            type=type,
        )

    def quote_add(
            self,
            client_id,
            name,
            order_queue_id,
            owner,
            expires=None,
            notes=None,
            status=None,
            term=None,
            term_type=None,
        ) -> Dict:
        """Add a New Quote

        API Method: client.quote_add

        Adds a new quote to a client's account.

        Args:
            client_id: Client ID,
            name: Quote Name,
            order_queue_id: Order Queue ID,
            owner: Owner,
            expires: Expires On. Defaults to None.
            notes: Notes. Defaults to None.
            status: Status. Defaults to None.
            term: Term Length. Defaults to None.
            term_type: Term Type. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.quote_add',
            client_id=client_id,
            name=name,
            order_queue_id=order_queue_id,
            owner=owner,
            **{'expires': expires} if expires else {},
            **{'notes': notes} if notes else {},
            **{'status': status} if status else {},
            **{'term': term} if term else {},
            **{'term_type': term_type} if term_type else {},
        )

    def quote_comment_list(
            self,
            quote_id,
            client_viewable=None,
            direction=None,
            filter_text=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List a Quote's Comments

        API Method: client.quote_comment_list

        This method is used to list a quote's comments.

        Args:
            quote_id: Quote ID,
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
            'client.quote_comment_list',
            quote_id=quote_id,
            **{'client_viewable': client_viewable} if client_viewable else {},
            **{'direction': direction} if direction else {},
            **{'filter_text': filter_text} if filter_text else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def quote_duplicate(
            self,
            quote_id,
            client_id=None,
        ) -> Dict:
        """Duplicate an Existing Quote

        API Method: client.quote_duplicate

        Duplicates a quote.

        Args:
            quote_id: Quote ID,
            client_id: Client ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.quote_duplicate',
            quote_id=quote_id,
            **{'client_id': client_id} if client_id else {},
        )

    def quote_get(
            self,
            quote_id,
            format=None,
        ) -> Dict:
        """Get an Quote

        API Method: client.quote_get

        This method is used to get details of a quote.

        Args:
            quote_id: Quote ID,
            format: Format. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.quote_get',
            quote_id=quote_id,
            **{'format': format} if format else {},
        )

    def quote_list(
            self,
            client_id=None,
            direction=None,
            limit=None,
            offset=None,
            order_by=None,
            status=None,
        ) -> Dict:
        """List Quotes

        API Method: client.quote_list

        Lists quotes.

        Args:
            client_id: Client ID. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            status: Status. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.quote_list',
            **{'client_id': client_id} if client_id else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'status': status} if status else {},
        )

    def quote_service_add(
            self,
            desserv,
            period,
            plan_id,
            quote_id,
            bill_type=None,
            discount=None,
            discount_type=None,
            meta=None,
            notes=None,
            options=None,
            parent=None,
            price=None,
            quantity=None,
            setup=None,
            setup_discount=None,
            setup_discount_type=None,
            setup_qs=None,
            tax_engine_id=None,
            taxes=None,
        ) -> Dict:
        """Add a New Service to a Quote

        API Method: client.quote_service_add

        Adds a service to a quote.

        Args:
            desserv: Description,
            period: Billing Period,
            plan_id: Plan ID,
            quote_id: Quote ID,
            bill_type: Bill Type. Defaults to None.
            discount: Discount. Defaults to None.
            discount_type: Discount Type. Defaults to None.
            meta: Custom Fields. Defaults to None.
            notes: Notes. Defaults to None.
            options: Options. Defaults to None.
            parent: Parent Service. Defaults to None.
            price: Price. Defaults to None.
            quantity: Quantity. Defaults to None.
            setup: Setup Fee. Defaults to None.
            setup_discount: Setup Discount. Defaults to None.
            setup_discount_type: Setup Discount Type. Defaults to None.
            setup_qs: Setup Fee Quantity Discount. Defaults to None.
            tax_engine_id: Tax Engine ID. Defaults to None.
            taxes: Array of Applicable Taxes. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.quote_service_add',
            desserv=desserv,
            period=period,
            plan_id=plan_id,
            quote_id=quote_id,
            **{'bill_type': bill_type} if bill_type else {},
            **{'discount': discount} if discount else {},
            **{'discount_type': discount_type} if discount_type else {},
            **{'meta': meta} if meta else {},
            **{'notes': notes} if notes else {},
            **{'options': options} if options else {},
            **{'parent': parent} if parent else {},
            **{'price': price} if price else {},
            **{'quantity': quantity} if quantity else {},
            **{'setup': setup} if setup else {},
            **{'setup_discount': setup_discount} if setup_discount else {},
            **{'setup_discount_type': setup_discount_type} if setup_discount_type else {},
            **{'setup_qs': setup_qs} if setup_qs else {},
            **{'tax_engine_id': tax_engine_id} if tax_engine_id else {},
            **{'taxes': taxes} if taxes else {},
        )

    def quote_service_delete(
            self,
            quote_service_id,
        ) -> Dict:
        """Deletes an Existing Quote Service

        API Method: client.quote_service_delete

        Deletes a quote's service.

        Args:
            quote_service_id: Quote Service ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.quote_service_delete',
            quote_service_id=quote_service_id,
        )

    def quote_service_duplicate(
            self,
            quote_id,
            quote_service_id,
        ) -> Dict:
        """Duplicate an Existing Quote Service

        API Method: client.quote_service_duplicate

        Copies a quote's service.

        Args:
            quote_id: Quote ID,
            quote_service_id: Quote Service ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.quote_service_duplicate',
            quote_id=quote_id,
            quote_service_id=quote_service_id,
        )

    def quote_service_update(
            self,
            quote_service_id,
            bill_type=None,
            desserv=None,
            discount=None,
            discount_type=None,
            meta=None,
            notes=None,
            options=None,
            parent=None,
            period=None,
            plan_id=None,
            price=None,
            quantity=None,
            setup=None,
            setup_discount=None,
            setup_discount_type=None,
            setup_qs=None,
            tax_engine_id=None,
            taxes=None,
        ) -> Dict:
        """Update an Existing Quote Service

        API Method: client.quote_service_update

        Edits a quote's service.

        Args:
            quote_service_id: Quote Service ID,
            bill_type: Bill Type. Defaults to None.
            desserv: Description. Defaults to None.
            discount: Discount. Defaults to None.
            discount_type: Discount Type. Defaults to None.
            meta: Custom Fields. Defaults to None.
            notes: Notes. Defaults to None.
            options: Options. Defaults to None.
            parent: Parent Service. Defaults to None.
            period: Billing Period. Defaults to None.
            plan_id: Plan ID. Defaults to None.
            price: Price. Defaults to None.
            quantity: Quantity. Defaults to None.
            setup: Setup Fee. Defaults to None.
            setup_discount: Setup Discount. Defaults to None.
            setup_discount_type: Setup Discount Type. Defaults to None.
            setup_qs: Setup Fee Quantity Discount. Defaults to None.
            tax_engine_id: Tax Engine ID. Defaults to None.
            taxes: Array of Applicable Taxes. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.quote_service_update',
            quote_service_id=quote_service_id,
            **{'bill_type': bill_type} if bill_type else {},
            **{'desserv': desserv} if desserv else {},
            **{'discount': discount} if discount else {},
            **{'discount_type': discount_type} if discount_type else {},
            **{'meta': meta} if meta else {},
            **{'notes': notes} if notes else {},
            **{'options': options} if options else {},
            **{'parent': parent} if parent else {},
            **{'period': period} if period else {},
            **{'plan_id': plan_id} if plan_id else {},
            **{'price': price} if price else {},
            **{'quantity': quantity} if quantity else {},
            **{'setup': setup} if setup else {},
            **{'setup_discount': setup_discount} if setup_discount else {},
            **{'setup_discount_type': setup_discount_type} if setup_discount_type else {},
            **{'setup_qs': setup_qs} if setup_qs else {},
            **{'tax_engine_id': tax_engine_id} if tax_engine_id else {},
            **{'taxes': taxes} if taxes else {},
        )

    def quote_sign(
            self,
            quote_id,
            signer,
            signer_ip,
            ach_aba=None,
            ach_acct=None,
            ach_bank=None,
            ach_type=None,
            address=None,
            billing_info_id=None,
            cc_cvv2=None,
            cc_exp=None,
            cc_num=None,
            city=None,
            company=None,
            contract=None,
            country=None,
            email=None,
            first=None,
            last=None,
            phone=None,
            state=None,
            threedsecure=None,
            zip=None,
        ) -> Dict:
        """Sign and Authorize a Quote

        API Method: client.quote_sign

        Sign and authorize a quote, as well as set the payment method.

        Args:
            quote_id: Quote ID,
            signer: Name of Signer,
            signer_ip: IP address of the signer,
            ach_aba: Routing Number. Defaults to None.
            ach_acct: Account Number. Defaults to None.
            ach_bank: Bank Name. Defaults to None.
            ach_type: Account Type. Defaults to None.
            address: Client Address. Defaults to None.
            billing_info_id: Billing Info ID. Defaults to None.
            cc_cvv2: Credit Card Verification. Defaults to None.
            cc_exp: Credit Card Expiration. Defaults to None.
            cc_num: Credit Card Number. Defaults to None.
            city: Client City. Defaults to None.
            company: Client Company. Defaults to None.
            contract: File containing Contract. Defaults to None.
            country: Client Country. Defaults to None.
            email: Client Email. Defaults to None.
            first: Client First Name. Defaults to None.
            last: Client Last Name. Defaults to None.
            phone: Client Phone. Defaults to None.
            state: Client State. Defaults to None.
            threedsecure: Provider specific 3D Secure parameters (array). Defaults to None.
            zip: Client Zip Code. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.quote_sign',
            quote_id=quote_id,
            signer=signer,
            signer_ip=signer_ip,
            **{'ach_aba': ach_aba} if ach_aba else {},
            **{'ach_acct': ach_acct} if ach_acct else {},
            **{'ach_bank': ach_bank} if ach_bank else {},
            **{'ach_type': ach_type} if ach_type else {},
            **{'address': address} if address else {},
            **{'billing_info_id': billing_info_id} if billing_info_id else {},
            **{'cc_cvv2': cc_cvv2} if cc_cvv2 else {},
            **{'cc_exp': cc_exp} if cc_exp else {},
            **{'cc_num': cc_num} if cc_num else {},
            **{'city': city} if city else {},
            **{'company': company} if company else {},
            **{'contract': contract} if contract else {},
            **{'country': country} if country else {},
            **{'email': email} if email else {},
            **{'first': first} if first else {},
            **{'last': last} if last else {},
            **{'phone': phone} if phone else {},
            **{'state': state} if state else {},
            **{'threedsecure': threedsecure} if threedsecure else {},
            **{'zip': zip} if zip else {},
        )

    def quote_update(
            self,
            quote_id,
            expires=None,
            name=None,
            notes=None,
            order_queue_id=None,
            owner=None,
            status=None,
            term=None,
            term_type=None,
        ) -> Dict:
        """Update an Existing Quote

        API Method: client.quote_update

        Edits a quote.

        Args:
            quote_id: Quote ID,
            expires: Expires On. Defaults to None.
            name: Quote Name. Defaults to None.
            notes: Notes. Defaults to None.
            order_queue_id: Order Queue ID. Defaults to None.
            owner: Owner. Defaults to None.
            status: Status. Defaults to None.
            term: Term Length. Defaults to None.
            term_type: Term Type. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.quote_update',
            quote_id=quote_id,
            **{'expires': expires} if expires else {},
            **{'name': name} if name else {},
            **{'notes': notes} if notes else {},
            **{'order_queue_id': order_queue_id} if order_queue_id else {},
            **{'owner': owner} if owner else {},
            **{'status': status} if status else {},
            **{'term': term} if term else {},
            **{'term_type': term_type} if term_type else {},
        )

    def reactivate(
            self,
            client_id,
        ) -> Dict:
        """Reactivate a Client

        API Method: client.reactivate

        This method is used to reactivate a client.

        Args:
            client_id: Client ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.reactivate',
            client_id=client_id,
        )

    def refund_list(
            self,
            client_id,
            begin=None,
            direction=None,
            end=None,
            invoice_id=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List a Client's Refunds

        API Method: client.refund_list

        This method is used to list a client's refunds.

        Args:
            client_id: Client ID,
            begin: Begin Time. Defaults to None.
            direction: Direction. Defaults to None.
            end: End Time. Defaults to None.
            invoice_id: Invoice ID. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.refund_list',
            client_id=client_id,
            **{'begin': begin} if begin else {},
            **{'direction': direction} if direction else {},
            **{'end': end} if end else {},
            **{'invoice_id': invoice_id} if invoice_id else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def renewal_list(
            self,
            user_login,
        ) -> Dict:
        """List Services for Renewal

        API Method: client.renewal_list

        This method is used to generate a list of services which are due for renewal in the specified period.

        Args:
            user_login: Client Login,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.renewal_list',
            user_login=user_login,
        )

    def send_welcome(
            self,
            service_id,
            user_login,
            body=None,
            email=None,
            ipaddress=None,
            password=None,
            reply=None,
            servername=None,
            service=None,
            subject=None,
            username=None,
        ) -> Dict:
        """Send a Welcome Letter

        API Method: client.send_welcome

        This method is used to send the welcome letter to a client.

        Args:
            service_id: Service ID,
            user_login: Client Login,
            body: Welcome Letter Body. Defaults to None.
            email: Email Address. Defaults to None.
            ipaddress: IP Address. Defaults to None.
            password: Password. Defaults to None.
            reply: Reply-To Address. Defaults to None.
            servername: Service Domain or Server Name. Defaults to None.
            service: Service Description. Defaults to None.
            subject: Welcome Letter Subject. Defaults to None.
            username: Username. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.send_welcome',
            service_id=service_id,
            user_login=user_login,
            **{'body': body} if body else {},
            **{'email': email} if email else {},
            **{'ipaddress': ipaddress} if ipaddress else {},
            **{'password': password} if password else {},
            **{'reply': reply} if reply else {},
            **{'servername': servername} if servername else {},
            **{'service': service} if service else {},
            **{'subject': subject} if subject else {},
            **{'username': username} if username else {},
        )

    def service_add(
            self,
            client_id,
            activation_date=None,
            auto_bill=None,
            balance=None,
            bill_prior=None,
            bill_type=None,
            cancel_after=None,
            cancel_bool=None,
            client_acceptance_date=None,
            comment=None,
            contract_term_id=None,
            custom_notes=None,
            description=None,
            discount=None,
            discount_type=None,
            end=None,
            expected_cancellation_date=None,
            facility_id=None,
            ip_address=None,
            meta=None,
            options=None,
            parent_id=None,
            passwd=None,
            period=None,
            plan_id=None,
            planned_activation_date=None,
            post_renew=None,
            price=None,
            prorated=None,
            quantity=None,
            rate_plan_id=None,
            renewdate=None,
            server=None,
            servtype=None,
            setup=None,
            setup_taxes=None,
            start=None,
            status=None,
            suspend_after=None,
            suspend_bool=None,
            tax_engine_id=None,
            tax_p2p_zip_code=None,
            tax_p2p_zip_code_setup=None,
            tax_situs_code=None,
            tax_situs_code_setup=None,
            tax_situs_code_setup_world=None,
            tax_situs_code_world=None,
            tax_trans_type_code=None,
            tax_trans_type_code_setup=None,
            tax_zip_code=None,
            tax_zip_code_setup=None,
            taxes=None,
            userid=None,
            zone_id=None,
        ) -> Dict:
        """Add a New Service

        API Method: client.service_add

        This method is used to add a new service to a client's account.

        Args:
            client_id: Client ID,
            activation_date: Activation Date. Defaults to None.
            auto_bill: Automatically Charge. Defaults to None.
            balance: Balance. Defaults to None.
            bill_prior: Number of Days Before to Bill for Service. Defaults to None.
            bill_type: How Pricing is Calculated. Defaults to None.
            cancel_after: Auto Cancel After X Days. Defaults to None.
            cancel_bool: Auto Cancel Enable. Defaults to None.
            client_acceptance_date: Client Acceptance Date. Defaults to None.
            comment: Service Comment. Defaults to None.
            contract_term_id: Contract Term ID. Defaults to None.
            custom_notes: Service Notes. Defaults to None.
            description: Service Description. Defaults to None.
            discount: Discount Level. Defaults to None.
            discount_type: Discount Type. Defaults to None.
            end: End Date. Defaults to None.
            expected_cancellation_date: Expected Cancellation Date. Defaults to None.
            facility_id: Facility ID. Defaults to None.
            ip_address: Service IP Address. Defaults to None.
            meta: Custom Fields. Defaults to None.
            options: Service Options Array. Defaults to None.
            parent_id: Parent Service ID. Defaults to None.
            passwd: Service Password. Defaults to None.
            period: Period. Defaults to None.
            plan_id: Service Plan ID. Defaults to None.
            planned_activation_date: Planned Activation Date. Defaults to None.
            post_renew: Post Renew Flag. Defaults to None.
            price: Price. Defaults to None.
            prorated: Prorated. Defaults to None.
            quantity: Quantity. Defaults to None.
            rate_plan_id: Rate Plan ID. Defaults to None.
            renewdate: Renewal Date. Defaults to None.
            server: Service Domain or Server Name. Defaults to None.
            servtype: Service Plan code. Defaults to None.
            setup: Setup Fee Amount. Defaults to None.
            setup_taxes: Setup Taxes. Defaults to None.
            start: Billing Start Date. Defaults to None.
            status: Service Status. Defaults to None.
            suspend_after: Auto Suspend After X Days. Defaults to None.
            suspend_bool: Auto Suspend Enable. Defaults to None.
            tax_engine_id: Tax Engine ID. Defaults to None.
            tax_p2p_zip_code: Point to Point Zip Code. Defaults to None.
            tax_p2p_zip_code_setup: Point to Point Setup Fee Zip Code. Defaults to None.
            tax_situs_code: Situs Rule (US/Canada). Defaults to None.
            tax_situs_code_setup: Setup Fee Situs Rule (US/Canada). Defaults to None.
            tax_situs_code_setup_world: Setup Fee Situs Rule (Non US/Canada). Defaults to None.
            tax_situs_code_world: Situs Rule (Non US/Canada). Defaults to None.
            tax_trans_type_code: Transaction Type Code. Defaults to None.
            tax_trans_type_code_setup: Setup Fee Transaction Type Code. Defaults to None.
            tax_zip_code: Zip Code. Defaults to None.
            tax_zip_code_setup: Setup Fee Zip Code. Defaults to None.
            taxes: Taxes. Defaults to None.
            userid: Service User ID. Defaults to None.
            zone_id: Zone ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_add',
            client_id=client_id,
            **{'activation_date': activation_date} if activation_date else {},
            **{'auto_bill': auto_bill} if auto_bill else {},
            **{'balance': balance} if balance else {},
            **{'bill_prior': bill_prior} if bill_prior else {},
            **{'bill_type': bill_type} if bill_type else {},
            **{'cancel_after': cancel_after} if cancel_after else {},
            **{'cancel_bool': cancel_bool} if cancel_bool else {},
            **{'client_acceptance_date': client_acceptance_date} if client_acceptance_date else {},
            **{'comment': comment} if comment else {},
            **{'contract_term_id': contract_term_id} if contract_term_id else {},
            **{'custom_notes': custom_notes} if custom_notes else {},
            **{'description': description} if description else {},
            **{'discount': discount} if discount else {},
            **{'discount_type': discount_type} if discount_type else {},
            **{'end': end} if end else {},
            **{'expected_cancellation_date': expected_cancellation_date} if expected_cancellation_date else {},
            **{'facility_id': facility_id} if facility_id else {},
            **{'ip_address': ip_address} if ip_address else {},
            **{'meta': meta} if meta else {},
            **{'options': options} if options else {},
            **{'parent_id': parent_id} if parent_id else {},
            **{'passwd': passwd} if passwd else {},
            **{'period': period} if period else {},
            **{'plan_id': plan_id} if plan_id else {},
            **{'planned_activation_date': planned_activation_date} if planned_activation_date else {},
            **{'post_renew': post_renew} if post_renew else {},
            **{'price': price} if price else {},
            **{'prorated': prorated} if prorated else {},
            **{'quantity': quantity} if quantity else {},
            **{'rate_plan_id': rate_plan_id} if rate_plan_id else {},
            **{'renewdate': renewdate} if renewdate else {},
            **{'server': server} if server else {},
            **{'servtype': servtype} if servtype else {},
            **{'setup': setup} if setup else {},
            **{'setup_taxes': setup_taxes} if setup_taxes else {},
            **{'start': start} if start else {},
            **{'status': status} if status else {},
            **{'suspend_after': suspend_after} if suspend_after else {},
            **{'suspend_bool': suspend_bool} if suspend_bool else {},
            **{'tax_engine_id': tax_engine_id} if tax_engine_id else {},
            **{'tax_p2p_zip_code': tax_p2p_zip_code} if tax_p2p_zip_code else {},
            **{'tax_p2p_zip_code_setup': tax_p2p_zip_code_setup} if tax_p2p_zip_code_setup else {},
            **{'tax_situs_code': tax_situs_code} if tax_situs_code else {},
            **{'tax_situs_code_setup': tax_situs_code_setup} if tax_situs_code_setup else {},
            **{'tax_situs_code_setup_world': tax_situs_code_setup_world} if tax_situs_code_setup_world else {},
            **{'tax_situs_code_world': tax_situs_code_world} if tax_situs_code_world else {},
            **{'tax_trans_type_code': tax_trans_type_code} if tax_trans_type_code else {},
            **{'tax_trans_type_code_setup': tax_trans_type_code_setup} if tax_trans_type_code_setup else {},
            **{'tax_zip_code': tax_zip_code} if tax_zip_code else {},
            **{'tax_zip_code_setup': tax_zip_code_setup} if tax_zip_code_setup else {},
            **{'taxes': taxes} if taxes else {},
            **{'userid': userid} if userid else {},
            **{'zone_id': zone_id} if zone_id else {},
        )

    def service_comment_list(
            self,
            service_id,
            client_viewable=None,
            direction=None,
            filter_text=None,
            limit=None,
            offset=None,
            order_by=None,
        ) -> Dict:
        """List a Service's Comments

        API Method: client.service_comment_list

        This method is used to list a service's comments.

        Args:
            service_id: Service ID,
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
            'client.service_comment_list',
            service_id=service_id,
            **{'client_viewable': client_viewable} if client_viewable else {},
            **{'direction': direction} if direction else {},
            **{'filter_text': filter_text} if filter_text else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
        )

    def service_deactivate(
            self,
            client_id,
            service_id,
        ) -> Dict:
        """Deactivate a Service

        API Method: client.service_deactivate

        This method is used to deactivate a service associated with a client.

        Args:
            client_id: Client ID,
            service_id: Service ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_deactivate',
            client_id=client_id,
            service_id=service_id,
        )

    def service_get(
            self,
            service_id,
            bill_date=None,
            metadata=None,
            modules=None,
            notes=None,
        ) -> Dict:
        """Get a Service

        API Method: client.service_get

        This method is used to get a service associated with a client.

        Args:
            service_id: Service ID,
            bill_date: Bill Date. Defaults to None.
            metadata: Custom Fields Flag. Defaults to None.
            modules: Modules Flag. Defaults to None.
            notes: Notes Flag. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_get',
            service_id=service_id,
            **{'bill_date': bill_date} if bill_date else {},
            **{'metadata': metadata} if metadata else {},
            **{'modules': modules} if modules else {},
            **{'notes': notes} if notes else {},
        )

    def service_list(
            self,
            bill_date=None,
            brand_id=None,
            client_id=None,
            devices=None,
            direction=None,
            limit=None,
            metadata=None,
            modules=None,
            notes=None,
            offset=None,
            options=None,
            order_by=None,
            order_id=None,
            pack_type_select=None,
            parentpack=None,
            period=None,
            plan_id=None,
        ) -> Dict:
        """List a Client's Services

        API Method: client.service_list

        This method is used to list a client's services.

        Args:
            bill_date: Bill Date. Defaults to None.
            brand_id: Brand ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            devices: Include Devices. Defaults to None.
            direction: Direction. Defaults to None.
            limit: Limit. Defaults to None.
            metadata: Include Custom Fields. Defaults to None.
            modules: Include Service Modules. Defaults to None.
            notes: Include Notes. Defaults to None.
            offset: Offset. Defaults to None.
            options: Include Service Options. Defaults to None.
            order_by: Order By. Defaults to None.
            order_id: Order ID. Defaults to None.
            pack_type_select: Service Selection. Defaults to None.
            parentpack: Parent Service ID. Defaults to None.
            period: Period. Defaults to None.
            plan_id: Service Plan ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_list',
            **{'bill_date': bill_date} if bill_date else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'devices': devices} if devices else {},
            **{'direction': direction} if direction else {},
            **{'limit': limit} if limit else {},
            **{'metadata': metadata} if metadata else {},
            **{'modules': modules} if modules else {},
            **{'notes': notes} if notes else {},
            **{'offset': offset} if offset else {},
            **{'options': options} if options else {},
            **{'order_by': order_by} if order_by else {},
            **{'order_id': order_id} if order_id else {},
            **{'pack_type_select': pack_type_select} if pack_type_select else {},
            **{'parentpack': parentpack} if parentpack else {},
            **{'period': period} if period else {},
            **{'plan_id': plan_id} if plan_id else {},
        )

    def service_metadata_get(
            self,
            service_id,
        ) -> Dict:
        """Get a Service's Custom Fields

        API Method: client.service_metadata_get

        This method is used to get a service's custom fields.

        Args:
            service_id: Service ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_metadata_get',
            service_id=service_id,
        )

    def service_metadata_single(
            self,
            service_id,
            metaconf_id=None,
            variable=None,
        ) -> Dict:
        """Get a Service's Custom Field Value

        API Method: client.service_metadata_single

        This method is used to get a single custom field value from a service.

        Args:
            service_id: Service ID,
            metaconf_id: Custom Field Item ID. Defaults to None.
            variable: Custom Field Variable Name. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_metadata_single',
            service_id=service_id,
            **{'metaconf_id': metaconf_id} if metaconf_id else {},
            **{'variable': variable} if variable else {},
        )

    def service_module_call(
            self,
            function,
            module_id,
            service_id,
            module_params=None,
        ) -> Dict:
        """Call a Service Module Function

        API Method: client.service_module_call

        This method is used to execute a service module function.

        Args:
            function: Function Name,
            module_id: Module Name,
            service_id: Service ID,
            module_params: Parameters. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_module_call',
            function=function,
            module_id=module_id,
            service_id=service_id,
            **{'module_params': module_params} if module_params else {},
        )

    def service_note_add(
            self,
            note,
            service_id,
            spn_id=None,
        ) -> Dict:
        """Add a New Service Note

        API Method: client.service_note_add

        This method is used to add a service note.

        Args:
            note: Note Text,
            service_id: Service ID,
            spn_id: Service Plan Note ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_note_add',
            note=note,
            service_id=service_id,
            **{'spn_id': spn_id} if spn_id else {},
        )

    def service_note_delete(
            self,
            note_id,
        ) -> Dict:
        """Delete a Service Note

        API Method: client.service_note_delete

        This method is used to delete a service note.

        Args:
            note_id: Note ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_note_delete',
            note_id=note_id,
        )

    def service_note_update(
            self,
            note,
            note_id,
        ) -> Dict:
        """Update a Service Note

        API Method: client.service_note_update

        This method is used to update a service note.

        Args:
            note: Note Text,
            note_id: Note ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_note_update',
            note=note,
            note_id=note_id,
        )

    def service_price_changes_list(
            self,
            service_id,
        ) -> Dict:
        """List a Service's Price changes

        API Method: client.service_price_changes_list

        This method is used to list a service's price changes.

        Args:
            service_id: Service ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_price_changes_list',
            service_id=service_id,
        )

    def service_price_set(
            self,
            price,
            service_id,
            bill_type=None,
            contract_term_id=None,
            discount=None,
            discount_type=None,
            options=None,
            period=None,
            permanent=None,
            plan_id=None,
            quantity=None,
            rate_plan_id=None,
            start_date=None,
        ) -> Dict:
        """Set a Service Price

        API Method: client.service_price_set

        This method is used to set a service price. If a price is already set for the specified date it will be updated.

        Args:
            price: Price,
            service_id: Service ID,
            bill_type: Bill Calculated. Defaults to None.
            contract_term_id: Contract Term ID. Defaults to None.
            discount: Discount. Defaults to None.
            discount_type: Discount Type. Defaults to None.
            options: Service Options. Defaults to None.
            period: Billing Period. Defaults to None.
            permanent: Permanent. Defaults to None.
            plan_id: Plan ID. Defaults to None.
            quantity: Quantity. Defaults to None.
            rate_plan_id: Rate Plan ID. Defaults to None.
            start_date: Start Date. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_price_set',
            price=price,
            service_id=service_id,
            **{'bill_type': bill_type} if bill_type else {},
            **{'contract_term_id': contract_term_id} if contract_term_id else {},
            **{'discount': discount} if discount else {},
            **{'discount_type': discount_type} if discount_type else {},
            **{'options': options} if options else {},
            **{'period': period} if period else {},
            **{'permanent': permanent} if permanent else {},
            **{'plan_id': plan_id} if plan_id else {},
            **{'quantity': quantity} if quantity else {},
            **{'rate_plan_id': rate_plan_id} if rate_plan_id else {},
            **{'start_date': start_date} if start_date else {},
        )

    def service_prorate(
            self,
            service_id,
            new_balance=None,
            new_renew=None,
            reason=None,
        ) -> Dict:
        """[Deprecated] Prorate a Service

        API Method: client.service_prorate

        This method is used to prorate a service associated with a client.
		[Deprecated]
		This method is no longer in use. Prorate values are calculated automatically based on the New Renewal Date.
		The use of `new_balance` or `reason` will generate an invalid parameter error.
		

        Args:
            service_id: Service ID,
            new_balance: [Removed] Desired Balance. Defaults to None.
            new_renew: New Renewal Date. Defaults to None.
            reason: [Removed] Prorate Reason. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_prorate',
            service_id=service_id,
            **{'new_balance': new_balance} if new_balance else {},
            **{'new_renew': new_renew} if new_renew else {},
            **{'reason': reason} if reason else {},
        )

    def service_storage_delete(
            self,
            item,
            service_id,
        ) -> Dict:
        """Delete a Service's Storage

        API Method: client.service_storage_delete

        This method is used to delete a service's storage.

        Args:
            item: Item,
            service_id: Service ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_storage_delete',
            item=item,
            service_id=service_id,
        )

    def service_storage_get(
            self,
            item,
            service_id,
        ) -> Dict:
        """Get a Service's Storage

        API Method: client.service_storage_get

        This method is used to get a service's storage.

        Args:
            item: Item,
            service_id: Service ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_storage_get',
            item=item,
            service_id=service_id,
        )

    def service_storage_list(
            self,
            items=None,
            service_id=None,
        ) -> Dict:
        """List a Service's Storage

        API Method: client.service_storage_list

        This method is used to list a service's storage.

        Args:
            items: Item(s). Defaults to None.
            service_id: Service ID(s). Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_storage_list',
            **{'items': items} if items else {},
            **{'service_id': service_id} if service_id else {},
        )

    def service_storage_set(
            self,
            item,
            service_id,
            value,
            encrypt=None,
        ) -> Dict:
        """Set a Service's Storage

        API Method: client.service_storage_set

        This method is used to set a service's storage.

        Args:
            item: Item,
            service_id: Service ID,
            value: Value,
            encrypt: Encrypt. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_storage_set',
            item=item,
            service_id=service_id,
            value=value,
            **{'encrypt': encrypt} if encrypt else {},
        )

    def service_update(
            self,
            service_id,
            activation_date=None,
            auto_adjustment=None,
            auto_bill=None,
            bill_prior=None,
            bill_type=None,
            billed=None,
            cancel_after=None,
            cancel_bool=None,
            client_acceptance_date=None,
            contract_term_id=None,
            description=None,
            discount=None,
            discount_type=None,
            end=None,
            expected_cancellation_date=None,
            facility_id=None,
            ip_address=None,
            lastrenew=None,
            meta=None,
            options=None,
            parent_id=None,
            passwd=None,
            period=None,
            plan_id=None,
            planned_activation_date=None,
            post_renew=None,
            price=None,
            prorate=None,
            prorate_date=None,
            quantity=None,
            rate_plan_id=None,
            renewdate=None,
            server=None,
            servtype=None,
            start=None,
            status=None,
            suspend_after=None,
            suspend_bool=None,
            tax_engine_id=None,
            tax_p2p_zip_code=None,
            tax_situs_code=None,
            tax_situs_code_world=None,
            tax_trans_type_code=None,
            tax_zip_code=None,
            taxes=None,
            userid=None,
            zone_id=None,
        ) -> Dict:
        """Update a Service

        API Method: client.service_update

        This method is used to update a service associated with a client.

        Args:
            service_id: Service ID,
            activation_date: Activation Date. Defaults to None.
            auto_adjustment: Auto Proration Adjustment. Defaults to None.
            auto_bill: Automatically Charge. Defaults to None.
            bill_prior: Number of Days Before to Bill for Service. Defaults to None.
            bill_type: How Pricing is Calculated. Defaults to None.
            billed: Billed Status. Defaults to None.
            cancel_after: Auto Cancel After X Days. Defaults to None.
            cancel_bool: Auto Cancel Enable. Defaults to None.
            client_acceptance_date: Client Acceptance Date. Defaults to None.
            contract_term_id: Contract Term ID. Defaults to None.
            description: Service Description. Defaults to None.
            discount: Discount Level. Defaults to None.
            discount_type: Discount Type. Defaults to None.
            end: End Date. Defaults to None.
            expected_cancellation_date: Expected Cancellation Date. Defaults to None.
            facility_id: Facility ID. Defaults to None.
            ip_address: Service IP Address. Defaults to None.
            lastrenew: Last Renewal Date. Defaults to None.
            meta: Custom Fields. Defaults to None.
            options: Service Options Array. Defaults to None.
            parent_id: Parent Service ID. Defaults to None.
            passwd: Service Password. Defaults to None.
            period: Period. Defaults to None.
            plan_id: Service Plan ID. Defaults to None.
            planned_activation_date: Planned Activation Date. Defaults to None.
            post_renew: Post Renew Flag. Defaults to None.
            price: Price. Defaults to None.
            prorate: Pro-rate Price Change. Defaults to None.
            prorate_date: Pro-rate Date. Defaults to None.
            quantity: Quantity. Defaults to None.
            rate_plan_id: Rate Plan ID. Defaults to None.
            renewdate: Next Renewal Date. Defaults to None.
            server: Service Domain or Server Name. Defaults to None.
            servtype: Service Plan code. Defaults to None.
            start: Billing Start Date. Defaults to None.
            status: Service Status. Defaults to None.
            suspend_after: Auto Suspend After X Days. Defaults to None.
            suspend_bool: Auto Suspend Enable. Defaults to None.
            tax_engine_id: Tax Engine ID. Defaults to None.
            tax_p2p_zip_code: Point to Point Zip Code. Defaults to None.
            tax_situs_code: Situs Rule (US/Canada). Defaults to None.
            tax_situs_code_world: Situs Rule (Non US/Canada). Defaults to None.
            tax_trans_type_code: Transaction Type Code. Defaults to None.
            tax_zip_code: Zip Code. Defaults to None.
            taxes: Taxes. Defaults to None.
            userid: Service User ID. Defaults to None.
            zone_id: Zone ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.service_update',
            service_id=service_id,
            **{'activation_date': activation_date} if activation_date else {},
            **{'auto_adjustment': auto_adjustment} if auto_adjustment else {},
            **{'auto_bill': auto_bill} if auto_bill else {},
            **{'bill_prior': bill_prior} if bill_prior else {},
            **{'bill_type': bill_type} if bill_type else {},
            **{'billed': billed} if billed else {},
            **{'cancel_after': cancel_after} if cancel_after else {},
            **{'cancel_bool': cancel_bool} if cancel_bool else {},
            **{'client_acceptance_date': client_acceptance_date} if client_acceptance_date else {},
            **{'contract_term_id': contract_term_id} if contract_term_id else {},
            **{'description': description} if description else {},
            **{'discount': discount} if discount else {},
            **{'discount_type': discount_type} if discount_type else {},
            **{'end': end} if end else {},
            **{'expected_cancellation_date': expected_cancellation_date} if expected_cancellation_date else {},
            **{'facility_id': facility_id} if facility_id else {},
            **{'ip_address': ip_address} if ip_address else {},
            **{'lastrenew': lastrenew} if lastrenew else {},
            **{'meta': meta} if meta else {},
            **{'options': options} if options else {},
            **{'parent_id': parent_id} if parent_id else {},
            **{'passwd': passwd} if passwd else {},
            **{'period': period} if period else {},
            **{'plan_id': plan_id} if plan_id else {},
            **{'planned_activation_date': planned_activation_date} if planned_activation_date else {},
            **{'post_renew': post_renew} if post_renew else {},
            **{'price': price} if price else {},
            **{'prorate': prorate} if prorate else {},
            **{'prorate_date': prorate_date} if prorate_date else {},
            **{'quantity': quantity} if quantity else {},
            **{'rate_plan_id': rate_plan_id} if rate_plan_id else {},
            **{'renewdate': renewdate} if renewdate else {},
            **{'server': server} if server else {},
            **{'servtype': servtype} if servtype else {},
            **{'start': start} if start else {},
            **{'status': status} if status else {},
            **{'suspend_after': suspend_after} if suspend_after else {},
            **{'suspend_bool': suspend_bool} if suspend_bool else {},
            **{'tax_engine_id': tax_engine_id} if tax_engine_id else {},
            **{'tax_p2p_zip_code': tax_p2p_zip_code} if tax_p2p_zip_code else {},
            **{'tax_situs_code': tax_situs_code} if tax_situs_code else {},
            **{'tax_situs_code_world': tax_situs_code_world} if tax_situs_code_world else {},
            **{'tax_trans_type_code': tax_trans_type_code} if tax_trans_type_code else {},
            **{'tax_zip_code': tax_zip_code} if tax_zip_code else {},
            **{'taxes': taxes} if taxes else {},
            **{'userid': userid} if userid else {},
            **{'zone_id': zone_id} if zone_id else {},
        )

    def set_login(
            self,
            client_id,
            uber_login=None,
            uber_pass=None,
        ) -> Dict:
        """Set a Client's Login

        API Method: client.set_login

        This method is used to set a client's login.

        Args:
            client_id: Client ID,
            uber_login: New Login Name. Defaults to None.
            uber_pass: New Password. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.set_login',
            client_id=client_id,
            **{'uber_login': uber_login} if uber_login else {},
            **{'uber_pass': uber_pass} if uber_pass else {},
        )

    def storage_delete(
            self,
            client_id,
            item,
        ) -> Dict:
        """Delete a Client's Storage

        API Method: client.storage_delete

        This method is used to delete a client's storage.

        Args:
            client_id: Client ID,
            item: Item,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.storage_delete',
            client_id=client_id,
            item=item,
        )

    def storage_get(
            self,
            client_id,
            item,
        ) -> Dict:
        """Get a Client's Storage

        API Method: client.storage_get

        This method is used to get a client's storage.

        Args:
            client_id: Client ID,
            item: Item,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.storage_get',
            client_id=client_id,
            item=item,
        )

    def storage_list(
            self,
            client_id=None,
            item=None,
        ) -> Dict:
        """List a Client's Storage

        API Method: client.storage_list

        This method is used to list a client's storage.

        Args:
            client_id: Client ID(s). Defaults to None.
            item: Item(s). Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.storage_list',
            **{'client_id': client_id} if client_id else {},
            **{'item': item} if item else {},
        )

    def storage_set(
            self,
            client_id,
            item,
            value,
            encrypt=None,
        ) -> Dict:
        """Set a Client's Storage

        API Method: client.storage_set

        This method is used to set a client's storage.

        Args:
            client_id: Client ID,
            item: Item,
            value: Value,
            encrypt: Encrypt. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.storage_set',
            client_id=client_id,
            item=item,
            value=value,
            **{'encrypt': encrypt} if encrypt else {},
        )

    def tax_exemption_add(
            self,
            certificate_id=None,
            client_id=None,
            end_date=None,
            pdf=None,
            start_date=None,
            status=None,
            tax_exemption_type_id=None,
        ) -> Dict:
        """Add a new Tax Exemption

        API Method: client.tax_exemption_add

        This method is used to add a tax exemption for a client.

        Args:
            certificate_id: Certificate ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            end_date: Expiration Date. Defaults to None.
            pdf: Certificate PDF. Defaults to None.
            start_date: Effective Date. Defaults to None.
            status: Status. Defaults to None.
            tax_exemption_type_id: Tax Exemption Type ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.tax_exemption_add',
            **{'certificate_id': certificate_id} if certificate_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'end_date': end_date} if end_date else {},
            **{'pdf': pdf} if pdf else {},
            **{'start_date': start_date} if start_date else {},
            **{'status': status} if status else {},
            **{'tax_exemption_type_id': tax_exemption_type_id} if tax_exemption_type_id else {},
        )

    def tax_exemption_get(
            self,
            tax_exemption_id,
        ) -> Dict:
        """Get a Client's Tax Exemption

        API Method: client.tax_exemption_get

        This method is used to get a client's tax exemption.

        Args:
            tax_exemption_id: Tax Exemption ID,
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.tax_exemption_get',
            tax_exemption_id=tax_exemption_id,
        )

    def tax_exemption_list(
            self,
            active=None,
            certificate_id=None,
            client_id=None,
            direction=None,
            end_date=None,
            inactive=None,
            limit=None,
            offset=None,
            order_by=None,
            start_date=None,
            status=None,
            tax_exemption_type_id=None,
        ) -> Dict:
        """List a Client's Tax Exemptions

        API Method: client.tax_exemption_list

        This method is used to list a client's tax exemptions.

        Args:
            active: Active Exemptions. Defaults to None.
            certificate_id: Certificate ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            direction: Direction. Defaults to None.
            end_date: Expiration Date. Defaults to None.
            inactive: Inactive Exemptions. Defaults to None.
            limit: Limit. Defaults to None.
            offset: Offset. Defaults to None.
            order_by: Order By. Defaults to None.
            start_date: Effective Date. Defaults to None.
            status: Status. Defaults to None.
            tax_exemption_type_id: Tax Exemption Type ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.tax_exemption_list',
            **{'active': active} if active else {},
            **{'certificate_id': certificate_id} if certificate_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'direction': direction} if direction else {},
            **{'end_date': end_date} if end_date else {},
            **{'inactive': inactive} if inactive else {},
            **{'limit': limit} if limit else {},
            **{'offset': offset} if offset else {},
            **{'order_by': order_by} if order_by else {},
            **{'start_date': start_date} if start_date else {},
            **{'status': status} if status else {},
            **{'tax_exemption_type_id': tax_exemption_type_id} if tax_exemption_type_id else {},
        )

    def tax_exemption_update(
            self,
            tax_exemption_id,
            certificate_id=None,
            client_id=None,
            end_date=None,
            pdf=None,
            start_date=None,
            status=None,
            tax_exemption_type_id=None,
        ) -> Dict:
        """Update a Client's Tax Exemption

        API Method: client.tax_exemption_update

        This method is used to update a Client's tax exemption.

        Args:
            tax_exemption_id: Tax Exemption ID,
            certificate_id: Certificate ID. Defaults to None.
            client_id: Client ID. Defaults to None.
            end_date: Expiration Date. Defaults to None.
            pdf: Certificate PDF. Defaults to None.
            start_date: Effective Date. Defaults to None.
            status: Status. Defaults to None.
            tax_exemption_type_id: Tax Exemption Type ID. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.tax_exemption_update',
            tax_exemption_id=tax_exemption_id,
            **{'certificate_id': certificate_id} if certificate_id else {},
            **{'client_id': client_id} if client_id else {},
            **{'end_date': end_date} if end_date else {},
            **{'pdf': pdf} if pdf else {},
            **{'start_date': start_date} if start_date else {},
            **{'status': status} if status else {},
            **{'tax_exemption_type_id': tax_exemption_type_id} if tax_exemption_type_id else {},
        )

    def update(
            self,
            client_id,
            access=None,
            active=None,
            address=None,
            auto_apply_credit=None,
            brand_id=None,
            charge_days=None,
            city=None,
            company=None,
            country=None,
            credit_bool=None,
            datedue=None,
            datepay=None,
            datesend=None,
            default_renew=None,
            discount=None,
            discount_type=None,
            email=None,
            fax=None,
            first=None,
            grace_due=None,
            last=None,
            late_fee_scheme_id=None,
            login_enabled=None,
            meta=None,
            phone=None,
            prebill_days=None,
            prebill_method=None,
            priority=None,
            prorate_min_days=None,
            referred=None,
            referred_by=None,
            retry_every=None,
            state=None,
            strict=None,
            uber_login=None,
            vat_id=None,
            zip=None,
        ) -> Dict:
        """Update a Client

        API Method: client.update

        This method is used to update a client's account information.

        Args:
            client_id: Client ID,
            access: Access Settings. Defaults to None.
            active: Client Status. Defaults to None.
            address: Street Address. Defaults to None.
            auto_apply_credit: Auto Apply Credit. Defaults to None.
            brand_id: Brand ID. Defaults to None.
            charge_days: Charge Delay. Defaults to None.
            city: City. Defaults to None.
            company: Company. Defaults to None.
            country: Country. Defaults to None.
            credit_bool: Billing Method. Defaults to None.
            datedue: Invoice Due Date. Defaults to None.
            datepay: Grace Period. Defaults to None.
            datesend: Invoice Send Date. Defaults to None.
            default_renew: Default Renew Date. Defaults to None.
            discount: Discount Level. Defaults to None.
            discount_type: Discount Type. Defaults to None.
            email: Email Address. Defaults to None.
            fax: Fax Number. Defaults to None.
            first: First Name. Defaults to None.
            grace_due: Due Date Method. Defaults to None.
            last: Last Name. Defaults to None.
            late_fee_scheme_id: Late Fee Schedule. Defaults to None.
            login_enabled: Enable Login. Defaults to None.
            meta: Custom Fields. Defaults to None.
            phone: Telephone Number. Defaults to None.
            prebill_days: Pre Bill Days. Defaults to None.
            prebill_method: Pre Bill Method. Defaults to None.
            priority: Ticket Priority. Defaults to None.
            prorate_min_days: Prorate Min. Days. Defaults to None.
            referred: Referred By. Defaults to None.
            referred_by: Referred By. Defaults to None.
            retry_every: Retry Interval. Defaults to None.
            state: State/Province. Defaults to None.
            strict: Strict Mode. Defaults to None.
            uber_login: Username. Defaults to None.
            vat_id: VAT ID. Defaults to None.
            zip: Zip/Postcode. Defaults to None.
        Returns:
            Dict: The dictionary response from the method 
        """
        return self._request(
            'client.update',
            client_id=client_id,
            **{'access': access} if access else {},
            **{'active': active} if active else {},
            **{'address': address} if address else {},
            **{'auto_apply_credit': auto_apply_credit} if auto_apply_credit else {},
            **{'brand_id': brand_id} if brand_id else {},
            **{'charge_days': charge_days} if charge_days else {},
            **{'city': city} if city else {},
            **{'company': company} if company else {},
            **{'country': country} if country else {},
            **{'credit_bool': credit_bool} if credit_bool else {},
            **{'datedue': datedue} if datedue else {},
            **{'datepay': datepay} if datepay else {},
            **{'datesend': datesend} if datesend else {},
            **{'default_renew': default_renew} if default_renew else {},
            **{'discount': discount} if discount else {},
            **{'discount_type': discount_type} if discount_type else {},
            **{'email': email} if email else {},
            **{'fax': fax} if fax else {},
            **{'first': first} if first else {},
            **{'grace_due': grace_due} if grace_due else {},
            **{'last': last} if last else {},
            **{'late_fee_scheme_id': late_fee_scheme_id} if late_fee_scheme_id else {},
            **{'login_enabled': login_enabled} if login_enabled else {},
            **{'meta': meta} if meta else {},
            **{'phone': phone} if phone else {},
            **{'prebill_days': prebill_days} if prebill_days else {},
            **{'prebill_method': prebill_method} if prebill_method else {},
            **{'priority': priority} if priority else {},
            **{'prorate_min_days': prorate_min_days} if prorate_min_days else {},
            **{'referred': referred} if referred else {},
            **{'referred_by': referred_by} if referred_by else {},
            **{'retry_every': retry_every} if retry_every else {},
            **{'state': state} if state else {},
            **{'strict': strict} if strict else {},
            **{'uber_login': uber_login} if uber_login else {},
            **{'vat_id': vat_id} if vat_id else {},
            **{'zip': zip} if zip else {},
        )
