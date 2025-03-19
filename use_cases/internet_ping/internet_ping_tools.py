class tools:
    def __init__(self):
        self.customer_accounts = {"Jane Doe, 456 Maple St": "123456"}

        self.network_usage_history = {'123456': '''[{"date": "2025-01-15", "usage": "500MB"}, {"date": "2025-01-16", "usage": "1GB"}]'''}

        self.device_connection_history = {'123456':  '''[ {"device": "Phone", "last_connected": "2025-01-16 10:00 AM"}, {"device": "Laptop", "last_connected": "2025-01-16 11:00 AM"}]'''}
        
        self.router_id = "R-987654"

    def get_customer_account(self, full_name, address):
        """
        Fetches the customer's account details using their full name and address.

        Args:
            full_name (str): Full name of the customer.
            address (str): Address of the customer.

        Returns:
            dict: Account details or an error message if not found.
        """
        key = f"{full_name}, {address}"
        if key in self.customer_accounts:
            return {
                "status_code": 1,
                "message": f"Authenticated successfully with account id {self.customer_accounts[key]}",
            }
        return {
            "status_code": 0,
            "message": "Account not found.",
        }

    def get_network_usage_history(self, account_id):
        """
        Fetches the network usage history of a customer's account.

        Args:
            account_id (str): Customer's account ID.

        Returns:
            list[dict]: Network usage history or an error message if not found.
        """
        if self.network_usage_history.get(account_id):
                return {
                    "status_code": 1,
                    "message": self.network_usage_history.get(account_id),
                }
        return {
            "status_code": 0,
            "message": "Network usage history not found for the account id.",
        }

    def get_device_connection_history(self, account_id):
        """
        Fetches the device connection history of a customer's account.

        Args:
            account_id (str): Customer's account ID.

        Returns:
            list[dict]: Device connection history or an error message if not found.
        """
        if self.device_connection_history.get(account_id):
                return {
                    "status_code": 1,
                    "message": self.device_connection_history.get(account_id),
                }
        return {
            "status_code": 0,
            "message": "Device connection histoy not found for the account id.",
        }

    def remote_reboot_router(self, router_id):
        """
        Remotely reboots the customer's router.

        Args:
            router_id (str): Router ID of the customer.

        Returns:
            dict: Reboot status or an error message if not found.
        """
        if self.router_id == router_id:
                return {
                    "status_code": 1,
                    "message": "Router successfully rebooted.",
                }
        return {
            "status_code": 0,
            "message": f"Router ID {router_id} is incorrect",
        }

    def transferToHuman(self):
        """
        Escalates the issue to the technical support team.

        Returns:
            dict: Escalation status or an error message if not found.
        """
        return {
                    "status_code": 1,
                    "message": "Issue successfully escalated to technical support.",
                }

    def mark_problem_resolved(self):
        """
        Marks the problem as resolved for the customer's account. Use this tool to mark the problem or issue is fixed after restarting the router
        Returns:
            dict: Resolution status or an error message if the account is not found.
        """
        # Check if the account exists
        return {
                "status_code": 1,
                "message": "The problem been successfully resolved. Thank you for using our services.",
            }

tools_description = [
    {
        "type": "function",
        "conf": {
            "func_name": "get_customer_account",
            "func_desc": "Use this tool to fetch the customer's account details using their full name and address.",
            "func_args": {
                "full_name": {
                    "type": "string",
                    "description": "Full name of the customer.",
                },
                "address": {
                    "type": "string",
                    "description": "Address of the customer.",
                },
            },
        },
        "required": ["full_name", "address"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "get_network_usage_history",
            "func_desc": "Use this tool to fetch the network usage history of a customer's account.",
            "func_args": {
                "account_id": {
                    "type": "string",
                    "description": "Customer's account ID.",
                },
            },
        },
        "required": ["account_id"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "get_device_connection_history",
            "func_desc": "Use this tool to fetch the device connection history of a customer's account.",
            "func_args": {
                "account_id": {
                    "type": "string",
                    "description": "Customer's account ID.",
                },
            },
        },
        "required": ["account_id"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "remote_reboot_router",
            "func_desc": "Use this tool to remotely reboot the customer's router with the user provided router ID.",
            "func_args": {
                "router_id": {
                    "type": "string",
                    "description": "Router ID of the customer's router.",
                },
            },
        },
        "required": ["router_id"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "transferToHuman",
            "func_desc": "You must use this tool to escalate the issue to the technical support team for further assitance or if the issue is not resolved.",
            "func_args": {},
        },
        "required": [],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "mark_problem_resolved",
            "func_desc": "USE this tool to when the internet issue is resolved after rebooting the router.",
            "func_args": {},
        },
        "required": [],
    }
]